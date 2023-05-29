#!/bin/bash

add_environment_variable() {
    if [ -z "$1" ] || [ -z "$2" ]; then
        echo "Error: Please provide both the name and value of the environment variable."
        exit 1
    fi

    setx "$1" "$2"

    if [ $? -eq 0 ]; then
        echo "The environment variable $1 has been added with the value $2."
    else
        echo "Error adding the environment variable."
        exit 1
    fi
}

name="$1"
value="$2"

add_environment_variable "$name" "$value"
