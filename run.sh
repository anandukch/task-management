
# if [[ "$DEBUG" = "True" ]]; then
#     uvicorn app.main:app --root-path ${BASE_PATH:-""} --port ${PORT:-5000} --host 0.0.0.0 --reload 
# else
#     uvicorn app.main:app --root-path ${BASE_PATH:-""} --port ${PORT:-8000} --host 0.0.0.0
# fi

export APP_MODULE=${APP_MODULE-app.main:app}
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-5000}

exec uvicorn --reload --host $HOST --port $PORT "$APP_MODULE"

# check if argument 1 is test or not if test run 
# echo "Running tests"
# pytest -v


