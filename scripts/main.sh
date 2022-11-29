#!/bin/sh

#sets the path as a variable
x=$(pwd)

# if the venv does exists then is does nothing
#if it doesn't it will create a new venv file
if [[ -d $x/.venv ]] 
then 
    echo "Exists"
else
    python3 -m venv .venv
    echo "done installing venv"
fi

#activates venv and then installs from requirements.txt
source "$x/.venv/bin/activate"
pip install -r requirements.txt

#install pre-commit
pre-commit install 

#test runs the scripts promting the user to see if everything is working
source "$x/scripts/db.sh"
source "$x/scripts/flask.sh"