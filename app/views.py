from django.shortcuts import render, HttpResponse
import requests
import json


# Create your views here.

def index(request):
    return HttpResponse('Testing View')


def profile(request):
    req = requests.get('https://api.github.com/users/mpankajarun')
    #content = req.text
    jsonList = []
    jsonList.append(json.loads(req.content))
    content = []
    userData = {}
    for data in jsonList:
        userData['name'] = data['name']
        userData['company'] = data['company']
        userData['location'] = data['location']
        userData['blog'] = data['blog']
        userData['email'] = data['email']
        userData['public_gists'] = data['public_gists']
        userData['public_repos'] = data['public_repos']
        userData['avatar_url'] = data['avatar_url']
        userData['followers'] = data['followers']
        userData['following'] = data['following']
    content.append(userData)
    #return HttpResponse(content)
    return render(request, 'app/profile.html', {'data': content})
