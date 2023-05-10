from django.urls import path
from.import views
urlpatterns = [
    
    path('',views.app1),
    path('b/',views.bigdata),
    path('da/',views.dataanalysis),
    path('dl/',views.deep_learning),
    
    
]