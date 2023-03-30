# New Mexico Water Resources Toolkit

This Docker project runs the Water Rights Visualizer and ET Toolbox on AWS.

## Docker

Install `docker-compose` on an Amazon Linux EC2 instance on AWS.

```
#!/bin/bash
sudo yum -y update
sudo yum install -y docker
sudo usermod -a -G docker $(whoami)
sudo service docker start
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

## Repository

Clone the repository on the EC2 instance.
```
git clone git@github.com:New-Mexico-Water-Resources/New-Mexico-Docker.git
```

## Keys

Copy `django.env` to the `New-Mexico-Docker` directory.

Copy `google_drive_key.txt` to the `New-Mexico-Docker/app` directory.

Copy `client_secrets.json` to the `New-Mexico-Docker/app` directory.

## Run

Run with `docker-compose`
```
docker-compose up -d
```
