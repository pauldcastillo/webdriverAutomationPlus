from base_driver import BaseDriver


class BaseTest(BaseDriver):
    """
    Class:
        BaseTest

    Purpose:
        BaseDriver

    Parameters:
        param (type): use

    Usage:
        BaseTest = BaseTest(param=param)

    Notes:
        -
    """

    def setup_method(self, method):
        """
        Method:
            setup_method

        Purpose:
            Start a test session.

        Parameters:
            method (method): The test method to start.

        Returns:
            -

        Usage:
            setup_method(method=method)

        Notes:
            Standard pytest start up method.
        """
        self.driver.get("about:blank")
        self.driver.maximize_window()

    def teardown_method(self, method):
        """
        Method:
            teardown_method

        Purpose:
            End a test session.

        Parameters:
            method (method): The test to end.

        Notes:
            Standard pytest teardown method.
        """
        self.driver.quit()