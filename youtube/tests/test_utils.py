import os
import pathlib
import json

from django.test import TestCase
from google.oauth2.credentials import Credentials

from youtube import (
    utils,
    settings
)

DUMMY_STR_TOKEN = "dummy-1"
DUMMY_DICT = {"foo": "bar"}


class DummyCredentials(Credentials):
    token: str = ""
    refresh_token: str = DUMMY_STR_TOKEN
    token_uri: str = DUMMY_STR_TOKEN
    client_id: str = DUMMY_STR_TOKEN
    client_secret: str = DUMMY_STR_TOKEN
    scopes: str = DUMMY_STR_TOKEN


class TestYoutubeCredentialsUtils(TestCase):

    def setUp(self) -> None:
        self.path = pathlib.Path(__file__).parent.absolute()
        self.expected_file = f"{str(self.path)}/{settings.CREDENTIALS_FILE}"
        self.credentials: Credentials = DummyCredentials(
            token=DUMMY_STR_TOKEN
        )

    def test_credentials_to_dict(self):
        cred_dict = utils.credentials_to_dict(self.credentials)
        self._assert_credentials(cred_dict)

    def test_save_credentials_to_file(self):
        utils.save_credentials_to_file(DUMMY_DICT, f"{str(self.path)}/")
        self.assertTrue(
            os.path.exists(self.expected_file) and os.path.isfile(self.expected_file)
        )
        with open(self.expected_file) as r:
            dict_from_file = json.load(r)
            self.assertEqual(
                DUMMY_DICT,
                dict_from_file
            )
        os.remove(self.expected_file)

    def test_load_credentials_from_file(self):
        cred_dict = utils.credentials_to_dict(self.credentials)
        utils.save_credentials_to_file(cred_dict, str(self.path))
        credentials: Credentials = utils.load_credentials_from_file(str(self.path))
        self.assertIsInstance(credentials, Credentials)
        self._assert_credentials(cred_dict)

    def _assert_credentials(self, cred_dict: dict):
        self.assertIsInstance(cred_dict, dict)
        self.assertIn("token", cred_dict)
        self.assertEqual(cred_dict.get("token"), DUMMY_STR_TOKEN)
        self.assertIn("refresh_token", cred_dict)
        self.assertEqual(cred_dict.get("refresh_token"), DUMMY_STR_TOKEN)
        self.assertIn("token_uri", cred_dict)
        self.assertEqual(cred_dict.get("token_uri"), DUMMY_STR_TOKEN)
        self.assertIn("client_id", cred_dict)
        self.assertEqual(cred_dict.get("client_id"), DUMMY_STR_TOKEN)
        self.assertIn("client_secret", cred_dict)
        self.assertEqual(cred_dict.get("client_secret"), DUMMY_STR_TOKEN)
        self.assertIn("scopes", cred_dict)
        self.assertEqual(cred_dict.get("scopes"), DUMMY_STR_TOKEN)
