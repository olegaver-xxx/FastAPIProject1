#!/usr/bin/env bash

SOURCE_PATH=$(dirname "$(realpath ${BASH_SOURCE[0]})")
export PYTHONPATH=$SOURCE_PATH

uvicorn app.main:app --port 8031 --reload