#!/bin/bash

# Make sure jq is installed

data=`curl "http://maps.googleapis.com/maps/api/geocode/json?address=Belsize%20+rd,+London&sensor=false&region=uk"`

server_name="address_components"

#echo "$data" | jq -r '.results[].address_components[] |"\(.long_name) , \(.short_name)"'


echo "The server name is \"$server_name\""
numfiles=0

while read server ; do
	numfiles=$((numfiles + 1))
	echo "The path to file $numfiles is $server"

done < <(echo "$data" | jq -r '.results[].'$server_name'[] |"\(.long_name)"') # \(.short_name)"')

echo "Number of files tracked: $numfiles"


