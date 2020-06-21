This script can be used to create addressobjects for your Fortigate (and maybe other FortOS devices aswell, on FG verified). 
Currently no support for names with whitespaces.
Note that the input file needs to be whitespace seperated for this script to work in the following order:

1. name    
2. type    
3. address     
4. netmask         
5. associated-interface

Output will be placed in a separate file with the following output for every line:

config firewall address
edit "name"
set type type
set subnet address netmask
set associated-interface associated-interface
end


There are no checks for invalid inputs and the code is not streamlined. All feedback is very much welcome.
