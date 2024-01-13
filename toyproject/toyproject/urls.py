from django.contrib import admin
from django.urls import include, path
from mainapp.views import base_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("mainapp.urls")), # 기본 url -> mainapp
    path("common/", include("common.urls")),
    # path("", base_views.qna_main, name='mainapp'),
]