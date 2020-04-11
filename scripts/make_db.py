from bs4 import BeautifulSoup
from pokemon.convert import handle_image_conversion
from pokemon.utils import save_json
import requests
import urllib
import os
import re
import pickle

'''
Copyright (c) 2016-2018 Vanessa Sochat
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

base = "http://pokemondb.net"
pokemon_index = "%s/pokedex/national" %(base)

# Make output folders for data, and raw images
database_dir = os.path.abspath('../pokemon/database')
image_dir = "%s/images" %(database_dir)
for dirname in [database_dir,image_dir]:
    if not os.path.exists(dirname):
        os.mkdir(dirname)


# Retrieve the page with all 8 generations
response = requests.get(pokemon_index)
soup = BeautifulSoup(response.text)
pokemon = soup.findAll("span",attrs={"class": "infocard-lg-data text-muted"})
if len(pokemon) != 890:
    print("WARNING: There should be 890 pokemon, %s found!" %(len(pokemon)))

# Old school, we will use wget command line :)
os.chdir(image_dir)

# Save each to a data structure
pokemons = dict()
for poke in pokemon:
    pid = int(poke.findChild('small').getText().replace("#",""))
    pokemon_name = poke.findChild('a',attrs={'class':'ent-name'}).getText()
    link = poke.findChild('a',attrs={'class':'ent-name'}).get('href')
    url = "%s%s" %(base,link)

    # Pokemon Individual Page
    response = requests.get(url)
    psoup = BeautifulSoup(response.text)
    img_div = psoup.find('div',attrs={"class":"grid-col span-md-6 span-lg-4 text-center"})
    img = img_div.findChild('img').get('src')
    ext = os.path.splitext(os.path.basename(img))[-1]
    image_file = "%s/%s%s" %(image_dir,pid,ext)
    if os.path.exists(image_file):
        os.remove(image_file)
    os.system("wget %s -O %s --no-check-certificate --secure-protocol=TLSv1" %(img,image_file))

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
            stats[header] = float(re.sub("lbs|[)]","",content.partition("(")[-1]))
        elif header == "Height":
            stats[header] = float(content.partition('m')[0])
        elif header in ["Abilities","Type"]:
            stats[header] = [x.getText().lower() for x in row.findAll('a')]

    # Save it!
    pokemons[pid] = {"id":pid,
                     "name":pokemon_name,
                     "link":url,
                     "ascii":ascii}

    for stat_name,stat_value in stats.items():
        pokemons[pid][stat_name.lower()] = stat_value

output_file = "%s/pokemons.json" %(database_dir)
save_json(pokemons,output_file)
