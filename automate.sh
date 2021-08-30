#!/bin/bash
#Automated script for build docker image and starting container
#Variable values are basically arbitrary

dockerimage=dimage
container=mysql-db
sql_pword=pw

echo -e "\e[1;36m Building Docker image:\e[0m" $dockerimage
sudo docker build -t $dockerimage .

echo -e "\e[1;36m Starting docker container:\e[0m" $container
sudo docker stop $container 2>&1 >/dev/null
sudo docker rm $container 2>&1 >/dev/null
sudo docker run -d -p 3306:3306 --name=$container -e MYSQL_ROOT_PASSWORD=$sql_pword $dockerimage

echo -e "\e[1;36m Container started \e[0m"
echo ""
echo -e "\e[1;36m Executing interactive container with bash terminal \e[0m"
sudo docker exec -it $container bash
