# Benign & Attack traffic generation on emulated Enterprise network
* An enterprise network comprising of DNS, HTTP, HTTPS, FTP, SMTP and DB servers.
* Network attacks
  * Bruteforce
  * Web
    * SQL injection
    * XSS
  * Probe
  * Phishing
  * Infiltration
  * DOS/DDOS
  * Botnet
  * Vulnerability exploit
  
## Setup

#### Pre-req : Kali Linux
> Not tested on other platforms yet but shouldn't be much different on any other Debian/Ubuntu Linux

#### Start POX [[Link to POX]](https://github.com/noxrepo/pox "POX Repo")
> ```console
> #./pox.py log.level DEBUG forwarding.l2_learning
> ```

#### Stop NetManager (to prevent it from updating /etc/resolve.conf)
> ```console
> #service NetworkManager stop
> ```

#### Check configs
> [/etc/resolve.conf](/resolve.conf) & [/etc/dnsmasq.hosts](/dnsmasq.hosts)

#### Start Mininet
> ```console
> #service openvswitch-switch start
> ```

> ```console
> #./my_net.sh
> ```

#### Start DNS (DOS/DDOS attack target)
> ```console
> mininet> xterm dns
> ```

> ```console
> xterm# dnsmasq --log-level --no-daemon
> ```

#### Start FTP (Bruteforce attack target)
> ```console
> #sudo apt-get install python-pyftpdlib
> ```

> ```console
> mininet> xterm l_ftp
> ```

> ```console
> xterm# python scripts/ftp/server_ftp/basic_ftpd.py
> ```

#### Start SMTP
> ```console
> mininet> xterm email
> ```

> ```console
> xterm# python scripts/smtp/smtpd_custom.py
> ```

#### Start PostgreSQL over HTTPS server
> ```console
> #service postgresql start
> ```

> PostgreSQL runs on local machine (fetch IP)

> Change IP in Engine in [app.py](scripts/http_postgre/app.py) & [insertable.py](/scripts/http_postgre/insertable.py) & [createtable.py](scripts/http_postgre/createtable.py)
> ```python
> engine = create_engine('postgresql://postgres:postgres@x.x.x.x:5432/test', echo=True)
> ```

> **Create *users* table in Postgre** (first time only)\
> ```console
> #python scripts/http_postgre/createtable.py
> ```

> **Insert 'username' and 'password' in *users* table** (first time only)\
> ```console
> #python scripts/http_postgre/insertable.py
> ```

> ```console
> mininet> xterm https
> ```

> ```console
> xterm# python scripts/http_postgre/app.py
> ```

#### Start HTTP with Upload
> ```console
> mininet> xterm web
> ```

> ```console
> xterm# python scripts/http_upload/shttpu.py 80
> ```

#### Start Vulnerable HTTP (Web attacks target)
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

#### Start TCPdump to capture network traffic
> ```console
> #./parse_offline.sh
> ```

## Benign Traffic
#### Start the scripts at the hosts

## Attack traffic
#### Start the mamlicious host
