sudo apt update

sudo apt install apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://get.docker.com | sudo sh

sudo systemctl start docker

sudo usermod -aG docker $USER

docker --version



sudo curl -L "https://github.com/docker/compose/releases/download/v2.18.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

docker-compose --version
