
<h1 align="left">Description</h1>
<img width="474" alt="image" src="https://user-images.githubusercontent.com/123561773/227206561-35625ef8-ce99-4d72-8834-61e383c0b8c2.png">
<br clear="both">
<p align="left">Autoscan is a scanning tool mixed of nmap, nikto and dirb. The tool performs the following steps:<br>* It uses Nmap to scan for open ports on a target system.<br>* If an HTTP service is found, it proceeds to the next step.<br>* It launches two other scanning tools - Nikto and Dirb - to scan for vulnerabilities and directories on the HTTP service.<br>* After all scans are completed, it generates a report that shows the results of all scans, including the results of the Nmap, Nikto, and Dirb scans.</p>



<h1 align="left">Usage</h1>


<p align="left">1) Selecting an appropriate scanning type
<br>2) Inputting the desired target for scanning
<br>3) Optionally specifying top ports to scan<br><br>

<img width="792" alt="image" src="https://user-images.githubusercontent.com/123561773/227206895-e5a5504c-f529-4d40-952c-2e2219be915e.png">

<br>4) Nmap scan is done and if there is an HTTP service, Nikto and Dirb scan is started for that port.</p>

<img width="794" alt="image" src="https://user-images.githubusercontent.com/123561773/227055478-f9568db9-d73b-4dc4-a733-f20b2da4edf1.png">

###


