from django.http import HttpRequest
from django.shortcuts import render
from .models import usersText

def HomePage(request):
    return render(request, "insertData.html")

def usersList(request):
    if request.method == 'POST':
        userName = request.POST.get('name')
        userText = request.POST.get('text')
        usersText.objects.create(userName = userName, userText = userText)

    mydb = usersText.objects.all()
    context = {
        'mydb' : mydb,
    }

    return render(request, "usersList.html", context)

def usersDetails(request, userNum):
    dbbase = usersText.objects.all()
    for i in dbbase: 
        if i.userID == userNum: 
            name = i.userName
            text = i.userText

    context = {
        'userID' : userNum,
        'name' : name,
        'text' : text,
    }
    return render(request, "usersDetails.html", context)

def savedDataUsers(request):
    if 'Delete' in request.POST: 
        result = request.POST.get('Delete')
        usersText.objects.filter(userID = result).delete()
        result = 'delete'
    elif 'Save' in request.POST: 
        result = request.POST.get('Save')
        text = request.POST.get('text')
        usersText.objects.filter(userID = result).update(userText = text)
        result = 'saved'

    context = {
        'testID' : result
    }

    return render(request, "savedDataUsers.html", context)