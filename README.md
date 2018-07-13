# Mininet
Emulation of an enterprise network comprising of DNS, HTTP, HTTPS, FTP and SMTP servers.

#### Start POX [[Link to POX]](https://github.com/noxrepo/pox "POX Repo")
> #./pox.py log.level DEBUG forwarding.l2_learning

#### Stop NetManager (to prevent it from updating /etc/resolve.conf)
> #service NetworkManager stop

#### Check configs
> [/etc/resolve.conf](/resolve.conf) & [/etc/dnsmasq.hosts](/dnsmasq.hosts)

#### Start Mininet
> #service openvswitch-switch start\
> #./my_net.sh

#### Start DNS
> mininet> xterm dns\
> xterm# dnsmasq --log-level --no-daemon

#### Start TCPdump
> #./parse_offline.sh
