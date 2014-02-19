Ascendancy
==========

A chess club API
-----------------------

The original idea for this project was to develop a simple API for creating and conducting 
[ladder tournaments](http://en.wikipedia.org/wiki/Ladder_tournament "Ladder Tournament - Wikipedia"), but in the
meantime the chess club I play at needs a new website backend, so it's getting repurposed.

The idea is that Ascendancy will be an [REST](http://en.wikipedia.org/wiki/Representational_state_transfer "Representational State Transfer - Wikipedia") service over which all the necessary [CRUD](http://en.wikipedia.org/wiki/Create,_read,_update_and_delete "Create, read, update and delete - Wikipedia") for
a chess club can be carried out, such as managing teams, games, competitions and players.


Getting started
---------------

**N.B. this project is inchoate, hardly written at all, so don't expect this to do much yet ;-)**

Ascendancy is being written using the [Flask framework](http://flask.pocoo.org/ "Flask (A Python Microframework)").
Assuming you're on a Linux machine, are familiar with Flask and have pip installed, the best way to get 
started is probably to clone this project, i.e.:

    git clone git@github.com:pgchamberlin/ascendancy.git ascendancy

And then if you don't already have virtualenv installed:

    pip install virtualenv
    
Now create a virtualenv on the clone directory:

    virtualenv ascendancy
    
Activate the virtualenv:

    . ascendancy/bin/activate
    
Navigate to the project's directory:

    cd ascendancy
    
Install Flask from pip:

    bin/pip install Flask

Install nose and mock for testing:

    bin/pip install nose mock

Install MySQLdb:

    bin/pip install MySQL-python
    
You should now be able to fire up the app on localhost:

    bin/python app.py

You should be able to find the app at http://127.0.0.1:5000, if not you might need to [consult the Flask docs](http://flask.pocoo.org/docs/installation/#installation "Flask documentation").

You should also be able to run the tests (which should all pass):

    bin/nosetests

Interface
---------

Draft routes:

    /clubs                          [GET,POST]
    /clubs/<club_id>                [GET,PUT,DELETE]
    /teams                          [GET,POST]
    /teams/<team_id>                [GET,PUT,DELETE]
    /competitions                   [GET,POST]
    /competitions/<competition_id>  [GET,PUT,DELETE]
    /fixtures                       [GET,POST]
    /fixtures/<fixture_id>          [GET,PUT,DELETE]
    /games                          [GET,POST]
    /games/<game_id>                [GET,PUT,DELETE]
    /players                        [GET,POST]
    /players/<player_id>            [GET,PUT,DELETE]

Resources
---------

Draft resource models:

### Club

    {
        'club': {
            'id': int,
            'name': string,
            'teams': [
                ...
            ]
        }
    }

### Team

    {
        'team': {
            'id': int,
            'club': {
                ...
            },
            'competitions': [
                ...
            ],
            'fixtures': [
                ...
            ]
        }
    }

### Competition

    {
        'competition': {
            'id': int,
            'name': string,
            'format': (league|tournament),
            'num_rounds': int,
            'time_control': {
                'methodology': (rapidplay|matchplay...),
                'initial_time': int,
                'increment_time': int,
                'num_time_periods': int
            },
            'grade_requirement': {
                'value': int,
                'operator': (gt|lt)
            },
            'teams': [  // optional
                ...
            ],
            'games': [
                ...
            ]
        }
    }

### Fixture

    {
        'fixture': {
            'id': id,
            'date': UTC date,
            'vanue': string,
            'competition': {
                ...
            },
            'teams': {
                ...
            },
            'games': {
                ...
            }
        }
    }

### Game

    {
        'game': {
            'id': int,
            'player_1': {
                ...
            },
            'player_2': {
                ...
            },
            'white_player': int, // id of player_1 or _2
            'result': (white|black|draw)
        }
    }

### Player

    {
        'player': {
            'id': int,
            'ecf_code': string,
            'ecf_member_code': string,
            'first_name': string,
            'surname': string,
            'grades': {
                ...
            }
        }
    }

