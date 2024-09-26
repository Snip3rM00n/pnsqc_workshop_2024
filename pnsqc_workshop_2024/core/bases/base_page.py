from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pnsqc_workshop_2024.core.extensions.extended_web_driver import BaseExtendedWebDriver

from pnsqc_workshop_2024.core.general_helpers import GeneralHelpers


class BasePage:

    def __init__(self, driver: "BaseExtendedWebDriver", navigate_to: bool = True):
        self.driver = driver

        if navigate_to:
            self.navigate_to()
            GeneralHelpers.wait_for(self.page_to_load)

    @property
    def base_uri(self):
        return "https://demoqa.com"

    @property
    def relative_uri(self):
        return ""

    @property
    def url(self):
        return f"{self.base_uri}/{self.relative_uri}"

    def navigate_to(self):
        self.pre_navigation_actions()
        self.driver.get(self.url)
        self.post_navigation_actions()

    def page_to_load(self):
        return False

    def pre_navigation_actions(self):
        pass

    def post_navigation_actions(self):
        pass
