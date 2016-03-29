import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_tutorial.settings')

import django
django.setup()
from django.utils import timezone
from polls.models import Question, Choice


def populate():
    question_new = add_question("What's New?")

    add_choice(question_id=question_new.id, choice_text='Not much')
    add_choice(question_id=question_new.id, choice_text='The sky')
    add_choice(question_id=question_new.id, choice_text='Just hacking again')

    question_book = add_question("What book do you like?")

    add_choice(question_id=question_book.id, choice_text='learn Django hard way')
    add_choice(question_id=question_book.id, choice_text='Django web development')
    add_choice(question_id=question_book.id, choice_text='Think like Pythoner')


def add_question(question_text):
    pub_date = timezone.now()
    try:
        q = Question.objects.get(question_text=question_text)
    except:
        q = Question.objects.create(question_text=question_text,pub_date=pub_date)
    return q


def add_choice(question_id, choice_text):
    c = Choice.objects.get_or_create(question_id=question_id, choice_text=choice_text)[0]
    return c


if __name__ == '__main__':
    print("Starting Polls population script...")
    populate()
