#!/bin/bash

#Automatically adds all relevant files+folders for staging.
#Remember to commit after!

#Database dump and then stage. The name of the container (i.e. mysql-db) shouldn't change.
#Note: The hyperopt database will be dumped into two places. Namely sclscripts and dbBackups. 
#sclscripts will form part of our git repo, but dbBackups will not. This will be a local directory to safeguard any potential corruptions
#by other team members.
#The entire mysql schema will also be backed-up (this is through the --all-databases command) but also only kept locally.


mkdir -p dbBackups
sudo docker exec mysql-db sh -c 'exec mysqldump hyperopt -uroot -ppw' >./sqlscripts/hyperopt.sql >./dbBackups/local_hyperopt_backup.sql  2> /dev/null 

sudo docker exec mysql-db sh -c 'exec mysqldump --all-databases -uroot -ppw' > ./dbBackups/dbBackup_complete.sql 2> /dev/null

git add sqlscripts/

#Source file staging
git add src/

#Miscellaneous
git add autodocker.sh
git add gitAuto.sh
git add Dockerfile
git add README.md

echo -e "Staging complete. Remember to commit now!\n"
echo -e "NOTE, do not manually add dbBackups to your commit. That is meant to be kept locally (i.e. not in our repo) just in case.\n"
