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

import json
import os


def get_installdir():
    """get_installdir
       returns installation directory of pokemon
    """
    return os.path.dirname(os.path.abspath(__file__))


def save_json(json_obj, output_file):
    with open(output_file, "w") as filey:
        filey.write(
            json.dumps(json_obj, sort_keys=True, indent=4, separators=(",", ": "))
        )
    return output_file


def save_txt(text, filename):
    with open(filename, "w") as filey:
        filey.writelines(text)
    return filename


def load_json(filename):
    with open(filename, "r") as filey:
        json_obj = json.loads(filey.read())
    return json_obj
