FROM mongo:latest

WORKDIR /data/db

ADD ./mongo.js /docker-entrypoint-initdb.d
ADD ./init.js /docker-entrypoint-initdb.d
ADD ./user-schema.js /docker-entrypoint-initdb.d

EXPOSE 27017
CMD ["mongod"]