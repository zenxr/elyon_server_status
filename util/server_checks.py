import socket

from .host_validator import assert_valid_host

def check_tcp_available(host, port, timeout = 1.0):
    '''
    Tests TCP connection to address, timeout (float) in seconds
    '''
    assert_valid_host(host)
    try:
        socket.create_connection((host, port), timeout = timeout)
        return True
    except (socket.error, socket.timeout) as e:
        return False

def check_udp_available(host, port, timeout = 1.0):
   assert_valid_host(host)
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   sock.settimeout(timeout)
   try:
      response = sock.connect_ex((host, port))
      sock.close()
      return True if response == 0 else False
   except (socket.timeout, socket.gaierror) as e:
      sock.close()
      return False

