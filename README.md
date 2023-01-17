# pokemon

Watch the pokemon ascii being born!

![img/generation.gif](https://github.com/vsoch/pokemon/raw/master/img/generation.gif)

This is a module for generating ascii art for any of the 890 pokemon, across 8 generations, in the Pokedex. The package includes functions for generating "gravatars" (pokemon associated with an identifier like an email address), and functions for searching and exploring the database. The library includes a [version of the database](pokemon/database/db.json) generated with [pokemon/make_db.py](pokemon/make_db.py) that can be updated by re-running the script. The choice of ascii art is to produce pokemon images or avatars that are suited for command line tools.

```bash
$ pokemon
usage: pokemon [-h] [--avatar AVATAR] [--pokemon POKEMON] [--message MESSAGE]
               [--catch] [--list]

generate pokemon ascii art and avatars

optional arguments:
  -h, --help         show this help message and exit
  --avatar AVATAR    generate a pokemon avatar for some unique id.
  --pokemon POKEMON  generate ascii for a particular pokemon (by name)
  --message MESSAGE  add a custom message to your ascii!
  --catch            catch a random pokemon!
  --list             list pokemon available
```

## Installation

You can install directly from pip:

```bash
$ pip install pokemon
```

or for the development version, clone the repo and install manually:

```bash
git clone https://github.com/vsoch/pokemon
cd pokemon
pip install .
```

## Produce an avatar

An "avatar" is an image that is consistently associated with some unique ID. In our case, this is an ascii avatar. For example,

![img/avatar.png](img/avatar.png)

To do this, I take the hash of a string, and then use modulus to get the remainder of that hash divided by the number of pokemon in the database. This means that, given that the database doesn't change, and given that the pokemon have unique IDs in the range of 1 to 721, you should always get the same image for some unique id (like an email).

**Note** the database was updated between version 0.34 and version 0.35, so you will
get different avatars depending on the version you are using. There are Docker tags
and pip installs available for each, and version 0.35 is suggested to use with Python 3.

```bash
$ pokemon --avatar vsoch

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@?:::::::::::::::+.+.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@*?%:::::::::*::****#SSSSS%.**S+@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@*???:::::::*********#...+****++++S:@@@@@@@@@@@@@@@@@@
@@@@@@@::SSS............S+.*....*****?%S+#@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@.?SS.S.....S?%%%%%%%%..**+....?@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@..%???????#%%%%%%%....**++.....?@@@@@@@@@@@@
@@@@@@@@@@@@@@..+++%????????????%%%%%%*.......%++%@@@@@@@@@@
@@@@@@@@@@@@S.+++++S%+++SS%..????%%%?..............@@@@@@@@@
@@@@@@@@@@@%++++S+S++++.......?@%%%%%......SSSSSS:@@@@@@@@@@
@@@@@@@@@?.++.+++++%**.#.....?.%%%%%,@@@@@@@@@@@#.%@@@@@@@@@
@@@@@@@?.*.....+.**.*.....%.....+++%@@#+++S.%?+++.%@@@@@@@@@
@@@@@#***......%:.**++%........++++#.#+++++.++++.S@@@@@@@@@@
@@@@,+%.......?+++++......#....#.**+++#@@%++++.SS@@@@@@@@@@@
@@@:+?+...?..S.......S%%%...S+++::.+++@%++++.?.#@@@@@@@@@@@@
@@@@@@@,?...S%%*@@.?%++SS.S++.+S...?#.+++S++..@@@@@@@@@@@@@@
@@@@@@@@@@@@@@*...?.@SS+.SS....?....#++%:+..S@@@@@@@@@@@@@@@
@@@@@@@@@@?+S.%?#+@@@@@S...#???%%%S@+:::...@@@@@@@@@@@@@@@@@
@@@@@@@++S....#@@@@@@@@@@@@@@@S.%...:::+#...@@@@@@@@@@@@@@@@
@@@@#++.....S@@@@@@@@@@@@@.S..++..%?:...+?...@@@@@@@@@@@@@@@
@@@.......?@@@@@@@@@@@@+.....+++......#.++....*@@@@@@@@@@@@@
@@.*+...@@@@@@@@@@@@S.....?.S+..S....++...S....@@@@@@@@@@@@@
@+*++@@@@@@@@@@@@,?........@:%.*SS?+++++..+.....%@@@@@@@@@@@
@:+%@@@@@@@@@@@:?........?@@@#:::.+++++#...+.....#@@@@@@@@@@
@S@@@@@@@@@@@@+.........#@@@@@@+..++++....+......S.,@@@@@@@@
@@@@@@@@@@@@@S%##.....S@@@@@@@@@*.??.......#@%...??.#@@@@@@@
@@@@@@@@@@@@@S%@....?S@@@@@@@@@@@@@%.?...?.@@@.S+.....@@@@@@
@@@@@@@@@@@@@@@@S.....?@@@@@@@@@@@@@@@.%S.?@@@@+++S....@@@@@
@@@@@@@@@@@@@@@@+......@@@@@@@@@@@@@@@@@@@@@@@@.+++S....@@@@
@@@@@@@@@@@@@@@.%......@@@@@@@@@@@@@@@@@@@@@@@@@++++......@@
@@@@@@@@@@@@@@.%......S@@@@@@@@@@@@@@@@@@@@@@@@@++++......@@
@@@@@@@@@@@@@S.#.....++@@@@@@@@@@@@@@@@@@@@@@@@@..+..+....S@
@@@@@@@@@@@.::++S.@@?+?@@@@@@@@@@@@@@@@@@@@@@@@@+...#S+?..SS
@@@@@@@@@@@@,@,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.+..*++,@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.::+@@

vsoch
```

You can also use the functions on command line:

```python
from pokemon.skills import get_avatar

# Just get the string!
avatar = get_avatar("vsoch", print_screen=False)
print(avatar)

# Remove the name at the bottom, print to screen (default)
avatar = get_avatar("vsoch", include_name=False)
```

## List Pokemon
Want a complete listing of your Pokemon choices in the database?

```bash
pokemon --list

Slugma
Machop
Druddigon
Magby
Clawitzer
Growlithe
Empoleon
Dusknoir
Rhydon
Krookodile
Hoppip
Swellow
Oddish
Scrafty
Boldore
Pancham
Beheeyem
Honedge
...
Jumpluff
Rotom
Frillish
Lapras
Clamperl
Wingull
Vespiquen
Keldeo
Mareep
Phantump
Medicham
Shuckle
Lickitung
Chingling
```

You could use this to parse through a function. Here we show a simple loop to print the name of the Pokemon, but you would be more creative!

```bash
for gotcha in $(pokemon --list)
    do
    echo $gotcha
done
```

## Randomly select a Pokemon

You might want to just randomly get a pokemon! Do this with the `--catch` command line argument!

```bash
      pokemon --catch

      @%,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      .????.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      .???????S@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      :?????????#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      *?????????????*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @???????#?????###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,*.??#
      @?????,##,S???#####@@@@@@@@@@@@@@@@@@@@@@@@@@S##????????????
      @?????*,,,,,,########@@@@@@@@@@@@@@@@@:###????????????????#@
      @##????,,,,,,,,,#####@@@@@@@@@@@@@.######?????#?:#????????@@
      @####?#,,,,,,,,,,,##@@@@@@@@@@@@@@#######*,,,,,*##+?????+@@@
      @######,,,,,,,,,,,S@@@@@@@@@@@@@@#.,,,,,,,,,,,,,,:?####@@@@@
      @######,,,,,,,,,,%@@,S.S.,@@@@@@@,,,,,,,,,,,,,,,######@@@@@@
      @@#####,,,,,,,,.,,,,,,,,,,,,,,,*#,,,,,,,,,,,,,.#####:@@@@@@@
      @@@@@@@@@@.#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,######@@@@@@@@@
      @@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,+######@@@@@@@@@@
      @@@@@@@@%,,,,,++:,,,,,,,,,,,,,,,,,,,,,@@:.######:@@@@@@@@@@@
      @@@@@@@:,,,:##@@@#,,,,,,,,,,,,?@S#,,,,,,@@@@@@@@@@@@@@@@@@@@
      @@@@@@@?,,,#######,,,,,,,,,,,#.@:##,,,:?@@@@@@@@@@@@@@@@@@@@
      @@@@@@@.,,S,??%?*,,,,,,,,,,,,####?%+,::%@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@?..*+,,,,,,*,,,,,,,,,,,+#S,::::*@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@%..*,,,,,,,,,,,,,,,,,,,:.*...%@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@.**::*::::::,,:::::::+.....@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@.@@@@?:**:::*::::::::::*...@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@?,,,,,,,,,:,##S::::**:::S#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@.,,,,,,:S#?##?########:#****#,@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@,%:*%,??#,,,,:*S##**:..****:,.*@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@+,,,,,,,,,,,,,,,,,,*...*:,.,@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@+,,,,,,,,,,,,,,,,,,?@@@@@*#?@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@*,,,,,,,,,,,,,,,,,,.@#########?@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@.*:,,,,,,,,,,,,,,:.##%,?#####????:@@@@@@@@@@@@@
      @@@@@@@@@@@@@@?.....*******....S@@@@@@:##?????@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@S.+..********...#%@@@@@@@@@##,@@@@@@@@@@@@@@@@
      @@@@@@@@@@@#*,,,,*.#@@@@@@@..*:,,*S@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@+@,%,,,#@@@@@@@@@@,S,,,%,,:@@@@@@@@@@@@@@@@@@@@@@@

      Pichu
```
You can equivalently use the `--message` argument to add a custom message to your catch!

```bash
      pokemon --catch --message "You got me!"

      @@@@@@@@@*.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@...+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@++++@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      :..+,@@+.+++%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @..++++S++++++.?...@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@:S.S+SSS.S%++.+++@@@@@@@@@@+.%.@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@:SSSSSSSSSS,@@@@@@@,:,:.SS+.....+.@@@@@@@@@@@@@@@@@@@@@@
      @@@@,:%SS++SS.,.%,:,S,,,,+..%.........S.@@@@@@@@@@@@@@@@@@@@
      @@@@@,:*...:,,+,.,,,,,,,*%%%++++..+++SSS+@@@@@@@@@@@@@@@@@@@
      @@@@@@,,.....%:,,,:.:.,:.%%.SSSS++SS+%+S%,+@@@@@@@@@@@@@@@@@
      @@@@@@@*.....S...***+,,,%..%++,?SSS.%.%%%:,.,@@@@@@@@@@@@@@@
      @@@@@@@@,+**........,,,,....++S@,+%..#..%,,S..@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@*..:,,,,,%..%++S%%.%%.S%%,,*+.+@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@S,,,,,,,,,%%%..SS..%?%%%,,,S+...@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@S.:::::::::%.%%S...%%%%:::*.....**@@@@@@@@@@
      @@@@@@@@@@@@@@@@.%%..:::::::S%%.?%%%%%:::....**,S,,:@@@@@@@@
      @@@@@@@@@@@@@@:::*%%%%?..*:::,.%%%%.,:*.%@@.*:,,,:,,S@....@@
      @@@@@@@@@@@@@:,:,::*.?%%%%%%?+*%%?.?%%%%%+@@,,,,,,,.++%++@@@
      @@@@@@@@@@@@@@*,,,,,**...*%%%%%%%%%%?++++++.@,,,,,SS+SS++@@@
      @@@@@@@@@@@@@,,.,S,,,,:....***%%?%++++++++++.@.,,+SSSSS.S+@@
      @@@@@@@@@@@@,,SSSS..:.%,:*..?%%??%%++++++.+S+@@@.S..%S.%.S++
      @@@@@@@@@@@,,S.....S::*.@@@%%%%@?%%#+++++%%%?S@@@@@.%.,@@...
      @@@@@@@@@@@:,,?.%%%::::@@@...%.@?.%.++++.+%%%%.@@@@..++@@@@@
      @@@@@@@@@@S,.%%.:,,,,,S@@@@@.?@@+SS,S..........@@@@@,@@@@@@@
      @@@@@@@@@@@+S...++.,,:@@@@@@@@@@@@@@@%....SSS+SS@@@@@@@@@@@@

      You got me!
```

You can also catch pokemon in your python applications. If you are going to be generating many, it is recommended to load the database once and provide it to the function, otherwise it will be loaded each time.

```bash
from pokemon.master import catch_em_all, get_pokemon

pokemons = catch_em_all()
catch = get_pokemon(pokemons=pokemons)
```

The catch is a dictionary, with keys as the pokemon ID, and the value being another dictionary with various meta data (height, weight, japanese, link, ascii, etc).


## Updating the database

The database was generated by running the script make_db.py, and you can update it by running it yourself, if at some point in the future new pokemon are added to the index.

```bash
git clone https://github.com/vsoch/pokemon
cd pokemon
cd scripts
pip install -r requirements.txt
python make_db.py
```

Then move your old database (and you can do this to keep it in case you don't want changes to persist):

```bash
mv pokemon/database dbbackup
mv ./database pokemon/database
```

The file pokemons.json will be saved under [pokemon/databases](pokemon/databases). Next, install as usual.

```
python setup.py install
```

## Docker
You can also use the [Docker image](https://hub.docker.com/r/vanessa/pokemon/),
which provides the various functions and [Scientific Filesystem](https://sci-f.github.io) apps.
The 0.35 tag was developed with Python 2, and the 0.35 tag is Python 3 and later
(with an updated database).

What can I do?

```bash
docker run vanessa/pokemon apps
      list
     catch
    avatar
```

Give me my avatar!

```bash
docker run vanessa/pokemon run avatar vsoch
```

Catch a random Pokemon

```bash
docker run vanessa/pokemon run catch
```

What Pokemon can I catch?

```bash
docker run vanessa/pokemon run list
```

Catch me Venusaur!

```bash
docker run vanessa/pokemon run catch Venusaur
```

You can also build the image locally:

```bash
docker build -t vanessa/pokemon .
```

## Singularity

We can do the same with Singularity containers!


```bash
sudo singularity build pokemons Singularity
```

What can I do?

```bash
./pokemons apps
    avatar
     catch
      list
```

Give me my avatar!

```bash
./pokemons run avatar vsoch
```

Catch a random Pokemon

```bash
./pokemons run catch
```

What Pokemons can I catch?

```bash
./pokemons list
...
Phantump
Trevenant
Pumpkaboo
Gourgeist
Bergmite
Avalugg
Noibat
Noivern
Xerneas
Yveltal
Zygarde
Diancie
Hoopa
Volcanion
```

Catch a specific Pokemon

```bash
./pokemons run catch Pikachu
[catch] executing /bin/bash /scif/apps/catch/scif/runscript Pikachu
@@@@@@@@@@@@@.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@,??@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@.###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@,##:,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*?@@
@@@@@@@@@#::::@@@@@@@@@@@@@@@@@@@@@@@@@,*.???%@@@@@@@@*,,,@@
@@@@@@@@::,,::@@@@@@@@@@@@@@@@@@%:,,:#####??,@@@@@@*,,,,,,:@
@@@@@@@@%:,,:.@@@@@@@@@@@@@@.:::::::.#####@@@@@@@.::,,,,,::@
@@@@@@@@%::::.,,,,:,:%@@:,:::::::::S###@@@@@@@@%,:::::,::,:%
@@@@@@@@.S,,,,,,,,::::::::::::::::?@@@@@@@@@@?::::::::::::::
@@@@@@@:,,,,,,,:,#.#?::::::+.,@@@@@@@@@@@@@.::::::::::::::::
@@@@@,#:S,,:,::::*#.,:::::::*@@@@@@@@@@@@,::::::::::::::::+@
@@@@@:%S::::::*,,:::...+.::::S@@@@@@@@@@:::::::::::::::%@@@@
@@@@*.::::,SSSS%::::+++++:::::%@@@@@@@@:::::::::::::%@@@@@@@
@@@@@.+:,,::S%+S::::.+++:::::::,@@@@@@@@@:::*::::S@@@@@@@@@@
@@@@@@.S:::::.*.::::::::::::::::@@@@@@@@@,****%@@@@@@@@@@@@@
@@@@@@@@.:::::::::::::::*:,**::::,@@@@@@@@,***@@@@@@@@@@@@@@
@@@@,%,::::::::::::::::*.****::,:S%@@@@@@......@@@@@@@@@@@@@
,**::::,,,,,,:::::::::::+:**:::::,::@@?.....S@@@@@@@@@@@@@@@
%:*:,:::,,,,,,,,,,,::::::%::::::,,,::,@S..+@@@@@@@@@@@@@@@@@
@@@@@,S%+::*,:,,::,:,,,,::::::::::::::?@@%SS?@@@@@@@@@@@@@@@
@@@@@@@@@@@@.:,,,,:,,,,,,,:::::::::::::+SSSSS.@@@@@@@@@@@@@@
@@@@@@@@@@@@@:,,,:::::,::::,:::::::::::*?.@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@+,:,:,::::::::::,,::,::::**.SS@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@S,,:,,,,::::::::::::::::****@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@:::::::::****::::::*******S@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@**********.%..***********@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@,?+S%@@@@@@@@@@@@......@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@+..*@@@@@@@@@@@@@:+**@@@@@@@@@@@@@@@@@@@@
```


## Issues and updates

Would you like different or updated functionality?
Please ping me by adding an [issue](https://github.com/vsoch/pokemon/issues)!
I did this for fun, might sneak it into a few command line applications,
and it's pretty simple so far! I hope you have fun with it! :D
