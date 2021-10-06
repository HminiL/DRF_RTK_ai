from django.conf.urls import url
from admin.crime import views

urlpatterns = {
    url(r'crime-model',views.create_crime_model),
    url(r'police-position',views.create_police_position)
}