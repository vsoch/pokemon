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

from pokemon.master import get_pokemon, catch_em_all, get_trainer


def get_ascii(pid=None, name=None, pokemons=None, return_pokemons=False, message=None):
    """get_ascii will return ascii art for a pokemon based on a name or pid.
    :param pid: the pokemon ID to return
    :param name: the pokemon name to return
    :param return_pokemons: return catches (default False)
    :param message: add a message to the ascii
    """
    pokemon = get_pokemon(name=name, pid=pid, pokemons=pokemons)
    printme = message
    if len(pokemon) > 0:
        for pid, data in pokemon.items():
            if message == None:
                printme = data["name"].capitalize()
            print("%s\n\n%s" % (data["ascii"], printme))

    if return_pokemons == True:
        return pokemon


def get_avatar(name, pokemons=None, print_screen=True, include_name=True):
    """get_avatar will return a unique pokemon for a specific avatar based on the hash
    :param name: the name to look up
    :param print_screen: if True, will print ascii to the screen (default True) and not return
    :param include_name: if True, will add name (minus end of address after @) to avatar
    """
    if pokemons is None:
        pokemons = catch_em_all()

    # The IDs are numbers between 1 and the max
    number_pokemons = len(pokemons)

    trainer = get_trainer(name)

    pid = str(trainer % number_pokemons)
    pokemon = get_pokemon(pid=pid, pokemons=pokemons)

    avatar = pokemon[pid]["ascii"]
    if include_name is True:
        avatar = "%s\n\n%s" % (avatar, name.split("@")[0])
    if print_screen is True:
        print(avatar)
    return avatar
