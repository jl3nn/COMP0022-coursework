# Use an official Node runtime as a base image for building
FROM node:14-alpine AS build

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install app dependencies
RUN npm install

# Copy the entire project to the working directory
COPY . .

# Build the production version
RUN npm run build

# Use an official Nginx image as a base image for serving
FROM nginx:alpine

# Copy the production build from the build folder to the default Nginx web root
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80 for the Nginx server
EXPOSE 80

# The CMD instruction sets the command to be executed when the container starts
CMD ["nginx", "-g", "daemon off;"]
