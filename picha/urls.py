from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from frontend.views import home_page
from photos.views import PhotoView
from feedback.views import FeedbackView


import frontend.urls
import photos.urls

urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^photos/', include(photos.urls), name='photos'),
    url('', include(frontend.urls)),
    url(r'^feedback/$', FeedbackView.as_view(), name="feedback"),

    path('admin/', admin.site.urls),
]
#     url(r'^$', PhotoView.as_view(), name="home"),
# url(r'^feedback/$', FeedbackView.as_view(), name="feedback"),
