from django.conf.urls import url
from admin.calculator import views

urlpatterns = {
    url(r'calculator',views.calculator),

}
