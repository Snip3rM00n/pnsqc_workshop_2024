from selenium.webdriver.common.by import By

from pnsqc_workshop_2024.core.extensions.extended_web_element import ExtendedWebElement
from pnsqc_workshop_2024.core.collection_helpers import CollectionHelpers
from pnsqc_workshop_2024.core.general_helpers import GeneralHelpers


class CustomSelectElement(ExtendedWebElement):
    """
    A wrapper that represents a select element thats compatible with the website under test.  Unfortunately it cannot
    use the built-in select element from Selenium because it's using custom HTML instead of standard select elements.

    Can you get this working properly?

    Need a Hint? A working example can be found at:
    https://github.com/Snip3rM00n/pnsqc_quality_jam_demo/blob/main/framework/wrappers/custom_select_element.py
    """

    @property
    def _selected_value_element(self):
        pass

    @property
    def selected_value(self):
        pass

    def select(self, value):
        pass
