FROM oven/bun:1

WORKDIR /app

# Copy package files and install dependencies
COPY package.json ./
RUN bun clean
RUN bun install

# Copy app files
COPY . .

# Build the app
RUN bun run build

# Use $PORT environment variable from Render and set host
ENV HOST=0.0.0.0
EXPOSE 10000

# Start the server
CMD ["bun", "run", "preview"]