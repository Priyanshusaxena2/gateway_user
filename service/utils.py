from functools import wraps

from django.http import JsonResponse


def validate_request(params_fields):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            request = request.request
            if request.method == 'GET':
                for field in params_fields:
                    if field not in request.GET or not request.GET.get(field):
                        return JsonResponse({'error': 'Invalid request'}, status=400)
            return func(request, *args, **kwargs)

        return wrapper
    return decorator

