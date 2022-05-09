import validators

class InvalidHostError(ValueError):
   pass

def assert_valid_host(address):
    if validators.ipv4(address):
        return True
    if validators.ipv6(address):
        return True
    if validators.domain(address):
        return True
    raise InvalidHostError()
