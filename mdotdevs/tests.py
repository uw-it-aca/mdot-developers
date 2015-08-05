from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import resolve

class MdotdevTest(TestCase):

    def setUp(self):
        self.client = Client()
        pass

    def test_url_home(self):
        resolver = resolve('/developers/')
        self.assertEqual('home', resolver.view_name)

    def test_url_guidelines(self):
        resolver = resolve('/developers/guidelines/')
        self.assertEqual('guidelines', resolver.view_name)

    def test_url_process(self):
        resolver = resolve('/developers/process/')
        self.assertEqual('process', resolver.view_name)

    def test_url_review(self):
        resolver = resolve('/developers/review/')
        self.assertEqual('review', resolver.view_name)

    def test_view_home(self):
        response = self.client.get('/developers/')
        self.assertEqual(response.status_code, 200)

    def test_view_guidelines(self):
        response = self.client.get('/developers/guidelines/')
        self.assertEqual(response.status_code, 200)

    def test_view_process(self):
        response = self.client.get('/developers/process/')
        self.assertEqual(response.status_code, 200)

    def test_view_review(self):
        response = self.client.get('/developers/process/')
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        pass
