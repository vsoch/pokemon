#!/usr/bin/python

# Copyright (c) 2020-2023 Vanessa Sochat

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# UTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pytest

from pokemon.master import catch_em_all, get_pokemon, get_trainer, lookup_pokemon
from pokemon.skills import get_avatar


def test_get_avatar(tmp_path):
    """
    test_write_read_files will test the functions write_file and read_file
    """
    avatar = get_avatar("vsoch", print_screen=False)
    assert avatar.endswith("vsoch")
    avatar = get_avatar("vsoch", include_name=False)
    assert not avatar.endswith("vsoch")


def test_get_pokemon(tmp_path):
    with pytest.raises(SystemExit):
        catch = get_pokemon(name="doesntexist")

    catch = get_pokemon(name="Pikachu")
    assert "25" in catch
    for param in [
        "abilities",
        "ascii",
        "height",
        "id",
        "link",
        "name",
        "type",
        "weight",
    ]:
        assert param in catch["25"]
    assert str(catch["25"]["id"]) == "25"

    # These should return same pokemon
    repeat = get_pokemon(pid="25")
    assert repeat == catch
    repeat = get_pokemon(pid=25)
    assert repeat == catch


def test_catch_pokemon(tmp_path):

    # Updated at Gen9
    catch = catch_em_all()
    assert len(catch) == 1008


def test_lookup_pokemon(tmp_path):

    catches = lookup_pokemon(field="name", value="Pikachu")
    assert len(catches) == 1


def test_get_trained(tmp_path):
    trainer = get_trainer("vsoch")
    assert trainer == 43492090
