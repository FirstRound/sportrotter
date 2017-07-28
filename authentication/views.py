from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from authentication.models import SportrotterUser


class Logout(APIView):
    queryset = SportrotterUser.objects.all()
    permission_classes = ()

    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

# class Register(APIView):
#     queryset = SportrotterUser.objects.all()
#     permission_classes = ()
#     def post(self, request):
#         data = request.json()
#         SportrotterUser(username = data['email'],
#                         email=data['email'], password)
        # pass