# Dynamic DNS script: checks machine's current IP address and updates DNS
# A-record if it's changed since the last time checked.

# Install DNS-Lexicon (https://dns-lexicon.readthedocs.io).
#   pip install dns-lexicon

# Set the DNS service name, domain and subdomain, and login credentials below.
# Use `which lexicon` to get the correct path for your system.

# Set up this script as a cron job (e.g. every 10 minutes). Use `which python`
# to get the correct Python path for your system.
#   crontab -e
#   */10 * * * * cd path/to/dir && path/to/python dns-update.py >> log.txt 2>&1

# If you're NOT running this as a cron job, you have the option to save
# credentials in environment variables rather than including them in the script
# (cron doesn't have easy access to environment variables).
#   export LEXICON_HOVER_USERNAME=my-username
#   export LEXICON_HOVER_PASSWORD=my-password

import os
from datetime import datetime as dt

with open('last-ip.txt', 'r') as f:
    last_ip = f.read()

print()
print(str(dt.now()))

ip = os.popen("dig @resolver4.opendns.com myip.opendns.com +short").read().strip()
print("IP is {}".format(ip))

if ip != last_ip:
    # This needs an absolute path to `lexicon` in order to run from cron
    result = os.popen("/Users/maurer/opt/anaconda3/bin/lexicon hover update smaur.io A --name paris-dynamic --content {} --auth-username my-username --auth-password my-password".format(ip)).read() 
    
    if ('True' in result):
        print("DNS A-record updated")

        with open('last-ip.txt', 'w') as f:
            f.write(ip)

    else:
        print(result)
