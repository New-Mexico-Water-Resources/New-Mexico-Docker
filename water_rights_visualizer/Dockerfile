FROM condaforge/mambaforge as base

ENV APP_ROOT /app

# update Ubuntu package manager
RUN apt-get update
RUN apt update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata
RUN apt install -y software-properties-common

# install fish shell
RUN apt-add-repository ppa:fish-shell/release-3; apt-get -y install fish; chsh -s /usr/local/bin/fish; mamba init fish

FROM base as environment

# install javascript
RUN apt-get -y install nodejs npm

# install dependencies
RUN mamba install -y -c conda-forge "python=3.10"
RUN mamba install -y -c conda-forge gdal pygeos pygrib pyresample
RUN mamba install -y cython
RUN pip install area geojson geopandas h5py pydrive2 rasterio seaborn termcolor tk

FROM environment as backend

# install water rights visualizer
WORKDIR /
RUN git clone https://github.com/New-Mexico-Water-Resources/Water-Rights-Visualizer.git
WORKDIR /Water-Rights-Visualizer
ADD google_drive_key.txt /Water-Rights-Visualizer
ADD client_secrets.json /Water-Rights-Visualizer
RUN python setup.py install
WORKDIR /

FROM backend as frontend

# install web user interface
RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}

ADD . ${APP_ROOT}
