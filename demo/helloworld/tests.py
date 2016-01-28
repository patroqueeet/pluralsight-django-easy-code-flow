"""
simple test for rendered html
"""

from django.test import TestCase
from django.test import Client


class HelloWorldTestCase(TestCase):

    def test_helloworld(self):

        client = Client()
        response = client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(u'Hello World' in response.content)
