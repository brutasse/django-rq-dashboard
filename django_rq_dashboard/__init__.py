VERSION = (0, 3, 3)


def get_version():
    return ".".join(map(str, VERSION))

__version__ = get_version()
