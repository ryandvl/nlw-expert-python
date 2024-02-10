from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

from src.controllers.tag_creator_controller import TagCreatorController

from src.errors.error_handler import handle_errors

class TagCreatorView:
    '''
        Responsability for interacting with HTTP
    '''

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        tag_creator_controller = TagCreatorController()

        body = http_request.body

        if not body or not body['product_code']:
            return handle_errors(Exception("'product_code'"))

        product_code = body["product_code"]

        # Business rule logic
        formatted_response = tag_creator_controller.create(product_code)

        # Return HTTP
        return HttpResponse(status_code=200, body=formatted_response)