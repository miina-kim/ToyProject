from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("mainapp.urls")), # 기본 url -> mainapp
    path("common/", include("common.urls")),
]