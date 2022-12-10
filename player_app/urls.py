from . import views
from django.urls import path
from django.views.generic import TemplateView
urlpatterns=[
    path('add-player/',views.player,name='player'),
    path('list/',views.players,name='players'),
    path('', TemplateView.as_view(template_name="base.html")),     # new

]