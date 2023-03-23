
<h1 align="left">Description</h1>

<br clear="both">
<p align="left">Autoscan is a scanning tool mixed of Nmap, Nikto and Dirb. The tool performs the following steps:<br>* It uses Nmap to scan for open ports on a target system.<br>* If an HTTP service is found, it proceeds to the next step.<br>* It launches two other scanning tools - Nikto and Dirb - to scan for vulnerabilities and directories on the HTTP service.<br>* After all scans are completed, it generates a report that shows the results of all scans, including the results of the Nmap, Nikto, and Dirb scans.</p>
<img width="480" alt="image" src="https://user-images.githubusercontent.com/123561773/227210707-7fb67da7-bdf9-4be6-9195-8d110468f143.png">




<h1 align="left">Usage</h1>


<p align="left">1) Run Scanner.py file 
<br>2) Selecting an appropriate scanning type
<br>3) Inputting the desired target for scanning
<br>4) Optionally specifying top ports to scan<br><br>

<img width="840" alt="image" src="https://user-images.githubusercontent.com/123561773/227214721-6ef8d0fb-6cb5-44f5-8c2c-f4558a085cb4.png">

<br>5) Nmap scan is done and if there is an HTTP service, Nikto and Dirb scan is started for that port.
<br>6) Optionally opening the report </p>


<img width="1412" alt="image" src="https://user-images.githubusercontent.com/123561773/227217572-49bc3760-7ac5-4ba0-b9ef-f6e4f722b6fe.png">


###


