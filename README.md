# Project Overview
This project automates basic firewall configuration on Linux systems using UFW (Uncomplicated Firewall) and a Bash script. The script sets secure default firewall policies, allows SSH access, and lets users interactively add custom port rules. This simplifies firewall management, reduces manual errors, and improves system security.

# Features
- Automatically installs UFW if not already present
- Enables UFW with default deny incoming and allow outgoing policies
- Opens SSH port 22 by default for remote access
- Interactive prompt to add additional ports securely
- Validates user input to ensure proper port numbers
- Idempotent: avoids adding duplicate rules on multiple runs

# Prerequisites
- Linux system with Bash shell
= UFW (the script will install it if missing)
- sudo privileges to modify firewall rules

# Setup Instructions
Clone this repository:
git clone https://github.com/YourUsername/ufw-firewall-automation.git

# Navigate into the project directory:
cd ufw-firewall-automation
# Make the script executable:
- chmod +x firewall-setup.sh
# Run the script with sudo:
- sudo ./firewall-setup.sh

#Usage
- The script will enable the firewall and set default policies.
- SSH port 22 will be opened automatically.
- You will be prompted to enter any additional ports to open (space-separated).
- Press Enter to skip adding extra ports.

# Project Structure
- firewall-setup.sh: The main Bash script to automate UFW setup
- README.md: Project documentation
- Additional supporting files or documentation as needed

# AI Tools Used
- ChatGPT: For brainstorming, code snippets, and scripting help
- GitHub Copilot: Assisted with code completion and syntax suggestions

# License
This project is licensed under the MIT License.
