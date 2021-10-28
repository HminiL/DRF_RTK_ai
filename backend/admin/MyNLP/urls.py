from django.conf.urls import url
from admin.MyNLP import views

urlpatterns = {
    url(r'imdb_process',views.imdb_process),
    url(r'web_scraping',views.naver_process),
    url(r'model_fit',views.naver_process),

}
