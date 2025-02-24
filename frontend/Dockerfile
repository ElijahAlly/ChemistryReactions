FROM oven/bun:1 as builder

WORKDIR /app

# Copy package files
COPY package.json ./

# Install dependencies
RUN bun install

# Copy app files
COPY . .

# Build the app
RUN bun run build

# Use a lightweight server to serve static files
FROM node:alpine

WORKDIR /app

# Install serve
RUN npm install -g serve

# Copy built files from builder stage
COPY --from=builder app/ .

# Use $PORT environment variable from Render
CMD ["sh", "-c", "serve -s build -l ${PORT:-3000}"]