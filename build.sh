#!/bin/bash
docker build -t error_master .
docker run -it --name error_master -p "31337:80" error_master