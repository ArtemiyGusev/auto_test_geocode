from selene.support.shared import browser
from selenium.webdriver import ActionChains
import selene
from selene.core.wait import Command


def double_click_to(x: int, y: int):
    def action(source: selene.Element):
        ActionChains(source.config.driver).move_by_offset(x, y).double_click().perform()

    return Command(f'click with offset x {x}, y {y}', action)


def drag_and_drop_to(x: int, y: int):
    def action(source: selene.Element):
        ActionChains(source.config.driver).drag_and_drop_by_offset(source(), x, y).perform()

    return Command(f'drag with x {x}, y {y}', action)


def url_open_size(url='/', width=1920, height=1080):
    browser.config.browser_name = 'chrome'
    browser.open(url).wait_until(5)
    browser.config.driver.set_window_size(width, height)
