FROM oven/bun:1

WORKDIR /app

# Copy package files and install dependencies
COPY package.json ./
RUN bun install

# Copy app files
COPY . .

# Build the app
RUN bun run build

# Use $PORT environment variable from Render and set host
ENV PORT=3000
ENV HOST=0.0.0.0
EXPOSE 3000

# Start the server
CMD ["bun", "run", "preview", "--", "--host", "0.0.0.0", "--port", "$PORT"]