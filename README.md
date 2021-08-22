# django-app-api [![Build Status](https://app.travis-ci.com/raomaster/django-app-api.svg?branch=main)](https://app.travis-ci.com/raomaster/django-app-api)
 Build a Backend REST API with Python &amp; Django - Advanced


 ## Introduction
 This repo contains an Rest App building with:
 - Django 3
 - Docker
 - TDD
 - Travis CI
 - Lint tool: Flake8

## comands using in building:

## start project
    docker-compose run app sh -c "django-admin startproject app ."

## Run testing

    docker-compose run app sh -c "python manage.py test"

    docker-compose run app sh -c "python manage.py startapp core"

    docker-compose run app sh -c "python manage.py makemigrations core"

