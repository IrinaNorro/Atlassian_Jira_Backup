from libraries.utils import get_library
import Browser

browser = Browser.Browser()


class LibraryBase:
    """Base RF library class for setting useful properties."""

    def __init__(self):
        self.toslib = get_library("TOSLibrary")
