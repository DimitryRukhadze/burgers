FROM node:16

WORKDIR /usr/src/star-burger
COPY package.json .
COPY package-lock.json .
COPY /bundles-src/ ./bundles-src
RUN npm ci --include=dev
RUN ./node_modules/.bin/parcel build bundles-src/index.js --dist-dir bundles --public-url="./"