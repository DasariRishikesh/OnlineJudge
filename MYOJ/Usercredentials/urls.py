from django.urls import path
#from . import admin
from . import views

urlpatterns = [
    #path("admin/", admin.site.urls),
    path("", views.index, name  = "index"),
    path("login/", views.login, name = "login"),
    path('register/', views.register_view, name='register'),
]
