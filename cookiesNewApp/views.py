from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cookies_new_count(request):
    count = request.COOKIES.get('counts',0)
    totalCount = int(count) + 1
    response = render(request,'cookiesNewcount.html' , {'newCount' : totalCount})
    response.set_cookie('counts',totalCount)
    return response
