FROM python:3.9.5-alpine

RUN pip install Flask

COPY . .

ENV FLASK_APP pizza_api.py

CMD ["flask", "run", "--host=0.0.0.0"]
