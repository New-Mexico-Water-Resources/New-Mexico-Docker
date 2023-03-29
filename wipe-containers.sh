#!/usr/bin/env bash
docker rm -f $(docker ps -a -f status=exited -q)
