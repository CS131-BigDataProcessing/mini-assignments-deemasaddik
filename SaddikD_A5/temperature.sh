#!/bin/bash

temp=$1

if [ "$temp" -gt 55 ]; then
        if [ "$temp" -lt 67 ]; then
                echo "cold"
        elif [ "$temp" -lt 85 ]; then
                echo "nice"
        else
                echo "hot"
        fi
else
        echo "freezing"

fi
