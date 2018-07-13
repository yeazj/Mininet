# Mininet
Emulation of an enterprise network

It comprises of DNS, HTTP, HTTPS, FTP and SMTP servers.

Start POX
# ./pox.py log.level DEBUG forwarding.l2_learning

Stop NetManager (to prevent it from updating /etc/resolve.conf)
# service NetworkManager stop

Check /etc/resolve.conf & /etc/dnsmasq.hosts

Start Mininet
# service openvswitch-switch start
# ./my_net.sh

Start DNS
# mininet> xterm dns
# xterm # dnsmasq --log-level --no-daemon
