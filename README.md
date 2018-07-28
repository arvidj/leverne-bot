[![Build Status](https://travis-ci.org/arvidj/leverne-bot.svg?branch=master)](https://travis-ci.org/arvidj/leverne-bot)

# Structure

The bot is structured as a docker-compose app. The services are
defined in docker-compose.yml.

# Running the bot

## Building

Run
	$ docker-compose build

to create the images needed. To run, use

	$ docker-compose up

## After changing some files

Run: `docker-compose build && docker-compose up`.

There is probably some smart way of just rebuilding levernebot
and restarting the levernebot contaier.

# Testing

Run: `./py.test test_bot.py`
