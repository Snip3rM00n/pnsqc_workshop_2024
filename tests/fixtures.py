import pytest

from pnsqc_workshop_2024.core.driver_helper import DriverHelper
from pnsqc_workshop_2024.framework.pages.practice_form import PracticeForm
from tests.assets.validation_form import ValidationForm

driver = None
validation_page = None
workshop_page = None
preferred_browser = "chrome"

@pytest.fixture()
def setup_dualing_pages(request):
    global driver, validation_page, workshop_page, preferred_browser

    if driver is None:
        driver = DriverHelper.get_extended_driver(preferred_browser)

    if validation_page is None:
        validation_page = ValidationForm(driver)

    if workshop_page is None:
        workshop_page = PracticeForm(driver)

    request.cls.validation_page = validation_page
    request.cls.workshop_page = workshop_page
    request.cls.driver = driver
    yield
    # driver.quit()

@pytest.fixture()
def setup_single_page(request):
    global driver, workshop_page, preferred_browser

    if driver is None:
        driver = DriverHelper.get_extended_driver(preferred_browser)

    if workshop_page is None:
        workshop_page = PracticeForm(driver)

    request.cls.workshop_page = workshop_page
    request.cls.driver = driver
    yield
#     driver.quit()