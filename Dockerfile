FROM python:3-alpine3.15
WORKDIR /dock
COPY . /dock
RUN pip install -r requirements.txt

EXPOSE 5000
CMD python3 ./app.py
