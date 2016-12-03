#!/usr/bin/env bash

UNAME="uname -a"
printf "Gathering system information with $UNAME command:\n"
$UNAME

DISKSPACE="df -h"
printf "\nGathering diskspace information with $DISKSPACE command:\n"
$DISKSPACE