from typing import TYPE_CHECKING

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pnsqc_workshop_2024.core.collection_helpers import CollectionHelpers

if TYPE_CHECKING:
    from pnsqc_workshop_2024.core.extensions.extended_web_driver import BaseExtendedWebDriver


class CheckableElement:

    def __init__(self, parent: "BaseExtendedWebDriver", input_id):
        self._parent = parent
        self._input_id = input_id

    @property
    def input_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self._parent.find_elements(By.ID, self._input_id))

    @property
    def label_element(self) -> WebElement:
        return self._parent.find_element_by_attribute("for", self._input_id)

    @property
    def is_checked(self):
        return self.input_element.is_selected()

    def click(self):
        self.label_element.click()

    @property
    def exists(self):
        return self.input_element is not None and self.label_element is not None
