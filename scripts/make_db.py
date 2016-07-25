from pokemon.convert import handle_image_conversion
from BeautifulSoup import BeautifulSoup
from pokemon.utils import save_json
import requests
import urllib
import os
import re

base = "http://pokemondb.net"
pokemon_index = "%s/pokedex/national" %(base)

# Make output folders for data, and raw images
database_dir = os.path.abspath('../pokemon/database')
image_dir = "%s/images" %(database_dir)
for dirname in [database_dir,image_dir]:
    if not os.path.exists(dirname):
        os.mkdir(dirname)


# Retrieve the page with all 7 generations
response = requests.get(pokemon_index)
soup = BeautifulSoup(response.text)
pokemon = soup.findAll("span",attrs={"class": "infocard-tall "})

if len(pokemon) != 721:
    print("WARNING: There should be 721 pokemon, %s found!" %(len(pokemon)))

# Old school, we will use wget command line :)
os.chdir(image_dir)

# Save each to a data structure
pokemons = dict()
for poke in pokemon:
    pid = int(poke.findChild('small').getText().replace("#",""))
    pokemon_name = poke.findChild('a',attrs={'class':'ent-name'}).getText()
    link = poke.findChild('a',attrs={'class':'pkg '}).get('href')
    url = "%s%s" %(base,link)

    # Pokemon Individual Page
    response = requests.get(url)
    psoup = BeautifulSoup(response.text)
    img_div = psoup.find('div',attrs={"class":"col desk-span-4 lap-span-6 figure"})
    img = img_div.findChild('img').get('src')
    ext = os.path.splitext(os.path.basename(img))[-1]
    image_file = "%s/%s%s" %(image_dir,pid,ext)
    if os.path.exists(image_file):
        os.remove(image_file)
    os.system("wget %s -O %s" %(img,image_file))

    # Make ascii
    ascii = handle_image_conversion(image_file,new_width=30)
    
    # Stats
    stats = {}
    save_stats = ["Japanese"]
    table = psoup.find("tbody")
    for row in table.findAll('tr'):
        header = row.find('th').getText()
        content = row.find('td').getText()
        if header in save_stats:
            stats[header] = content
        elif header == "Weight":
            stats[header] = float(content.split('lbs')[0])
        elif header == "Height":
            stats[header] = float(re.sub("m|[)]","",content.split("(")[-1]))
        elif header in ["Abilities","Type"]:
            stats[header] = [x.getText().lower() for x in row.findAll('a')]

    # Save it!
    pokemons[pid] = {"id":pid,
                     "name":pokemon_name,
                     "link":url,
                     "ascii":ascii}

    for stat_name,stat_value in stats.iteritems():
        pokemons[pid][stat_name.lower()] = stat_value

output_file = "%s/pokemons.json" %(database_dir)
save_json(pokemons,output_file)
