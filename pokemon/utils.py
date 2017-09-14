import json
import os

def get_installdir():
    '''get_installdir
       returns installation directory of pokemon
    '''
    return os.path.dirname(os.path.abspath(__file__))


def save_json(json_obj,output_file):
    with open(output_file,'wb') as filey:
        filey.write(json.dumps(json_obj, sort_keys=True,indent=4, separators=(',', ': ')))
    return output_file

def save_txt(text,filename):
    with open(filename,"w") as filey:
        filey.writelines(text)
    return filename


def load_json(filename):
    with open(filename,'r') as filey:
        json_obj = json.loads(filey.read())
    return json_obj
