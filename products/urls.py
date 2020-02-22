from django.urls import path
from .views import List, WriteCont, WriteAttr

urlpatterns = [
    path('', List.as_view()),
    path('list', List.as_view()),
    path('write/cont/', WriteCont.as_view()),
    path('write/attr/', WriteAttr.as_view()),
]
