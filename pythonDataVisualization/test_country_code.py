import unittest
from country_codes import get_country_code


class TestCountryCodes(unittest.TestCase):
    """针对get_country_codes的测试类"""

    def test_country_codes_inner(self):
        country_name = 'Yemen, Rep.'
        code = get_country_code(country_name)
        self.assertEqual(code, 'ye')

    def test_country_codes_outer(self):
        country_name = 'Australia'
        code = get_country_code(country_name)
        self.assertEqual(code, 'au')


unittest.main()