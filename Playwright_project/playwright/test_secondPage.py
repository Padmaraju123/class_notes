import time

from playwright.sync_api import Page, expect


def test_selecting_products_in_cart(page: Page):
    print("This is test is working...........")
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    time.sleep(5)

    # here using id
    # page.locator("#username").fill("rahulshettyacademy")
    # time.sleep(5)

    # using name
    # page.locator("[name='username']").fill("rahulshettyacademy")
    # time.sleep(5)

    # xpath
    page.locator("//input[@id='username']").fill("rahulshettyacademy")
    time.sleep(5)

    page.locator("#password").fill("learning")
    time.sleep(5)

    # drop down
    page.get_by_role("combobox").select_option("Teacher")
    time.sleep(5)

    # checkbox
    page.locator("[name='terms']").check()
    time.sleep(5)

    # signin button
    page.locator(".btn.btn-info.btn-md").click()
    time.sleep(5)

    # here we need to filter the required the product names only
    # for the first collect all product elements which as common tag

    # here getting all products with tagname
    # once collected with filter method we check the given text and compare to the product names
    item_page1 = page.locator("app-card").filter(has_text="iphone X")
    # here with item_page nothing but just like page obj only the difference it search only particular item content only
    item_page1.get_by_role("button",name="Add").click()
    time.sleep(5)

    # Nokia item
    item_page2 = page.locator("app-card").filter(has_text="Nokia Edge")
    item_page2.get_by_role("button", name="Add").click()
    time.sleep(5)

    # click the checkout button
    page.get_by_text("Checkout").click()
    time.sleep(5)

    # now the check the count of products in cart by assertions by mention the actual count
    # if don't match then assertion error will occur
    expect(page.locator(".media-body")).to_have_count(2)
    time.sleep(5)


# this test case teach how to jump into child tabs from parent tab
def test_tabWindows(page:Page):
    # this is parent page/tab
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    # so whenever you click a link in current page then it will redirect to another page/tab
    # now once it moved we can't do any operations on new page with current obj_page.

    # page.get_by_role("link",name="Free Access to InterviewQues/ResumeAssistance/Material").click()
    # page.locator(".blinkingText").click()
    # page.get_by_text("Free Access to InterviewQues/ResumeAssistance/Material").click()

    # here whenever the new popup/newtab opens while running the inside block code
    # the expect_popup() activates and assign to newPage_info
    # now the by using value we pass the address to newpage obj
    with page.expect_popup() as newPage_info:
        page.locator("//a[text()='Free Access to InterviewQues/ResumeAssistance/Material']").click()
        new_page = newPage_info.value

        # now with using the new_page we do operation just like page
        obtained_text = new_page.locator(".im-para.red").text_content()


        assert "mentor@rahulshettyacademy.com" in obtained_text











