#!/bin/sh

errno=1
while [ $errno -ne 0 ]; do
    $@
    errno=$?
done



