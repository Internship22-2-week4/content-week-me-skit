from django.http import HttpResponse
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hello World! Now is {}'.format(now))


def sort(request):
    numbers = [int(i) for i in request.GET['numbers'].split(', ')]
    sorted_ints = sorted(numbers)
    data = {
      'status': 'ok',
      'numbers': sorted_ints,
      'message': 'Integers sorted successfully.'
    }
    # import pdb; pdb.set_trace()
    return HttpResponse(json.dumps(data), content_type='application/json')


def hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Djangogram'.format(name)

    return HttpResponse(message)
