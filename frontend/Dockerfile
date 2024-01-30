FROM node:20

WORKDIR /swaphub
COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

CMD ["npm", "start"]
