from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from pnsqc_workshop_2024.core.collection_helpers import CollectionHelpers


class MultiValueItem:

    def __init__(self, parent: WebElement):
        self._parent = parent

    @property
    def _label_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(
            self._parent.find_elements(By.CLASS_NAME, "subjects-auto-complete__multi-value__label")
        )

    @property
    def remove_button(self) -> WebElement:
        return CollectionHelpers.first_or_none(
            self._parent.find_elements(By.CLASS_NAME, "subjects-auto-complete__multi-value__remove")
        )

    @property
    def name(self):
        return self._label_element.text


class MultiValueTextBox:

    def __init__(self, items: "[MultiValueItem]", add_element: WebElement):
        super().__init__()
        self._items = items
        self._add_element = add_element

    def append(self, value):
        self._add_element.send_keys(value)
        self._add_element.send_keys(Keys.RETURN)

    def remove(self, value):
        if value in self:
            self[value].remove_button.click()

    def extend(self, values):
        for value in values:
            self.append(value)

    def __add__(self, other):
        if isinstance(list, other):
            self.extend(other)
        else:
            self.append(other)

    def __sub__(self, other):
        if isinstance(list, other):
            self.extend(other)
        else:
            self.remove(other)

    def __iter__(self):
        for item in self._items:
            yield item.name

    def __getitem__(self, value):
        return next(item for item in self._items if item.name == value)

    def __repr__(self):
        return f"[{', '.join(self)}]"
