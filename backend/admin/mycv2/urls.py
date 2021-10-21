from django.conf.urls import url
from admin.mycv2 import views

urlpatterns = {
    url(r'lena',views.lena),
    url(r'girl',views.girl),
    url(r'face_detect', views.face_detect),

}
