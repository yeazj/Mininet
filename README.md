## Benign & Attack traffic generation on an emulated Enterprise network
* An emulated enterprise network on Mininet comprising of DNS, HTTP, HTTPS, FTP, SMTP and DB servers.
* Network attacks
  * Bruteforce attack using Metasploit
  * Web attacks using cURL
    * SQL injection
    * XSS
  * Probe attacks using NMAP
  * Phishing attacks using Harvester
  * Infiltration attacks using Meterpreter payload
  * DOS attacks using Hping (SYN Flood)
  * DDOS attacks using LOIC
  * Botnet attacks using Ares
  * Vulnerability exploits using Nessus
  * Mitm attacks using Dnsmasq cache poisoning
  
## Setup

#### Pre-req : Kali Linux
> Not tested on other platforms yet but shouldn't be much different on any other Debian/Ubuntu Linux \
> Ensure there's no Internet connectivty as this will auto-update DNS entries.

#### 1. Start POX [[Link to POX]](https://github.com/noxrepo/pox "POX Repo")
> ```console
> #./pox.py log.level DEBUG forwarding.l2_learning
> ```

#### 2. Stop NetManager (to prevent it from updating /etc/resolve.conf)
> ```console
> #service NetworkManager stop
> ```

#### 3. Check configs
> [/etc/resolve.conf](/resolve.conf) & [/etc/dnsmasq.hosts](/dnsmasq.hosts)

> ```diff
> - TBA - Add dnsmasq config
> ```

#### 4. Start Mininet
> ```console
> #service openvswitch-switch start
> ```

> ```console
> #./my_net.sh
> ```
> Ensure NetworkManager is still stopped.

#### 5. Start DNS (DOS/DDOS attack target)
> ```console
> mininet> xterm dns
> ```

> ```console
> xterm# dnsmasq --log-queries --no-daemon
> ```

#### 6. Start FTP (Bruteforce attack target)
> ```console
> #sudo apt-get install python-pyftpdlib
> ```

> ```console
> mininet> xterm l_ftp
> ```

> ```console
> xterm# python scripts/ftp/server_ftp/basic_ftpd.py
> ```

#### 7. Start SMTP
> ```console
> mininet> xterm email
> ```

> ```console
> xterm# python scripts/smtp/smtpd_custom.py
> ```

#### 8. Start PostgreSQL over HTTPS server
> ```diff
> - TBA - Add postgre config
> ```

> ```console
> #service postgresql start
> ```

> PostgreSQL runs on local machine (fetch IP)

> Change IP in Engine in [app.py](scripts/http_postgre/app.py) & [insertable.py](/scripts/http_postgre/insertable.py) & [createtable.py](scripts/http_postgre/createtable.py)
> ```python
> engine = create_engine('postgresql://postgres:postgres@x.x.x.x:5432/test', echo=True)
> ```

> Create *users* table in Postgre (first time only)
> ```console
> #python scripts/http_postgre/createtable.py
> ```

> Insert 'username' and 'password' in *users* table (first time only)
> ```console
> #python scripts/http_postgre/insertable.py
> ```

> ```console
> mininet> xterm https
> ```

> ```console
> xterm# python scripts/http_postgre/app.py
> Pass phrase is : mssd
> ```

#### 9. Start HTTP with Upload
> ```console
> mininet> xterm web
> ```

> ```console
> xterm# python scripts/http_upload/shttpu.py 80
> ```

#### 10. Start Vulnerable HTTP (Web attacks target)
> [Link to YAVW - Yet Another Vulnerable Webserver](https://github.com/noleti/yavw)

> ```console
> mininet> xterm yavw
> ```

> ```console
> xterm# cd scripts/http_login
> ```

> ```console
> xterm# python yavw.py
> ```

#### 11. Start TCPdump to capture network traffic
> ```console
> #./parse_offline.sh
> ```


## Benign Traffic Generation
#### Start the scripts at the hosts
H1 -> ./scripts/ftp/client_ftp/both.sh

H2 -> ./scripts/smtp/run_email_cont.sh

H3 -> ./scripts/http_upload/host_run.sh

H4 -> ./scripts/http_login/curl_yavw.sh

H5 -> ./scripts/https/curl-https.sh

## Attack Traffic Generation
#### Start the malicious host
