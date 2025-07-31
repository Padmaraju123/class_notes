import time

from playwright.sync_api import Page, expect, Playwright


# here playwright is an fixture which is used for invoke the browsers
# in selenium we create the fixtures for browser setup and teardown to every test case
# but here no need to do it is predefined in playwright web framework by running the command: pytest-playwright


def test_play1(playwright):
    # here invoking the chromium engine to run the website in both chrome and microsoft
    # here browser is an object

    browser = playwright.chromium.launch(headless=False)
    context_obj = browser.new_context()
    page1_obj = context_obj.new_page()
    page1_obj.goto("http://www.rahulshettyacademy.com/")

    page1_obj.wait_for_timeout(5000)


# this is shorted way of above case
# here we use default fixture "page" as argument to the test case
# with this no need to do browser_obj, page_obj by default this page fixture will do
# but incase you want to run in firefox browser don't use this page fixture
# since it works only chrome, microsoft and headless mode

# here with page obj comes under Page class so we need to import it
# from playwright.sync_api import Page
# if you declare page:Page as a argument to the test
# then autosuggestions will come

def test_play2(page: Page):
    page.goto("http://www.rahulshettyacademy.com/")
    print("this is working")
    page.wait_for_timeout(5000)


def test_play3(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.wait_for_timeout(5000)


def test_play4(page: Page):
    print("This is test case 4...............")
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    # entering the username
    # if you want to enter the text in username it has attached label so by using that we put the text
    page.get_by_label("Username:").fill("rahulshettyacademy")

    page.wait_for_timeout(5000)

    # entering the password
    page.get_by_label("Password:").fill("learning")
    page.wait_for_timeout(5000)

    # drop down selection here it called as combobox
    # here select_option means the options showing under the drop down so paste the attribute value which ever you want

    page.get_by_role("combobox").select_option("consult")
    page.wait_for_timeout(5000)

    # if we want to use the css selector
    # id = #attribute_value
    # class = .attribute_value

    page.locator("#terms").click()
    time.sleep(5)

    # clicking the button
    # here in case only one button available in dashboard then use below way with get_by_role
    # page.get_by_role("button").click()

    # else if more than one and want to access particular button then mention the name of the button
    # page.get_by_role("button", name="name_of_button").click()

    page.get_by_role("button", name="Sign In").click()
    time.sleep(5)


# using wrong credentials and get the text which displayed on screen
def test_play5(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    time.sleep(5)
    page.get_by_label("Password:").fill("learning")
    time.sleep(5)
    page.locator("#terms").click()
    time.sleep(5)
    page.get_by_role("button", name="Sign In").click()

    # in playwright, we don't need to give explicit wait or time to display any text just like selenium
    # by default it wait until the text display because backend it will take care
    # so by using get_by_text() method and we pass the required the text and
    # checking whether it is expected if not through assertion error

    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()


# if we want to run the test cases in firefox then we have create page obj from scratch
# because if we pass page:Page to the test case by default the test case run on chrome or edge

def test_firefoxbrowser(playwright):
    print("running the test cases in firefox browser.......")
    firefox_browser = playwright.firefox.launch(headless=False)
    context_obj1 = firefox_browser.new_context()
    page1_obj = context_obj1.new_page()
    page1_obj.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page1_obj.get_by_label("Username:").fill("rahulshettyacademy")
    time.sleep(5)
    page1_obj.get_by_label("Password:").fill("learning")
    time.sleep(5)
    page1_obj.locator("#terms").click()
    time.sleep(5)
    page1_obj.get_by_role("button", name="Sign In").click()
    time.sleep(5)




