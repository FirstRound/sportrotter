import os
import random
import string

from django.conf import settings


def id_generator(size=32,
                 chars=string.ascii_lowercase +
                       string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def make_new_path(ext=''):
    if not os.path.isdir(settings.FILE_ROOT):
        os.makedirs(settings.FILE_ROOT)
    file_id = id_generator() + '.' + ext
    return os.path.join(settings.FILE_ROOT, file_id), \
           os.path.join(settings.STORAGE_URL, file_id)
