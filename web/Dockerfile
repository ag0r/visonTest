FROM node:18-alpine3.15
copy . /app/
WORKDIR /app/web
RUN npm install
ENV NODE_OPTIONS "--openssl-legacy-provider"
ENV HTTPS true
ENTRYPOINT [ "npm" ]
CMD [ "start" ]
EXPOSE 3000
