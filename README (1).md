# HackTheBox-FlowOverride
This repository documents the FlowOverride challenge from HackTheBox

# Challenge Scenario
A trusted friend gives you full access to his water treatment plant for a security test. The Siemens PLCs use S7comm — Can you break in and disrupt at least three pieces of equipment? 

![image](https://github.com/syncfailed/HackTheBox-FlowOverride/blob/main/img/InitialView.JPG)

# Tools Used
- Nslookup​
- Dig​
- Traceroute​
- Curl​
- Python

# Tools Deemed Incompatible this use case 
Tools that rely on public information or OSINT did not contribute as this challenge as it simulates an open-door test of the S7 protocol used by the machinery PLC logic.
- Nikto
- Metsploit
- OWASP Zap

**#Traceroute**
Traceroute helped us map the network path to the target. It showed the different hops between our system and the HackTheBox host, giving us a better idea of the network structure and where the target sits.

**#Nikto**
Next, we used Nikto to scan for web server vulnerabilities. However, it did not find any significant issues. This helped us rule out common web-based attack vectors.

**#Sn1per**
We also used Sn1per, which is an automated reconnaissance tool. It performed a broader scan of the system, but it did not detect any vulnerabilities either. This suggested that the system was not vulnerable to standard automated scans.

**#Metasploit**
Finally, we tried Metasploit to look for possible exploits. We tested modules related to industrial protocols, but they did not work for this case because the system used the S7 communication protocol, which is not fully supported.

Overall, these tools helped us understand that traditional penetration testing methods were not effective for this challenge, and a more specialized approach was required.

# Observations
The PLC logic constantly updates three bytes of data: Control, Mode and one component. Instead of targeting these we can work with the other 97 bytes to change the vaues in the PLC backend. The PLC logic will constantly try to reset or bring the machine metrics back to a healthy state depending on which is targeted first. 

# Final Outcome
We wera able to obtain the flag by disrupting three machines via the Python snap7 library as it provides access to the PLC logic and database which can be manipulated.
![image](https://github.com/syncfailed/HackTheBox-FlowOverride/blob/main/img/FinalView.JPG)

# Security Recommendations
- Disallow open programmatic access over the internet​
- Lock down PLC controls with least-privilege account permissions​
- The PLC logic only overrides three of the 100 bytes we chose to override. It should have an implementation to backup and halt access if commands cause failure​
