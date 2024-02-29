FROM condaforge/mambaforge as linux

ENV APP_ROOT /drought

# update Ubuntu package manager
RUN apt-get update
RUN apt-get -y install gcc g++
# install fish shell
RUN apt-add-repository ppa:fish-shell/release-3; apt-get -y install fish; chsh -s /usr/local/bin/fish; mamba init fish

FROM linux as mamba

# install dependencies
# install dependencies
RUN mamba update -y mamba
RUN mamba update -y --all
RUN mamba install -y -c conda-forge "python=3.10"
RUN mamba install -y -c conda-forge cython gdal pygrib pyresample wget
RUN pip install astropy beautifulsoup4 cmake python-dateutil descartes ephem geopandas h5py imageio imageio-ffmpeg jupyter keras matplotlib mgrs netcdf4 nose pip pycksum pygrib pyhdf pyresample pysolar pystac-client rasterio requests scikit-image sentinelsat setuptools shapely spacetrack tensorflow termcolor untangle urllib3 xmltodict

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
