from django.views.generic import ListView, CreateView

from main.forms import GoodsForm
from main.models import Goods


class GoodsView(ListView):
    model = Goods


class FormView(CreateView):
    template_name = 'main/goods_create.html'
    form_class = GoodsForm
    success_url = '/'
