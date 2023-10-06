#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Создаем или очищаем файл error.log
> "$DIR/error.log"

#echo "0 */12 * * * cd $DIR && ./venv/bin/python main.py" | tee -a /tmp/mycron # 12h
echo "*/2 * * * * cd $DIR && ./venv/bin/python main.py >> $DIR/error.log 2>&1" | tee -a /tmp/mycron # 2m
crontab /tmp/mycron
rm /tmp/mycron

echo "Cron job set up successfully!"
