
from django.contrib import admin
from django.urls import path

from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', todo),
    path('delete-todo/<int:a>/', delete),
    path('login/' , login_view),
    path('logout/', logout_view)
]

