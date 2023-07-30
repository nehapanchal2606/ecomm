from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import *
# from .models import wishlist
from django.urls import reverse
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from account.forms import *
from django.contrib import messages
from django.views.generic.edit import CreateView
# from .models import people, experience, educcation
# Create your views here.


class product_list(TemplateView):

    template_name = 'shop.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(product_list, self).get_context_data()
        context['object_list'] = product.objects.filter()
        context['sub_categories'] = sub_category.objects.filter()
        return context


def EditProfileView(request, id):
    return render(request, 'my-account.html')

    # template_name = 'my-account.html'
    # model = UserProfile
    # form_class = ProfileUpldateForm

    # def get_success_url(self):
    #     return reverse('EditProfileView', kwargs={'pk': self.get_object().id})

    # def get_context_data(self, **kwargs):
    #     context = super(EditProfileView, self).get_context_data(**kwargs)
    #     context['user_form'] = RegistrationForm(
    #         instance=self.request.user)
    #     return context


class PasswordChangeView(LoginRequiredMixin, UpdateView):
    template_name = 'my-account.html'
    model = UserProfile
    form_class = ChangePasswordForm

    def get_success_url(self):
        return reverse('PasswordChangeView', kwargs={'pk': self.get_object().id})

    def get_context_data(self, **kwargs):
        context = super(PasswordChangeView, self).get_context_data(**kwargs)
        context['user_form'] = ChangePasswordForm(
            instance=self.request.user)
        return context


class about_us(TemplateView):
    template_name = 'about-us.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(about_us, self).get_context_data()
        context['object_list'] = product.objects.filter()
        context['sub_categories'] = sub_category.objects.filter()
        return context


class contact(CreateView):
    model = contact_us
    fields = ['user_id', 'enquiry']
    template_name = 'contact.html'

    def get_success_url(self):
        messages.success(self.request, 'Data has been added successfully')
        return reverse('contact')


class single_product(DetailView):
    model = product
    template_name = 'single-product.html'


def shop_list(request, id):
    get_products = product.objects.filter(sub_category_id=id)
    object_list = product.objects.filter()
    sub_categories = sub_category.objects.filter()
    print(get_products)
    return render(request, 'shop-list.html', {'get_products': get_products, 'object_list': object_list, 'sub_categories': sub_categories})


def product_cart(request):
    if request.method == 'POST':
        qua = request.POST.get('qtybutton')
        print(qua)
    return render(request, 'cart.html')


class wishlistView(CreateView):
    template_name = "wishlist.html"
    model = wishlist
    fields = ['product_id', 'user_id']


def addcart(request):
    if request.method == "POST":
        request.POST.get = "quantity"
    else:
        return HttpResponse("Something is wrong")
    return render(request, 'cart.html')

# class AddCartFormView(FormView):
#     template_name = 'shop/product/detail.html'
#     form_class = CartAddProductForm()

#     def get_success_url(self):
#         return reverse('cart:cart_detail')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Your form is already inside context by the name of "form"
#         context['product'] = get_object_or_404(Product, id=product_id, slug=slug, available=True)
#         return context

#     def post(self, request, *args, **kwargs):
#         form = self.get_form()
#         cart = Cart(request)
#         product = get_object_or_404(Product, id=kwargs.get('product_id'))

#         if form.is_valid():
#             cd = form.cleaned_data
#             cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)


def load_header(request):
    return render(request, 'header.html')


# def add_people(request):
#     data = experience()

#     data.company_name = "tata"
#     data.company_url = "https://www.linkedin.com/cmp/tata"
#     data.designation = "IT Department"
#     data.yearofexp = "5 Year"
#     data.subdesigntion = ""
#     data.subyearofexp = ""

#     data.save()

#     return HttpResponse("Data Added")
