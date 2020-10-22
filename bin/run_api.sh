#!/bin/bash

export APP_PID=$!;
echo  {$APP_PID};
if [[ "" !=  "$APP_PID" ]]; then
  echo "killing $APP_PID"
  kill -9 $APP_PID
fi
sudo python main.py >> log.txt 2>&1 &;

