
class LoginPage:

    def __init__(self, page):
        self.page = page

    def navigate_url(self):
        self.page.goto("https://automationexercise.com/")
        self.page.get_by_role("link", name=" Signup / Login").click()

    def user_details(self, user_mail, user_pass):
        self.page.locator("//input[@data-qa='login-email']").fill(user_mail)
        self.page.get_by_placeholder('Password').fill(user_pass)
        self.page.get_by_role("button", name="Login").click()
        self.page.screenshot(path=r"C:\Users\HP\Documents\Playwright_project\Screenshot\photo2.png")

    def deleting_existing_user(self):
        self.page.locator("//a[text()=' Delete Account']").click()
        confirm_text = self.page.get_by_text("Account Deleted!").text_content()
        print(confirm_text)
        self.page.locator("//a[@data-qa='continue-button']").click()