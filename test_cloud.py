from playwright.sync_api import expect


def test_go_to_api_page_from_main_page(browser):
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://cloud.ru")
    page.wait_for_selector("//li[normalize-space(.)='Сервисы']").click()
    page.wait_for_selector("//div[@id='portal']//div[normalize-space(.)='Инфраструктура']").click()
    page.wait_for_selector(
        "//div[@id='portal']//h2[normalize-space(.)='Инфраструктура']/following-sibling::a[contains(@href, "
        "'api-gateway')]").click()
    page.wait_for_url("https://cloud.ru/ru/products/oblachnyj-api-gateway-hosting")

    expect(page).to_have_title("API Gateway")

