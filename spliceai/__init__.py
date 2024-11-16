import signal
import sys
from importlib.metadata import version, PackageNotFoundError
from keras.models import load_model
from pkg_resources import resource_filename

signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))

name = 'spliceai'
try:
    __version__ = version(name)
except PackageNotFoundError:
    __version__ = 'unknown'

paths = ('models/spliceai{}.h5'.format(x) for x in range(1, 6))
MODELS = [load_model(resource_filename('spliceai', x)) for x in paths]