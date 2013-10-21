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


