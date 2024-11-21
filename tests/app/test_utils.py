import os
import unittest

from cdk import utils


class TestUtils(unittest.TestCase):
    def test_lack_of_environment_vals(self):
        os.environ["CDK_APP_STAGE"] = "staging"
        os.environ["CDK_DEFAULT_ACCOUNT"] = "1234567890"
        os.environ["CDK_DEFAULT_REGION"] = "us-west-2"
        self.assertFalse(utils.lack_of_environment_vals())

        del os.environ["CDK_APP_STAGE"]
        self.assertTrue(utils.lack_of_environment_vals())

        os.environ["CDK_APP_STAGE"] = "staging"
        del os.environ["CDK_DEFAULT_ACCOUNT"]
        self.assertTrue(utils.lack_of_environment_vals())

        os.environ["CDK_DEFAULT_ACCOUNT"] = "1234567890"
        del os.environ["CDK_DEFAULT_REGION"]
        self.assertTrue(utils.lack_of_environment_vals())

    def test_name(self):
        name_trunk = "name-trunk"
        os.environ["CDK_APP_STAGE"] = "staging"
        self.assertEqual(utils.name(name_trunk), "staging-name-trunk")
        del os.environ["CDK_APP_STAGE"]
        self.assertIsNone(utils.name(name_trunk))

    def test_app_stage_is_production(self):
        os.environ["CDK_APP_STAGE"] = "production"
        self.assertTrue(utils.app_stage_is_production())
        del os.environ["CDK_APP_STAGE"]
        self.assertFalse(utils.app_stage_is_production())

    def test_app_stage(self):
        os.environ["CDK_APP_STAGE"] = "staging"
        self.assertEqual(utils.app_stage(), "staging")
