FROM ruby:2.7.1-slim
COPY details.rb /opt/microservices/details.rb
ENV SERVICE_VERSION v1
ENV ENABLE_EXTERNAL_BOOK_SERVICE true
EXPOSE 9080
CMD ["ruby", "/opt/microservices/details.rb", "9080"]
