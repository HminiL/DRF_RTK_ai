from django.conf.urls import url

from admin.user import views

urlpatterns = [
    url(r'^join', views.users), # name='users' URL 공백일때 처리하는 이름
    url(r'^login', views.login),
    url(r'^delete/<slug:id>', views.remove),    # /<slug:id> 자바의 /{id}@pathvariable과 비슷한 역할
]
# r은 정규식임을 알리는 것, ^ : 문자열이나 행의 처음을 의미한다.