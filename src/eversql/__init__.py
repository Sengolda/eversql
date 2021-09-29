from importlib.metadata import version

try:
    dist_name = "eversql"
    __version__ = version(dist_name)
except Exception:
    __version__ = None


from .columns import *
from .table import *
