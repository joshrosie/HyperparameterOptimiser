#!/bin/bash

#Short script to update the DB stored on the docker volume with
#the one that has been pulled from the repo.

if sudo docker ps -a --format '{{.Names}}' | grep -q "mysql-db"; then

	sudo docker start mysql-db > /dev/null
	sudo docker exec -i mysql-db sh -c 'exec mysql -uroot -ppw hyperopt' <./sqlscripts/hyperopt.sql

	echo -e "\e[1;36mHyperopt database in docker container has been restored\nfrom hyperopt.sql database stored in sqlscripts.\e[0m\n"

else
	echo -e "\e[1;36mmysql-db container does not exist. 
Please first run ./autodocker.sh and then you can use this script.\e[0m\n"

fi


