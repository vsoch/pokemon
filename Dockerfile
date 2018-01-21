FROM continuumio/miniconda3

# docker build -t vanessa/pokemon .
# docker run vanessa/pokemon --avatar vsoch

ADD pokemon.scif /
RUN /opt/conda/bin/pip install scif
RUN /opt/conda/bin/scif install /pokemon.scif
RUN /opt/conda/bin/pip install pokemon
ENTRYPOINT ["scif"]
