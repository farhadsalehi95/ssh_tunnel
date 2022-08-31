

import os
import subprocess
#import pyufw as ufw
import datetime
import logging
import json
import argparse
import ipaddress

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s' , '--sip' , dest = 'source_ip' , nargs='+',  help="add source ip address you want allow on ufw like this 192.168.1.1 192.168.2.2 192.168.3.3 and you can add 0.0.0.0 for any")
    parser.add_argument('-sp' , '--sport' , dest = 'source_port' , nargs='+' , help='add source port you want allow on ufw like this 3306 3389 22')
    parser.add_argument('-d' , '--dip' , dest = 'destination_ip' , nargs='+' , help="add destination ip address you want allow on ufw like this 192.168.1.1 192.168.2.2 192.168.3.3 and you can add 0.0.0.0 for any")
    parser.add_argument('-dp' , '--dport' , dest = 'destination_port' , nargs='+' , help='add destination port you want allow on ufw like this 3306 3389 22')
    return parser.parse_args()

def ipValidation(args):
    try:
        for i in args:
            try:
                ipaddress.ip_address(i)
            except ValueError:
                print(f'IP {i} is not valid')
    except:
        pass

def portValidation(args):
    try:
        for i in args:
            try:
                if int(i) > 65535:
                    print (f'port {i} is greater than 65535')
                elif not int(i.isdigit()):
                    print (f'please input number for port not {i}')
            except:
                pass
    except:
        pass

args = getArgs()
ipValidation(args.source_ip)
ipValidation(args.destination_ip)
portValidation(args.source_port)
portValidation(args.destination_port)

