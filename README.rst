``restful-ssh-config``
~~~~~~~~~~~~~~~~~~~~~~

..
    image:: https://badge.fury.io/py/restful-ssh-config.svg
    :target: https://badge.fury.io/py/restful-ssh-config

..
    image:: https://travis-ci.org/wizardsoftheweb/restful-ssh-config.svg?branch=master
    :target: https://travis-ci.org/wizardsoftheweb/restful-ssh-config

..
    image:: https://coveralls.io/repos/github/wizardsoftheweb/restful-ssh-config/badge.svg?branch=master
    :target: https://coveralls.io/github/wizardsoftheweb/restful-ssh-config?branch=master

The goal of this application is to provide a RESTful API in Flask that is capable of building SSH config files.

**VERY IMPORTANT NOTES**
========================

* While in early development, this uses SQLite to manage data. That means anything you put in it is essentially public. Normally your ``.ssh/config`` is ``u=rw,go=``, i.e. only you and ``root`` can read it.
* While in early development, things may or may not be encrypted. This means anything you put in it could be snooped on. Normally you don't pass off sensitive information like SSH config to an unknown third party API.
* While in early development, there will probably be very little in the way of locking down access. This means anything you leave somewhere else could be picked up without much trouble. Normally you don't leave sensitive information sitting in the open on foreign machines.

Basically I'm trying to strongly hint that you shouldn't put anything sensitive in this in the near future unless you're running it yourself on your machine. Even then, you should still take the time to make sure it's not phoning home.

Overview
========

As of ``v0.1.0``, this has a stripped-down proof-of-concept, some model sketches, and some data generators. It does not have a REST API. Yet.

Roadmap
=======

These percentages are pretty arbitrary. Today's 47% could be tomorrow's 90% or vice versa.

Main Features
-------------

Once all of these are finished, I'll release ``v1``. Until then, ``v0`` should be used with caution, because it's not stable.

.. csv-table::
    :header: "Progress", "Feature"

    "0%", "Connect Flask, SQLAlchemy, and Marshmallow"
    "0%", "Create some sort of schedule for data file generation"
    "0%", "Move data to user land"
    "0%", "Investigate other data stores"
    "0%", "Sphinx docs"
    "-10%", "Testing"

Eventual Features
-----------------

These are things I'd like to add, but might not be included in ``v1``. If not, they'll most likely constitute one or more minor version increments.

.. csv-table::
    :header: "Progress", "Feature"

    "0%", "Simple frontend for the API"
    "0%", "Fill sensitive fields with dummy values"
    "0%", "Create exportable script for replacing dummy values"
