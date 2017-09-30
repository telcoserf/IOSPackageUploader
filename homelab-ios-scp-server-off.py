#!/usr/bin/env python

"""
INFO: This script connects to an IOS device and disables the SCP server.

AUTHOR: zmw

DATE: 20170504 17:00 PDT
"""

#Make script compatible with both Python2 and Python3.
from __future__ import absolute_import, division, print_function

#Import functions/libraries needed.
import netmiko
import json
import sys
import signal
import os

#Silently exit upon user interruption (eg. Ctrl-C).
signal.signal(signal.SIGPIPE, signal.SIG_DFL) #IOError: Broken Pipe
signal.signal(signal.SIGINT, signal.SIG_DFL) #KeyboardInterrupt: Ctrl-C

#Identifying possible exceptions/errors that may arise.
netmiko_exceptions = (netmiko.ssh_exception.NetMikoAuthenticationException, netmiko.ssh_exception.NetMikoTimeoutException)

#Prompt user for their username.
username = os.environ["username"]
password = os.environ["password"]

#Get device name from encapsulating bash script and load into variable 'device'.
device = os.environ["host"]

#Tell NetMiko's ConnectHandler what it needs to know about the device.
ip = 'device'
device_type = 'cisco_ios'
username = username
password = password

#Connect to device, get running configuration, print, then disconnect.
connection = netmiko.ConnectHandler(ip=device, device_type=device_type,
									username=username, password=password)
print()
print('===> Disabling the SCP server on', device, '...')
connection.config_mode()
commands = [
            'no ip scp server enable'
            ]
connection.send_config_set(commands)
connection.exit_config_mode()
print('     Done!')
connection.disconnect()
