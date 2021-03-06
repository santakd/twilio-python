# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class ConfigurationTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.conversations.v1.configuration().fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://conversations.twilio.com/v1/Configuration',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "default_chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "default_messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "default_inactive_timer": "PT1M",
                "default_closed_timer": "PT10M",
                "url": "https://conversations.twilio.com/v1/Configuration",
                "links": {
                    "service": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Configuration"
                }
            }
            '''
        ))

        actual = self.client.conversations.v1.configuration().fetch()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.conversations.v1.configuration().update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://conversations.twilio.com/v1/Configuration',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "default_chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "default_messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "default_inactive_timer": "PT1M",
                "default_closed_timer": "PT10M",
                "url": "https://conversations.twilio.com/v1/Configuration",
                "links": {
                    "service": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Configuration"
                }
            }
            '''
        ))

        actual = self.client.conversations.v1.configuration().update()

        self.assertIsNotNone(actual)
