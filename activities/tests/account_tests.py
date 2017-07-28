import io
import logging
import os
import shutil

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from activities.views import UserList
from authentication.models import SportrotterUser
from sportrotter import settings

logger = logging.getLogger('django_test')

TEST_MEDIA_ROOT = os.path.join(settings.BASE_DIR, 'tmp/django_test')


@override_settings(MEDIA_ROOT=TEST_MEDIA_ROOT)
class AccountTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        """
        creating a default user to authenticate against
        :return:
        """
        super(AccountTests, cls).setUpClass()
        file_field = SimpleUploadedFile('best_file_eva.txt',
                                        b'these are the file contents!')
        u = SportrotterUser(username="admin", password="admin",
                            avatar=file_field)
        u.save()

    @classmethod
    def tearDownClass(cls):
        super(AccountTests, cls).tearDownClass()
        shutil.rmtree(TEST_MEDIA_ROOT)

    def test_create_account(self):
        """
        Ensure we can create a new user.
        """
        url = reverse(UserList.view_name)
        tmp_file = io.BytesIO(b'avatar')
        data = {'username': 'u',
                'password': 'p',
                'avatar': tmp_file}
        response = self.client.post(url, data, format='multipart')
        logger.info(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
