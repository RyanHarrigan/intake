# Intake
[![CircleCI](https://circleci.com/gh/codeforamerica/intake.svg?style=svg)](https://circleci.com/gh/codeforamerica/intake)  [![Code Climate](https://codeclimate.com/github/codeforamerica/intake/badges/gpa.svg)](https://codeclimate.com/github/codeforamerica/intake) 


[Tech Overview](https://github.com/codeforamerica/intake/wiki)

[Quickstart](https://github.com/codeforamerica/intake/wiki/Quickstart)

[Installation & Setup](https://github.com/codeforamerica/intake/wiki/Installation-&-Setup)

[Testing & Debugging](https://github.com/codeforamerica/intake/wiki/Testing-&-Debugging)

[Releasing & Deploying](https://github.com/codeforamerica/intake/wiki/Releasing-&-Deploying)

[Administrative Access](https://github.com/codeforamerica/intake/wiki/Administrative-Access)


## Docker install
Below are instructions to get the environment up and running. Currently, we are not supporting dev/stage/prod environment deployments

### Dependencies
- docker-machine and docker-compose
- At least 4GB of space

### Instructions
1) Clone the repo to a directory `git clone {REPO} expungement_journey`
1) Cd to the repo dir `cd expungement_journey`
1) Copy you `.env` file to the current directory
1) Run `docker-compose up -d` and wait for it to build (may take a while)
1) Run the database migrations 
    1) `docker exec -it expungement_journey_web_1 /bin/bash`
    1) `python3 ./manage.py makemigrations`
    1) `python3 ./manage.py migrate`
    
That's it! The app should be up and running!

Well - not really. Contact Ryan to set up the superuser. 