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

Draft for API operations

    /ladder [GET]
    /ladder/new [POST]
    /ladder/<ladder_id> [GET,PUT,DELETE]
    /ladder/<ladder_id>/challenge/<challenger>/<challengee> [GET,PUT,POST,DELETE]
    /competitor [GET]
    /competitor/new [POST]
    /competitor/<competitor_id> [GET,PUT,DELETE]

