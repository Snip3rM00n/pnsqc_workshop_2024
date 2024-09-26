from selenium.webdriver.common.by import By

from pnsqc_workshop_2024.core.extensions.extended_web_element import ExtendedWebElement
from pnsqc_workshop_2024.core.collection_helpers import CollectionHelpers
from pnsqc_workshop_2024.core.general_helpers import GeneralHelpers


class CustomSelectElement(ExtendedWebElement):

    @property
    def _selected_value_element(self):
        return self.find_element_by_attribute("class", "-singleValue", "$=")

    @property
    def selected_value(self):
        if self._selected_value_element is not None:
            return self._selected_value_element.text
        return ""

    def select(self, value):
        def select_option_exists():
            element = CollectionHelpers.first_or_none(
                self.find_elements(By.XPATH, f"//*[contains(text(), '{value}')]")
            )
            return element is not None

        self.click()
        GeneralHelpers.wait_for(select_option_exists, time_out_in_seconds=5)
        self.find_element(By.XPATH, f"//*[contains(text(), '{value}')]").click()
