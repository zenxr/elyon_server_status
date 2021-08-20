import socket
import re
import sys

def check_server_available(address, port, timeout = 1.0):
    '''
    Tests TCP connection to address, timeout (float) in seconds
    '''
    try:
        sock = socket.create_connection((address, port), timeout = timeout)
        return True
    except (socket.error, socket.timeout) as e:
        return False