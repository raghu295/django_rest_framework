from rest_framework import renderers
import json

# Custom renderer class to render the response in JSON format

class UserRenderer(renderers.JSONRenderer):
    charset = 'utf-8'
    
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        
        if 'ErrorDetail' in str(data):
            response = json.dumps({'errors': data})
        else:
            response = json.dumps({'data': data})
        
        return response