from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm #この文を新たに追記
# from .forms import HelloForm
from django.views.generic import ListView
from django.views.generic import DetailView
from .forms import FindForm #この文を追記
from django.core.paginator import Paginator

class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend

def index(request, num=1):
    data = Friend.objects.all()
    page = Paginator(data, 3)
    params = {
        'title': 'Hello',
        'message':'',
        'data': page.get_page(num),
    }
    return render(request, 'telme/index.html', params)

# create model
def create(request):
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/telme')
    params = {
        'title': 'Hello',
        'form': FriendForm(),
    }
    return render(request, 'telme/create.html', params)

def edit(request, num):
    obj = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/telme')
    params = {
        'title': 'Hello',
        'id':num,
        'form': FriendForm(instance=obj),
    }
    return render(request, 'telme/edit.html', params)

def find(request):
    
    if (request.method == 'POST'):
        msg = request.POST['find']
        form = FindForm(request.POST)
        sql = 'select * from telme_friend'
        if (msg != ''):
            sql += ' where ' + msg
        data = Friend.objects.raw(sql)
        msg = sql
    else:
        msg = 'search words...'
        form = FindForm()
        data = 'dumy'
    #     data =Friend.objects.all()

    params = {
        'title': 'Hello',
        'message': msg,
        'form':form,
        'data':data,
    }
    return render(request, 'telme/find.html', params)


