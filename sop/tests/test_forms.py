from unittest.mock import MagicMock, patch, Mock

from django.test import TestCase
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile

from sop.forms import SOPSubmitForm, MyForm

import os
from django.conf import settings


# class SOPSubmitFormTest(TestCase):

#     def test_form_valication_for_blank_name(self):
#         file_mock = MagicMock(spec=File, name="file")
#         form = SOPSubmitForm(
#             data={
#                 'name': "alamin",
#                 'email': "abc@gamil.com",
#                 'msg': "hi",
#                 'file': file_mock

#             })

#         self.assertTrue(form.is_valid())






class MyFormTest(TestCase):

    def test_mock(self):
        file = MagicMock(spec=File, name='file')
        file.name = "abc.txt"
        # file.read.return_value = b"alamin"
        # file.length = 50
        form = MyForm(files={'file': file})
        print (form)
        print (form.errors)
        self.assertTrue(form.is_valid())

    def test_my_form4(self):
        upload_file = open(os.path.join(settings.MEDIA_ROOT, 'forms.pyc'), 'rb')
        f2 = SimpleUploadedFile(upload_file.name, upload_file.read())
        print (type(f2))
        file_dict = {'file': f2}
        # file = SimpleUploadedFile(upload_file.name, upload_file.read())
        # print (type(upload_file))
        # print (upload_file.read())
        # print (file.size)
        form = MyForm(files={'file': f2})
    


        self.assertTrue(form.is_valid())

    # def test_my_form2(self):
    #     upload_file = File(open(os.path.join(settings.MEDIA_ROOT, 'sop.doc')))
    #     output_file = open(
    #         os.path.join(settings.MEDIA_ROOT, 'output.doc'), 'w')

    #     # output_file.close()
    #     form = MyForm({'file': output_file})

    #     self.assertTrue(form.is_valid())
    #     output_file.close()

    # def test_my_form(self):
    #     upload_file = (open(os.path.join(settings.MEDIA_ROOT, 'sop.doc')))

    #     print(upload_file)
    #     print (type(upload_file))
    #     form = MyForm({'file': "alamin"})
    #     # print (type(form.file))
    #     print (form.errors)
    #     print(form.is_valid())
    #     self.assertTrue(form.is_valid())
    #     




    def test_my_form(self):
        # best way to test this kind of form to create a client and post data using the client.
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'sop.txt')
        upload_file = open(file_path,'rb')
        inmemoryfile = SimpleUploadedFile(upload_file.name, upload_file.read())
        # or you can simply create in memory file like this
        # inmemoryfile = SimpleUploadedFile('testfile.docx', b'this is test file')
        file_dict = {'file': inmemoryfile}
        form = MyForm(files=file_dict)
        print('errors',form.errors)
        self.assertTrue(form.is_valid())
        upload_file.close()