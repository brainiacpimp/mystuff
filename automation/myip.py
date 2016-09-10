#!/usr/bin env python

### external ip getter

import urllib


class IPGetter( object ):
    """ DocString """
    ipv4 = 'http://ipv4.myexternalip.com/raw'
    ipv6 = 'http://ipv6.myexternalip.com/raw'
    
    def __init__(self):
        """ Initializes External IP retreiver """
        self.ip4 = ''
        self.ip6 = ''

        self._update_ip()
        
    def __str__(self):
        """ String Representation """
        return 'IPV4: {0}\n\nIPV6: {1}'.format(self.ip4, self.ip6)
        
    def _update_ip(self):
        """ Updates the IP addresses """
        self.ip4 = urllib.urlopen(self.ipv4).read()
        self.ip6 = urllib.urlopen(self.ipv6).read()

        

if __name__ == '__main__':
    myips = IPGetter()
    print(myips)
    
