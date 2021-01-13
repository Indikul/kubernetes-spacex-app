#Use ubuntu base image for the app to run on
FROM ubuntu

#Getting requied packages and making the environment for the task
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y python3.8 python3-pip sudo mysql-server libmysqlclient-dev
RUN python3 -m  pip install flask flask-mysqldb
RUN sudo service mysql start

#Copy app file and html templates inside ubuntu operating system
COPY ./cw_app.py /opt/
COPY ./templates/ /opt/templates/

EXPOSE 5000
ENTRYPOINT FLASK_APP=/opt/cw_app.py flask run --host=0.0.0.0
#Expose the continer to 5000 and run the app