from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, FormView

from account.models import UserProfile
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.shortcuts import render
from django.views.generic import ListView
from client.models import sub_category, product


class HomeView(ListView):
    model = UserProfile
    get_context_data = 'user'
    template_name = 'base.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['object_list'] = UserProfile.objects.filter()
        context['sub_categories'] = sub_category.objects.filter()
        context['product_lists'] = product.objects.all()
        return context


class RegistrationView(CreateView):
    template_name = 'account/signup.html'
    success_url = '/'
    form_class = RegistrationForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        super().form_valid(form)

        user, created = User.objects.get_or_create(
            username=self.object.username,
            first_name=self.object.first_name,
            last_name=self.object.last_name,
            email=self.object.email
        )
        print(created)
        user.set_password(self.request.POST.get('password'))
        user.is_active = True
        user.save()
        self.object.user = user
        self.object.save()

        messages.success(self.request,
                         "User register successfully. Please varify your email for login"
                         )
        return redirect('login')


class LoginView(FormView):
    template_name = "account/signin.html"
    form_class = LoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        messages.success(self.request, "User logged in successfully.")
        return redirect("home")


class LogoutView(FormView):
    def get(self, *args, **kwargs):
        logout(self.request)
        messages.success(self.request, "User logged out successfully.")
        return redirect('/')
