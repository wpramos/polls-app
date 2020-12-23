import datetime

from django.test import TestCase

from django.utils import timezone

from .models import Choice, Question

# Create your tests here.

class QuestionModelTests(TestCase):
    
    def test_was_published_recently_with_future_question(self):
        future_time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=future_time)

        self.assertIs(future_question.was_published_recently(), False)
