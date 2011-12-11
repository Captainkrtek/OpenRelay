import socket

from django.conf import settings

from server_talk.literals import DEFAULT_PASSPHRASE


PORT = getattr(settings, 'SERVER_PORT', 8000)
IPADDRESS = getattr(settings, 'SERVER_IPADDRESS', socket.gethostbyname(socket.gethostname()))
HEARTBEAT_QUERY_INTERVAL = getattr(settings, 'SERVER_HEARTBEAT_QUERY_INTERVAL', 10)
INVENTORY_QUERY_INTERVAL = getattr(settings, 'SERVER_INVENTORY_QUERY_INTERVAL', 30)
SIBLINGS_QUERY_INTERVAL = getattr(settings, 'SERVER_SIBLINGS_QUERY_INTERVAL', 30)
HEARTBEAT_FAILURE_THRESHOLD = getattr(settings, 'SERVER_HEARTBEAT_FAILURE_THRESHOLD', 30)
KEY_PASSPHRASE = getattr(settings, 'SERVER_KEY_PASSPHRASE', DEFAULT_PASSPHRASE)
