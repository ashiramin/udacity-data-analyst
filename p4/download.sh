#!/bin/bash
wget https://s3.amazonaws.com/metro-extracts.mapzen.com/austin_texas.osm.bz2 -O data/austin_texas.osm.bz2

bzip2 -d data/austin_texas.osm.bz2
