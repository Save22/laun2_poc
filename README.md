## Save22 Website Redesigning Project

The Save22 is a bit dated and will be redesigned using Django Mezzanine.

#### Usage

1. Setup a virtual environment

    `virtualenv env`

2. Source to your virtual environment

    `source env/bin/activate`

3. Clone your fork of this repository

    `git clone https://github.com/<username>/laun2_poc.git`

4. Change directory to the created project on your computer

    `cd laun2_poc`

5. Create a copy of keys.json.sample to keys.json located inside config folder

    `cp config/keys.json.sample config/keys.json`

6. Edit keys.json and change SECRET_KEY to your secret key

    `vim config/keys.json`

7. Create initial database

    `python manage.py createdb`

8. Start your projects server

    `python manage.py runserver 0.0.0.0:800x`
