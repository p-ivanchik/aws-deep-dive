import json

from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('HelloWorld-handler')


class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass

    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        # todo implement business logic
        return 200


HANDLER = HelloWorld()


def lambda_handler(event, context):
    PATH = '/hello'
    path = event["rawPath"]
    method = event["requestContext"]["http"]["method"]
    is_valid = path == PATH

    statusCode = is_valid and 200 or 400
    message = is_valid and "Hello from Lambda" or f"Bad request syntax or unsupported method. Request path: {path}. HTTP method: {method}"
    return {
        "body": {
            "statusCode": statusCode,
            "message": message
        }
    }
