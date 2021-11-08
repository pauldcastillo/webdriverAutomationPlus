from base_driver import BaseDriver


class BasePage(BaseDriver):
    """
    Class:
        BasePage

    Purpose:
        BaseDriver

    Parameters:
        url (str): The url of the page to open or verify.

    Usage:
        home_page = BasePage(url="https://www.slack.com")

    TODO:
        Implement substituting the base url with a specific environment.
    """

    def __init__(self, url):
        """
        Method:
            __init___

        Purpose:
            Initialize a BasePage.

        Parameters:
            url (str): The url of the page to open or verify.
        """
        self.url = url

    def open(self, verify=True):
        """
        Method:
            open

        Purpose:
            Open the page's url. Then optionally validate the controls.

        Parameters:
            Optional:
                verify (bool): Whether to validate the controls or not.
                    Defaults to True.

        Usage:
            home_page.open(verify=True)
        """
        self.driver.get(self.url)
        self.verify_url()
        if verify:
            self.verify_controls_visible()
            self.verify_content()

    def verify_content(self, controls=[]):
        """
        Method:
            verify_content

        Purpose:
            Validate the given controls have the correct text. Uses the page's
            content_controls by default.

        Parameters:
            controls (list): The controls to check. If this list is Falsy will
                attempt to use the page's content_controls.

        Usage:
            home_page.verify_content()
            home_page.verify_content(
                controls=[self.sign_in_button, self.header],
            )
        """
        controls = controls or self.content_controls
        list(map(lambda control: control.verify_text, controls))

    def verify_controls_visible(self, controls=[]):
        """
        Method:
            verify_controls_visible

        Purpose:
            Verify the given controls are all visible. If a Falsy value is sent
            defaults to the page_load_controls.

        Parameters:
            Optional:
                controls (list): The controls to validate are visible. Defaults
                    to the page_load_controls.

        TODO:
            Implement a timeout over the overall method instead of allowing
            each visible to take it's own.
        """
        controls = controls or self.page_load_controls
        list(map(lambda control: control.verify_visible, controls))

    def verify_url(self):
        """
        Method:
            verify_url

        Purpose:
            Validate the current url matches the page's url.
        """
        assert self.driver.current_url == self.url
