from django.shortcuts import render,redirect
from .models import Search
import requests
from bs4 import BeautifulSoup


base_url ='https://www.prothomalo.com/sports'
def home(request):
    if request.method == 'POST':
        list= request.POST['search']
        return redirect('/')
    return render(request,'base.html',{})


def new_search(request):

    if request.method == 'POST':
        list =request.POST['search']
        search=Search.objects.create(search=list)
        response=requests.get(base_url)
        data= response.text
        print(data)

        context={'post_list':search}

        return render(request,'my_app/new_search.html',context)
    return render(request,'base.html')
