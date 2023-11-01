from django.urls import path
from.import views

urlpatterns=[
    # path("",views.index,name="index")
    # path('',views.toLogin_view)# 这样，就将127.0.0.1:8000/polls/这个url和叫做login.html的函数关联起来。
    path('',views.tempera_here)
]