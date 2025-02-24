# Deployment Steps

1. Initialize Git and Create GitHub Repository:
```bash
# Initialize git if not already done
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit"

# Create a new repository on GitHub through the web interface
# Then link your local repo (replace with your username/repo)
git remote add origin https://github.com/yourusername/chemreactions.git
git branch -M main
git push -u origin main
```

2. Set up GitHub Repository Settings:
- Go to your repository settings on GitHub
- Under "Security > Actions > General":
  - Enable "Read and write permissions" under "Workflow permissions"
- Under "Security > Secrets and variables > Actions":
  Add these secrets:
  - `SERVER_IP`: Your server's IP address
  - `SSH_PRIVATE_KEY`: Your SSH private key
  - `GITHUB_USERNAME`: Your GitHub username

3. Create deployment workflow:

```yaml .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    needs: [build-and-push-backend, build-and-push-frontend]
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2
        
      - name: Copy deployment files
        uses: appleboy/scp-action@master
        with:
          host: ${{ secrets.SERVER_IP }}
          username: root
          key: ${{ secrets.SSH_PRIVATE_KEY }}
          source: "docker-compose.prod.yml,nginx-proxy.conf"
          target: "/opt/chemreactions"
          
      - name: Deploy to Digital Ocean
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.SERVER_IP }}
          username: root
          key: ${{ secrets.SSH_PRIVATE_KEY }}
          script: |
            cd /opt/chemreactions
            export GITHUB_USERNAME=${{ secrets.GITHUB_USERNAME }}
            docker-compose -f docker-compose.prod.yml pull
            docker-compose -f docker-compose.prod.yml down
            docker-compose -f docker-compose.prod.yml up -d
```

4. Create the proxy configuration file:

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

5. Server Setup Commands:
```bash
# SSH into your server
ssh root@your-server-ip

# Update system
apt update && apt upgrade -y

# Install Docker and Docker Compose
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
apt install -y docker-compose

# Create project directory and SSL directories
mkdir -p /opt/chemreactions/certbot/conf /opt/chemreactions/certbot/www
cd /opt/chemreactions

# Initialize SSL certificates
docker run -it --rm --name certbot \
  -v "/opt/chemreactions/certbot/conf:/etc/letsencrypt" \
  -v "/opt/chemreactions/certbot/www:/var/www/certbot" \
  certbot/certbot certonly \
  --webroot -w /var/www/certbot \
  --email your@email.com \
  -d chemreactions.org -d www.chemreactions.org \
  --agree-tos
```

6. Push all changes to GitHub:
```bash
git add .
git commit -m "Add deployment configurations"
git push origin main
```

After completing these steps:

1. The GitHub Actions workflows will:
   - Build your Docker images
   - Push them to GitHub Container Registry
   - Deploy them to your server

2. Your application will be accessible at:
   - https://chemreactions.org
   - https://www.chemreactions.org

3. To monitor the deployment:
   - Check the "Actions" tab in your GitHub repository
   - On your server, use `docker-compose -f docker-compose.prod.yml logs -f` to view logs

Remember to:
- Update DNS settings at your domain registrar to point to your server IP
- Test the site thoroughly after deployment
- Monitor the logs for any issues
- Set up regular backups
- Keep your server and containers updated