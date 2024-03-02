FROM node:14-alpine AS build

WORKDIR /app

COPY package*.json .
COPY tsconfig.json .
RUN npm install

COPY src /app/src
COPY public /app/public

ENV CI true
RUN npm test
RUN npm run build

FROM nginx:alpine

COPY --from=build /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
