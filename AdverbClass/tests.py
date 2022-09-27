from adverb_class import Advert
import tests_constants
import unittest


class TestAdvert(unittest.TestCase):
    def test_without_title(self):
        self.assertRaises(AttributeError, Advert, tests_constants.NO_TITLE)

    def test_keywords(self):
        el = Advert(tests_constants.KW_AND_CLR)
        self.assertTrue(hasattr(el, 'class_'), 'keyword-attributes deleted')

    def test_nested_attr_via_point(self):
        self.assertEqual(Advert(tests_constants.NESTED_ATTR).loc.address.city,
                         'Самара', 'getting nested attribute via point failed')

    def test_negative_temperature_construct(self):
        self.assertRaises(ValueError, Advert, tests_constants.NEG_TEMP_CONSTR)

    def test_negative_temperature_setter(self):
        el = Advert(tests_constants.NEG_TEMP_SET)
        message = 'it must not be allowed to set a negative price'
        with self.assertRaises(ValueError, msg=message):
            el.price = -1

    def test_yellow_color_print(self):
        el = Advert(tests_constants.KW_AND_CLR)
        self.assertEqual(el.__str__(), '\033[1;33mВельш-корги | 0 ₽',
                         'print-color is not yellow')
