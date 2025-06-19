

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class ExampleDotComTest(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    def test_example_com_title(self):
        url = "https://example.com"
        expected_title = "Example Domain"

        self.driver.get(url)
        actual_title = self.driver.title
        self.assertEqual(actual_title, expected_title,
                         f"Page title does not match. Expected: '{expected_title}', Actual: '{actual_title}'")

    def tearDown(self):
        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()

