import allure
from playwright.sync_api import Page

from elements.button_element import ButtonElement
from elements.element import Element
from elements.input_element import InputElement
from enums.genders import Genders
from pages.page import BasePage


class PracticeFormPage(BasePage):
    BASE_URL = "https://demoqa.com/automation-practice-form"

    def __init__(self, page: Page):
        super().__init__(page)
        self.form = Element(self._page, "//*[@id='userForm']")
        self.first_name = InputElement(self._page, "//*[@id='firstName']")
        self.last_name = InputElement(self._page, "//*[@id='lastName']")
        self.user_mail = InputElement(self._page, "//*[@id='userEmail']")
        self.male_radiobutton = ButtonElement(self._page, "//label[text()='Male']")
        self.female_radiobutton = ButtonElement(self._page, "//label[text()='Female']")
        self.other_radiobutton = ButtonElement(self._page, "//label[text()='Other']")
        self.mobile = InputElement(self._page, "//*[@id='userNumber']")
        self.submit_button = ButtonElement(self._page, "//*[@id='submit']")
        self.summary_name = Element(self._page, "//td[text()='Student Name']/following-sibling::td")
        self.summary_email = Element(self._page, "//td[text()='Student Email']/following-sibling::td")
        self.summary_mobile = Element(self._page, '//td[text()="Mobile"]/following-sibling::td')
        self.summary_gender = Element(self._page, '//td[text()="Gender"]/following-sibling::td')

    def fill_first_name(self, string: str):
        with allure.step(f"Fill first name with '{string}'"):
            self.first_name.input(string)
            return self

    def fill_last_name(self, string: str):
        with allure.step(f"Fill last name with '{string}'"):
            self.last_name.input(string)
            return self

    def fill_user_mail(self, string: str):
        with allure.step(f"Fill email with '{string}'"):
            self.user_mail.input(string)
            return self

    def choose_gender(self, gender: Genders):
        with allure.step(f"Choose gender: {gender.value}"):
            if gender is Genders.male:
                self.male_radiobutton.click()
            if gender is Genders.female:
                self.female_radiobutton.click()
            if gender is Genders.other:
                self.other_radiobutton.click()
            return self

    def fill_mobile(self, string: str):
        with allure.step(f"Fill mobile with: '{string}'"):
            self.mobile.input(string)
            return self

    def submit(self):
        with allure.step("Submit form by button click"):
            self.submit_button.click()
            return self

    def form_submit(self):
        with allure.step("Submit form"):
            self.form.submit()
            return self

    def get_summary_name_text(self) -> str:
        self.summary_name.wait()
        return self.summary_name.get_text()

    def get_summary_email_text(self) -> str:
        self.summary_email.wait()
        return self.summary_email.get_text()

    def get_summary_mobile_text(self) -> str:
        self.summary_mobile.wait()
        return self.summary_mobile.get_text()

    def get_summary_gender_text(self) -> str:
        self.summary_gender.wait()
        return self.summary_gender.get_text()

    @staticmethod
    def get_border_color(element: Element) -> str:
        return str(element.get_border_color())
