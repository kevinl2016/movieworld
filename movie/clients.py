import requests
from django.conf import settings

class ApiClient():
    default_headers = {
        'Accept': 'Application/json'
    }

    def request(self, mothed='get', api_path='/', additional_headers=None, **request_kwargs):
        request_headers = self.default_headers.copy()
        request_headers.update(
            { 'x-access-token': settings.API_TOKEN }
        )
        if additional_headers:
            request_headers.update(additional_headers)
        
        response = getattr(requests, mothed) (
            '{}{}'.format(settings.SERVICE_API_URL, api_path),
            headers=request_headers,
            **request_kwargs
        )
        return response
