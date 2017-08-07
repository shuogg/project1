#coding=utf-8
from django.utils import six
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from django.http import *
import datetime,json

class JsonResponse(Response):
    """
    An HttpResponse that allows its data to be rendered into
    arbitrary media types.
    """

    def __init__(self, data=None, code=None, message=None,
                 status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None):
        """
        Alters the init arguments slightly.
        For example, drop 'template_name', and instead use 'data'.
        Setting 'renderer' and 'media_type' will typically be deferred,
        For example being set automatically by the `APIView`.
        """
        super(Response, self).__init__(None, status=status)

        if isinstance(data, Serializer):
            msg = (
                'You passed a Serializer instance as data, but '
                'probably meant to pass serialized `.data` or '
                '`.error`. representation.'
            )
            raise AssertionError(msg)

        self.data = {'code': code, 'message': message, 'data': data}
        self.template_name = template_name
        self.exception = exception
        self.content_type = content_type
        if headers:
            for name, value in six.iteritems(headers):
                self[name] = value



def R_Head(code):
    response = HttpResponse(json.dumps({"status": code})) 
    response["Access-Control-Allow-Origin"] = "http://192.168.137.1" 
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS" 
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*" 
    response["Access-Control-Allow-Credentials"] = 'true'
    return response


