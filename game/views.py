from django.shortcuts import render
from .models import MyTable
# Create your views here.
from django.http import HttpResponse
import random as rd
from django.shortcuts import redirect
from django.urls import reverse
users = {}
class user:
    def __init__(self):
        self.random = 0
        self.data = []
        self.len = 0
        self.stat = 0
    def set_random(self):
        
        self.random = rd.randrange(1,501)
        

def login(request):
    print(reverse('game:login'))
    return render(request, 'login.html')

def index(request):
    if request.method == 'POST' and 'username' in request.POST:
        if request.POST['username'] != 'key':
            return redirect('game:login') 
    elif request.method == 'GET' and request.COOKIES.get('username') != 'key':
        return redirect('game:login')
   
    req_headers = request.META
    x_forwarded_for_value = req_headers.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for_value:
        ip_addr = x_forwarded_for_value.split(',')[-1].strip()
    else:
        ip_addr = req_headers.get('REMOTE_ADDR')
    ip_addr = str(ip_addr)    
    if ip_addr not in users.keys():
        users[ip_addr] = user()
        users[ip_addr].set_random()
    
    
    if request.method == 'POST':    
        if 'guess' in request.POST:
            guess = int (request.POST['guess'])
            print(request.POST['guess'])
            users[ip_addr].data.append(guess)
            users[ip_addr].len += 1
            if guess == users[ip_addr].random:
                users[ip_addr].stat = 1
        elif 'again' in request.POST:
            users[ip_addr].set_random()
            users[ip_addr].data.clear()
            users[ip_addr].stat = 0
            users[ip_addr].len = 0
            

    context = {}
    context['user'] = users[ip_addr]   
    response =  render(request, 'game1.html', context)
    response.set_cookie('username', 'key', max_age=3600)
    return response

