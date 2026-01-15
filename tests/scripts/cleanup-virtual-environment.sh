#!/bin/bash -eu
venvDir=$1

echo "Searching for Old venv Directory"

if [ -e "${venvDir}" ]; then
    echo "venv Directory Found Cleaning Up venv Directory:"
    "cd $venvDir || exit"
    pwd
    "rm -rf *"
else
    echo "venv Directory Found Cleaning Up venv Directory:"
fi

