# Program No 2:
#!usr/bin/env python3
import subprocess
import optparse

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="Specify the interface for whoes mac address has to be changed")
    parser.add_option("-m","--mac",dest="new_mac",help="Specify the new mac address")
    (options,arguments)=parser.parse_args()
    if not options.interface:

    return options

def change_mac(interface,new_mac):
    subprocess.run(["ip","link","set",interface,"down"])
    subprocess.run(["ip","link","set",interface,"address",new_mac])
    subprocess.run(["ip","link","set",interface,"up"])

options = get_args()
change_mac(options.interface,options.new_mac)