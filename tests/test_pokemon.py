#!/usr/bin/python

# Copyright (c) 2020 Vanessa Sochat

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

import os
import shutil
import pytest


def test_get_avatar(tmp_path):
    """test_write_read_files will test the functions write_file and read_file
    """
    from pokemon.skills import get_avatar

    avatar = get_avatar("vsoch", print_screen=False)
    assert avatar.endswith("vsoch")
    avatar = get_avatar("vsoch", include_name=False)
    assert not avatar.endswith("vsoch")


def test_get_pokemon(tmp_path):
    from pokemon.master import get_pokemon

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


def test_get_pokemon(tmp_path):
    from pokemon.master import catch_em_all

    catch = catch_em_all()
    assert len(catch) == 1030


def test_lookup_pokemon(tmp_path):
    from pokemon.master import lookup_pokemon

    catches = lookup_pokemon(field="name", value="Pikachu")
    assert len(catches) == 1


def test_get_trained(tmp_path):
    from pokemon.master import get_trainer

    trainer = get_trainer("vsoch")
    assert trainer == 43492090


def test_lookup_pokemon_and_formes(tmp_path):
    from pokemon.master import lookup_pokemon

    rotom = lookup_pokemon(field="name", value="Rotom")
    assert rotom["566"]["type"][0] == "electric"
    assert rotom["566"]["type"][1] == "ghost"

    # heat rotom is fire instead of ghost
    heat_rotom = lookup_pokemon(field="name", value="Rotom (Heat Rotom)")
    assert heat_rotom["567"]["type"][0] == "electric"
    assert heat_rotom["567"]["type"][1] == "fire"

    # wash rotom is water instead of ghost
    wash_rotom = lookup_pokemon(field="name", value="Rotom (Wash Rotom)")
    assert wash_rotom["568"]["type"][0] == "electric"
    assert wash_rotom["568"]["type"][1] == "water"

    # frost rotom is ice instead of ghost
    frost_rotom = lookup_pokemon(field="name", value="Rotom (Frost Rotom)")
    assert frost_rotom["569"]["type"][0] == "electric"
    assert frost_rotom["569"]["type"][1] == "ice"

    # fan rotom is flying instead of ghost
    fan_rotom = lookup_pokemon(field="name", value="Rotom (Fan Rotom)")
    assert fan_rotom["570"]["type"][0] == "electric"
    assert fan_rotom["570"]["type"][1] == "flying"

    # mow rotom is grass instead of ghost
    mow_rotom = lookup_pokemon(field="name", value="Rotom (Mow Rotom)")
    assert mow_rotom["571"]["type"][0] == "electric"
    assert mow_rotom["571"]["type"][1] == "grass"
