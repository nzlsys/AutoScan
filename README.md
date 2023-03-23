
<h1 align="left">Description</h1>

<br clear="both">
<p align="left">Autoscan is a scanning tool mixed of Nmap, Nikto and Dirb. The tool performs the following steps:<br>* It uses Nmap to scan for open ports on a target system.<br>* If an HTTP service is found, it proceeds to the next step.<br>* It launches two other scanning tools - Nikto and Dirb - to scan for vulnerabilities and directories on the HTTP service.<br>* After all scans are completed, it generates a report that shows the results of all scans, including the results of the Nmap, Nikto, and Dirb scans.</p>
<img width="480" alt="image" src="https://user-images.githubusercontent.com/123561773/227210707-7fb67da7-bdf9-4be6-9195-8d110468f143.png">




<h1 align="left">Usage</h1>


<p align="left">1) Run Scanner.py file 
<br>2)Selecting an appropriate scanning type
<br>3) Inputting the desired target for scanning
<br>4) Optionally specifying top ports to scan<br><br>

![image](https://user-images.githubusercontent.com/123561773/227210292-1a488142-1d35-45d0-9990-070dcb660a71.png)

<br>5) Nmap scan is done and if there is an HTTP service, Nikto and Dirb scan is started for that port.</p>

<img width="794" alt="image" src="https://user-images.githubusercontent.com/123561773/227055478-f9568db9-d73b-4dc4-a733-f20b2da4edf1.png">

###


