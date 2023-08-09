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

# # install gunicorn server
# RUN mamba install -y -c conda-forge gunicorn
# # install Django server
# RUN mamba install -y -c conda-forge django
# RUN mamba install -y -c conda-forge pytz
# # install Django forms
# RUN pip install django-crispy-forms

# # install water rights visualizer
# RUN mamba install -y geojson
# RUN mamba install -y geopandas
# RUN mamba install -y h5py
# RUN mamba install -y rasterio
# RUN mamba install -y seaborn
# RUN mamba install -y termcolor
# RUN mamba install -y tk
# RUN pip install area

# install Google Drive
RUN add-apt-repository ppa:alessandro-strada/ppa; apt-get update; apt-get install -y google-drive-ocamlfuse

# install mamba dependencies
# RUN mamba install -y -c conda-forge django geojson geopandas gunicorn h5py pytz rasterio seaborn termcolor tk
RUN pip install area django django-crispy-forms django-pymemcache geojson geopandas gunicorn h5py pydrive2 pytz rasterio scipy seaborn termcolor tk

# install pip dependencies
# RUN pip install area django-crispy-forms
# RUN pip install django-pymemcache

# install water rights dependencies
# install dependencies
# RUN mamba install -y geojson geopandas h5py pydrive2 rasterio seaborn termcolor tk
# RUN pip install area pydrive2

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
