FROM oven/bun:1

WORKDIR /app

# Copy package files and install dependencies
COPY package.json ./
RUN bun install

# Copy app files
COPY . .

# Build the app
RUN bun run build

# Use $PORT environment variable from Render
ENV PORT=3000
EXPOSE 3000

# Start the server
CMD ["bun", "run", "preview"]