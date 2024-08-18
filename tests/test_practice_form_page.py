import allure
from assertpy import soft_assertions, assert_that
from enums.genders import Genders
from pages.practice_form_page import PracticeFormPage


class TestPracticeForm:

    def test_fill_only_required_fields(self, page):
        form_page = PracticeFormPage(page)
        first_name = "John"
        last_name = "Dou"
        email = "j.dou@gmail.com"
        mobile = "1234567890"
        gender = Genders.male
        (
            form_page
            .open()
            .fill_first_name(first_name)
            .fill_last_name(last_name)
            .fill_user_mail(email)
            .fill_mobile(mobile)
            .choose_gender(gender)
            .submit()
         )
        with soft_assertions():
            assert_that(form_page.get_summary_name_text()).is_equal_to_ignoring_case(f"{first_name} {last_name}")
            assert_that(form_page.get_summary_email_text()).is_equal_to_ignoring_case(email)
            assert_that(form_page.get_summary_mobile_text()).is_equal_to_ignoring_case(mobile)
            assert_that(form_page.get_summary_gender_text()).is_equal_to_ignoring_case(gender.value)

    def test_do_not_fill_required_fields(self, page):
        form_page = PracticeFormPage(page)
        alert_color = "rgb(220, 53, 69)"
        (
            form_page
            .open()
            .submit()
        )
        with soft_assertions():
            assert_that(form_page.get_border_color(form_page.first_name)).is_equal_to_ignoring_case(alert_color)
            assert_that(form_page.get_border_color(form_page.last_name)).is_equal_to_ignoring_case(alert_color)
            assert_that(form_page.get_border_color(form_page.mobile)).is_equal_to_ignoring_case(alert_color)
            assert_that(form_page.get_border_color(form_page.male_radiobutton)).is_equal_to_ignoring_case(alert_color)
            assert_that(form_page.get_border_color(form_page.female_radiobutton)).is_equal_to_ignoring_case(alert_color)
            assert_that(form_page.get_border_color(form_page.other_radiobutton)).is_equal_to_ignoring_case(alert_color)
