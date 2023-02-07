from django.urls import path
from . import views
urlpatterns=[
     path('',views.fun,name='fun'),
     path('orange/<int:orange_id>',views.org_details,name='org_details')

]