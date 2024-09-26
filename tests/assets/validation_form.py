import os
import sys
from datetime import datetime

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pnsqc_workshop_2024.core.general_helpers import GeneralHelpers
from tests.assets.wrappers.checkable import CheckableElement
from tests.assets.wrappers.custom_select_element import CustomSelectElement
from tests.assets.wrappers.multi_value_item import MultiValueItem, MultiValueTextBox
from pnsqc_workshop_2024.core.collection_helpers import CollectionHelpers
from pnsqc_workshop_2024.core.bases.base_page import BasePage


class ValidationForm(BasePage):

    def __init__(self, driver: "BaseExtendedWebDriver"):
        super().__init__(driver, navigate_to=False)

    @property
    def relative_uri(self):
        return "automation-practice-form"

    def page_to_load(self):
        return self._first_name_element is not None and self._last_name_element is not None

    @property
    def _header_group_elements(self):
        return self.driver.find_elements(By.CLASS_NAME, "group-header")

    @property
    def _item_8_element(self):
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "item-8"))

    def _ready_to_scroll(self):
        return self._item_8_element is not None and self._item_8_element.is_displayed()

    @property
    def _first_name_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "firstName"))

    @property
    def first_name(self):
        return self._first_name_element.get_attribute("value")

    @property
    def _last_name_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "lastName"))

    @property
    def last_name(self):
        return self._last_name_element.get_attribute("value")

    @property
    def _email_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "userEmail"))

    @property
    def email(self):
        return self._email_element.get_attribute("value")

    # region - Male Gender Element

    @property
    def _male_gender_element(self) -> CheckableElement:
        return CheckableElement(self.driver, "gender-radio-1")

    @property
    def male(self) -> bool:
        return self._male_gender_element.is_checked

    # endregion

    # region - Female Gender Element

    @property
    def _female_gender_element(self) -> CheckableElement:
        return CheckableElement(self.driver, "gender-radio-2")

    @property
    def female(self) -> bool:
        return self._female_gender_element.is_checked

    # endregion

    # region - Other Gender Element
    @property
    def _other_gender_element(self) -> CheckableElement:
        return CheckableElement(self.driver, "gender-radio-3")

    @property
    def other(self) -> bool:
        return self._other_gender_element.is_checked

    # endregion

    @property
    def _mobile_number_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "userNumber"))

    @property
    def mobile_number(self):
        return self._mobile_number_element.get_attribute("value")

    @property
    def _date_of_birth_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "dateOfBirthInput"))

    @property
    def date_of_birth(self):
        value = self._date_of_birth_element.get_attribute("value")
        return datetime.strptime(value, "%d %b %Y")

    @property
    def _subjects_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "subjectsInput"))

    @property
    def _subjects_list_parent(self) -> WebElement:
        return CollectionHelpers.first_or_none(
            self.driver.find_elements(By.CLASS_NAME, "subjects-auto-complete__value-container")
        )

    @property
    def _subject_element_list(self) -> "[WebElement]":
        return self._subjects_list_parent.find_elements(By.CLASS_NAME, "subjects-auto-complete__multi-value")

    @property
    def _subject_models(self):
        return [MultiValueItem(element) for element in self._subject_element_list]

    @property
    def subjects(self):
        return MultiValueTextBox(self._subject_models, self._subjects_element)

    @property
    def _sports_element(self) -> CheckableElement:
        return CheckableElement(self.driver, "hobbies-checkbox-1")

    @property
    def sports(self) -> bool:
        return self._sports_element.is_checked

    @property
    def _reading_element(self) -> CheckableElement:
        return CheckableElement(self.driver, "hobbies-checkbox-2")

    @property
    def reading(self) -> bool:
        return self._reading_element.is_checked

    @property
    def _music_element(self) -> CheckableElement:
        return CheckableElement(self.driver, "hobbies-checkbox-3")

    @property
    def music(self) -> bool:
        return self._music_element.is_checked

    @property
    def _current_address_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "currentAddress"))

    @property
    def current_address(self):
        return self._current_address_element.get_attribute("value")

    @property
    def _state_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "state"))

    @property
    def _state_select_element(self) -> CustomSelectElement:
        if self._state_element is not None:
            return CustomSelectElement.from_element(self._state_element)

    @property
    def state(self):
        return self._state_select_element.selected_value

    @property
    def _city_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "city"))

    @property
    def _city_select_element(self) -> CustomSelectElement:
        if self._city_element is not None:
            return CustomSelectElement.from_element(self._city_element)

    @property
    def city(self):
        return self._city_select_element.selected_value
