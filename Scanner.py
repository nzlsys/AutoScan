import os
import scans

def scan_type(type):
    while True: 
        inp=input("Do you want to specify desired top-ports number? Otherwise, a full scan will be started.(y/n) \n") 
        if inp=='y' or inp=='Y': # asking full scan or desired top-ports
            portNum=input("Please enter the desired top ports\n")
            port=f'-top-ports {portNum}'
            if type=='nmap':
                scans.nmap_scan(ip,port)
            elif type=='file': 
                scans.file_scan(path,port) # scanning from a given file
            break
        elif inp=='n' or inp=='N': # full scanning
            port='-p-'
            if type=='nmap':
                scans.nmap_scan(ip,port)
            elif type=='file':
                scans.file_scan(path,port)
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'") 

print("\nWelcome to AutoScan Tool\n-------------------------------------------------------\nPlease specify from the list below what you want to do.")
while True:
    i=input("1)Scanning an IP or IP range \n2)Scanning from a list of targets \n")
    if i=='1':
        ip=str(input("Please enter the target: (Range format is: 192.168.1.1-80)\n")) 
        scan_type('nmap')
        break
    elif i=='2':
        path=input("Please specify the path of the file:\n")
        if os.path.exists(path): #validating the file path
            scan_type('file')
        else:
            print("The file does not exist")
        break
    else:
        print("Input is not valid. Please enter '1' or '2'")
