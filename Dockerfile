FROM python:3.8

ENV FLASK_APP "app.py"
WORKDIR /app

RUN pip install flask requests
COPY . .
COPY . .

RUN useradd -ms /bin/bash  flask
RUN chown -R flask:flask /app
RUN chmod 777 /app
USER flask

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]