from django.http import HttpResponse

def showFriendsList(request):
    return HttpResponse("List of your friends")


def addFriend(request):
    return HttpResponse('add a new friend in a list')


def removeFriend(response):
    return HttpResponse('Friend XXX was removed from a list')
