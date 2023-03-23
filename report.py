import os

def nmap(ip): 
    file=open(f"Report-for-{ip}.txt",'w') # creating a report file   
    file.write(f'\n\n\t\t\tAUTOSCAN REPORT for target: {ip}\n\n')
    nmapfile=open(f'Nmap-for-{ip}.txt','r') # reading the nmap output file
    lines=nmapfile.read()
    content=f"Nmap Scan for {ip}: {lines}"
    file.writelines(content)  # writing the nmap file to the final report 
    file.close()
    nmapfile.close()

def dirb_and_nikto(ip,ipRange): # reading the dirb and nikto output files and write them to the final report
    scan_types=['Dirb','Nikto']
    for type in scan_types:
        file=open(f'{type}-for-{ip}.txt','r')
        res=file.read()
        content="\n--------------------------------------------------------------------------------------\n{} SCAN\t\t for host:{}\n{}\n\n".format(type,ip,res)
        file=open(f'Report-for-{ipRange}.txt','a')
        file.writelines(content)
        file.close()
        os.system(f"rm {type}-for-{ip}.txt") # removing dirb and nikto output files  
    os.system(f"rm Nmap-for-{ipRange}.*") # removing nmap output files

def show(file): # showing the final report or not
    inp=input(f"Do you want to open the report: 'Report-for-{file}.txt' ? (y/n)\n")
    if inp=='y':
        file=open(f"Report-for-{file}.txt",'r')
        print(file.read())
        file.close()
    elif inp=='n':
        None
    else :
        print("İnvalid input ")






