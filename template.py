import os
from pathlib import Path
import logging # now not doing loggic we will do it later
#log means record what happend therefore logging module keeps track of
#events in programs and most used for debugging purpose

logging.basicConfig(level=logging.INFO)
#we take basic configuration of logging module and set the level to INFO
#this means take in build configured log messages

project_name = "DS_Project"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    f"src/{project_name}/utils.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    "app.py",
    "main.py",
    "requirements.txt",
    "setup.py",
    "Dockerfile",
]

for filepath in list_of_files:

    filepath = Path(filepath)
    #convert the string to Path object

    filedir, filename = os.path.split(filepath)
    #separate the directory path and file name from the filepath using os.path.split() function

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        #crate the dirctory if it doesn't exist using os.makedirs() function
        #if exist_ok=True means if the directory already exists, don't raise an error

        logging.info(f"Creating directory: {filedir} for file {filename}")
        # this means that logging.info() is showing display as well as
        # keeping note that cause behind displaying it and process while happing there

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        #check file don't exist or file is empty
        #if file doen't exist then what will be filesize?
        #as filesize for non existing file can't be calculated
        #we use the logic that true or anything is always true don't check the 2nd condition if 1st is true

        with open(filepath, "w") as f:
            # with open in writting mode make sure that file is created if doesn't exist
            #file will go under after creating file or laredy existing file
            #and remainber while we are in read mode file is not created if ir doesn't exist
            # also with open will make sure that file is closed after the code is executed

            pass
            #after creating non existing file and opening under writting mode
            #and closing it or just opening the existing file and closing it
            #we don't want to do anything just pass

        logging.info(f"Creating empty file: {filepath}")
        #take recod of creating empty file and display it as well

    else:
        logging.info(f"{filename} already exists")