'''
utils包
'''

from config import POSTGRES_CONFIG, REDIS_CONFIGL
from proxy import get_proxy

__all__ = [
    'POSTGRES_CONFIG',
    'REDIS_CONFIGL',
    'get_proxy',
]