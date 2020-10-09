#!/usr/bin/env python3

import subprocess
from getpass import getpass
from rich.console import Console
from rich.table import Table
import itertools

good_list = []
bad_list = []

#SNMP Settings
auth_proto = "SHA"
priv_proto = "AES"
#snmp_oid = "1.3.6.1.2.1.1"
snmp_oid = "system"
device_count = 0
snmp_version = "SNMPv3"
number_of_lines = 0
username = "Not set"
print("Current settings:")
print(f"SNMP Version: {snmp_version}")
print(f"Username: {username}")
print(f"Auth protocol: {auth_proto}")
print(f"Priv protocol: {priv_proto}")
print(f"SNMP OID: {snmp_oid}")

username = input("Username: ")
authpassword = getpass(prompt="AUTH password: ")
privpassword = getpass(prompt="PRIV password: ")

#Read the amount of lines in a file to calculate progress
with open("reader.txt", "r") as f:
    filelines = f.readlines()
for line in filelines:
    number_of_lines += 1

#Read the text file and snmpwalk once per row. No check for valid IP address.
with open("reader.txt", "r") as f:
    filelines = f.readlines()
for ip in filelines:
    print(f'\nReading {ip}')
    getResult = subprocess.Popen(
        f"snmpwalk -v3  -l authPriv -u '{username}' -a {auth_proto} -A '{authpassword}' -x {priv_proto} -X '{privpassword}' {ip} '{snmp_oid}'",
        shell=True,
        stdout=subprocess.PIPE,
    ).stdout
    device_count += 1
    output = getResult.read()
    result = output.decode("utf-8", "ignore")
    #print(result)
    print(f'Read done')
    print(f'Result: ')
    if "MIB" in result:
        good_list.append(ip)
        print("Successful!")
    else:
        bad_list.append(ip)
        print("Did not work!")
    progress = ("{0:.0f}%".format(device_count/number_of_lines * 100))   
    print(f'Progress: {device_count}/{number_of_lines} ({progress})\n')
     

table = Table(title="\n \nSUMMARY REPORT \n")
table.add_column("Successful Hosts", justify="center", style="green")
table.add_column("Failed Hosts", justify="center", style="red")
for (success, fail) in itertools.zip_longest(good_list, bad_list):
    table.add_row(success, fail)
console = Console()
console.print(table)
