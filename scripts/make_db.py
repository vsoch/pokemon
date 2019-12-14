#from pokemon.convert import handle_image_conversion
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

from PIL import Image

'''Credit goes to https://www.hackerearth.com/notes/beautiful-python-a-simple-ascii-art-generator-from-images/
The one modification I added was to scale the new_width by 2, because text characters tend to be thinner than they
are wide, and the current method produced images that were (generally) too tall!
'''
ASCII_CHARS = [ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']

def scale_image(image, new_width):
    """Resizes an image preserving the aspect ratio.
    """
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width)
    # This scales it wider than tall, since characters are biased
    new_image = image.resize((new_width*2, new_height))
    return new_image

def convert_to_grayscale(image):
    return image.convert('L')

def map_pixels_to_ascii_chars(image, range_width=25):
    """Maps each pixel to an ascii char based on the range
    in which it lies.
    0-255 is divided into 11 ranges of 25 pixels each.
    """
    pixels_in_image = list(image.getdata())
    pixels_to_chars = [ASCII_CHARS[pixel_value//range_width] for pixel_value in
            pixels_in_image]
    return "".join(pixels_to_chars)

def convert_image_to_ascii(image, new_width):
    image = scale_image(image,new_width)
    image = convert_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [pixels_to_chars[index: index + new_width*2] for index in
            range(0, len_pixels_to_chars, new_width*2)]
    return "\n".join(image_ascii)

def handle_image_conversion(image_filepath,new_width=100):
    image = None
    try:
        image = Image.open(image_filepath)
    except:
        print("Unable to open image file {image_filepath}.".format(image_filepath=image_filepath))
        print(e)
        return
    image_ascii = convert_image_to_ascii(image,new_width)
    print(image_ascii)
    return image_ascii

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
pokemon = soup.findAll("span",attrs={"class": "infocard-lg-data text-muted"})
if len(pokemon) != 721:
    print("WARNING: There should be 721 pokemon, %s found!" %(len(pokemon)))

# Old school, we will use wget command line :)
os.chdir(image_dir)

# Save each to a data structure
pokemons = dict()
for poke in pokemon:
    pid = int(poke.findChild('small').getText().replace("#",""))
    pokemon_name = poke.findChild('a',attrs={'class':'ent-name'}).getText()
    link = poke.findChild('a',attrs={'class':'ent-name'}).get('href')
    url = "%s%s" %(base,link)
    print(url)

    # Pokemon Individual Page
    response = requests.get(url)
    psoup = BeautifulSoup(response.text)
    img_div = psoup.find('div',attrs={"class":"grid-col span-md-6 span-lg-4 text-center"})
    img = img_div.findChild('img').get('src')
    ext = os.path.splitext(os.path.basename(img))[-1]
    image_file = "%s/%s%s" %(image_dir,pid,ext)
    if os.path.exists(image_file):
        os.remove(image_file)
    os.system("wget %s -O %s" %(img,image_file))

    # Make ascii
    
    ascii = handle_image_conversion(image_file)
    
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
            weight = float(content.partition('kg')[0])
            #print(weight)
            #stats[header] = float(content.split('lbs')[0])
            stats[header] = float(content.partition('kg')[0])
        elif header == "Height":
            #print((re.sub("m|[)]","",content.split("(")[-1])))
            #stats[header] = float(re.sub("m|[)]","",content.split("(")[-1]))
            whatis = float(content.partition('m')[0])
            #print(whatis)
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
