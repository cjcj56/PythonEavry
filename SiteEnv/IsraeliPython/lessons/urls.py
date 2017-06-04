"""IsraeliPython URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views

app_name = 'lessons'
urlpatterns = [
    url(r'^(?P<lesson_module_name>basic)/', include([
        url(r'^$',views.render_index, name='index'),
        url(r'^index/$',views.render_index, name='index'),
        url(r'^(?P<lesson_num>\d+)/', include([
            url(r'^(?P<lesson_type>lesson)$', views.render_lesson, name='lesson'),
            url(r'^(?P<lesson_type>practice)/$', views.render_lesson, name='practice'),
            url(r'^(?P<lesson_type>solution)/$', views.render_lesson, name='solution'),
        ])),
    ])),
]
