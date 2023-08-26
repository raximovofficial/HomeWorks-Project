# from django.urls import path
# from .views import WeekdaysUzView, WeekdaysEnView, WeekdaysRuView

# urlpatterns = [
#     path('', WeekdaysUzView, name='weekdays/uz'),
#     path('', WeekdaysEnView, name='weekdays/en/'),
#     path('', WeekdaysRuView, name='weekdays/ru'),
#     # path('', WeekdaysUzView, name='weekdays-uz'),
#     # path('', WeekdaysEnView, name='weekdays-en'),
#     # path('weekdays/ru/', WeekdaysRuView, name='weekdays-ru'),
# ]

from django.urls import path
from . import views

app_name = 'HomeWorks'

urlpatterns = [
    path('weekdays/<str:language>/', views.weekdays_view, name='weekdays'),
]