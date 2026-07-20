# Vendored SOCKS plugins for ghostsurf
from ghostsurf.relay.servers.socksplugins.http import HTTPSocksRelay
from ghostsurf.relay.servers.socksplugins.https import HTTPSSocksRelay

# Register available SOCKS relay plugins
SOCKS_RELAYS = [HTTPSocksRelay, HTTPSSocksRelay]
