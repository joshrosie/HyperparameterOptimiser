#!/bin/bash
#Automated script for build docker image, volume and starting container
#Values for Docker image, volume and container variables should be kept the same
#because other script files use these exact names to refer to the same image, container
#and volume.

dockerimage=dimage
container=mysql-db
volume=mysql-vol-cap
sql_pword=pw

#Checks to see if the specified image already exists.
if  sudo docker image ls -a $dockerimage | grep -Fq $dockerimage >/dev/null ; then
	
	#If the script is run without parameters, then the docker image is rebuilt.
	#NB by default image must be rebuilt because any changes made locally will not reflect
	#In the docker container if the image isn't rebuilt
	
	if [ -z "$1" ]; then
		
		echo -e "\e[1;36mRebuilding Docker image:\e[0m ${dockerimage}\n"
        	sudo docker build -t $dockerimage .
	
	#If the user however chooses to skip the build, then the image is not rebuilt.
	#One might choose to do this if they aren't currently changing source files locally.
	elif [ "$1" == skip ]; then
		echo -e "\e[1;36mImage <${dockerimage}> exists and build skipped.\e[0m\n"

		
	fi	

#If the image does not yet exist (i.e. in the case of it being run on a new machine or it was removed), build it.
else
	echo -e "\e[1;36mImage <${dockerimage}> doesn't exist. Building Docker image:\e[0m ${dockerimage}\n"
        sudo docker build -t $dockerimage .

fi


#Check to see if the docker volume exists. If it doesn't create it, otherwise do nothing.
if ( !(sudo docker volume ls -q | grep -q $volume >/dev/null) ) ; then
	docker volume create $volume >/dev/null
	echo -e "\e[1;36mCreated docker volume:\e[0m ${volume}\n"
	
else
	echo -e "\e[1;36mUsing docker volume:\e[0m ${volume}"	
fi

#Checks to see if the mysql container has already been created. If it is, then it needs to be stopped and removed before restarting it.
if sudo docker ps -a --format '{{.Names}}' | grep -Eq "^${container}\$"; then
#if sudo docker ps -a --format '{{.Names}}' | grep -Fq $container ; then
        echo -e "\e[1;36mContainer <${container}> already exists. Stopping and removing it first.\e[0m\n"
        sudo docker stop $container >/dev/null
        sudo docker rm $container >/dev/null

fi


#The port number stuff might need to be changed (could cause an error if the client has a container running on that port.
echo -e "\e[1;36mStarting docker container:\e[0m" $container

sudo docker run -d -p 3310:3310 --name=$container -v $volume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=$sql_pword $dockerimage

echo -e "\e[1;36mContainer started \e[0m\n"

echo -e "\e[1;32mExecuting interactive container with bash terminal\n\n 
If you haven't yet already, please see README.md file for steps on how to run our program.
\nIt is available in this current directory (type more README.md)\n\n\e[0m"

sudo docker exec -it $container bash