from pokemon.utils import get_installdir, load_json
import numpy

base = get_installdir()

def get_pokemon(pid=None,name=None,pokemons=None):
    '''get_pokemon will return a pokemon with a specific ID, or if none is given,
    will select randomly. First the pid will be used, then the name, then any filters.
    :param pid: the pokemon ID to return
    :param pokemons: the pokemons data structure
    '''
    if pokemons == None:
        pokemons = catch_em_all()

    # First see if we want to find a pokemon by name
    if name != None:
        catches = lookup_pokemon(field="name",
                                 value=name,
                                 pokemons=pokemons)            
        if len(catches) > 0:
            return catches

    # Next see if they want a random pokemon
    if pid == None:
        pid = numpy.random.choice(pokemons.keys())

    # Retrieve the random, or user selected pokemon
    if pid != None and str(pid) in pokemons.keys():
        return {pid:pokemons[str(pid)]}

    else:
       print("Cannot find pokemon with this criteria!")


def catch_em_all(data_file=None):
    '''catch_em_all returns the entire database of pokemon, a base function for starting
    :param data_file: location of pokemons.json data file (not required)
    '''
    if data_file == None:
        data_file = "%s/database/pokemons.json" %(base)

    pokemons = load_json(data_file)
    return pokemons
    
def lookup_pokemon(field,value,pokemons=None):
    '''lookup_pokemon will search a particular field (name) for a value. If no pokemons
    data structure is provided, all will be used.
    :param field: the field to look up.
    :param pokemons: the pokemons data structure
    '''
    if pokemons == None:
        pokemons = catch_em_all()

    catches = {}
    for pid,data in pokemons.iteritems():
        if isinstance(data[field],list):
            for entry in data[field]:
                found = search_entry(entry,value)        
                if found == True:
                    catches[pid] = data
        else:
            found = search_entry(data[field],value)
            if found == True:
                catches[pid] = data
                            
    if len(catches) > 0:
        return catches
    return None

def search_entry(field,value):
    if isinstance(field,float) or isinstance(field,int):
        if field == value:
            return True
    elif isinstance(field,str) or isinstance(field,unicode):
        if field.lower() == value.lower():
            return True
    return False
