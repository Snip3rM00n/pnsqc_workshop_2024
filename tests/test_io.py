from datetime import datetime

import pytest

from pnsqc_workshop_2024.core.driver_helper import DriverHelper
from pnsqc_workshop_2024.core.general_helpers import GeneralHelpers
from pnsqc_workshop_2024.framework.pages.practice_form import PracticeForm
from tests.assets.validation_form import ValidationForm
from tests.fixtures import setup_dualing_pages

@pytest.mark.usefixtures("setup_dualing_pages")
class TestPageIO:

    def test_a_first_name(self):
        self.workshop_page.first_name = "Amelia"
        assert self.validation_page.first_name == "Amelia"

    def test_b_last_name(self):
        self.workshop_page.last_name = "Bedelia"
        assert self.validation_page.last_name == "Bedelia"

    def test_c_email(self):
        self.workshop_page.email = "maid_2b_literal@noemail.com"
        assert self.validation_page.email == "maid_2b_literal@noemail.com"

    def test_d_gender_male(self):
        self.workshop_page.male = True

        assert self.validation_page.male is True
        assert self.validation_page.female is False
        assert self.validation_page.other is False

    def test_e_gender_female(self):
        self.workshop_page.female = True

        assert self.validation_page.male is False
        assert self.validation_page.female is True
        assert self.validation_page.other is False

    def test_f_gender_other(self):
        self.workshop_page.other = True

        assert self.validation_page.male is False
        assert self.validation_page.female is False
        assert self.validation_page.other is True

    def test_g_mobile(self):
        self.workshop_page.mobile_number = "3605551234"
        assert self.validation_page.mobile_number == "3605551234"

    def test_h_dob(self):
        birthday = datetime(1969, 4, 20)
        self.workshop_page.date_of_birth = birthday
        assert self.validation_page.date_of_birth == birthday

    def test_i_subjects(self):
        subjects = ["Computer Science", "Maths", "History"]
        self.workshop_page.subjects.extend(subjects)

        for subjects in subjects:
            assert subjects in self.validation_page.subjects

        self.workshop_page.subjects.remove("Maths")
        assert "Maths" not in self.validation_page.subjects

    def test_j_hobbies_sports(self):
        assert self.validation_page.sports is False
        self.workshop_page.sports = True
        assert self.validation_page.sports is True

        msg = "Did you remember to check the current value of the 'sports' element?"
        self.workshop_page.sports = True
        assert self.validation_page.sports is True, msg

    def test_k_hobbies_reading(self):
        assert self.validation_page.reading is False
        self.workshop_page.reading = True
        assert self.validation_page.reading is True

        msg = "Did you remember to check the current value of the 'reading' element?"
        self.workshop_page.reading = True
        assert self.validation_page.reading is True, msg

    def test_l_hobbies_music(self):
        assert self.validation_page.music is False
        self.workshop_page.music = True
        assert self.validation_page.music is True

        msg = "Did you remember to check the current value of the 'music' element?"
        self.workshop_page.music = True
        assert self.validation_page.music is True, msg

    def test_m_address(self):
        self.workshop_page.current_address = "123 Starshine Ln."
        assert self.validation_page.current_address == "123 Starshine Ln."

    def test_n_state(self):
        self.workshop_page.state = "Haryana"
        assert self.validation_page.state == "Haryana"

    def test_o_city(self):
        self.workshop_page.city = "Panipat"
        assert self.validation_page.city == "Panipat"

    def test_p_fill_out_form(self):
        self.workshop_page.navigate_to()
        GeneralHelpers.wait_for(self.workshop_page.page_to_load)

        dob = datetime(1996, 2, 14)
        self.workshop_page.fill_out_form(
            first_name="Lilah",
            last_name="Aemel'da",
            email="astromaid@noemail.com",
            gender="female",
            phone_number="3605556789",
            dob=dob,
            subjects=["Maths", "Arts"],
            hobbies=["Music", "Reading"],
            address="Mists, W:25-P:32",
            state="NCR",
            city="Noida"
        )

        assert self.validation_page.first_name == "Lilah"
        assert self.validation_page.last_name == "Aemel'da"
        assert self.validation_page.email == "astromaid@noemail.com"
        assert self.validation_page.female is True
        assert self.validation_page.male is False
        assert self.validation_page.other is False
        assert self.validation_page.mobile_number == "3605556789"
        assert self.validation_page.date_of_birth == dob
        assert "Maths" in self.validation_page.subjects
        assert "Arts" in self.validation_page.subjects
        assert self.validation_page.sports is False
        assert self.validation_page.reading is True
        assert self.validation_page.music is True
        assert self.validation_page.current_address == "Mists, W:25-P:32"
        assert self.validation_page.state == "NCR"
        assert self.validation_page.city == "Noida"
