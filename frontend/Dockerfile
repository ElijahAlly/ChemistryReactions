FROM oven/bun:1

WORKDIR /app

# Copy package files and install dependencies
COPY package.json ./
RUN bun clean
RUN bun install

# Copy app files
COPY . .

# Add debugging commands before build
RUN ls -la
RUN echo "Content of svelte.config.js:"
RUN cat svelte.config.js
RUN echo "Content of vite.config.ts:"
RUN cat vite.config.ts
RUN echo "Content of package.json:"
RUN cat package.json

# Build with verbose logging
RUN VITE_LOG_LEVEL=debug bun run build || (echo "Build failed with error code $?" && exit 1)

# Use $PORT environment variable from Render and set host
ENV HOST=0.0.0.0
EXPOSE 10000

# Start the server
CMD ["bun", "run", "preview"]