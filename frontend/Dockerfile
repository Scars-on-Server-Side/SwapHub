FROM node:20

WORKDIR /swaphub
COPY package*.json ./

RUN npm install
RUN npm install axios
RUN npm install @mui/material @emotion/react @emotion/styled @mui/styled-engine-sc styled-components @mui/icons-material

COPY . .

RUN npm run build

CMD ["npm", "start"]
