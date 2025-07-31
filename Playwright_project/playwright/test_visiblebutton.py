import time

from playwright.sync_api import Page, expect



"""
id with value hide-textbox
page.locator("#hide-textbox").click()

finding the button with get_by_role
page.get_by_role("button",name="Hide").click()

Finding the elements with possible ways using Xpath

page.locator("//input[@value='Hide']").click()
page.locator("//input[@onclick='hideElement()']").click()
page.locator("(//input[@type='submit'])[3]").click()
page.locator("(//input[@class='btn-style class2'])[1]").click()
page.locator("//input[@id='hide-textbox']").click()

finding the elements with possible ways using CSS

page.locator("input[id='hide-textbox']").click()
page.locator("input[class='btn-style class2']:nth-child(2)").click()
page.locator("input[value='Hide']").click()
page.locator("input[onclick='hideElement()']").click()
page.locator("input[type='submit']:nth-child(2)").click()


doing assertion where it is visible or not, if not it will throw assertion error

with placeholder
page.get_by_placeholder("Hide/Show Example").fill("hello")
page.locator("[placeholder='Hide/Show Example']").fill("hello")

with id
page.locator("#displayed-text").fill("hello")
page.locator("[id='displayed-text']").fill("hello")

with class
page.locator(".inputs.displayed-class").fill("hello")
page.locator("[class='inputs displayed-class']").fill("hello")
page.locator(".displayed-class").fill("hello")

with name attribute
page.locator("[name='show-hide']").fill("hello") """


def test_UIChecks(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    time.sleep(5)
    expect(page.locator("//input[@id='displayed-text']")).to_be_visible()

    # now clicking the hide button
    page.get_by_role("button",name="Hide").click()

    # now checking the place holder is visible or not
    expect(page.locator("[onclick='hideElement()']")).to_be_visible()

    time.sleep(5)


# Handling alerts
def test_alerts(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    time.sleep(5)

    page.on("dialog", lambda dialog: dialog.accept())
    time.sleep(5)

    # The above line will take care if any dialog box/pop up comes automatically it will accepts
    page.get_by_role("button", name="Alert").click()
    time.sleep(5)


def test_iframes(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    time.sleep(5)

    # here we are jumping from parent page into iframe page by finding the entire page
    iframe_page = page.frame_locator("#courses-iframe")
    iframe_page.get_by_role("link",name="Learning paths").click()

    # to check one text contains our required text on iframe page
    # expect(iframe_page.get_by_text("A Learning Path is a selection")).to_contain_text("padmaraju")
    time.sleep(5)



