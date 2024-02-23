#!/usr/bin/env python

import scapy.all
import argparse

def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Specify target IP/IP range")
    ops = parser.parse_args()
    return ops

def scan(ip):

    arpRequest = scapy.all.ARP(pdst = ip)
    # print(arpRequest.summary())
    broadcast = scapy.all.Ether(dst="ff:ff:ff:ff:ff:ff")
    # print(broadcast.summary())

    arpBroadcast = broadcast/arpRequest
    # print(arpBroadcast.summary())

    ans, unans = scapy.all.srp(arpBroadcast, timeout=1)
    # print(ans)

    targets = []

    for target in ans:
        # print(target)
        # break
        temp = {"ip":target[1].psrc, "mac":target[1].hwsrc}
        targets.append(temp)
    
    return targets

def getResult(targets):

    print("\nFound",len(targets),"active targets!\n")

    print("IP \t\t MAC Address \n------------------------------------------")
    for target in targets:
        print(target["ip"] + "\t\t" + target["mac"])

ops = arguments()
scanRes = scan(ops.target)
getResult(scanRes)