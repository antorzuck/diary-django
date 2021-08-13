from django.contrib import admin
from django.urls import path
from accounts.views import *
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('signin/', home, name='signin'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('show', show, name='show'),
    path('add', add, name='add'),
    path('logout', logout, name='logout'),
    path('search', search, name='search')
]
