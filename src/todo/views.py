from django.http import HttpResponse 
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Item
import json

#todos = ['Write code', 'Create commit', 'Push code']


@login_required
def indexPageView(request):

    todos = Item.objects.filter(owner=request.user)
    return render(request, 'pages/index.html', {'items': todos})


#@login_required
#def todoView(request):
#    todos = Item.objects.filter(owner=request.user)
#    return JsonResponse({'todos' : [{'name': i} for i in todos]})


@csrf_exempt
def addTodo(request):

    if request.method == 'POST':
        note = request.POST.get('note')
        currentUser = request.user

        newNoteEntry = Item.objects.create(owner=currentUser, note=note)
        newNoteEntry.save()
        
    return redirect('/')

@login_required
def delete(request):
    f = Item.objects.get(pk=request.POST.get('id'))
    if request.user.id != f.owner.id:
        return redirect('/')
    f.delete()
    return redirect('/')