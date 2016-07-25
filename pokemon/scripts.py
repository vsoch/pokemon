#!/usr/bin/env python

'''
script.py: part of pokemon-ascii package

'''

from pokemon.skills import get_ascii, get_avatar
from pokemon.master import get_pokemon
from glob import glob
import argparse
import sys
import os

def main():
    parser = argparse.ArgumentParser(
    description="generate pokemon ascii art and avatars")
    parser.add_argument("--avatar", dest='avatar', help="generate a pokemon avatar for some unique id.", type=str, default=None)
    parser.add_argument("--pokemon", dest='pokemon', help="generate ascii for a particular pokemon (by name)", type=str, default=None)
    parser.add_argument("--message", dest='message', help="add a custom message to your ascii!", type=str, default=None)
    parser.add_argument('--catch', help="catch a random pokemon!", dest='catch', default=False, action='store_true')
    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(0)

    # If the user wants to generate ascii for a pokemon
    if args.pokemon != None:
        get_ascii(name=args.pokemon,message=args.message)

    # If the user wants to create an avatar
    elif args.avatar != None:
        get_avatar(args.avatar,print_screen=True,include_name=True)    

    elif args.catch == True:
        catch = get_pokemon()
        get_ascii(pid=catch.keys()[0],message=args.message)

if __name__ == '__main__':
    main()
