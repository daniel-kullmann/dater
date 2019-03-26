from django.http import HttpResponse

import json

def view1(request):
    response = HttpResponse(json.dumps([]), content_type='application/json')
    return response

