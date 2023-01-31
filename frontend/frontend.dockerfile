# => Build container
FROM --platform=$BUILDPLATFORM amd64/node:alpine as builder
WORKDIR /app
COPY package.json .
COPY package-lock.json .
#COPY yarn.lock .
RUN yarn
COPY . .
RUN yarn build

# => Run container
FROM amd64/nginx:1.15.2-alpine

# Nginx config
RUN rm -rf /etc/nginx/conf.d
COPY conf /etc/nginx

# Static build
COPY --from=builder /app/build /usr/share/nginx/html/

# Default port exposure
EXPOSE 80

# Copy .env file and shell script to container
WORKDIR /usr/share/nginx/html
COPY ./env.sh .
COPY .env .

# Add bash
RUN apk add --no-cache bash

# Make our shell script executable
RUN chmod +x env.sh

ARG TARGETPLATFORM
ARG BUILDPLATFORM


RUN echo "Build platform architecture is $BUILDPLATFORM, while target architecture is $TARGETPLATFORM" > /log

# Start Nginx server
CMD ["bash", "-c", "/usr/share/nginx/html/env.sh && nginx -g \"daemon off;\""]