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
> #./pox.py log.level DEBUG forwarding.l2_learning

#### Stop NetManager (to prevent it from updating /etc/resolve.conf)
> #service NetworkManager stop

#### Check configs
> [/etc/resolve.conf](/resolve.conf) & [/etc/dnsmasq.hosts](/dnsmasq.hosts)

#### Start Mininet
> #service openvswitch-switch start

> #./my_net.sh

#### Start DNS
> mininet> xterm dns

> xterm# dnsmasq --log-level --no-daemon

#### Start TCPdump
> #./parse_offline.sh

#### Start FTP (Bruteforce attack victim)
> #sudo apt-get install python-pyftpdlib

> mininet> xterm l_ftp

> xterm# python /scripts/ftp/server_ftp/basic_ftpd.py

#### Start SMTP
> mininet> xterm email

> xterm# python scripts/smtp/smtpd_custom.py

#### Start PostgreSQL over HTTPS server
> PostgreSQL runs on local machine (fetch IP)

> #service postgresql start

> Change IP in Engine in [app.py](scripts/http_postgre/app.py) & [insertable.py](/scripts/http_postgre/insertable.py) & [createtable.py](scripts/http_postgre/createtable.py)
> ```python
> engine = create_engine('postgresql://postgres:postgres@x.x.x.x:5432/test', echo=True)
> ```

> **Create *users* table in Postgre\**
> #python scripts/http_postgre/createtable.py

> **Insert 'username' and 'password' in *users* table\**
> #python scripts/http_postgre/insertable.py

> mininet> xterm https

> xterm# python scripts/http_postgre/app.py

>

#### Start HTTP with Upload

#### Start Vulnerable HTTP (Web attacks victim)
