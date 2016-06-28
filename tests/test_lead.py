from unittest import TestCase
from pyrdstation.client import Lead

__author__ = 'zamboni'


class TestLead(TestCase):
    def setUp(self):
        self.obj = Lead(email="test@test.com", conversion_id="1234567890")

    def test_email(self):
        self.assertEqual(self.obj.email, self.obj._email)
        self.assertEqual(self.obj.email, "test@test.com")

    def test_conversion_id(self):
        self.assertEqual(self.obj.conversion_id, self.obj._conversion_id,
                         msg="External conversion_id property is not equal to the internal _conversion_id property")
        self.assertEqual(self.obj.conversion_id, "1234567890",
                         msg="External conversion_id property is not equal to 1234567890")

    def test_name(self):
        self.obj.name = "Test Name"
        self.assertEqual(self.obj.name, self.obj._name)
        self.assertEqual(self.obj.name, "Test Name")

    def test_job_position(self):
        self.obj.job_position = "Test Job"
        self.assertEqual(self.obj.job_position, self.obj._job_position)
        self.assertEqual(self.obj.job_position, "Test Job")

    def test_company(self):
        self.obj.company = "Test Company"
        self.assertEqual(self.obj.company, self.obj._company)
        self.assertEqual(self.obj.company, "Test Company")

    def test_employee_qty(self):
        self.obj.employee_qty = 100
        self.assertEqual(self.obj.employee_qty, self.obj._employee_qty)
        self.assertEqual(self.obj.employee_qty, 100)

    def test_company_address(self):
        self.obj.company_address = "3321 Test Ave. Boston, MA"
        self.assertEqual(self.obj.company_address, self.obj._company_address)
        self.assertEqual(self.obj.company_address, "3321 Test Ave. Boston, MA")

    def test_phone(self):
        self.obj.phone = "+1 702 555-5555"
        self.assertEqual(self.obj.phone, self.obj._phone)
        self.assertEqual(self.obj.phone, "+1 702 555-5555")

    def test_mobile(self):
        self.obj.mobile = "+1 702 555-5544"
        self.assertEqual(self.obj.mobile, self.obj._mobile)
        self.assertEqual(self.obj.mobile, "+1 702 555-5544")

    def test_website(self):
        self.obj.website = "www.test.com"
        self.assertEqual(self.obj.website, self.obj._website)
        self.assertEqual(self.obj.website, "www.test.com")

    def test_twitter(self):
        self.obj.twitter = "@testcompany"
        self.assertEqual(self.obj.twitter, self.obj._twitter)
        self.assertEqual(self.obj.twitter, "@testcompany")

    def test_c_utmz(self):
        self.obj.c_utmz = "google tag"
        self.assertEqual(self.obj.c_utmz, self.obj._c_utmz)
        self.assertEqual(self.obj.c_utmz, "google tag")

    def test_tags(self):
        self.obj.tags = "#tag_test"
        self.assertEqual(self.obj.tags, self.obj._tags)
        self.assertEqual(self.obj.tags, "#tag_test")

    def test_to_dict(self):
        self.obj.name = "Test Name"
        self.obj.job_position = "Test Job"
        self.obj.company = "Test Company"
        self.obj.employee_qty = 100
        self.obj.company_address = "3321 Test Ave. Boston, MA"
        self.obj.phone = "+1 702 555-5555"
        self.obj.mobile = "+1 702 555-5544"
        self.obj.website = "www.test.com"
        self.obj.twitter = "@testcompany"
        self.obj.c_utmz = "google tag"
        self.obj.tags = "#tag_test"
        dict_after = self.obj.to_dict()
        self.assertEqual('email' in dict_after.keys(), True)
        self.assertEqual('identificador' in dict_after.keys(), True)
        self.assertEqual('nome' in dict_after.keys(), True)
        self.assertEqual('cargo' in dict_after.keys(), True)
        self.assertEqual('empresa' in dict_after.keys(), True)
        self.assertEqual('numero-de-funcionarios' in dict_after.keys(), True)
        self.assertEqual('endereco-empresa' in dict_after.keys(), True)
        self.assertEqual('telefone' in dict_after.keys(), True)
        self.assertEqual('celular' in dict_after.keys(), True)
        self.assertEqual('website' in dict_after.keys(), True)
        self.assertEqual('twitter' in dict_after.keys(), True)
        self.assertEqual('c_utmz' in dict_after.keys(), True)
        self.assertEqual('tags' in dict_after.keys(), True)

        self.assertEqual(dict_after['email'], "test@test.com")
        self.assertEqual(dict_after['identificador'], "1234567890")
        self.assertEqual(dict_after['nome'], "Test Name")
        self.assertEqual(dict_after['cargo'], "Test Job")
        self.assertEqual(dict_after['empresa'], "Test Company")
        self.assertEqual(dict_after['numero-de-funcionarios'], 100)
        self.assertEqual(dict_after['endereco-empresa'], "3321 Test Ave. Boston, MA")
        self.assertEqual(dict_after['telefone'], "+1 702 555-5555")
        self.assertEqual(dict_after['celular'], "+1 702 555-5544")
        self.assertEqual(dict_after['website'], "www.test.com")
        self.assertEqual(dict_after['twitter'], "@testcompany")
        self.assertEqual(dict_after['c_utmz'], "google tag")
        self.assertEqual(dict_after['tags'], "#tag_test")

    def test_to_rdstation_json(self):
        expected_json = '{"c_utmz": "google tag", "cargo": "Test Job", "celular": "+1 702 555-5544", "email": "test@test.com", "empresa": "Test Company", "endereco-empresa": "3321 Test Ave. Boston, MA", "identificador": "1234567890", "nome": "Test Name", "numero-de-funcionarios": "100", "tags": "#tag_test", "telefone": "+1 702 555-5555", "token_rdstation": "token", "twitter": "@testcompany", "website": "www.test.com"}'
        self.obj.name = "Test Name"
        self.obj.job_position = "Test Job"
        self.obj.company = "Test Company"
        self.obj.employee_qty = 100
        self.obj.company_address = "3321 Test Ave. Boston, MA"
        self.obj.phone = "+1 702 555-5555"
        self.obj.mobile = "+1 702 555-5544"
        self.obj.website = "www.test.com"
        self.obj.twitter = "@testcompany"
        self.obj.c_utmz = "google tag"
        self.obj.tags = "#tag_test"
        self.assertEqual(self.obj.to_rdstation_json('token'), expected_json)
