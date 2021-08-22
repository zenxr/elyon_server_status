import socket
import re
import sys
import validators

def _is_valid_address(address):
    if validators.ipv4(address):
        return True
    if validators.ipv6(address):
        return True
    if validators.url(address):
        return True
    return False

def check_server_available(address, port, timeout = 1.0):
    '''
    Tests TCP connection to address, timeout (float) in seconds
    '''
    if not _is_valid_address(address):
        raise TypeError(f'Invalid address : {address}')
    try:
        sock = socket.create_connection((address, port), timeout = timeout)
        return True
    except (socket.error, socket.timeout) as e:
        return False