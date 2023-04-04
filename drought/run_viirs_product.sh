#!/usr/bin/env bash
echo "starting VIIRS product generation container"
watch -n 10800 /drought/process_viirs_tiles.sh
tail -F anything