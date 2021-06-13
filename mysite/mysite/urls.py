"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.views.static import serve

from django1 import views
from django1.views import LoginRegister

from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from mysite import settings
from mysite.settings import MEDIA_ROOT

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   #permission_classes=(permissions.AllowAny,),
)


router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(
        r"swagger(?P<format>\.json|\.yaml)",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    # path("api/login/", views.login),
    path('', TemplateView.as_view(template_name="index.html")),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # path("register/", LoginRegister.register)
]
# +list(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

router.register('token', views.TokenInfo)
router.register('login_register', views.LoginRegister)
router.register('user', views.UserInfoView)
router.register('upload', views.Upload)
router.register('articleTag', views.ArticleTagInfo)
# router.register('circle', views.CircleInfo)
# router.register('comment', views.BookCommentInfo)
router.register('search', views.Search)
router.register('discuss', views.DiscussTagInfo)
# router.register('note', views.NoteInfo)
urlpatterns += path('api/', include(router.urls)),

# urlpatterns = [
#     url(r'^media/(?P<path>.*)$', {"document_root": MEDIA_ROOT})
# ]
