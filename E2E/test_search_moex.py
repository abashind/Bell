from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChOpts
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest


class TestSearchMoex:

    want_to_find = 'Московская биржа'
    has_to_be_found = 'https://www.moex.com/'

    for_google = ['https://www.google.com/', '[name=q]', "#search"]
    for_yandex = ['https://www.yandex.ru/', '#text', '.content__left']

    @pytest.mark.parametrize('s_engine,s_field,after_loading', [for_google, for_yandex])
    def test_search_moex(self, s_engine, s_field, after_loading):
        opts = ChOpts()
        opts.headless = True
        driver = Chrome(options=opts)
        driver.implicitly_wait(3)

        driver.get(s_engine)
        wait = WebDriverWait(driver, 10)
        search_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, s_field)))
        search_field.send_keys(self.want_to_find)
        search_field.send_keys(Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, after_loading)))

        try:
            driver.find_element_by_css_selector(f'a[href="{self.has_to_be_found}"]')
            assert True
        except Exception:
            assert False, f"{self.has_to_be_found} wasn't found in search results..."
