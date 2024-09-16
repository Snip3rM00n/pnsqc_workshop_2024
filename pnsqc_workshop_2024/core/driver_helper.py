import os
from typing import List

from selenium.webdriver import Chrome, Edge, Firefox, Safari
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium_driver_updater import DriverUpdater

from pnsqc_workshop_2024.core.exceptions import BrowserNotSupportedError
from pnsqc_workshop_2024.core.extensions.extended_web_driver import ChromeExtendedDriver


class DriverHelper:
    supported_browsers = {
        # Google Chrome
        "chrome": {
            "driver_class": Chrome,
            "install_name": DriverUpdater.chromedriver,
            "options_class": ChromeOptions
        },
        "extended_chrome": {
            "driver_class": ChromeExtendedDriver,
            "install_name": DriverUpdater.chromedriver,
            "options_class": ChromeOptions
        },

        # Microsoft Edge (Chromium)
        "edge": {
            "driver_class": Edge,
            "install_name": DriverUpdater.edgedriver,
            "options_class": EdgeOptions
        },
        "extended_edge": {
            "driver_class": ChromeExtendedDriver,
            "install_name": DriverUpdater.edgedriver,
            "options_class": EdgeOptions
        },

        # Firefox (Gecko)
        "firefox": {
            "driver_class": Firefox,
            "install_name": DriverUpdater.geckodriver,
            "options_class": FirefoxOptions
        },
        "extended_firefox": {
            "driver_class": ChromeExtendedDriver,
            "install_name": DriverUpdater.geckodriver,
            "options_class": FirefoxOptions
        },

        # Safari (WebKit)
        "safari": {
            "driver_class": Safari,
            "install_name": DriverUpdater.safaridriver,
            "options_class": SafariOptions
        },
        "extended_safari": {
            "driver_class": ChromeExtendedDriver,
            "install_name": DriverUpdater.safaridriver,
            "options_class": SafariOptions
        }
    }

    @staticmethod
    def browser_supported(browser: str):
        """

        :param browser:
        :return:
        """
        return browser in DriverHelper.supported_browsers.keys()

    @staticmethod
    def get_extended_driver(browser: str, install: bool = True, update: bool = True, browser_args: List = None):
        """

        :param browser:
        :param install:
        :param update:
        :param browser_args:
        :return:
        """
        if not browser.startswith("extended_"):
            browser = f"extended_{browser.replace('extended', '').replace('_', '')}"

        return DriverHelper.get_driver(browser, install, update, browser_args)

    @staticmethod
    def get_driver(browser: str, install: bool = True, update: bool = True, browser_args: List = None):
        """

        :param browser:
        :param install:
        :param update:
        :param browser_args:
        :return:
        """

        if not DriverHelper.browser_supported(browser):
            msg = (f"{browser.title()} Browser is not supported by this workshop.  If you want to add it, consider "
                   f"adding it to '{DriverHelper.__module__}.{DriverHelper.__name__}.supported_browsers'.")
            raise BrowserNotSupportedError(msg)

        driver_detail = DriverHelper.supported_browsers[browser]

        if install:
            DriverHelper._install_driver(driver_detail["install_name"], update)

        options = driver_detail["options_class"]()

        if isinstance(browser_args, list):
            for arg in browser_args:
                options.add_argument(arg)

        driver = driver_detail["driver_class"](options=options)

        return driver

    @staticmethod
    def _install_driver(browser_type: str, update: bool):
        """

        :param browser_type:
        :param update:
        :return:
        """
        venv_dir = os.environ.get("VIRTUAL_ENV")
        bin_name = "bin" if os.name.lower() == "posix" else "Scripts"  # TODO: Confirm Windows venv script folder
        bin_dir_path = os.path.join(venv_dir, bin_name)

        DriverUpdater.install(browser_type, path=bin_dir_path, upgrade=update)
