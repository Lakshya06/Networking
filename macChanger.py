#!/usr/bin/env python

import subprocess
import optparse
import re

parser = optparse.OptionParser()

def changeMac(interface, mac):
    print("Changing MAC Adress to " + mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])

def getCurrentMac(interface):

    temp = subprocess.check_output(["ifconfig", interface])
    ifconfigRes = temp.decode('utf-8')
    # print(ifconfigRes)

    macSearchRes = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfigRes)

    if not macSearchRes:
        print("Could not find MAC Address!")
        return
    return macSearchRes.group(0)
    

parser.add_option("-i", "--interface", dest="interface", help="Specify interface")
parser.add_option("-m", "--mac", dest="mac", help="Enter MAC Adress")

(options, args) = parser.parse_args()

if not options.interface:
    parser.error("Please specify an interface!")
if not options.mac:
    parser.error("Please Enter a MAC address!")

changeMac(options.interface, options.mac)

currMac = getCurrentMac(options.interface)
# print(currMac)

if currMac == options.mac:
    print("MAC Address successfully changed to: ", str(currMac))
else:
    print("Failed to change MAC Address, Try Again!")

# print(options)
# print(args)

# subprocess.call("ifconfig", shell=True)
    
# 08:00:27:21:b1:d0