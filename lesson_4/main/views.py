from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import ListView, CreateView

from main.forms import GoodsForm
from main.models import Goods


class GoodsView(ListView):
    model = Goods


def save_good_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            goods = Goods.objects.all()
            data['html_goods_list'] = render_to_string('main/goods_list.html', {'object_list': goods})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


class FormView(CreateView):
    template_name = 'main/goods_create.html'
    form_class = GoodsForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        view = save_good_form(request, self.form_class, self.template_name)
        return view

    def post(self, request, *args, **kwargs):
        view = save_good_form(self.request.POST, self.form_class, 'main/goods_list.html')
        return view





