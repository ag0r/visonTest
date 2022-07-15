FROM node:18-alpine3.15
COPY package.json .
RUN npm install
ENV NODE_OPTIONS "--openssl-legacy-provider"
COPY . /app/
WORKDIR /app/web
ENTRYPOINT [ "npm" ]
CMD [ "start" ]
EXPOSE 3000
