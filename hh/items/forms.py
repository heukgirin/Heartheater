from django import forms

class FormAdd(forms.Form):
    article = forms.CharField(max_length=20, label='아티클')
    category = forms.CharField(max_length=20, label='카테고리')
    brand = forms.CharField(max_length=20, label='브랜드')
    name_model = forms.CharField(max_length=20, label='모델명')
    name_kor = forms.CharField(max_length=50, label='제품명(한글)')
    name_eng = forms.CharField(max_length=50, label='제품명(영문)')
    price_sale = forms.IntegerField(label='판매가격')
    price_order = forms.IntegerField(label='입고가격')
    delivery_price = forms.IntegerField(label='배송비')
    delivery_send = forms.CharField(max_length=100, label='배송주체')
    delivery_return = forms.CharField(max_length=100, label='교환/반품주체')
    company_make = forms.CharField(max_length=20, label='제조회사')
    company_sale = forms.CharField(max_length=20, label='판매회사')
    company_as = forms.CharField(max_length=20, label='AS책임자')
    inform = forms.CharField(label='추가정보')
