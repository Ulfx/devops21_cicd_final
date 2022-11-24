#!/bin/sh

"""checks if the .venv file exist"""
"""if it doens't it will create a new virtual environment"""
if [ ! -f /home/usko/repos/devops21_cicd_final/.venv/bin/activate ]
then 
echo "Exists"
else
python3 -m venv .venv
fi

"""activates the virtual environment and then pip installs from requirements.txt"""
source "/home/usko/repos/devops21_cicd_final/.venv/bin/activate"
pip install -r requirements.txt

"""lastly runs the 2 test scripts in scripts/"""

source "/home/usko/repos/devops21_cicd_final/scripts/db.sh"
source "/home/usko/repos/devops21_cicd_final/scripts/flask.sh"