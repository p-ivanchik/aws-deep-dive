from tests.test_lambda_fun import LambdaFunLambdaTestCase


class TestSuccess(LambdaFunLambdaTestCase):

    def test_success(self):
        self.assertEqual(self.HANDLER.handle_request(dict(), dict()), 200)

