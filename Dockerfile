FROM node:18-alpine3.15
#RUN apk add --no-cache python3 g++ make
copy infrastructure-interview-takehome-main/web/ /app/
WORKDIR /app/infrastructure-interview-takehome-main/web
RUN npm install
ENV NODE_OPTIONS "--openssl-legacy-provider"
#CMD ["node", "infrastructure-interview-takehome-main/web/public/index.html"]
CMD ["npm", "start"]
EXPOSE 3000
