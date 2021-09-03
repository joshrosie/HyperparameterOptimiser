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
	the source files and just want to run CarlSAT as is.

Once the docker environment is running, to run our python programme, type the following:
	
	python3 src/wrapper.py src/<problem.wcard> <timeout>

Developer notes:

	Quick reference: 
	
	1) Pull from git
	
	2) Run ./updatelocalHyperDB.sh (if you want to sync your hyperopt DB
	with the git repo one). Like running a manual google drive sync.
	
	3) Run ./autodocker.sh Builds docker environment, runs container
	interactively.

	4) When work is complete and you want to stage files and commit
	changes. Run ./gitAuto.sh then write commit message, then push.
	

	Further explanations are below:

	When you pull from the git and you want to update your local
	version of the hyperopt database, run the script ./updatelocalHyperDB
	This will overwrite the database that you currently have stored on
	your local volume with the latest one from the repo. It's basically
	restoring your DB from an sql dump.
	
	Running autodocker.sh does the neccessary building images, creating
	a volume (for persisting data), starting the containers and then
	runs the container interactively.  
