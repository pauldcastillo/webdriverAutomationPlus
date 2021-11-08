from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver


class BaseDriver(object):
    """
    Class:
        BaseDriver

    Purpose:
        Contain a single instance of webdriver for a test to use.

    Notes:
        Only meant to be inherited later.

    TODO:
        Add support for different browsers.
    """
    driver = webdriver.Chrome()

def prevent_stale_element(func):
    """
    Method:
        prevent_stale_element

    Purpose:
        Prevent a StaleElementReferenceException by flushing the element to
        force a requery.

    Parameters:
        func (method): The method to wrap.
    """
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except StaleElementReferenceException:
            self._element = None
            return func(self, *args, **kwargs)
    return wrapper
