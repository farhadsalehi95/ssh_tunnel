

import os
import subprocess
#import pyufw as ufw
import datetime
import logging
import json
import argparse
import ipaddress



parser = argparse.ArgumentParser()

parser.add_argument('-s' , '--sip' , dest = 'source_ip' , nargs='+',  help="add source ip address you want allow on ufw like this 192.168.1.1 192.168.2.2 192.168.3.3 and you can add 0.0.0.0 for any")
parser.add_argument('-sp' , '--sport' , dest = 'source_port' , nargs='+' , help='add source port you want allow on ufw like this 3306 3389 22')
parser.add_argument('-d' , '--dip' , dest = 'destination_ip' , nargs='+' , help="add destination ip address you want allow on ufw like this 192.168.1.1 192.168.2.2 192.168.3.3 and you can add 0.0.0.0 for any")
parser.add_argument('-dp' , '--dport' , dest = 'destination_port' , nargs='+' , help='add destination port you want allow on ufw like this 3306 3389 22')

args = parser.parse_args()

input_sips = args.source_ip
input_dips = args.destination_ip
input_sport = args.source_port
input_dport = args.destination_port

for a  in input_sips:
    ipaddress
ip_address_dictionary = {"ernyka_respina": "46.209.212.16/28" , "ernyka_afranet" : "217.11.27.194" , "ernyka_hetzner" : "162.55.76.101" }
