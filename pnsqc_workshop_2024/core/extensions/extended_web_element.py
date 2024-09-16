from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pnsqc_workshop_2024.core.collection_helpers import CollectionHelpers


class ExtendedWebElement(WebElement):

    @classmethod
    def from_element(cls, element: WebElement):
        return cls(parent=element._parent, id_=element._id)

    def find_element_by_attribute(self, attribute_name, value, equality="=") -> "WebElement":
        return CollectionHelpers.first_or_none(self.find_elements_by_attribute(attribute_name, value, equality))

    def find_elements_by_attribute(self, attribute_name, value, equality="=") -> "[WebElement]":
        return self.find_elements(By.CSS_SELECTOR, f'*[{attribute_name}{equality}"{value}"]')
