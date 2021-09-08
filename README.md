# Capstone-Project

CSC3002S Capstone Project
Group:
	RSNJOS005 - Josh Rosenthal
	FSHJAR002 - Jarred Fisher
	WLSKIE001 - Kiera Wilson

Instructions for Dockerfile build and running the project:

	To build the docker environment, run the script autodocker.sh
	This can easily be done by typing the following in the project
	directory: ./autodocker.sh

	NOTE 1: The script will search for a docker image by the name of "dimage"
	and if it does not find it, it will build the image from the
	dockerfile always regardless of parameters passed to the script.

	NOTE 2: By default, even if an image is present it'll still be
	rebuilt. This is because any changes made to the source files would
	not reflect in the docker environment if the image wasn't rebuilt.

	However, you can force the script to skip rebuilding the image by running the script
	as follows: ./autodocker.sh skip
	The use case for this would be if you haven't made any changes to
	the source files and just want to run the project as is.

Once the docker environment is running, to run our python programme, type the following:
	
	python3 src/wrapper.py src/<problem.wcard> <timeout>

Developer notes:

	Quick reference (usual order of operation): 
	
	1) Pull from git

	2) (OPTIONAL) Run ./updatelocalHyperDB.sh (if you want to sync your local hyperopt DB
	with the git repo one).
	
	3) Run ./autodocker.sh Builds docker environment, runs container
	interactively.

	4) When work is complete and you want to stage files and commit
	changes. Run ./gitAuto.sh then write commit message, then push.
	

	Further explanations are below:

	When you pull from the git it  will not overwrite any data/ db entries you
        currently have stored on your docker volume)
	However, if you want to update your local version of the hyperopt database,
	run the script ./updatelocalHyperDB This will overwrite the hyperopt database
	that you currently have stored on your local docker volume with the latest one from the repo.
	It's basically restoring your DB from an sql dump. This IS NOT a merging of the databases.
	It is completely overwriting what you had previously with what is in sqlscripts/hyperopt.sql
	
	Running autodocker.sh does the neccessary building of an image, creating
	a volume (for persisting data), starting the containers and then
	runs the container interactively. It does some relevant checks to
	see if these docker components already exist and adjusts accordingly
	(for example stopping and removing the container if it already
	exists before booting it back up).   

	The gitAuto.sh script stages all relevant files in the project directory
	and it also creates an sql dump (basically copies your DB) and puts
	it in two directories - where both form part of the git repo. 
	The first is into sqlscripts/hyperopt.sql. This overwrites that file
	with your local hyperopt DB, meaning that the next time someone pulls from the repo
	and updates their local hyperoptDB, they will be using your most recent version
	of the hyperopt DB. This is how we create a semblance of a concurrent database.

	Furthermore, the script makes a backup of your local hyperopt DB and
	adds it to the dbBackup directory. Every backup is unique, and is
	date and time stamped.

  