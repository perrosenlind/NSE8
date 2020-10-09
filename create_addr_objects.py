#!/usr/bin/env python3
import csv
#Variables:
#filename/path:
f_input = 'addresslist.csv'
f_output = 'addresslist_from_csv.conf'

#Open a file with access mode 'a+'
output = open(f_output, 'a+')

with open(f_input) as addresslist:
    csv_reader = csv.reader(addresslist, delimiter=';')
    addresslist.readline() #Skip csv header
    line_count = 0
    output.write('config firewall address\n')
    for line in csv_reader:
        output.write('edit "' + line[0] + '"\n')
        output.write('set type' + line[1] + '\n')
        output.write('set comment "' + line[5] + '"\n')
        output.write('set associated-interface "' + line[4] + '"\n')
        output.write('set subnet "' + line[2] + line[3] + '"\n')
        output.write('next\n')
        line_count += 1
    output.write('end\n')

#close the file
output.close()
#Inform the user about how many objects that has been created.
print(f'Created {line_count} objects.')

