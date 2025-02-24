FROM python:3.9-slim

# Create a non-root user
RUN useradd -m -u 1000 app

# Install system dependencies (with libpq for PostgreSQL support)
RUN apt-get update && apt-get install -y \
    libxrender1 \
    libxext6 \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set up working directory and change ownership
WORKDIR /app
RUN chown app:app /app

# Switch to non-root user
USER app

# Create and activate virtual environment
ENV VIRTUAL_ENV=/app/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy requirements first to leverage Docker cache
COPY --chown=app:app requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY --chown=app:app . .

# Use $PORT environment variable from Render
ENV PORT=8000
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]