from django.http import JsonResponse
from django.views import View
from rest_framework import generics, permissions, status

from activities import utils
from authentication.models import SportrotterUser
from authentication.serializers import SportrotterUserSerializer


class Me(generics.GenericAPIView):
    view_name = 'me'
    queryset = SportrotterUser.objects.all()
    serializer_class = SportrotterUserSerializer
    permissions = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        me = self.get_queryset().filter(id=self.request.user.id).get()
        serializer = self.get_serializer(me)
        return JsonResponse(serializer.data)


class FileUploadView(View):
    view_name = 'file-upload'

    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES['file']
        ext = uploaded_file.name.split('.')[-1]
        file_path, file_url = utils.make_new_path(ext=ext)

        with open(file_path, 'wb') as runner_file:
            for chunk in uploaded_file.chunks():
                runner_file.write(chunk)
        return JsonResponse(status=status.HTTP_201_CREATED,
                            data={'url': file_url})
