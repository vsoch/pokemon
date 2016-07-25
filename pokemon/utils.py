import __init__
import json
import os

def get_installdir():
    '''get_installdir
       returns installation directory of pokemon
    '''
    return os.path.dirname(os.path.abspath(__init__.__file__))


def save_json(json_obj,output_file):
    filey = open(output_file,'wb')
    filey.write(json.dumps(json_obj, sort_keys=True,indent=4, separators=(',', ': ')))
    filey.close()
    return output_file

def save_txt(text,filename):
    filey = open(filename,"w")
    filey.writelines(text)
    filey.close()
    return filename


def load_json(filename):
    filey = open(filename,'r')
    json_obj = json.loads(filey.read())
    filey.close()
    return json_obj
