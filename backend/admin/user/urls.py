from django.conf.urls import url

from admin.user import views

urlpatterns = [
    url(r'^register', views.users),    url(r'^list', views.users)
]
# r은 정규식임을 알리는 것, ^ : 문자열이나 행의 처음을 의미한다.