from django.test import TestCase
from django.contrib.auth.models import User

from .forms import AuthForm


class ErrorFormMethodTests(TestCase):

    def setUp(self):

        self.post_data = {
            'first': {
                'login': 'test',
                'password': 'for_test'
            },
            'second': {
                'login': 'test',
                'password': 'test_for'
            }
        }

    @classmethod
    def setUpTestData(cls):

        User.objects.create_user(username='test', password='for_test')

    def test_get_errors_and_is_has_errors(self):

        # If data is valid

        form = AuthForm(self.post_data['first'])
        self.assertEqual(form.is_valid(), True)
        self.assertEqual(form.get_errors(), False)
        self.assertEqual(form.is_has_errors(), False)

        # If data is invalid

        form_2 = AuthForm(self.post_data['second'])
        self.assertEqual(form_2.is_valid(), False)
        self.assertEqual(form_2.get_errors()[0], 'Invalid login or password!')
        self.assertEqual(form_2.is_has_errors(), True)
