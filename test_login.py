from playwright.sync_api import Page, expect

def test_basarili_giris(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")

    # Sayfada "You logged into a secure area" metni görünene kadar bekle, sonra kontrol et
    expect(page.locator("body")).to_contain_text("You logged into a secure area")

    page.wait_for_timeout(5000)