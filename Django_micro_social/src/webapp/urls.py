from django.urls import path
from django.http import HttpResponse
import sys, os
sys.path.append('..')
from src.users import friends
from src.users import profile



def homePage(request):
    return HttpResponse('Hello')


urlpatterns = [
    path('user/profile', profile.showProfile),
    path('user/profile/edit', profile.editProfile),
    path('user/profile/delete', profile.deleteProfile),
    path('user/friends', friends.showFriendsList),
    path('user/friends/add', friends.addFriend),
    path('user/friends/remove', friends.removeFriend),
    path('', homePage)

]