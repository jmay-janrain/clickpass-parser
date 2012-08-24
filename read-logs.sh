#!/bin/sh

heroku logs --app clickpass-current -n 1500 | ./parse-clickpass.py
