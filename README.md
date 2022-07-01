# Augmented Design

Augmented Design is aimed to enhance building design with automation and artificial intellengence. Currently it provides "Floorplan Evaluation" service, which enables architects to quickly calculate the key indicators of a building plan and evaluate its design. In the future, Augmented Design will provide richer functions to help architects improve their design and increase design efficiency.

## Set Up

`git clone git@github.com:shiyan-chen/augmented-design.git`
- clone the project repo to local

`cd augmented-design`
`python3 -m venv .venv`
- create an environment

`. .venv/bin/activate`
- activate the encironment

`brew install node`
`pip install Flask`
- install node.js, flask

`pip install -r requirements.txt`
- install dependencies

`cd aug_service/`
`export FLASK_APP=aug_serving && flask run`
- start evaluation service

`cd webapp/frontend/ && npm install`
`npm start`
- start website

## Test

`pip install -r requirements.txt`
`python -m unittest discover -s aug_service`

## Webpage Showcase
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/70275050/176905158-cb282ccb-c7ef-4f65-9290-30b4f37f1ddc.png">
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/70275050/176905238-31de16d6-ca9c-44e5-a00b-b56c286e5394.png">
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/70275050/176905317-bd9cdcb8-91af-40cd-ae9e-32ddeddc089a.png">



