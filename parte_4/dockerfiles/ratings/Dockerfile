FROM node:12.18.1-slim
COPY package.json /opt/microservices/package.json
COPY ratings.js /opt/microservices/ratings.js
WORKDIR /opt/microservices
RUN npm install
ENV SERVICE_VERSION v1
EXPOSE 9080
CMD ["node", "ratings.js", "9080"]
