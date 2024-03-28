from django.shortcuts import render, redirect, get_object_or_404
from django.template import context
from .models import *
from shopapp.models import FeaturedModel, ShopBanner
from django.views.generic.edit import FormMixin
from django.views.generic import CreateView, DetailView
from .forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse, reverse_lazy
# Create your views here.


class HomeView(CreateView):
    template_name = 'index.html'
    form_class = BookingForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        homea = HomeModel.objects.filter(is_active=True)
        if len(homea) > 0:
            context['home'] = homea[0]
        else:
            homea = None
        context['catry'] = CategoryModel.objects.all()
        category = self.request.GET.get('category')
        if category:
            context['fruits'] = ProductModel.objects.filter(type=category)
        else:
            context['fruits'] = ProductModel.objects.all()
        context['vegetab'] = ProductModel.objects.filter(type='1')
        context['best'] = ProductModel.objects.filter(is_exclusive=False)[:6]
        context['exbest'] = ProductModel.objects.filter(is_exclusive=True)[:4]
        stars_range = range(1, 6)
        context['stars_range'] = stars_range
        context['features'] = FeaturesModel.objects.all()
        context['featurs'] = FeatursModel.objects.all()
        context['fact'] = FactModel.objects.all()
        context['reviews'] = ReviewModel.objects.all()
        bannerr = BannerModel.objects.filter(is_active=True)
        if len(bannerr) > 0:
            context['banner'] = bannerr[0]
        else:
            bannerr = None

        return context


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            # review.name = request.user.username
            review.stars = form.cleaned_data['stars']
            review.save()
            return redirect('testimonial')
    else:
        form = ReviewForm()
    return render(request, 'contact.html', {'form': form})


def review_success(request):
    reviews = ReviewModel.objects.all()
    return render(request, 'testimonial.html', {'reviews': reviews})


class DetailView(FormMixin, DetailView):
    template_name = 'shop-detail.html'
    model = ProductModel
    context_object_name = 'detail'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stars_range = range(1, 6)
        context['stars_range'] = stars_range
        context['feat'] = FeaturedModel.objects.all()[:6]
        context['vegetab'] = ProductModel.objects.filter(type=1)
        context['banner'] = ShopBanner.objects.all()[:1]

        return context

    def get_success_url(self):
        self.object = self.get_object()
        comment = self.object.comment.last()
        if comment:
            return reverse_lazy('food_slug', kwargs={'pk': comment.post.pk})
        else:
            return

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.name = self.request.user.username
        self.object.post = self.get_object()
        self.object.save()
        stars = form.cleaned_data['stars']
        self.object.stars = stars
        self.object.save()
        return super().form_valid(form)


class RegView(CreateView):
    template_name = 'regis.html'
    form_class = RegForm
    success_url = reverse_lazy('home')


class LoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginUserForm

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')