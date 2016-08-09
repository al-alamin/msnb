from django.test import TestCase

from common.models import Author, AuthorRole


class TestViews(TestCase):

    def test_model_call_advisors_return_correct_data(self):
        role = AuthorRole(role='R')
        role.save()
        author = Author(first_name='abu', last_name='obaida', email='tareqbuet@gmail.com',)
        author.save()
        author = Author(first_name='abu', last_name='tareq', email='tareqbuet@gmail.com')
        author.save()
        advisors = Author.objects.all()
        print('advisors',advisors)
