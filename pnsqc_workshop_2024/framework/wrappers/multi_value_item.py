from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from pnsqc_workshop_2024.core.collection_helpers import CollectionHelpers


class MultiValueItem:
    """
    A wrapper that represents a given item in a multi-value text box.

    Can you get this working properly?

    Need a Hint? A working example can be found at:
    https://github.com/Snip3rM00n/pnsqc_quality_jam_demo/blob/main/framework/wrappers/multi_value_item.py#L8
    """

    def __init__(self, parent: WebElement):
        self._parent = parent

    @property
    def _label_element(self) -> WebElement:
        pass

    @property
    def remove_button(self) -> WebElement:
        pass

    @property
    def name(self):
        pass


class MultiValueTextBox:
    """
    A wrapper that represents a Multi-value text box.  This acts exactly as a list does in python, however it
    implements how the Multi-Value text box works under the website under test through Selenium controls.

    Can you get this working properly?

    Need a Hint? A working example can be found at:
    https://github.com/Snip3rM00n/pnsqc_quality_jam_demo/blob/main/framework/wrappers/multi_value_item.py#L30
    """

    def __init__(self, items: "[MultiValueItem]", add_element: WebElement):
        super().__init__()
        self._items = items
        self._add_element = add_element

    def append(self, value):
        pass

    def remove(self, value):
        pass

    def extend(self, values):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __iter__(self):
        pass

    def __getitem__(self, value):
        pass

    def __repr__(self):
        pass
