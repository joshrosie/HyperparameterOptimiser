#!/bin/bash

#Short script to update the DB stored on the docker volume with
#the one that has been pulled from the repo.

sudo docker start mysql-db > /dev/null
sudo docker exec -i mysql-db sh -c 'exec mysql -uroot -ppw hyperopt' <./sqlscripts/hyperopt.sql

echo -e "\e[1;36mHyperopt database in docker container has been restored\nfrom hyperopt.sql database stored in sqlscripts.\e[0m\n"