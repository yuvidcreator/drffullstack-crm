ARG NODE_VERSION=16.17.1-alpine3.15

FROM node:${NODE_VERSION} as node

FROM node as client-local-build

ARG APP_HOME=/app

WORKDIR ${APP_HOME}

COPY ./package*.json . 

COPY ./yarn.lock .

RUN yarn

COPY . ${APP_HOME}

CMD ["yarn", "start"]

