#! /usr/bin/env bash

# Run the api
exec uvicorn shornel_finance_api.main:app --reload --host 0.0.0.0 --port 8000