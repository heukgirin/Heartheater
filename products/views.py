from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from .models import Attr, Cont
from .forms import FormAdd

class List(View):
    def get(self, request):
        product_list = Attr.objects.order_by('article').all()
        group_list = Cont.objects.values_list('group', flat=True)
        context = {'product_list': product_list, 'group_list': group_list}
        return render(request, 'index.html', context)

class WriteCont(View):
    def get(self, request):
        context = {'product_list': product_list}
        return render(request, 'write_attr.html', context)

class WriteAttr(View):
    def post(self, request):
        form = FormAdd(request.POST)
        if form.is_valid():
            obj = Attr(
                group = form.data['group'],
                article = form.data['article'],
                category = form.data['category'],
                brand = form.data['brand'],
                name_model = form.data['name_model'],
                name_kor = form.data['name_kor'],
                name_eng = form.data['name_eng'],
                price_sale = form.data['price_sale'],
                price_order = form.data['price_order'],
                delivery_price = form.data['delivery_price'],
                delivery_send = form.data['delivery_send'],
                delivery_return = form.data['delivery_return'],
                company_make = form.data['company_make'],
                company_sale = form.data['company_sale'],
                company_as = form.data['company_as'],
                # company_as = form.data['inform']
            )
            obj.save()
            return HttpResponseRedirect('/products/')

    def get(self, request):
        forms = FormAdd()
        exist_list = Attr.objects.values_list('article', flat=True)
        context = {'exist_list': exist_list, 'forms' : forms}
        return render(request, 'input.html', context)
