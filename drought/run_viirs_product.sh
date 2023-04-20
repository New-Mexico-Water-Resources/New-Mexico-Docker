#!/usr/bin/env bash
echo "starting VIIRS product generation container"
New-Mexico-VIIRS-Server --working /new_mexico_VIIRS --static /static --GEOS5FP /GEOS5FP --LANCE /LANCE --SRTM /SRTM --output /VIIRS_output
