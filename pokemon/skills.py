from pokemon.master import get_pokemon, catch_em_all
import numpy

def get_ascii(pid=None,name=None,pokemons=None,return_pokemons=False,message=None):
    '''get_ascii will return ascii art for a pokemon based on a name or pid.
    :param pid: the pokemon ID to return
    :param name: the pokemon name to return
    :param return_pokemons: return catches (default False)
    :param message: add a message to the ascii
    '''
    pokemon = get_pokemon(name=name,pid=pid,pokemons=pokemons)
    printme = message
    if len(pokemon) > 0:
        for pid,data in pokemon.iteritems():
            if message == None:
                printme = data["name"].capitalize()
            print "%s\n\n%s" %(data['ascii'],printme)
          
    if return_pokemons == True:
        return pokemon  

def get_avatar(string,pokemons=None,print_screen=True,include_name=True):
    '''get_avatar will return a unique pokemon for a specific avatar based on the hash
    :param string: the string to look up
    :param print_screen: if True, will print ascii to the screen (default True) and not return
    :param include_name: if True, will add name (minus end of address after @) to avatar
    '''
    if pokemons == None:
        pokemons = catch_em_all()

    # The IDs are numbers between 1 and the max
    number_pokemons = len(pokemons)
    pid = numpy.mod(hash(string),number_pokemons)
    pokemon = get_pokemon(pid=pid,pokemons=pokemons)
    avatar = pokemon[pid]["ascii"]
    if include_name == True:
        avatar = "%s\n\n%s" %(avatar,string.split("@")[0])
    if print_screen == True:
        print avatar    
    else:
        return avatar
