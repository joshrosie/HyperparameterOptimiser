# Capstone-Project

CSC3002S Capstone Project
Group:
	RSNJOS005 - Josh Rosenthal
	FSHJAR002 - Jarred Fisher
	WLSKIE001 - Kiera Wilson

Instructions for Dockerfile build:

	To build the docker environment, run the script automate.sh
	This can easily be done by typing the following in the project
	directory: ./automate.sh

	NOTE 1: The script will search for a docker image by the name of "dimage"
	and if it does not find it, it will build the image from the
	dockerfile always regardless of parameters passed to the script.

	NOTE 2: By default, even if an image is present it'll still be
	rebuilt. This is because any changes made to the source files would
	not reflect in the docker environment if the image wasn't rebuilt.

	However, you can force the script to skip rebuilding the image by running the script
	as follows: ./automate.sh skip
	The use case for this would be if you haven't made any changes to
	the source files and just want to run CarlSAT as is.

Once the docker environment is running, to run our python programme, type the following:
	
	python3 src/wrapper.py src/<problem.wcard> <timeout>


