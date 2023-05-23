# DRF with React-JS

this is a simple project that uses DRF and React-js

## Table of Contents

- [Project Overview](#project-overview)
- [requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

## Project Overview

This project consists of two parts, first one is the backend with drf and second one is the frontend with React-JS.

## Requirements

- [Python](https://www.python.org/downloads/)
- [nodejs](https://nodejs.org/en)

## Installation

clone this project from [github repo.](git@github.com:aliharby12/drf-with-react.git)

## Usage:

## To run the backend
```bash
cd backend

# create virtual-environment:
virtualenv venv

# activate virtualenv:
source venv/bin/activate

# install dependencies
pip3 install -r requirements.txt

# run the backend
python3 manage.py runserver

# run tests
python3 manage.py test ./tests
```

## To run the frontend
```bash
cd frontend

# install dependencies
npm install

# run the frontend
npm run
```

## Features

Features available in this project:

- CRUDs for invoices.
- Pagination & Rate limits for endpoints.
- Search in list invoices.
- Unit test for every endpoint.
