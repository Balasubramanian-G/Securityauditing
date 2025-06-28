# Securityauditing

This first python script perform  Basic security auditing and the second one stimulate a DOS(Denial of service) Attack to Understand the concept of (DoS) attacks.

Description:

Task:1
     The fisrt task performs the basic security auditing like it checks for open ports and the service running on the open ports ,it ckecks for  basic security flaws.It checks the http header for the vulnerability.It takes the input from the user whether it is IP or domain name it takes input from user and the port range from the user and it checks for the open ports.also it get the services running on the opened port.After completing the port scanning it checks for the HTTP header .First it send a HTTP GET REQUEST to the desired domain and the server will respond to the HTTP GET REQUEST after it checks for the HTTP header finally it generate a report.

Task:2
     The second task stimulates a DOS ATTACK .The purpose of this task is to Understand the concept of Denial of Service (DoS) attacks and we can mitigate the attack by using methods like Rate limiting,using firewalls,setting session time etc.. 

Packages used:

Task:1
   Python: subprocess, requests

Task:2
  Python: requests for sending repeated HTTP requests

Sample output:

Task:1

      --- Security Audit Report ---
Target: 127.0.0.1

Open Ports:
 - Port 5000 is OPEN

Service Banners:
 - Port 5000: timed out

HTTP Security Headers:
 - Content-Security-Policy: Missing
 - Strict-Transport-Security: Missing
 - X-Content-Type-Options: Missing
 - X-Frame-Options: Missing
 - X-XSS-Protection: Missing

