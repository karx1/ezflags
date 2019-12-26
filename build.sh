#!/bin/bash

echo "Building, please wait. This may take a few minutes"
rm -rf .build-env/ build/ dist/ ezflags.egg-info/
python -m venv .build-env
source .build-env/bin/activate
which python
python --version
python -m pip install wheel nose
python setup.py test
python setup.py sdist bdist_wheel
deactivate
rm -rf .build-env
echo "Build finished."
