FROM python:3
WORKDIR /usr/src/app
COPY . .
RUN pip3 install Django
RUN pip3 install firebase-admin
RUN pip3 install python-dateutil
ENV PORT=8000
CMD python3 /usr/src/app/API/manage.py runserver 0.0.0.0:8000