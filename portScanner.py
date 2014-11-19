# This is a very simple program made by pure python
# Its mission is to find open ports on a network and report the results back to us
# Let's get started!

# INTRODUCTION:
# This program uses the following functions in the Socket API:
# 1. socket.gethostbyname(hostname) - Takes a hostname such as www.google.com and returns the IP address (74.125.228.100)
# 2. socket.gethostbyaddr(ip address) - Takes a ip address such as 74.125.228.100 and returns the hostname www.google.com 
# 3. socket.socket([family[, type[, proto]]]) - This function creates the instance of a new socket given the family
# 4. socket.create_connection(address[, timeout[, source_address]]) - This function takes a 2-tuple (host, port) and returns an 
# instance of a new socket. It also has the option of taking the timeout and source address.

import optparse
