#!/usr/bin/env bash
echo "starting VIIRS product generation container"
cd /drought
git pull
make reinstall-soft
cd /new_mexico_VIIRS
New-Mexico-VIIRS-Server --working /new_mexico_VIIRS --static /static --GEOS5FP /GEOS5FP --LANCE /LANCE --SRTM /SRTM --output /VIIRS_output
