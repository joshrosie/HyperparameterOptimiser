#!/bin/bash
#Automated script for build docker image, volume and starting container
#Values for Docker image, volume and container variables should be kept the same
#because other script files use these exact names to refer to the same image, container
#and volume.

dockerimage=dimage
container=mysql-db
volume=mysql-vol-cap
sql_pword=pw

#Flag variables
wcard=''
timeout=2
interactive='false'
updateLocalDB='false'
freshImage='false'

#Help message if the user misuses the script.
print_usage() {
	printf "\nUSAGE:
./autorun.sh [options]\n
OPTIONS:
-w : ARG\tProblem wcard, no default value. Must be specified if -i flag not passed
-t : ARG\tTimeout for CarlSAT, default = 2. Should be specified along with -w flag.
-i\t\tEnable run container interactively, default = false. Must be specified if not passing -w and -t flag.
-u\t\tUpdate local hyperopt database with gitLab synched sqlscripts/hyperopt.sql DB, default = false
-f\t\tRemove associated docker image and rebuild from scratch. i.e. docker image is purged\n
NOTE:
The -i flag is mutually exclusive from the -w and -t flags. The -i flag will not directly call the Wrapper class
as interactive mode is intended for development and debugging. Passing in the -w and -t flags will run the container as a Daemon
and call the Wrapper class directly with relevant output being printed to console.\n 
EXAMPLES:
./autorun.sh -w test1.wcard -t 2 -f -u 
./autorun.sh -i\n"
}

#If the user doesn't pass any options.
if [ $# -eq 0 ]; then
   print_usage
   exit 1
fi



while getopts :w:t:ifu flag; do
	case "${flag}" in
    	w) wcard=${OPTARG}
    		;;
    	t) timeout=${OPTARG}
    		;;
		i) interactive='true'
			;;
		f) freshImage='true'
			;;
		u) updateLocalDB='true'
			;;
    	*) echo "Invalid option: -$flag"
			print_usage
			exit 1
			;;
	esac
done

#Checks if the user tried to run with interactive mode enabled as well as specified a wcard

if ( [ "$interactive" == 'true' ] ) && ( [ -n "$wcard" ] ) ; then
	print_usage
	echo -e "\n\e[1;31mUSAGE ERROR: Script can't be called with interactive mode set to true AND having specified a wcard\e[0m\n"
	exit 1
fi

#Checks if the user tried to run in non-interactive mode, but didn't specify a problem card.

if ( [ "$interactive" == 'false' ] ) && ( [ -z "$wcard" ] ) ; then
	print_usage
	echo -e "\n\e[1;31mUSAGE ERROR: If not running in interactive mode, please specify -w wcard\e[0m\n"
	exit 1
fi

if [ "$freshImage" == 'true' ] ; then
	sudo docker stop $container >/dev/null
    sudo docker rm $container >/dev/null
	sudo docker image rm dimage
fi

sudo docker build -t $dockerimage .


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

if [ $updateLocalDB == 'true' ] ; then
	echo -e "\e[1;36mUpdate local DB specified\e[0m\n"
	sudo docker exec -i mysql-db sh -c 'exec mysql -uroot -ppw hyperopt' <./sqlscripts/hyperopt.sql

	echo -e "\e[1;36mHyperopt database in docker container has been restored\nfrom hyperopt.sql database stored in sqlscripts.\e[0m\n"
fi

if [ $interactive == 'true' ] ; then
	echo -e "\e[1;32mExecuting interactive container with bash terminal\n 
If you haven't yet already, please see README.md file for steps on how to run our program.
It is available in this current directory (type more README.md)\n\n\e[0m"

	
	sudo docker exec -it $container bash

else
	
	#need to work out how to run docker container in non-interactive mode but still pipe out console output
fi