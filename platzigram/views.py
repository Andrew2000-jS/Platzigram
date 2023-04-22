from django.http import HttpResponse
from datetime import datetime
import json


def sort_integers(request):
    numbers = sorted([int(i) for i in request.GET['numbers'].split(',')])
    data = {
        'status': 'ok',
        'data': numbers,
        'message': 'Integers sorted successfully'
    }

    return HttpResponse(
        json.dumps(data, indent=4),
        content_type="application/json"
    )


def say_hi(request, **kwards):
    name, age = kwards['name'], kwards['age']
    print(type(age))
    data = {
        'status': False,
        'message': ''
    }

    if age < 12:
        data['status'] = False
        data['message'] = 'Sorry you cannot access to this site'
    else:
        data['status'] = True
        data['message'] = f'Welcome {name}'

    return HttpResponse(json.dumps(data), content_type="application/json")
