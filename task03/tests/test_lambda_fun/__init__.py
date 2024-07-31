import unittest
import importlib
from tests import ImportFromSourceContext

with ImportFromSourceContext():
    LAMBDA_HANDLER = importlib.import_module('lambdas.lambda_fun.handler')


class LambdaFunLambdaTestCase(unittest.TestCase):
    """Common setups for this lambda"""

    def setUp(self) -> None:
        self.HANDLER = LAMBDA_HANDLER.LambdaFun()

