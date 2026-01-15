#!/bin/bash -eu
pythonVersionList=("python3.11" "python3.12" "python3.13")

echo "Check installed Python versions:"

for pythonVersion in "${pythonVersionList[@]}"; do
    echo "==> ${pythonVersion} --version"
    "${pythonVersion} --version"

    echo "==> which ${pythonVersion}"
    which "${pythonVersion}"
done
