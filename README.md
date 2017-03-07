
# Structure

The bot is structured as a docker-compose app. The services are
defined in docker-compose.yml.

# Running the bot

## Docker general


Run when starting to guarnatneee that docker is running:

	$ bash --login '/Applications/Docker/Docker Quickstart Terminal.app/Contents/Resources/Scripts/start.sh'

When finishing:

	$ docker-machine stop default


## Building

	$ docker-compose build

creates the images needed

	$ docker-compose up

creates the images needed
and starts? not sure but it rebuilds the app


## After changing some files

Run: `docker-compose build && docker-compose up`.

There is probably some smart way of just rebuilding levernebot
and restarting the levernebot contaier.

## What to do next:

Send proper result to inline query, see:

https://www.reddit.com/r/TelegramBots/comments/4a8gwz/return_arbitrary_text_from_inline_query/



