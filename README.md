# ScoreBoard

# Usage

It's best to install Python projects in a Virtual Environment. Once you have set up a VE, clone this project

https://github.com/sudheerdhanu/ScoreBoard.git

#Then

cd ScoreBoard

check manage.py file and there commands

#Run

pip install -r requirements.txt #install required packages
python manange.py migrate # run first migration
python manage.py makemigrations # Do makemigrations
python manange.py migrate
python manange.py runserver # run the server

Then locate http://127.0.0.1:8000
