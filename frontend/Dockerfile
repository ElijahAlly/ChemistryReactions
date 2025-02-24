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

# Use the same bun image for production
FROM oven/bun:1

WORKDIR /app

# Copy the build output
COPY --from=builder /app/build .
COPY --from=builder /app/package.json .
COPY --from=builder /app/node_modules ./node_modules

# Install production dependencies
RUN bun install --production

# Use $PORT environment variable from Render
ENV PORT=3000
EXPOSE 3000

# Start the server
CMD ["bun", "build/index.js"]