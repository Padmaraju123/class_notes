import time

from playwright.sync_api import Page


def test_ProvTab(page: Page):
    page.goto("file:///C:/Users/HP/Downloads/InstanceTest.html")
    page.locator(".dropdown").hover()
    page.locator('//a[@onclick="showPage(\'instances\')"]').click()
    # time.sleep(5)

    groups = ["Group B"]
    for group_name in groups:

        cloud_list = ["Azure", "GCP"]
        type_vm = ["kvm", "vmware"]
        i = 0
        for cloud_name in cloud_list:
            # group A
            page.get_by_role("button", name="Add").click()
            time.sleep(2)
            page.locator("[value='kvm']".format(type_vm[i])).click()
            i += 1

            # selecting the group
            time.sleep(2)
            page.locator("#groupSelect").select_option(label=group_name)
            time.sleep(2)

            # selecting the cloud
            page.locator("#cloudSelect").select_option(label=cloud_name)
            time.sleep(2)

            list_status = ["Stopped", "Pending"]
            for status in list_status:
                page.get_by_role("button", name="Add").click()
                time.sleep(2)

                # selecting the Status
                page.locator("#statusSelect").select_option(label=status)
                time.sleep(2)

                # OK button
                page.get_by_role("button", name="OK").click()
                time.sleep(3)

    buttons = page.locator("//button[@onclick='deleteInstance(this)']")
    count = buttons.count()

    for i in reversed(range(count)):
        buttons.nth(i).click()
        time.sleep(2)


def test_clouds(page: Page):
    page.goto("file:///C:/Users/HP/Downloads/InstanceTest.html")
    page.locator(".dropdown").hover()
    page.locator('//a[@onclick="showPage(\'instances\')"]').click()
    time.sleep(3)

    page.locator("#filterGroup").select_option("Group A")
    time.sleep(3)

    cloud_list = ["AWS", "Azure", "GCP"]
    list_status = ["Running", "Stopped", "Pending"]

    for i in range(3):

        page.locator("#filterCloud").select_option(cloud_list[i])
        time.sleep(3)

        page.locator("#filterStatus").select_option(list_status[i])
        time.sleep(4)

        page.get_by_role("button", name="Add").click()
        time.sleep(2)

        list_status = ["Running", "Stopped", "Pending"]

        for status_name in list_status:
            page.locator("[value='kvm']").click()

            page.locator("#statusSelect").select_option(label=status_name)
            time.sleep(5)

            page.get_by_role("button", name="OK").click()
            time.sleep(2)

            page.get_by_role("button", name="Add").click()
            time.sleep(2)

        # Deleting the vm's
        page.get_by_role("button", name="Delete").click()
        time.sleep(5)









