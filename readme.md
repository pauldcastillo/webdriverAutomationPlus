### Test Saved Messages
=====================================
# Description:
Tests the user can save messages then find them in search and Saved items.

# Dependencies
- [python](https://www.python.org/downloads/).
- [Selenium Webdriver](https://www.selenium.dev/documentation/en/selenium_installation/).
- [pytest](https://docs.pytest.org/en/stable/getting-started.html).
- [requests](https://requests.readthedocs.io/en/latest/user/install/#install)

# How to run
1. Install dependencies.
2. Navigate to 'pc' folder in terminal of your choice.
3. Run pytest.

# TODO
- Implement allowing multiple assertions to fail without stopping the test. (It's much more useful to be able to continue if only search fails, for instance.)
- Implement getting the message id from the html attributes and using that to validate it's the same message. Using a unique timestamp works ok.

# Notes:
- This was implemented using python2.7.12 since that's what I had installed, but I think it should still work with python3.x.