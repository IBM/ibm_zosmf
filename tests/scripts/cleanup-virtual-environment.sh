#!/bin/zsh
venvDir=$1

echo "Cleanup venv dir:"

cd $venvDir

pwd
rm -rf *