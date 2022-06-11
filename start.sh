#!/bin/bash

set -x

count=`ps aux | grep gun | wc -l`
echo $count
if [[ $count > 1 ]];then
	killall -9 gunicorn
fi

gunicorn -D -b 0.0.0.0:5000 app:app
