from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import boto3
import json


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def queens(request):
    s3client = boto3.client('s3')
    objects = s3client.list_objects_v2(
        Bucket = 'guess-her-heroku-static-files',
        Prefix = 'queens/')
    object_keys = json.dumps(['https://guess-her-heroku-static-files.s3.us-east-2.amazonaws.com/' + object['Key'] for object in objects['Contents']])
    print(object_keys)

    return render(request, "queens.html", {"images" : object_keys})


def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
