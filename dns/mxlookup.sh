#!/bin/bash

host jcatalog.club | xargs | grep $1

while [ $? -ne 0 ];
do
#	echo not yet!
	sleep 5
	dig jcatalog.club MX | xargs | grep $1
done

echo DOOOOOOOOOOOOOOOOOOOOOOOOOONE!!!!!!!!!!!!!

notify-send 'Got MX' 'Cloudmailin is set in $1' --icon=dialog-information
