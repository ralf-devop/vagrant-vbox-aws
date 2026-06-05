#!/bin/sh
if [ -z "$AWS_DEFAULT_REGION" ] ; then
    echo "Environment variable 'AWS_DEFAULT_REGION' is unset!"
fi

if [ -z "$AWS_DEFAULT_OUTPUT" ] ; then
    echo "Environment variable 'AWS_DEFAULT_OUTPUT' is unset!"
fi

if [ -z "$AWS_ACCESS_KEY_ID" ] ; then
    echo "Environment variable 'AWS_ACCESS_KEY_ID' is unset!"
fi

if [ -z "$AWS_SECRET_ACCESS_KEY" ] ; then
    echo "Environment variable 'AWS_SECRET_ACCESS_KEY' is unset!"
fi
