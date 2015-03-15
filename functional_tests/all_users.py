from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    """docstring for NewVisitorTest"""
    def setup(self):
        self.browser = webdriver.chrome()
        self.browser.implicitly_wait(3)

    def teardown(self):
        self.browser.quit()

    def test_it_worked(self):
        self.browser.get('127.0.0.1:8000')
        self.assertIn('Welcom to django!', self.browser.title)

if __name__ == '__main__':
    unittest.main()
