"""
Environment setup for Behave Testing
"""
from os import getenv
from selenium import webdriver

# Default configuration values
WAIT_SECONDS = int(getenv("WAIT_SECONDS", "30"))
BASE_URL = getenv("BASE_URL", "http://localhost:8080")
DRIVER = getenv("DRIVER", "firefox").lower()


def before_all(context):
    """Executed once before all tests start"""
    context.base_url = BASE_URL
    context.wait_seconds = WAIT_SECONDS

    # Initialize the appropriate WebDriver
    if "firefox" in DRIVER:
        context.driver = init_firefox()
    else:
        context.driver = init_chrome()

    context.driver.implicitly_wait(context.wait_seconds)
    context.config.setup_logging()


def after_all(context):
    """Executed once after all tests finish"""
    context.driver.quit()


######################################################################
# Utility functions for WebDriver initialization
######################################################################

def init_chrome():
    """Initialize a headless Chrome WebDriver"""
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    return webdriver.Chrome(options=options)


def init_firefox():
    """Initialize a headless Firefox WebDriver"""
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    return webdriver.Firefox(options=options)
