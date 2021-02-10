from django.http import HttpResponse


def showProfile(request):
    return HttpResponse('This is the user profile')


def editProfile(request):
    return HttpResponse('editing profile')


def deleteProfile(request):
    return HttpResponse('delinting profile')
