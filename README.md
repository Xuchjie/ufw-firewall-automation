# Basic Firewall Rule Automation Using UFW and Bash

## Project Overview  
This project automates basic firewall configuration on Linux systems using UFW (Uncomplicated Firewall) and a Bash script. The script installs UFW if missing, sets secure default firewall policies, allows SSH access, and lets users interactively add custom port rules. This simplifies firewall management, reduces manual errors, and improves system security.

## Features  
- Automatically installs UFW if it’s not already installed  
- Enables UFW with default policies: deny all incoming, allow all outgoing  
- Opens SSH port 22 by default for remote access  
- Interactive prompt to add additional ports securely  
- Validates user input to allow only valid port numbers  
- Idempotent: avoids adding duplicate rules if run multiple times  

## Prerequisites  
- Linux system with Bash shell  
- `sudo` privileges to modify firewall rules  

## Setup Instructions  
1. Clone this repository:  
   ```bash
   git clone https://github.com/Xuchjie/ufw-firewall-automation.git


