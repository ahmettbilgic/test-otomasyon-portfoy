from playwright.sync_api import Page, expect

def test_yanlıs_sifre(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "sauce")
    page.click("#login-button")     
    

    expect(page.locator("[data-test='error']")).to_contain_text("Username and password do not match")

