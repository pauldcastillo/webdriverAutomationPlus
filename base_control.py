from base_driver import BaseDriver
from base_driver import prevent_stale_element
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


class BaseControl(BaseDriver):
    """
    Class:
        BaseControl

    Purpose:
        Contain methods common to all controls.

    Inherits:
        <BaseDriver>

    Parameters:
        selector (str): The css selector for finding the element.

    Usage:
        control = BaseControl(selector="div.foo-bar")
        control = BaseControl(selector="div.foo-bar", expected_text="Foo Bar")

    TODO:
        Implement more ways to find elements, e.g. by text.
        Implement not visible.
        Implement accepting arbitrary kwargs as control attributes.
    """

    def __init__(self, selector, expected_text=None, index=0):
        """
        Method:
            __init___

        Purpose:
            Initialize a BaseControl

        Parameters:
            selector (str): The string identifier for finding the element.

            Optional:
                expected_text (str): The string expected to appear in the
                    element. Defaults to None.
                index (int): The index of the element based on selector.
                    Generally preferred to not use, but available as last
                    resort. Defaults to the first (0).
        """
        self._element = None
        self._elements = None
        self.expected_text = expected_text
        self.index = index
        self.selector = selector

    def click(self):
        """
        Method:
            click

        Purpose:
            Click the element.
        """
        self.get_element().click()

    def get_element(self):
        """
        Method:
            get_element

        Purpose:
            Get the element to operate on.

        Returns:
            WebElement to operate on.
        """
        if self._element ==  None:
            # Wait three seconds for now.
            self._elements = WebDriverWait(self.driver, timeout=3).until(
                lambda driver: driver.find_elements_by_css_selector(
                    self.selector,
                ),
            )
            self._element = self._elements[self.index]
        return self._element

    @prevent_stale_element
    def get_text(self):
        """
        Method:
            get_text

        Purpose:
            Get the text within the element.

        Returns:
            The inner text of the element.

        Notes:
            Equivalent to use elem.innerText in the browser console.
        """
        return self.get_element().text

    @prevent_stale_element
    def hover(self):
        """
        Method:
            hover

        Purpose:
            Hover over the element. Does not check anything else.
        """
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_element())
        actions.perform()

    def send_text(self, text):
        """
        Method:
            send_text

        Purpose:
            Send the specified text at the control. Typically used with
            input-type controls.

        Parameters:
            text (str): Text to send.

        Usage:
            >>> BaseControl('input.test-input').send_text(text="foo")

        Notes:
            This doesn't raise an error if element is not interactable, e.g.
            a text element.
        """
        self.get_element().send_keys(text)

    def verify_text(self, text=""):
        """
        Method:
            verify_text

        Purpose:
            Validate the expected text appears in the element.

        Parameters:
            text (str): The text expected to appear in the element. If a Falsy
                value is sent for text, defaults to self.expected_text.

        Usage:
            >>> BaseControl('div.foo', expected_text='Foo').verify_text()
            True

            >>> BaseControl('div.foo').verify_text(text="Foo")
            False

        Notes:
            The typical usage of this should be the first example.
        """
        text = text or self.expected_text
        assert text == self.get_text()

    def verify_visible(self, timeout=30):
        """
        Method:
            verify_visible

        Purpose:
            Validate the control is visible.

        Parameters:
            timeout (int): The number of seconds to wait for the element to be
                visible.

        Usage:
            BaseControl('a.test-link').verify_visible(timeout=30)

        """
        assert self.visible(timeout)

    def visible(self, timeout=5):
        """
        Method:
            visible

        Purpose:
            Check whether the element is visible or not.

        Parameters:
            timeout (int/float): The number of seconds to wait for the element
                to be visible. Defaults to five seconds.

        Returns:
            bool: True if the element is visible within the timeout. False
            otherwise.

        Usage:
            BaseControl('a.test-link').visible(timeout=30)

        TODO:
            Implement a better way to wait.
        """
        return WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.find_element_by_css_selector(
                self.selector).is_displayed(),
        )