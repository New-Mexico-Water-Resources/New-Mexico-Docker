FROM condaforge/mambaforge as linux

ENV APP_ROOT /drought

# update Ubuntu package manager
RUN apt-get update
RUN apt-get -y install gcc
# install fish shell
RUN apt-add-repository ppa:fish-shell/release-3; apt-get -y install fish; chsh -s /usr/local/bin/fish; mamba init fish

FROM linux as mamba

# install dependencies
# install dependencies
RUN mamba update -y mamba
RUN mamba update -y --all
RUN mamba install -y "python=3.9"
RUN mamba install -y pygrib
RUN mamba install -y python-dateutil
RUN mamba install -y wget
RUN mamba install -y xtensor xtensor-python
RUN mamba install -y "gdal>3.1" "rasterio>1.0.0" "setuptools!=58" "shapely<2.0.0" "tensorflow!=2.11.0"
RUN pip install astropy beautifulsoup4 cmake descartes ephem geopandas h5py imageio imageio-ffmpeg jupyter keras matplotlib mgrs netcdf4 nose pip pycksum pygeos pyhdf pyresample pysolar pystac-client requests scikit-image sentinelsat spacetrack termcolor untangle urllib3 xmltodict

FROM mamba as toolbox

WORKDIR /
RUN git clone https://github.com/New-Mexico-Water-Resources/ET-Toolbox-Product-Generator.git
WORKDIR /ET-Toolbox-Product-Generator/ETtoolbox
ADD spacetrack_credentials.txt /ET-Toolbox-Product-Generator/spacetrack_credentials
ADD ERS_credentials.txt /ET-Toolbox-Product-Generator/ERS_credentials
WORKDIR /ET-Toolbox-Product-Generator
RUN python setup.py install
WORKDIR /

# install app
RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}
ADD . ${APP_ROOT}
