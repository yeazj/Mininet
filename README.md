# Mininet
* Emulation of an enterprise network comprising of DNS, HTTP, HTTPS, FTP, SMTP and DB servers.
* Emulation of Network attacks
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

> xterm# python scripts/smtp/smtpd_custom.py
> ```

#### Start PostgreSQL over HTTPS server
> #service postgresql start

> PostgreSQL runs on local machine (fetch IP)

> Change IP in Engine in [app.py](scripts/http_postgre/app.py) & [insertable.py](/scripts/http_postgre/insertable.py) & [createtable.py](scripts/http_postgre/createtable.py)
> ```python
> engine = create_engine('postgresql://postgres:postgres@x.x.x.x:5432/test', echo=True)
> ```

> **Create *users* table in Postgre** (first time only)\
> #python scripts/http_postgre/createtable.py

> **Insert 'username' and 'password' in *users* table** (first time only)\
> #python scripts/http_postgre/insertable.py

> mininet> xterm https

> xterm# python scripts/http_postgre/app.py

>

#### Start HTTP with Upload
> mininet> xterm web

> xterm# python scripts/http_upload/shttpu.py 80

#### Start Vulnerable HTTP (Web attacks target)
> [Link to YAVW - Yet Another Vulnerable Webserver](https://github.com/noleti/yavw)

> mininet> xterm yavw

> xterm# cd scripts/http_login

> xterm# python yavw.py

#### Start TCPdump
> #./parse_offline.sh
