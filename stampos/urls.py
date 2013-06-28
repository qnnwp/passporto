from django.conf.urls import *
from views.ui import home
from views.badges import BadgeView

urlpatterns = patterns('stampos.views',
    (r'^$', home),
    (r'^api/v1/badges/?$', BadgeView().run),
)

