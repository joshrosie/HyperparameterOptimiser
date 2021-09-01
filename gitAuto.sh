#!/bin/bash

#Automatically adds all relevant files+folders for staging.
#Remember to commit after!

#Database dump and then stage. The name of the container (i.e. mysql-db) shouldn't change.
#Note: The hyperopt database will be dumped into two places. Namely sclscripts and dbBackups. 
#sclscripts will form part of our git repo, but dbBackups will not. This will be a local directory to safeguard any potential corruptions
#by other team members.
#The entire mysql schema will also be backed-up (this is through the --all-databases command) but also only kept locally.

#Dump for git repo (this will be shared with the whole team) then stage
sudo docker exec mysql-db sh -c 'exec mysqldump hyperopt -uroot -ppw' >./sqlscripts/hyperopt.sql 2> /dev/null
git add sqlscripts/

#Dump for local (not shared with team, just in case of a problem)
mkdir -p dbBackups
sudo docker exec mysql-db sh -c 'exec mysqldump hyperopt -uroot -ppw' >./dbBackups/local_hyperopt_backup.sql  2> /dev/null 

sudo docker exec mysql-db sh -c 'exec mysqldump --all-databases -uroot -ppw' > ./dbBackups/dbBackup_complete.sql 2> /dev/null

#Source file staging
git add src/

#Miscellaneous
git add autodocker.sh
git add gitAuto.sh
git add Dockerfile
git add README.md
git add updateLocalHyperDB.sh

echo -e "\e[1;36mStaging complete. Remember to commit now!\n"
echo -e "NOTE, do not manually add dbBackups to your commit. That is meant to be kept locally (i.e. not in our repo) just in case.\e[0m\n"
