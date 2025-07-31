# https://automationexercise.com/
import json
import time

import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="class", autouse=True)
def setup(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=1500)
    ing_session = browser.new_context(viewport={'width': 1920, 'height': 1080})
    page = ing_session.new_page()
    yield page
    page.close()
    browser.close()


class TestingDemo:

    @pytest.fixture(autouse=True)
    def init_page(self, setup):
        self.page = setup

    def test_1(self):
        # actually browser interactions starts here

        page = self.page
        page.goto("https://automationexercise.com/")

        # 3. Verify that home page is visible successfully
        current_url = page.url
        print("The current url is {}".format(current_url))

        # 4. Click on 'Signup / Login' button
        page.get_by_role("link", name=" Signup / Login").click()

        # Signup
        page.get_by_placeholder("Name").fill("Padmaraju")
        page.locator("[data-qa='signup-email']").fill("padmaraju084@gmail.com")
        page.get_by_role("button", name="Signup").click()
        page.locator("#id_gender1").click()
        page.locator("#password").fill("AutomationPractice123@@")

        page.locator("#days").select_option("9")
        page.locator("[data-qa='months']").select_option("February")
        page.locator("//select[@name='years']").select_option("1998")
        page.evaluate("window.scrollTo(0, 500)")
        page.locator("//p/input[@data-qa='first_name']").fill("Padmaraju")
        page.locator("[name='last_name']").fill("Siddanatham")
        page.locator("//input[@id='company']").fill("XYZ")
        page.locator("#address1").fill("8-472 Gandhi nagar")
        page.evaluate("window.scrollTo(500, 1000)")
        page.get_by_role("combobox", name="Country").select_option("India")
        page.locator("#state").fill("Andhra pradesh")
        page.locator("//input[@id='city']").fill("Anantapur")
        page.locator("[name='zipcode']").fill("515672")
        page.locator("#mobile_number").fill("0000000000")
        page.get_by_role("button", name="Create Account").click()
        time.sleep(5)
        page.screenshot(path=r"C:\Users\HP\Documents\Playwright_project\Screenshot\photo1.png")

        # Confirmation message after the signup
        msg = page.locator("//div[@class='col-sm-9 col-sm-offset-1']").text_content()
        page.locator("//a[@data-qa='continue-button']").click()
        print(msg)

    def test_contact(self):
        page = self.page
        page.get_by_role("link", name="Contact us").click()

        page.locator("//input[@name='name']").fill("Padmaraju")
        page.locator("input[data-qa='email']").fill("padmaraju084@gmail.com")
        page.get_by_placeholder("Subject").fill("Feedback about website")
        page.locator("#message").fill("""Hi, the website is very helpful to do automation with customize way and completely user
    friendly mode.


    Thanks
    Padmaraju""")
        page.locator("input[data-qa='submit-button']").click()
        time.sleep(5)

    def test_logout(self):
        page = self.page
        time.sleep(5)
        page.locator("//a[text()=' Logout']").click()

    with open(r"C:\Users\HP\Documents\Playwright_project\Data\credentials.json", "r") as f:
        data = json.load(f)
        user_data = data["user_credentials"]

    @pytest.mark.parametrize("user_credential", user_data)
    def test_Invalid_valid_credentials(self, user_credential):
        page = self.page
        page.locator("//input[@data-qa='login-email']").fill(user_credential["login_email"])
        page.get_by_placeholder('Password').fill(user_credential["password"])
        page.get_by_role("button", name="Login").click()
        time.sleep(5)
        page.screenshot(path=r"C:\Users\HP\Documents\Playwright_project\Screenshot\photo2.png")

    def test_delete_account(self):
        page = self.page
        # Text after delete the account
        time.sleep(5)
        page.locator("//a[text()=' Delete Account']").click()
        confirm_text = page.get_by_text("Account Deleted!").text_content()
        print(confirm_text)
        page.locator("//a[@data-qa='continue-button']").click()
