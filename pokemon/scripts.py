#!/usr/bin/env python

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

from pokemon.skills import get_ascii, get_avatar
from pokemon.master import get_pokemon, catch_em_all
from glob import glob
import argparse
import sys
import os


def main():
    parser = argparse.ArgumentParser(
        description="generate pokemon ascii art and avatars"
    )
    parser.add_argument(
        "--avatar",
        dest="avatar",
        help="generate a pokemon avatar.",
        type=str,
        default=None,
    )
    parser.add_argument(
        "--pokemon",
        dest="pokemon",
        help="generate ascii for a particular pokemon (by name)",
        type=str,
        default=None,
    )
    parser.add_argument(
        "--message",
        dest="message",
        help="add a custom message to your ascii!",
        type=str,
        default=None,
    )
    parser.add_argument(
        "--catch",
        help="catch a random pokemon!",
        dest="catch",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "--list",
        help="list pokemon available",
        dest="list",
        default=False,
        action="store_true",
    )
    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(0)

    if args.list is True:
        names = catch_em_all(return_names=True)
        print("\n".join(names))

    elif args.pokemon is not None:
        get_ascii(name=args.pokemon, message=args.message)

    # If the user wants to create an avatar
    elif args.avatar != None:
        get_avatar(args.avatar)

    elif args.catch == True:
        catch = get_pokemon()
        pid = list(catch.keys())[0]
        get_ascii(pid=pid, message=args.message)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
