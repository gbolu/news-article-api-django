from django.http import JsonResponse, HttpResponse


class Paginate:
    page = 1
    limit = 10

    def set_page(self, page):
        self.page = page
        return self

    def set_limit(self, limit):
        self.limit = limit
        return self

# Create a response object in JSON format to be sent via HTTP


def composeResponse(data, message, code=200, error=None):
    response_data = {}
    response_data['code'] = code
    response_data['data'] = data
    response_data['message'] = message
    response_data['status'] = True

    if error is not None:
        response_data['error'] = error
        response_data['status'] = False

    return HttpResponse(JsonResponse(response_data, safe=False), status=code, content_type='application/json')
