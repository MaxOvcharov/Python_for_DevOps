#!/usr/bin/env bash
function uname_func ()
{
    UNAME="uname -a"
    printf "Gathering system information with $UNAME command:\n"
    $UNAME
}

function diskspace_func ()
{
    DISKSPACE="df -h"
    printf "\nGathering diskspace information with $DISKSPACE command:\n"
    $DISKSPACE
}

function main ()
{
    uname_func
    diskspace_func
}

main