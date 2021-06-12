from unittest import TestCase

from subscrypt import Subscrypt
import json

with open('config.json', 'r') as f:
    config = json.load(f)


class TestSubscrypt(TestCase):
    def setUp(self):
        self.client = Subscrypt()

    def test_is_connected_returns_true(self):
        self.assertEqual(self.client.is_connected(), True)

    def test_check_subscription_returns_bool(self):
        self.assertIn(
            self.client.check_subscription(config['test']['userAddress'], config['test']['providerAddress'], 0),
            [True, False])

    def test_check_subscription_with_username_returns_bool(self):
        self.assertIn(
            self.client.check_subscription(config['test']['username'], config['test']['providerAddress'], 0),
            [True, False])

    def test_get_username_works(self):
        self.assertEqual(self.client.get_username(config['test']['userAddress']), config['test']['username'])

    def test_retrieve_whole_data_with_username_works(self):
        self.assertIsNotNone(self.client.retrieve_whole_data_with_username(
            config['test']['username'], config['test']['passWord']))

    def test_retrieve_data_with_username_works(self):
        self.assertIsNotNone(self.client.retrieve_data_with_username(
            config['test']['username'], config['test']['providerAddress'], config['test']['passWord']))

    def test_is_username_available_returns_false(self):
        self.assertEqual(self.client.is_username_available(config['test']['username']), False)

    def test_check_auth_true(self):
        self.assertEqual(self.client.check_auth(config['test']['userAddress'], config['test']['providerAddress'],
                                                config['test']['passWord']), True)

    def test_check_auth_with_username_true(self):
        self.assertEqual(
            self.client.check_auth_with_username(config['test']['username'], config['test']['providerAddress'],
                                                 config['test']['passWord']), True)

    def test_user_check_auth_with_username_true(self):
        self.assertEqual(
            self.client.user_check_auth_with_username(config['test']['username'],
                                                      config['test']['passWord']), True)

    def test_get_plan_data(self):
        plans = config['test']['plansData']
        index = 0
        for plan in plans:
            self.assertEqual(
                self.client.get_plan_data(config['test']['providerAddress'],
                                          index), plan)
            index += 1

    def test_provider_check_auth_true(self):
        self.assertEqual(
            self.client.provider_check_auth(config['test']['providerAddress'],
                                            config['test']['passWord']), True)

    def test_provider_check_auth_with_username_true(self):
        self.assertEqual(
            self.client.provider_check_auth_with_username(config['test']['providerUsername'],
                                                          config['test']['passWord']), True)

    def test_get_plan_data(self):
        for i in range(len(config['test']['plansData'])):
            self.assertEqual(
                self.client.get_plan_characteristics(config['test']['providerAddress'],
                                          i), config['test']['plansCharacteristic'][i])
