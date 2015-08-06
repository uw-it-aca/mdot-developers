from django.test import TestCase
from mdotdevs.forms import ReviewForm


class MdotdevsFormTest(TestCase):

    def setUp(self):
        pass

    def test_form_input_consumption(self):
        form_data = {
            'campus_audience': 'Student',
            'campus_need': 'Test',
            'sponsor_name': 'Test Case',
            'sponsor_netid': 'testcase',
            'sponsor_email': 'testcase@uw.edu',
            'dev_name': 'Test Case',
            'dev_email': 'testcase@uw.edu',
            'support_name': 'Test Case',
            'support_email': 'testcase@uw.edu',
            'app_code': '<?php ?>'}
        form = ReviewForm(data=form_data)
        self.assertTrue(form.is_valid())

    def tearDown(self):
        pass
