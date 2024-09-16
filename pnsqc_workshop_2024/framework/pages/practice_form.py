import os
import sys
from datetime import datetime
    
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pnsqc_workshop_2024.framework.wrappers.checkable import CheckableElement
from pnsqc_workshop_2024.framework.wrappers.custom_select_element import CustomSelectElement
from pnsqc_workshop_2024.framework.wrappers.multi_value_item import MultiValueItem, MultiValueTextBox

from pnsqc_workshop_2024.core.collection_helpers import CollectionHelpers
from pnsqc_workshop_2024.core.general_helpers import GeneralHelpers
from pnsqc_workshop_2024.core.bases.base_page import BasePage


class PracticeForm(BasePage):

    @property
    def select_all(self):
        return f"{Keys.COMMAND}A" if sys.platform == "darwin" else f"{Keys.CONTROL}A"

    # region - Boiler Plate
    @property
    def relative_uri(self):
        return "automation-practice-form"

    def page_to_load(self):
        return self._first_name_element is not None and self._last_name_element is not None

    def post_navigation_actions(self):
        self._remove_ads()

        if len(self._header_group_elements) > 0:
            self._header_group_elements[0].click()

        GeneralHelpers.wait_for(self._ready_to_scroll, time_out_in_seconds=5, throw_on_timeout=False)
        self.driver.execute_script(script="window.scrollBy(0, 200);")

    def _remove_ads(self):
        current_dir = os.path.dirname(__file__)
        script_file = os.path.join(current_dir, "scripts", "removeAds.js")

        with open(script_file, "r") as reader:
            script = reader.read()

        self.driver.execute_script(script)

    @property
    def _header_group_elements(self):
        return self.driver.find_elements(By.CLASS_NAME, "group-header")

    @property
    def _item_8_element(self):
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "item-8"))

    def _ready_to_scroll(self):
        return self._item_8_element is not None and self._item_8_element.is_displayed()

    # endregion - Boiler Plate

    # region - First Name ----------------------------------------------------------------------------------------------

    # REQUIREMENTS: Capture the first name element and wrap it with a getter/setter that treats it like a string.

    # endregion - First Name -------------------------------------------------------------------------------------------

    # region - Last Name -----------------------------------------------------------------------------------------------

    # REQUIREMENTS: Capture the last name element and wrap it with a getter/setter that treats it like a string.

    # endregion - Last Name --------------------------------------------------------------------------------------------

    # region - Email Address -------------------------------------------------------------------------------------------

    # REQUIREMENTS: Capture the Email Address element and wrap it with a getter/setter that treats it like a string.

    # endregion - Email Address ----------------------------------------------------------------------------------------

    # region - Male Gender Element -------------------------------------------------------------------------------------

    # REQUIREMENTS:
    #   1. Capture the Male Gender element and wrap it with a getter/setter that treats it like a boolean.
    #   2. The checkbox should only ever change if it's set to a value that != to its current "checked" value.
    #      - For example: `If it's checked and `male = True` is set, it should not be clicked again.
    #
    # HINT: Because of the warning below - this is where the class `CheckableElement` will be useful.  Note that that
    #       class is bare and needs to be given an implementation in order to work properly.
    #
    # WARNING - Known Website Issue:
    #   The website under test is implemented in such a way where you need to click the element with tag `label` for the
    #   checkbox in order for it to work.  Clicking on the element with tag `input` for the checkbox does nothing.

    # endregion - Male Gender Element ----------------------------------------------------------------------------------

    # region - Female Gender Element -----------------------------------------------------------------------------------

    # REQUIREMENTS:
    #   1. Capture the Female Gender element and wrap it with a getter/setter that treats it like a boolean.
    #   2. The checkbox should only ever change if it's set to a value that != to its current "checked" value.
    #      - For example: `If it's checked and `female = True` is set, it should not be clicked again.
    #
    # HINT: Because of the warning below - this is where the class `CheckableElement` will be useful.  Note that that
    #       class is bare and needs to be given an implementation in order to work properly.
    #
    # WARNING - Known Website Issue:
    #   The website under test is implemented in such a way where you need to click the element with tag `label` for the
    #   checkbox in order for it to work.  Clicking on the element with tag `input` for the checkbox does nothing.

    # endregion - Female Gender Element --------------------------------------------------------------------------------

    # region - Other/Non Binary Gender Element -------------------------------------------------------------------------
    
    # REQUIREMENTS:
    #   1. Capture the Other Gender element and wrap it with a getter/setter that treats it like a boolean.
    #   2. The checkbox should only ever change if it's set to a value that != to its current "checked" value.
    #      - For example: `If it's checked and `other_gender = True` is set, it should not be clicked again
    #
    # HINT: Because of the warning below - this is where the class `CheckableElement` will be useful.  Note that that
    #       class is bare and needs to be given an implementation in order to work properly.
    #
    # WARNING - Known Website Issue:
    #   The website under test is implemented in such a way where you need to click the element with tag `label` for the
    #   checkbox in order for it to work.  Clicking on the element with tag `input` for the checkbox does nothing.

    # endregion - Other/Non Binary Gender Element ----------------------------------------------------------------------

    # region - Mobile Number Element -----------------------------------------------------------------------------------

    # REQUIREMENTS: Capture the Email Address element and wrap it with a getter/setter that treats it like a string.
    #               Bonus: Restrict the string to numerical and special characters only.

    # endregion - Mobile Number Element --------------------------------------------------------------------------------

    # region - Date of Birth Element -----------------------------------------------------------------------------------

    # REQUIREMENTS:
    #   1. Capture the Date of Birth element and wrap it with a getter/setter that treats it like a DateTime.
    #   2. Have the setter press the escape key to close the date picker box.
    #   Bonus: Add support for getting and setting it as a string as well.
    #
    # HINTS:
    #   Hint 1: The format the date of birth field supports is "%d %b %Y"
    #   Hint 2: Don't try to automate the date picker, the ROI is not worth it.
    #   Hint 3: Although it operates as a date/time, to set its value you need to use a `send_keys` call with a string.
    #
    # WARNING - Known Website Issue:
    #   The website under test has a bug where if the Date of Birth element is emptied/cleared it will
    #   remove ALL content on the website and result in an empty browser window.  To get around this you
    #   will need to select all content in the field type over it.
    #
    #   To perform this you can use this following line command to select the content of the field:
    #
    #   _date_of_birth_element.send_keys(self.select_all)
    #

    # endregion - Date of Birth Element --------------------------------------------------------------------------------

    # region - Subjects Element ----------------------------------------------------------------------------------------

    # REQUIREMENTS:
    #   1. Capture the subjects input element in it's own property.
    #   2. Capture the parent element of the list of elements representing the subjects
    #   3. Using the parent element, capture the child elements in a list[WebElement] collection.
    #   4. Cast the child elements into a List[MultiValueItem] collection as '_subject_models' or 'subject_items'.
    #   5. Finally, create a MultiValueTextBox using the List[MultiValueItem] the 'items' and the subjects
    #      element as the 'add_element'
    #
    # HINTS:
    #   1. This is where the `MultiValueItem` and `MultiValueTextBox` classes come into play.  These classes have a
    #      bare implementation in this workshop.  Can you implement it properly?
    #   2. This is an advanced form of wrapping using the concept of a Model or Component.  This requires capturing
    #      a list of webelements and then converting that into a list of the representative Model.  In this case, the
    #      model would be implemented as the MultiValueItem.
    #   3. If implemented properly, a developer would only need to call `subjects.append("Computer Science")` to add
    #      computer science to their list of subjects or `subjects.remove("Computer Science") to remove it.
    #
    # GET STUCK?
    #   If you get stuck, consider looking at the original implementation from the 2024 PNSQC Quality Jam example:
    #   https://github.com/Snip3rM00n/pnsqc_quality_jam_demo/blob/main/framework/pages/practice_form.py#L180-L200

    # endregion - Subjects Element -------------------------------------------------------------------------------------

    # region - Interests: Sports Element -------------------------------------------------------------------------------

    # REQUIREMENTS:
    #   1. Capture the Sports element and wrap it with a getter/setter that treats it like a boolean.
    #   2. The checkbox should only ever change if it's set to a value that != to its current "checked" value.
    #      - For example: `If it's checked and `sports = True` is set, it should not be clicked again.
    #
    # HINT: Because of the warning below - this is where the class `CheckableElement` will be useful.  Note that that
    #       class is bare and needs to be given an implementation in order to work properly.
    #
    # WARNING - Known Website Issue:
    #   The website under test is implemented in such a way where you need to click the element with tag `label` for the
    #   checkbox in order for it to work.  Clicking on the element with tag `input` for the checkbox does nothing.

    # endregion - Interests: Sports Element ----------------------------------------------------------------------------

    # region - Interests: Reading Element ------------------------------------------------------------------------------

    # REQUIREMENTS:
    #   1. Capture the Sports element and wrap it with a getter/setter that treats it like a boolean.
    #   2. The checkbox should only ever change if it's set to a value that != to its current "checked" value.
    #      - For example: `If it's checked and `reading = True` is set, it should not be clicked again.
    #
    # HINT: Because of the warning below - this is where the class `CheckableElement` will be useful.  Note that that
    #       class is bare and needs to be given an implementation in order to work properly.
    #
    # WARNING - Known Website Issue:
    #   The website under test is implemented in such a way where you need to click the element with tag `label` for the
    #   checkbox in order for it to work.  Clicking on the element with tag `input` for the checkbox does nothing.

    # endregion - Interests: Reading Element ---------------------------------------------------------------------------

    # region - Interests: Music Element --------------------------------------------------------------------------------

    # REQUIREMENTS:
    #   1. Capture the Sports element and wrap it with a getter/setter that treats it like a boolean.
    #   2. The checkbox should only ever change if it's set to a value that != to its current "checked" value.
    #      - For example: `If it's checked and `music = True` is set, it should not be clicked again.
    #
    # HINT: Because of the warning below - this is where the class `CheckableElement` will be useful.  Note that that
    #       class is bare and needs to be given an implementation in order to work properly.
    #
    # WARNING - Known Website Issue:
    #   The website under test is implemented in such a way where you need to click the element with tag `label` for the
    #   checkbox in order for it to work.  Clicking on the element with tag `input` for the checkbox does nothing.

    # endregion - Interests: Music Element -----------------------------------------------------------------------------

    # region - Current Address Element ---------------------------------------------------------------------------------

    # REQUIREMENTS: Capture the first name element and wrap it with a getter/setter that treats it like a string.

    # endregion - Current Address Element ------------------------------------------------------------------------------

    # region - State Element -------------------------------------------------------------------------------------------

    # REQUIREMENTS:
    #   1. Capture the state element in its own property.
    #   2. Cast that state element into a `CustomSelectElement`
    #   3. Create an implementation for the `CustomSelectElement` if you haven't already done so.
    #   4. Create a getter/setter for the State element that allows the developer to interact with the element as they
    #      would a string.  However, instead of using `send_keys` on the `_state_element` in the setter, it must
    #      use the `CustomSelectElement.select()` function.  Likewise, the getter must return the
    #      `CustomSelectElement.selected_value` property.
    #
    # HINTS:
    #   1. This is where the `CustomSelectElement` class comes into play.  This class has a bare implementation in this
    #      workshop.  Can you implement it properly?
    #   2. Before casting the state element, consider checking if it exists first.  If it doesn't, simply return None.
    #
    # GET STUCK?
    #   If you get stuck, consider looking at the original implementation from the 2024 PNSQC Quality Jam example:
    #   https://github.com/Snip3rM00n/pnsqc_quality_jam_demo/blob/main/framework/pages/practice_form.py#L255-L270

    # endregion - State Element ----------------------------------------------------------------------------------------

    # region - City Element --------------------------------------------------------------------------------------------

    # REQUIREMENTS:
    #   1. Capture the city element in its own property.
    #   2. Cast that city element into a `CustomSelectElement`
    #   3. Create an implementation for the `CustomSelectElement` if you haven't already done so.
    #   4. Create a getter/setter for the city element that allows the developer to interact with the element as they
    #      would a string.  However, instead of using `send_keys` on the `_city_element` in the setter, it must
    #      use the `CustomSelectElement.select()` function.  Likewise, the getter must return the
    #      `CustomSelectElement.selected_value` property.
    #
    # HINTS:
    #   1. This is where the `CustomSelectElement` class comes into play.  This class has a bare implementation in this
    #      workshop.  Can you implement it properly?
    #   2. Before casting the city element, consider checking if it exists first.  If it doesn't, simply return None.
    #
    # GET STUCK?
    #   If you get stuck, consider looking at the original implementation from the 2024 PNSQC Quality Jam example:
    #   https://github.com/Snip3rM00n/pnsqc_quality_jam_demo/blob/main/framework/pages/practice_form.py#L272-L287

    # endregion - City Element -----------------------------------------------------------------------------------------

    # region - Fill Out Form Function ----------------------------------------------------------------------------------

    # REQUIREMENTS:
    #   1. Write a function called `fill_out_form` that fills out the form that touches all setters in the class.
    #   2. This function should not call the Driver or Elements itself, rather it should rely on the setters to do that
    #      for it.
    #   3. The function should take the following inputs and apply them to the correct setter:
    #         - first_name: str
    #         - last_name: str
    #         - email: str
    #         - gender: str
    #         - phone_number: str
    #         - dob: datetime
    #         - subjects: List[str]
    #         - hobbies: List[str]
    #         - address: str
    #         - state: str
    #         - city: str
    #
    # CHALLENGES:
    #   1. Using the gender as a string, can you set the proper gender boolean to true in one line of code?
    #   2. With the hobbies as a list string, can you loop through them and set the hobby booleans (music, reading,
    #      sports) to true or false using only three lines of code?

    # endregion - Fill Out Form Function -------------------------------------------------------------------------------
