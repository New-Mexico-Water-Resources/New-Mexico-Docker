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

# install Google Drive
RUN add-apt-repository ppa:alessandro-strada/ppa; apt-get update; apt-get install -y google-drive-ocamlfuse

# install mamba dependencies
RUN pip install area django django-crispy-forms django-pymemcache geojson geopandas gunicorn h5py pydrive2 pytz rasterio scipy seaborn termcolor tk

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
