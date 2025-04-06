web: gunicorn dmoj.wsgi:application --bind 0.0.0.0:$PORT --workers 3
worker:celery -A dmoj worker --pool=solo --loglevel=info
websocket: python websocket_server.py
runbridge: python runbridge.py