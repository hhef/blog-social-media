"""
This script will fill data base with a superuser, 20 random users and 20 random posts. All users password will be
'password', superuser username will be 'admin' and password will be 'password'. Run this script after migrations
if you are using other database than this in this project.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blog_socjal_media.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import Post
from faker import Faker
import random


def create_superuser():
    superuser = User.objects.create_superuser('admin', 'admin@admin.com', 'password')
    superuser.save()


def create_users():
    faker = Faker()
    for _ in range(20):
        name = faker.first_name() + faker.last_name()
        email = faker.email()
        password = 'password'
        user = User.objects.create_user(name, email, password)
        user.save()


def create_posts():
    faker = Faker()
    for _ in range(20):
        author_id = str(random.randint(2, 15))
        title = faker.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        content = faker.texts(nb_texts=3, max_nb_chars=200, ext_word_list=None)
        post = Post(title=title, content=content, author_id=author_id)
        post.save()


create_superuser()
create_users()
create_posts()

