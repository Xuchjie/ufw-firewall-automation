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
2. Navigate into the project directory:
cd ufw-firewall-automation
3. Make the script executable:
cd ufw-firewall-automation
4. Run the script with sudo:
sudo ./firewall-setup.sh
5. When prompted, enter any additional ports you want to allow separated by spaces, or press Enter to skip.

## Usage
The script will automatically install UFW if missing and enable it.
Sets default firewall policies: deny incoming, allow outgoing.
Opens SSH port 22 for remote administration.
Prompts for additional ports to open securely.
Validates ports before adding rules to avoid errors.

Project Structure
- firewall-setup.sh: Bash script that automates UFW firewall setup
- README.md: Project documentation

## AI Tools Used
- ChatGPT: Assisted with brainstorming, code snippets, and scripting help
- GitHub Copilot: Provided code completions and syntax suggestions





