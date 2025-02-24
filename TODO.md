
# Step 1

Yes, you can use GitHub Container Registry (ghcr.io) to host your Docker containers and GitHub Actions to automate the build and deployment process. I'll help you set this up for both your Python backend and Svelte frontend.

First, let's create the necessary Dockerfiles and GitHub Actions workflows:

```dockerfile backend/Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]
```

```dockerfile frontend/Dockerfile
FROM node:16-alpine as builder

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

```nginx frontend/nginx.conf
server {
    listen 80;
    server_name _;

    root /usr/share/nginx/html;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

Now, let's create GitHub Actions workflows to build and push the containers:

```yaml .github/workflows/backend.yml
name: Build and Push Backend Container

on:
  push:
    branches: [ main ]
    paths:
      - 'backend/**'
      - '.github/workflows/backend.yml'

env:
  REGISTRY: ghcr.io
  BACKEND_IMAGE_NAME: ${{ github.repository }}-backend

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Log in to the Container registry
        uses: docker/login-action@v1
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build and push Backend Docker image
        uses: docker/build-push-action@v2
        with:
          context: ./backend
          push: true
          tags: ${{ env.REGISTRY }}/${{ env.BACKEND_IMAGE_NAME }}:latest
```

```yaml .github/workflows/frontend.yml
name: Build and Push Frontend Container

on:
  push:
    branches: [ main ]
    paths:
      - 'frontend/**'
      - '.github/workflows/frontend.yml'

env:
  REGISTRY: ghcr.io
  FRONTEND_IMAGE_NAME: ${{ github.repository }}-frontend

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Log in to the Container registry
        uses: docker/login-action@v1
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build and push Frontend Docker image
        uses: docker/build-push-action@v2
        with:
          context: ./frontend
          push: true
          tags: ${{ env.REGISTRY }}/${{ env.FRONTEND_IMAGE_NAME }}:latest
```

To use this setup:

1. Make sure your repository has this structure:
```
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── main.py
├── frontend/
│   ├── Dockerfile
│   ├── nginx.conf
│   └── ... (your Svelte app files)
└── .github/
    └── workflows/
        ├── backend.yml
        └── frontend.yml
```

2. Enable GitHub Actions in your repository settings.

3. Make sure your repository has permissions to create packages:
   - Go to your repository settings
   - Navigate to "Packages"
   - Enable "Inherit access from repository"

4. Push your code to GitHub. The workflows will automatically:
   - Build Docker images for both frontend and backend
   - Push them to GitHub Container Registry

5. To pull and run the containers:
```bash
# Pull the images
docker pull ghcr.io/your-username/your-repo-backend:latest
docker pull ghcr.io/your-username/your-repo-frontend:latest

# Run the containers
docker run -d -p 8000:8000 ghcr.io/your-username/your-repo-backend:latest
docker run -d -p 80:80 ghcr.io/your-username/your-repo-frontend:latest
```

You can also create a docker-compose.yml file to manage both containers:

```yaml docker-compose.yml
version: '3.8'

services:
  backend:
    image: ghcr.io/your-username/your-repo-backend:latest
    ports:
      - "8000:8000"

  frontend:
    image: ghcr.io/your-username/your-repo-frontend:latest
    ports:
      - "80:80"
    depends_on:
      - backend
```

Remember to:
1. Replace `your-username/your-repo` with your actual GitHub username and repository name
2. Make sure your Python backend is listening on port 8000
3. Update any environment variables or configuration files as needed
4. Configure CORS in your backend to allow requests from your frontend

The containers will be publicly available in your GitHub Container Registry, and you can pull them from any machine with Docker installed.

<br />
<br />
<br />

# Step 2. 

To make your app accessible via chemreactions.org, you'll need to:

1. Set up a server (like DigitalOcean, AWS, or similar)
2. Configure DNS settings
3. Set up HTTPS with SSL certificates
4. Deploy your containers

Here's a step-by-step guide using DigitalOcean as an example (it's one of the simpler options):

1. First, create a `docker-compose.prod.yml` file with additional production settings:

```yaml docker-compose.prod.yml
version: '3.8'

services:
  backend:
    image: ghcr.io/your-username/your-repo-backend:latest
    restart: always
    environment:
      - CORS_ORIGIN=https://chemreactions.org
    networks:
      - app-network

  frontend:
    image: ghcr.io/your-username/your-repo-frontend:latest
    restart: always
    networks:
      - app-network

  nginx-proxy:
    image: nginx:alpine
    restart: always
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx-proxy.conf:/etc/nginx/conf.d/default.conf
      - ./certbot/conf:/etc/letsencrypt
      - ./certbot/www:/var/www/certbot
    networks:
      - app-network
    depends_on:
      - frontend
      - backend

  certbot:
    image: certbot/certbot
    volumes:
      - ./certbot/conf:/etc/letsencrypt
      - ./certbot/www:/var/www/certbot
    entrypoint: "/bin/sh -c 'trap exit TERM; while :; do certbot renew; sleep 12h & wait $${!}; done;'"

networks:
  app-network:
    driver: bridge
```

2. Create an Nginx proxy configuration:

```nginx nginx-proxy.conf
server {
    listen 80;
    server_name chemreactions.org www.chemreactions.org;
    
    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl;
    server_name chemreactions.org www.chemreactions.org;

    ssl_certificate /etc/letsencrypt/live/chemreactions.org/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/chemreactions.org/privkey.pem;

    # Frontend
    location / {
        proxy_pass http://frontend:80;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    # Backend API
    location /api/ {
        proxy_pass http://backend:8000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

3. Set up the server (using DigitalOcean):

```bash
# On your local machine
ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
```

4. Go to DigitalOcean:
- Create an account
- Create a new Droplet (their term for a VM)
- Choose Ubuntu 20.04 LTS
- Choose a plan ($5-10/month should be fine for starting)
- Add your SSH key
- Choose a datacenter region close to your users

5. Point your domain to the server:
- Go to your domain registrar (where you purchased chemreactions.org)
- Update DNS settings:
  ```
  A record: chemreactions.org → Your server IP
  A record: www.chemreactions.org → Your server IP
  ```

6. SSH into your server and set it up:

```bash
# SSH into your server
ssh root@your-server-ip

# Update system
apt update && apt upgrade -y

# Install Docker and Docker Compose
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
apt install -y docker-compose

# Create project directory
mkdir -p /opt/chemreactions
cd /opt/chemreactions

# Create directories for SSL certificates
mkdir -p certbot/conf certbot/www
```

7. Create a deployment script:

```bash deploy.sh
#!/bin/bash

# Pull latest images
docker-compose -f docker-compose.prod.yml pull

# Stop and remove existing containers
docker-compose -f docker-compose.prod.yml down

# Start new containers
docker-compose -f docker-compose.prod.yml up -d
```

8. Initial SSL certificate setup:

```bash init-letsencrypt.sh
#!/bin/bash

domains=(chemreactions.org www.chemreactions.org)
email="your-email@example.com"
rsa_key_size=4096

# Install certbot certificates
docker-compose -f docker-compose.prod.yml run --rm --entrypoint "\
  certbot certonly --webroot -w /var/www/certbot \
    --email $email \
    --agree-tos \
    --no-eff-email \
    --force-renewal \
    ${domains[@]/#/-d }"
```

9. Deploy:

```bash
# On your server
cd /opt/chemreactions

# Copy your docker-compose.prod.yml and nginx-proxy.conf files to the server
# (You can use scp from your local machine)

# Make scripts executable
chmod +x deploy.sh init-letsencrypt.sh

# Initial SSL setup
./init-letsencrypt.sh

# Deploy
./deploy.sh
```

10. Set up automatic deployments using GitHub Actions by adding deployment step to your workflows:

```yaml .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    needs: [build-and-push] # Add this after your existing build jobs

    steps:
      - name: Deploy to Digital Ocean
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.SERVER_IP }}
          username: root
          key: ${{ secrets.SSH_PRIVATE_KEY }}
          script: |
            cd /opt/chemreactions
            ./deploy.sh
```

Add these secrets to your GitHub repository:
- `SERVER_IP`: Your DigitalOcean droplet IP
- `SSH_PRIVATE_KEY`: Your SSH private key

Now your app should be accessible at:
- https://chemreactions.org
- https://www.chemreactions.org

The setup provides:
- Automatic HTTPS/SSL certificates
- Automatic certificate renewal
- Automatic deployments when you push to main
- Proper proxy configuration for both frontend and backend
- Container restart on failure

Remember to:
1. Update your backend CORS settings to allow chemreactions.org
2. Configure any environment variables needed for production
3. Set up proper logging
4. Consider setting up monitoring (like Uptime Robot)
5. Regularly backup any persistent data
6. Keep your server updated

This setup should give you a professional, secure deployment of your application under your domain name.