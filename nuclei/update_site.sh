BOLD="\e[1m"
CYAN='\033[0;36m'
RED='\033[0;31m'
black='\033[0;30m'
green='\033[0;32m'
yellow='\033[0;33m'
magenta='\033[0;35m'
NC='\033[0m' # A part of the puzzle

echo -e "\n$RED${BOLD} [x]$green Updating Database $RED${BOLD}[x]$NC$CYAN"
sed 's/\x1b\[[0-9;]*m//g' vuln.db > vuln_cleaned.db
python3 turn_cleaned_jsn.py 
echo -e "\n$RED${BOLD} [!]$green Done Updating Database $RED${BOLD}[!]$NC"
