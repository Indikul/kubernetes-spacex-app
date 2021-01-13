#Use mysql base image
FROM mysql

#Setting up environment varialbes & create database and use it
ENV MYSQL_ROOT_PASSWORD=1234
ENV MYSQL_DATABASE cw_db

#Expose to the default mysql port
EXPOSE 3306
#Copy the script file and create the table
COPY ./scripts/ /docker-entrypoint-initdb.d/

CMD ["mysqld"]