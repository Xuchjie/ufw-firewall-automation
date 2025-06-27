#!/bin/bash

echo "=== Basic UFW Firewall Setup ==="

# Check if UFW is installed
if ! command -v ufw >/dev/null 2>&1; then
    echo "UFW is not installed. Installing..."
    sudo apt update && sudo apt install -y ufw
fi

# Enable UFW if not already active
ufw status | grep -q inactive && {
    echo "Enabling UFW..."
    sudo ufw enable
}

# Set default policies
echo "Setting default policies..."
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Allow SSH (port 22)
echo "Allowing SSH (port 22)..."
sudo ufw allow 22/tcp

# Ask user to enter additional ports to allow
read -p "Enter additional ports to allow (space-separated), or press Enter to skip: " ports

if [ -n "$ports" ]; then
    for port in $ports; do
        echo "Allowing port $port..."
        sudo ufw allow "$port"
    done
fi

echo "Firewall setup complete!"
ufw status verbose
