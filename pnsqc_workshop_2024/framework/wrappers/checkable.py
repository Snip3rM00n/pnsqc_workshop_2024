from typing import TYPE_CHECKING

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pnsqc_workshop_2024.core.collection_helpers import CollectionHelpers

if TYPE_CHECKING:
    from pnsqc_workshop_2024.core.extensions.extended_web_driver import BaseExtendedWebDriver


class CheckableElement:
    """
    A wrapper that represents a checkable element like a checkbox or a radio button.

    Can you get this working properly?

    Need a Hint? A working example can be found at:
    https://github.com/Snip3rM00n/pnsqc_quality_jam_demo/blob/main/framework/wrappers/checkable.py
    """

    def __init__(self, parent: "BaseExtendedWebDriver", input_id):
        self._parent = parent
        self._input_id = input_id

    @property
    def input_element(self) -> WebElement:
        pass

    @property
    def label_element(self) -> WebElement:
        pass

    @property
    def is_checked(self) -> bool:
        pass

    def click(self):
        pass

    @property
    def exists(self) -> bool:
        pass
