## Getting started (local)

First, you will need pip installed in your local environment.
I'm sure you know how to do this yourself.

    brew install python
    or
    sudo easy_install pip

if you need to install brew

    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Once that is done, create your virtual environment:

    virtualenv env
    source env/bin/activate

If you are on Windows, you activate your environment this way:

    virtualenv env
    source env/Scripts/activate

If you're on OSX, you'll also need to install a few binaries if you don't have cFFI and MySQL installed.

    brew install libffi
    brew install mysql

Or, if you're on CentOS:

    yum install libffi-devel.x86_64
    yum install python-cffi.x86_64
    yum install python-devel
    yum install mysql mysql-devel mysql-common mysql-libs gcc


Now, need to install all requirements.
    cd <project_name>
    pip install -r requirements.txt

Next, set up your local settings.
    config.py

You'll then probably want to change DATABASES to something like this:

    DATABASE_SQL = {
        'drivername': 'mysql',
        'host': 'localhost',
        'port': '3306',
        'username': 'root',
        'password': '',
        'database': 'test_db'
    }
or, if you're developing locally use SQLite:

    DATABASE = {
        'drivername': 'sqlite',
        'database': os.path.join(basedir, 'test.db')
    }

Setup JS :
    
    npm install -g bower
    bower install

Useful commands:
    
    cd FlaskAPI
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt
    bower install
    python FlaskAPI.py
