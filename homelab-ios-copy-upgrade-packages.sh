#!/bin/bash

# This script will connect to each device in a list, configure it as an SCP
## server, copy software upgrade packages to the device, remove the SCP server
### config and default aaa values, then disconnect and move on to the next
#### device.

echo ""
echo "**********************************************************************"
echo "* This script will enable SCP on, copy software upgrade packages to, *"
echo "* and finally disable SCP on a list of devices...                    *"
echo "**********************************************************************"

username="your-username"
password="your-password"
export username
export password

# For Loop - processes each line in the text file as a host/device
for host in $(cat homelab-cat3750-list.txt); do
  echo ""
  echo "Processing $host..."
  export host
  python homelab-ios-scp-server-on.py "$host"
  echo "===> Copying test01.txt to $host; enter your login password when prompted ..."
  scp -oKexAlgorithms=+diffie-hellman-group1-sha1 test01.txt zmw@"$host":/test01.txt
  echo ""
  echo "Done with $host!"
  echo ""
  echo "-------------------------------------------------------------------------"
done

echo ""
echo "****************************"
echo "* Finished running script! *"
echo "****************************"
echo ""

# eof
