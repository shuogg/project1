#coding=utf-8
from django.contrib.auth import views as auth_views
from django.conf.urls import patterns, include, url
from django.contrib import admin
from p1.views import *
from django.contrib.auth.views import *
from p1.v1 import *
admin.autodiscover()
from django.conf.urls import url, include
from rest_framework import routers
from p1.models import *
from rest_framework.urlpatterns import format_suffix_patterns
from api import views as aviews
from api import vserch  as sviews


#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'devices', views.DevicesViewSet)



urlpatterns = patterns('',

    #url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/search/User/$', sviews.UserSearch.as_view()),
    url(r'^api/search/Accounts/$', sviews.AccountsSearch.as_view()),
    url(r'^api/v1/User/$', aviews.UserList.as_view()),
    url(r'^api/v1/User/(?P<pk>[0-9]+)/$', aviews.UserDetail.as_view()),
    url(r'^api/v1/(?P<TbName>\w+)/$',aviews.TbNameList.as_view()),
    url(r'^api/v1/(?P<TbName>\w+)/(?P<pk>[0-9]+)/$',aviews.TbNameDetail.as_view()),
    url(r'^accounts/$', aviews.AccountsList.as_view()),
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login$', login_v1),
    url(r'^logout$', logout_v1),
    url(r'^change$', change_v1),
    url(r'^profile$',profile),
    url(r'^t1$',t1),
    url(r'^register$',register_v1),
    url(r'^check_user$',check_user),
    url(r'^check_code$',check_code),
    url(r'^upload/$',upload),
)

urlpatterns = format_suffix_patterns(urlpatterns)
