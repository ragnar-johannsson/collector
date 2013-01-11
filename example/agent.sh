#!/bin/bash
#
# A sample script that posts a hostname and the output from uptime(1) 
# to the resource configured in the complementing config.yml
#

SERVER_URL="http://localhost:5000/uptime"
SECRET="mysecret"

function initialize {
    DATAFILE="/tmp/api-data.$RANDOM$RANDOM.txt"
    PARAMS="timestamp=$(date +%s)"
    SIGNATURE=$(sign "$PARAMS" "$SECRET")
    PARAMS="$PARAMS&signature=$SIGNATURE"
    URL="$SERVER_URL?$PARAMS"

    trap "rm -f $DATAFILE" EXIT
}

function hash_hmac {
    local digest="$1"
    local data="$2"
    local key="$3"
    shift 3
    echo -n "$data" | openssl dgst "-$digest" -hmac "$key" "$@"
}

function sign {
    hash_hmac "sha1" "$1" "$2" -binary | base64 | sed -e 's/+/-/g' -e 's-/-_-g' -e 's/\n//g'
}

# main
initialize "$@"

cat <<EOF > $DATAFILE
{
    "hostname" : "$(hostname)",
    "uptime" : "$(uptime)"
}
EOF

curl -X POST -d @$DATAFILE "$URL"

