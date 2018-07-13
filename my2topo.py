"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

	#One network with webserver
	
	h3 = self.addHost('dns', ip='10.0.0.1')
	h4 = self.addHost('web', ip='10.0.0.82') #act as webserver
	h6 = self.addHost('email', ip='10.0.0.83')
	h7 = self.addHost('l_ftp', ip='10.0.0.84')
	#h5 = self.addHost('ssh', ip='10.0.0.85')
	h10 = self.addHost('yavw', ip='10.0.0.86')
	h11 = self.addHost('https', ip='10.0.0.87')
	s1 = self.addSwitch('s1')

	h1 = self.addHost('h1', ip='10.0.1.1')
	h2 = self.addHost('h2', ip='10.0.1.2')
	h8 = self.addHost('h3', ip='10.0.1.3')
	h9 = self.addHost('h4', ip='10.0.1.4')
	h12 = self.addHost('h5', ip='10.0.1.5')
	h13 = self.addHost('h6', ip='10.0.1.6')
	h14 = self.addHost('h7', ip='10.0.1.7')
	h15 = self.addHost('h8', ip='10.0.1.8')
	h16 = self.addHost('h9', ip='10.0.1.9')
	s2 = self.addSwitch('s2')
	
	#h10 = self.addHost('db', ip='10.0.0.5')
	#h11 = self.addHost('ftp_db', ip='10.0.0.13')
	#s3 = self.addSwitch('s3')s3 = self.addSwitch('s3')
	
	#Connecting all the links for network
	self.addLink(h1, s1)
	self.addLink(h2, s1)
	self.addLink(h8, s1)
	self.addLink(h9, s1)
	self.addLink(h10, s1)
	self.addLink(h11, s1)
	#self.addLink(h5, s1)
	self.addLink(h6, s2)
	self.addLink(h7, s2)
	self.addLink(h3, s2)
	self.addLink(h4, s2)
	self.addLink(h12, s2)
	self.addLink(h13, s2)
	self.addLink(h14, s2)
	self.addLink(h15, s2)
	self.addLink(h16, s2)
	#self.addLink(h10, s3)
	#self.addLink(h11, s3)
	self.addLink(s1, s2)
	#self.addLink(s3, s1)

topos = { 'mytopo': ( lambda: MyTopo() ) }
