FROM node:18-alpine3.15
RUN apk add --no-cache python3 g++ make
WORKDIR /app
copy . .
RUN yarn install --production
CMD ["node", "src/index.js"]
EXPOSE 5000
