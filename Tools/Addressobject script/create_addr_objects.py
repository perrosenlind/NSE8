#!/usr/bin/env python3

#Variables:
#filename:
f_input = '/Users/perrosenlind/Documents/GitHub/NSE8/Tools/Addressobject script/addresslist.txt'
f_output = '/Users/perrosenlind/Documents/GitHub/NSE8/Tools/Addressobject script/addresslist.conf'

#Open a file with access mode 'a+'
output = open(f_output, 'a+')

with open(f_input,) as f:
    addresslist = f.read()

for line in addresslist.splitlines():
    fields = line.split()
    name = fields[0]
    addrtype = fields[1]
    address = fields[2]
    netmask = fields[3]
    assoicatedinterface = fields[4]
    output.write('\n')
    output.write('config firewall address')
    output.write('\n')
    output.write('edit ')
    output.write(name)
    output.write('\n')
    output.write('set type ')
    output.write(addrtype)
    output.write('\n')
    output.write('set subnet')
    output.write(address)
    output.write(' ')
    output.write(netmask)
    output.write('\n')
    output.write('set associated-interface ')
    output.write(assoicatedinterface)
    output.write('\n')
    output.write('end')
    output.write('\n')
    
#close the file
output.close()

