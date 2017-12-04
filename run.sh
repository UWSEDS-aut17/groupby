#!/bin/bash

# run this script via: bash run.sh

# run the unit tests
nosetests --with-coverage --cover-package=utils groupby/tests/test_groupby.py

# run the PEP8 checker
pycodestyle groupby/groupby.py groupby/tests/test_groupby.py
