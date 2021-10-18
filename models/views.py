from django.http.response import HttpResponse
from django.shortcuts import render

def auth(Request):
    return render(Request, 'index.html')


def users(Request, name_user):
    return render(Request, 'users.html', {'name_user':name_user})


def list(Request):
    return(
        HttpResponse('list')
    )