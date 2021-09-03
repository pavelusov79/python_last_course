from django.urls import path

from main.views import GoodsView, FormView

app_name = 'main'

urlpatterns = [
    path('', GoodsView.as_view(), name='goods'),
    path('add_goods/', FormView.as_view(), name='add_goods'),
]
