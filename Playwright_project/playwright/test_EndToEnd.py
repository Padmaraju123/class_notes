# https://automationexercise.com/
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
import pytest
from PageObjects.login import LoginPage
from PageObjects.Signup import SignUpPage

with open(r"C:\Users\HP\Documents\Playwright_project\Data\NewUser.json", "r") as f:
    new_user_data = json.load(f)
    newuser = new_user_data["NewUser"]


@pytest.mark.parametrize("get_details", newuser)
def test_1(playwright, get_details):

    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context_obj = browser.new_context()
    page = context_obj.new_page()

    username = get_details["username"]
    user_mail = get_details["email_id"]
    passd = get_details["password"]
    mnth = get_details["month"]
    dte = get_details["date"]
    yr = get_details["year"]
    first_name = get_details["first_name"]
    last_name = get_details["last_name"]
    company_name = get_details["company"]
    given_add = get_details["address"]
    country_name = get_details["country"]
    state_name = get_details["state"]
    city_name = get_details["City"]
    pin_code = get_details["Pincode"]
    mobile_no = get_details["Mobile No"]

    Details = [username, user_mail, passd, dte, mnth, yr, first_name,
               last_name, company_name, given_add, country_name, state_name, city_name,
               pin_code, mobile_no]

    new_obj = SignUpPage(page)
    new_obj.navigate()
    new_obj.Creating_user(Details)

    # Signup
    # page.get_by_placeholder("Name").fill("Padmaraju")
    # page.locator("[data-qa='signup-email']").fill("padmaraju084@gmail.com")
    # page.get_by_role("button", name="Signup").click()
    # page.locator("#id_gender1").click()
    # page.locator("#password").fill("AutomationPractice123@@")

    # Confirmation message after the signup


#
# def test_contact():
#     page.get_by_role("link", name="Contact us").click()
#
#     page.locator("//input[@name='name']").fill("Padmaraju")
#     page.locator("input[data-qa='email']").fill("padmaraju084@gmail.com")
#     page.get_by_placeholder("Subject").fill("Feedback about website")
#     page.locator("#message").fill("""Hi, the website is very helpful to do automation with customize way and completely user
# friendly mode.
#
#
# Thanks
# Padmaraju""")
#     page.locator("input[data-qa='submit-button']").click()
#     time.sleep(5)
#
#
# def test_logout():
#     page = self.page
#     time.sleep(5)
#     page.locator("//a[text()=' Logout']").click()
# ------------------------------------------------------------------------------------

with open(r"C:\Users\HP\Documents\Playwright_project\Data\credentials.json", "r") as f:
    data = json.load(f)
    user_data = data["user_credentials"]


@pytest.mark.parametrize("user_credential", user_data)
def test_Invalid_valid_credentials(playwright, user_credential):
    user_mail = user_credential["login_email"]
    user_pass = user_credential["password"]

    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context_obj = browser.new_context()
    page = context_obj.new_page()

    # actually browser interactions starts here
    # creating obj of the class: LoginPage in login.py from the pageObject directory
    login_obj = LoginPage(page)
    login_obj.navigate_url()
    login_obj.user_details(user_mail, user_pass)
    login_obj.deleting_existing_user()

