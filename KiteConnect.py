import logging
from kiteconnect import KiteConnect

logging.basicConfig(level=logging.DEBUG)
import logging
from kiteconnect import KiteConnect

logging.basicConfig(level=logging.DEBUG)

kite = KiteConnect(api_key="evy9s0l388cogz5m")
# Fetch all orders
kite.orders()

# Get instruments
kite.instruments()


