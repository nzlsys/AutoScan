import xml.etree.cElementTree as ET
import subprocess
import report

class Service: # keeping the running services' information
    def __init__(self, ipaddr,service_name, port_number,product):
        self.ipaddr=ipaddr
        self.service_name = service_name
        self.port = port_number
        self.product=product
        self.list={
            'ip adress':self.ipaddr,
            'port number':self.port, 
            'service':self.service_name,
            'product':self.product}
        
def nmap_scan(ip,port): # nmap scanning
    print("--------------------------------------------------------------------")
    print("Nmap scan is starting")
    cmd1=f"nmap -sSV --open -Pn -oX Nmap-for-{ip}.xml {ip} {port}"  # xml file for the parsing 
    cmd2=f"nmap -sSV --open -Pn -oN Nmap-for-{ip}.txt {ip} {port}"  
    subprocess.run(cmd1,shell=True, capture_output=True) # executing shell commands for nmap 
    subprocess.run(cmd2,shell=True)
    report.nmap(ip) # writing nmap result to the final report
    parser(ip) 
    report.show(ip) # asking for showing the report or not

def file_scan(path,port): # nmap scanning from a given file 
    print("--------------------------------------------------------------------")
    print("Nmap scan is starting")
    cmd1=f"nmap -sSV --open -Pn -iL {path} -oX Nmap-for-{path}.xml {port}"
    cmd2=f"nmap -sSV --open -Pn -iL {path} -oN Nmap-for-{path}.txt {port}"
    subprocess.run(cmd1,shell=True, capture_output=True)
    subprocess.run(cmd2,shell=True)
    report.nmap(path)
    parser(path)
    report.show(path)

def nikto(ip,portnumber):
    cmd1=f"nikto -h http://{ip}:{portnumber} -o Nikto-for-{ip}.txt"
    print("--------------------------------------------------------------------")
    print("Nikto scan is starting")
    subprocess.run(cmd1,shell=True)

def dirb(ip,portnumber):
    cmd1=f"dirb http://{ip}:{portnumber} -S -o Dirb-for-{ip}.txt"
    print("--------------------------------------------------------------------")
    print("Dirb scan is starting")
    subprocess.run(cmd1,shell=True)

def parser(ip): # parsing function for nmap xml file
    availableService=[]
    currentService=[]
    List=[]
    tree=ET.parse(f'Nmap-for-{ip}.xml') 
    root=tree.getroot()
    for host_tag in root.findall(f".//host"): # entering host tag
        for host_ip in host_tag.findall(f"./address/[@addrtype!='mac']"):# finding host ip
            for port in host_tag.findall(f"./ports/port"):  # finding portid 
                port_number=str(port.get('portid'))
                for y in port.findall(".//service"): # finding services' product and version information
                    service_name=str(y.get('name'))
                    product=str(y.get('product'))
                    ipaddr=str(host_ip.get('addr'))
                    serviceList = Service(ipaddr,service_name,port_number, product)
                    List.append(serviceList.list) # saving ip adresses and port numbers information
                    currentService.append(service_name)
                    availableService=set(currentService) # making the service list unique

    if not len(availableService)==0: # checking available service is empty
        print(f"Avaiable services are:\t{availableService}")
        key='http'
        httpServices=[sub for sub in List if key in list(sub.values())] # finding http services and their ip adresses
        if not len(httpServices)==0:
            print(f"Information about hosts that have http service: {httpServices}") 
            http=[]
            portNum=[]
            for i in range(len(httpServices)):
                http.append(httpServices[i]['ip adress'])   # creating http list and portNum list
                portNum.append(httpServices[i]['port number'])
            
            for i in range(len(http)): 
                if not len(http)==0: # dirb and nikto scan for hosts that have http service
                    dirb(http[i],portNum[i]) 
                    nikto(http[i],portNum[i])  
                report.dirb_and_nikto(http[i],ipRange=ip) # writing the dirb and nikto scan result to the final report
