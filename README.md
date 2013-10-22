Ascendancy
==========

A ladder tournament API
-----------------------

In case you're unsure what a ladder tournament is [here's a link to Wikipedia](http://en.wikipedia.org/wiki/Ladder_tournament "Ladder Tournament - Wikipedia").

The idea of this project is to develop a simple API for creating and conducting ladder tournaments which can be
used as the back end for a web or mobile games app.

The API should be agnostic to the type of game being played, being concerned only with the players, results, and lifecycle 
of the tournament. I hope that the API will support a number of different ranking mechanisms such as swapping places when 
a challenger wins, or using points-based systems like Elo ratings.

Getting started
---------------

N.B. this project is inchoate, hardly written at all, so don't expect this to do much yet ;-)

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

    pip install Flask
    
You should now be able to fire up the app on localhost:

    python ascendancy_app.py
    
You should be able to find the app at http://127.0.0.1:5000, if not you might need to [consult the Flask docs](http://flask.pocoo.org/docs/installation/#installation "Flask documentation").

Operations
----------

Draft API operations, based on the system's resources being limited to Ladders, Challenges, and Competitors.

    /ladders                       [GET,POST]
    /ladders/<ladder_id>           [GET,PUT,DELETE]
    /challenges                    [GET,POST]
    /challenges/<challenge_id>     [GET,PUT,DELETE]
    /competitors                   [GET,POST]
    /competitors/<competitor_id>   [GET,PUT,DELETE]

Resources
---------

### Ladder

    {
        'ladder': {
            'id': <ladder_id>,
            'competitors': {
                <rank> : <simplified_competitor_object>
            },
            'settings': {
                'challenges_can_be_declined': true|false,
                ...
            },
            'created': <date>,
            'expires': <date>,
            ...
        }
    }

### Challenge

    {
        'challenge': {
            'id': <challenge_id>,
            'ladder': <ladder_id>,
            'challenger': <simplified_competitor_object>,
            'challengee': <simplified_competitor_object>,
            'status': ('pending'|'accepted'|'declined'),
            'outcome': ('win'|'lose'|'draw'|'forfeit'|'no result'),
            'expires': <date>,
            'created': <date>,
            ...
        }
    }

### Competitor

    {
        'competitor': {
            'id': <competitor_id>,
            'ladders': [
                {
                    'id': <ladder_id>,
                    'rank': <ladder_rank>,
                    'rating': <ladder_rating>,
                    ...
                }
            ],
            ...
        }
    }

