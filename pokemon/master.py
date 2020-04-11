"""

Copyright (c) 2016-2020 Vanessa Sochat

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

"""

from pokemon.utils import get_installdir, load_json
from random import choice
import hashlib
import sys

base = get_installdir()


def get_pokemon(pid=None, name=None, pokemons=None):
    """get_pokemon will return a pokemon with a specific ID, or if none is given,
    will select randomly. First the pid will be used, then the name, then any filters.
    :param pid: the pokemon ID to return
    :param pokemons: the pokemons data structure
    """
    if pokemons == None:
        pokemons = catch_em_all()

    # First see if we want to find a pokemon by name
    if name is not None:
        catches = lookup_pokemon(field="name", value=name, pokemons=pokemons)
        if catches is not None:
            return catches
        print("We don't have a pokemon called %s" % name)
        sys.exit(1)

    # Next see if they want a random pokemon
    if pid is None:
        choices = list(pokemons.keys())
        pid = int(choice(choices))

    # Retrieve the random, or user selected pokemon
    if pid is not None and str(pid) in pokemons.keys():
        return {pid: pokemons[str(pid)]}

    else:
        print("Cannot find pokemon with this criteria!")


def get_trainer(name):
    """return the unique id for a trainer, determined by the md5 sum
    """
    name = name.lower()
    return int(hashlib.md5(name.encode("utf-8")).hexdigest(), 16) % 10 ** 8


def catch_em_all(data_file=None, return_names=False):
    """catch_em_all returns the entire database of pokemon, a base function for starting
    :param data_file: location of pokemons.json data file (not required)
    """
    if data_file == None:
        data_file = "%s/database/pokemons.json" % (base)

    pokemons = load_json(data_file)

    if return_names is True:
        names = []
        for key, meta in pokemons.items():
            names.append(meta["name"])
        return names
    return pokemons


def lookup_pokemon(field, value, pokemons=None):
    """lookup_pokemon will search a particular field (name) for a value. If no pokemons
    data structure is provided, all will be used.
    :param field: the field to look up.
    :param pokemons: the pokemons data structure
    """
    if pokemons == None:
        pokemons = catch_em_all()

    catches = {}
    for pid, data in pokemons.items():
        if isinstance(data[field], list):
            for entry in data[field]:
                found = search_entry(entry, value)
                if found == True:
                    catches[pid] = data
        else:
            found = search_entry(data[field], value)
            if found == True:
                catches[pid] = data

    if len(catches) > 0:
        return catches
    return None


def search_entry(field, value):
    if isinstance(field, float) or isinstance(field, int):
        if field == value:
            return True
    elif isinstance(field, str) or isinstance(field, unicode):
        if field.lower() == value.lower():
            return True
    return False
