# Port Scanner

This project is a simple port scanner built using Python. The program is used to scan a specified range of ports on a given target IP address so it can search for any open ports. 

## Description
The port scanner is particularly used in the field of cybersecurity and network administration to probe a server or host so open ports can be found using the provided IP address. It’s a basic yet quite an effective tool when it comes to exploring a network.

## Installation Process
**1) Clone this repository** 

```bash
git clone https://github.com/firewallumbra/port-scanner-yay
cd port-scanner-yay
```

**2) Install the package necessary for running the program: python3 (note that the following code is exclusive to the Alpine Linux distribution)**

```bash
   apk update
   apk add python3
```
   
**3) Run the port scanner:**

   ```bash
python3 port_scanner.py
```

Below is an example output, done using one of Google's public DNS' two IP addresses:

- Enter the target IP address: 8.8.8.8
- Enter the start port: 0
- Enter the end port: 100
- Starting scan on host: 8.8.8.8
- Port 25: Open
- Port 53: Open
- Scanning completed in: 0:01:38.638363
