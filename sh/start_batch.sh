#!/bin/bash

APP_NAME=ai-recruit
BASE_DIR=/usr/local/${APP_NAME}

cd ${BASE_DIR}

export PYTHONPATH="${BASE_DIR}:$PYTHONPATH"

echo env:${ENV}

python ${APP_NAME}/"$@"
