# automaton-v5
Automation framework (API) - an example. Based on Python, Unittest

[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/BurhanH/automaton-v5/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/BurhanH/automaton-v5.svg?branch=master)](https://travis-ci.org/BurhanH/automaton-v5)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/179c8d7e01a0486ebe5005e1e6183809)](https://app.codacy.com/app/BurhanH/automaton-v5?utm_source=github.com&utm_medium=referral&utm_content=BurhanH/automaton-v5&utm_campaign=Badge_Grade_Dashboard)

## Requirements
Python 3.6.\*, Unittest, <br> 
virtualenv (virtual environment manager) <br>

## Project structure
```text
-- automaton-v5
   |-- .gitattributes
   |-- .gitignore
   |-- .travis.yml
   |-- calls.py
   |-- LICENSE
   |-- README.md
   |-- requirements.txt
   `-- tests
       |-- initial.py
       |-- test_api.py
```

## How to prepare environment
1) Install [Python](https://www.python.org/downloads/)
2) Install and configure [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
3) Clone or copy (download) the repository into your virtual environment
4) Activate virtual environment, move to `automaton-v5` folder, and execute command `pip install -r requirements.txt`

## How to run tests
1) Open terminal window
2) Move to virtual environment folder
3) Activate virtual environment
4) Move to `automaton-v5` folder
5) Execute `python -m unittest discover tests "*.py" -v`

To be continue ...
