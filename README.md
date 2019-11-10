# Blog - Portfolio Project #3
> This application is a blog/social media

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
After programming bootcamp I'am constantly learning and doing new projects, mostly with
YouTubers courses. This app was made after few YouTube courses and thought me lots of new
things in django mainly working with generic views. All frontend was already made

## Technologies
* Python 3.7
* Django 2.2.6

## Setup
Create new virtualenv and install everything from requirements.txt. If you want
to use other database than this in this project, run populate_sript.py after migrate

## Code Examples
```python
def get_queryset(self):
    query = self.request.GET.get('q')
    queryset_list = Post.objects.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query) |
        Q(author__username__icontains=query) |
        Q(author__first_name__contains=query) |
        Q(author__last_name__icontains=query)
    ).distinct()
    return queryset_list.order_by('-date_posted')
```

## Features
List of features ready and TODOs for future development
* You can create user, edit profile and picture, reset password with email
* You can make a post, edit and delete it
* Posts have adding date and also edit date
* By clicking on user you will see all his posts
* Superuser can delete posts
* You can search any information on blog

To-do list:
* Posts comments

## Status
Project is _in progress_. I'm also doing other projects for my portfolio but I hope
I'll come back to this

## Inspiration
This is an app was made with [Corey Schafer](https://www.youtube.com/user/schafer5) YouTube
Django course

## Contact
Created by [@hef](https://twitter.com/hef4rl) - feel free to contact me!