from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.auth import UserAuthSerializer, UserSerializer


class AuthToken(APIView):

    @csrf_exempt
    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        token, _ = Token.objects.get_or_create(user=user)

        data = {
            'token': token.key,
            'user': UserSerializer(user).data
        }

        return Response(data)
