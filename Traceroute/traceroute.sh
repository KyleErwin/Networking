#!/bin/bash
# My first script

echo "Hello!"
echo "Translating" $1 "into numeric address..."
ADDRESS=`nslookup $1 | awk '/^Address: / { print $2 ; exit }'`
echo "Numeric address: " $ADDRESS
traceroute $ADDRESS
