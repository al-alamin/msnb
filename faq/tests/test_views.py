from django.test import TestCase
from models import models


class TestRelatedModels(TestCase):
    def insert_data_into_models(self):
        type = models.Type(name='Standard Test')
        type.save()
        cat = models.Category(name='GRE', type=type)
        cat.save()
        cat = models.Category(name='TOEFL', type=type)
        cat.save()
        type = models.Type(name='News')
        type.save()
        cat = models.Category(name='News', type=type)
        cat.save()
        author = models.Author(first_name='abu', last_name='obaida', email='tareqbuet@gmail.com')
        author.save()
        question = models.Question(author=author,text='sample question')
        question.save()
        ans = models.Answer(author=author, question=question, text='sample ans 1')
        ans.save()
        ans = models.Answer(author=author, question=question, text='sample ans 2')
        ans.save()

    def test_categoris_arranged_by_types(self):
        self.insert_data_into_models()
        types = models.Type.objects.all().exclude(name='News')
        for type in types:
            print('type', type.name)
            for cat in type.category_set.all():
                print(cat.name)

    def test_can_get_all_questions_and_corresponding_answer_set(self):
        questions = models.Question.objects.all()
        self.assertTrue(questions)
        for q in questions:
            print('q', q.text)
