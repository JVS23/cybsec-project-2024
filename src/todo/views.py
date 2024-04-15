from django.http import HttpResponse 
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Item
import json

msg = "Hello authenticated user who's definitely logged in!"


@login_required
def indexPageView(request):
    todos = Item.objects.filter(owner=request.user)
    return render(request, 'pages/index.html', {'items': todos})


# Should be accessible only by logged in users, remove comment from line 20 to enable correct behavior
# @login_required
def userGreetingView(request):
    owner=request.user
    return render(request, 'pages/greeting.html', {'msg': msg, 'visitor': owner})


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

    # The following codeblock is an simplified validity check, by uncommenting it
    # you can make sure that only the "jvs" user can delete items even if they see the button
    
    #if request.user.username != 'jvs':
    #    return redirect('/')


    f = Item.objects.get(pk=request.POST.get('id'))
    if request.user.id != f.owner.id:
        return redirect('/')
    f.delete()
    return redirect('/')


# Showcase a SQL injection vulnerability
@login_required
def getItemsVulnerable(request):
    owner_id = request.GET.get('owner', '')


    query = "SELECT * FROM todo_item WHERE owner_id = '%s'" % owner_id
    items = Item.objects.raw(query)

    # You can fix the injection by using the safe way to process queries below,
    # and commenting out the previous two lines

    #items = Item.objects.filter(owner=owner_id)

    itemsList = []
    for item in items:
        itemsList.append(item.note)
    return JsonResponse(itemsList, safe=False)