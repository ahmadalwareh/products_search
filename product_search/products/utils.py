
import jwt
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed


def authenticate(request):
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        raise AuthenticationFailed('Authorization header missing')

    try:
        _, token = auth_header.split()
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user_id = payload['user_id']

        return user_id

    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Token has expired')

    except jwt.InvalidTokenError:
        raise AuthenticationFailed('Invalid token')
