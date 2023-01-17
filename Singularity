BootStrap: docker
From: continuumio/miniconda3

#
# sudo singularity build pokemons Singularity
#

%runscript
    if [ $# -eq 0 ]
        then
        echo "Try one of these commands:"
        exec /opt/conda/bin/scif apps
    else
        exec /opt/conda/bin/scif "$@"
    fi

%files
    pokemon.scif

%post
    apt-get update

    /opt/conda/bin/pip install scif
    /opt/conda/bin/pip install pokemon
    /opt/conda/bin/scif install /pokemon.scif
