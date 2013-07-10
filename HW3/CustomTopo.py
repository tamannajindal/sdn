#!/usr/bin/python

'''
Coursera:
- Software Defined Networking (SDN) course
-- Module 3 Programming Assignment

Professor: Nick Feamster
Teaching Assistant: Muhammad Shahbaz
'''

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel

class CustomTopo(Topo):
    "Simple Data Center Topology"

    "linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    "fanout - number of child switch per parent switch"
    def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)
        
        # Add your logic here ...
        # Add core
        # print "Adding Core"
        core = self.addSwitch('c1')

        agg_count = 1;
        edge_count = 1;
        host_count = 1;

        #Add Aggregation
        for i in irange(1,fanout):
            # print "Adding Aggregation a%s" %agg_count
            agg = self.addSwitch('a%s' %agg_count)
            self.addLink(core, agg, **linkopts1)
            agg_count = agg_count+1
            
            #Add edge
            for j in irange(1,fanout):
                # print "Adding Edge e%s" %edge_count
                edge = self.addSwitch('e%s' %edge_count)
                self.addLink(agg, edge, **linkopts2)
                edge_count = edge_count+1
        
	        # Add host
	        for k in irange(1,fanout):
                    # print "Adding host h%s" %host_count
	            host = self.addHost('h%s' %host_count)
                    self.addLink(host, edge, **linkopts3)
                    host_count = host_count+1
                    
topos = { 'custom': ( lambda: CustomTopo() ) }
