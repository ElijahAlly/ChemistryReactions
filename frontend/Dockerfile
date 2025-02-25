FROM oven/bun:1

WORKDIR /app

# Copy package files and install dependencies
COPY package.json ./
RUN bun install

# Copy app files
COPY . .

# Generate prisma client
RUN bunx svelte-kit sync

# Build the app
RUN bun run build

# Use $PORT environment variable from Render and set host
ENV PORT=10000
ENV HOST=0.0.0.0
EXPOSE 10000

# Start the server
CMD ["bun", "run", "preview"]