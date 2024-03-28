from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from homeapp.models import ProductModel
from .forms import *
from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView, RedirectView
# Create your views here.


class ShopView(ListView):
    template_name = 'shop.html'
    model = ShopModel
    context_object_name = 'shop'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feat'] = FeaturedModel.objects.all()[:3]
        stars_range = range(1, 6)
        context['stars_range'] = stars_range
        context['banner'] = ShopBanner.objects.all()[:1]
        context['catry'] = Category.objects.all()

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        max_price = self.request.GET.get('max_price')
        fruitlist = self.request.GET.get('fruitlist')
        additional_category = self.request.GET.get('Categories-1')

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        if fruitlist:
            if fruitlist == 'popularity':
                queryset = queryset.order_by('-popularity')
            elif fruitlist == 'organic':
                queryset = queryset.filter(organic=True)
            elif fruitlist == 'fantastic':
                queryset = queryset.filter(fantastic=True)

        if additional_category:
            if additional_category == 'Organic':
                queryset = queryset.filter(Organic=True)
            elif additional_category == 'Fresh':
                queryset = queryset.filter(Fresh=True)
            elif additional_category == 'Sales':
                queryset = queryset.filter(Sales=True)
            elif additional_category == 'Discount':
                queryset = queryset.filter(Discount=True)
            elif additional_category == 'Expired':
                queryset = queryset.filter(Expired=True)

        return queryset


def view_cart(request):
    cart_items = AddCart.objects.all()
    shipping_methods = ShippingMethod.objects.all()

    subtotal = 0
    for item in cart_items:
        if item.product_home:
            item.total_price = item.product_home.price * item.quantity
        elif item.product_shop:
            item.total_price = item.product_shop.price * item.quantity
        subtotal += item.total_price

    selected_shipping_method = None
    shipping_price = 0

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            shipping_method_id = form.cleaned_data['shipping_method']
            selected_shipping_method = ShippingMethod.objects.get(id=shipping_method_id)
            shipping_price = selected_shipping_method.price
            # Calculate total price including shipping
            total_price = subtotal + shipping_price

    else:
         form = CheckoutForm()

    total_price = subtotal + shipping_price

    return render(request, 'cart.html', {'cart_items': cart_items, 'subtotal': subtotal, 'form': form, 'total_price': total_price})


def checkout(request):
    cart_items = AddCart.objects.all()
    shipping_methods = ShippingMethod.objects.all()
    payment_methods = PaymentMethod.objects.all()

    subtotal = 0
    for item in cart_items:
        if item.product_home:
            item.total_price = item.product_home.price * item.quantity
        elif item.product_shop:
            item.total_price = item.product_shop.price * item.quantity
        subtotal += item.total_price

    selected_shipping_method = None
    shipping_price = 0

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            shipping_method_id = form.cleaned_data['shipping_method']
            selected_shipping_method = ShippingMethod.objects.get(id=shipping_method_id)
            shipping_price = selected_shipping_method.price
            # Calculate total price including shipping
            total_price = subtotal + shipping_price

            # Save order to database
            order = Order(
                user=request.user,
                shipping_method=selected_shipping_method,
                payment_method=form.cleaned_data['payment_method'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city'],
                country=form.cleaned_data['country'],
                postcode=form.cleaned_data['postcode'],
                mobile=form.cleaned_data['mobile'],
                email=form.cleaned_data['email'],
                order_notes=form.cleaned_data['order_notes'],
                total_price=total_price
            )
            order.save()

            for item in cart_items:
                order.cart_items.add(item)

            # Clear cart items after placing order
            cart_items.delete()

            return redirect('checkout')  # Redirect to success page after placing order

    else:
        form = CheckoutForm()

    # Calculate total price including shipping
    total_price = subtotal + shipping_price

    context = {
        'form': form,
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping_methods': shipping_methods,
        'payment': payment_methods,
        'total_price': total_price,
        'selected_shipping_method': selected_shipping_method,
    }

    return render(request, 'chackout.html', context)


# def checkout(request):
#     cart_items = AddCart.objects.all()
#     shipping_methods = ShippingMethod.objects.all()
#     payment_methods = PaymentMethod.objects.all()
#
#     subtotal = 0
#     for item in cart_items:
#         if item.product_home:
#             item.total_price = item.product_home.price * item.quantity
#         elif item.product_shop:
#             item.total_price = item.product_shop.price * item.quantity
#         subtotal += item.total_price
#
#     selected_shipping_method = None
#     shipping_price = 0
#
#     if request.method == 'POST':
#         form = CheckoutForm(request.POST)
#         if form.is_valid():
#             shipping_method_id = form.cleaned_data['shipping_method']
#             selected_shipping_method = ShippingMethod.objects.get(id=shipping_method_id)
#             shipping_price += selected_shipping_method.price
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             address = form.cleaned_data['address']
#             city = form.cleaned_data['city']
#             country = form.cleaned_data['country']
#             postcode = form.cleaned_data['postcode']
#             mobile = form.cleaned_data['mobile']
#             email = form.cleaned_data['email']
#             shipping_method = form.cleaned_data['shipping_method']
#             payment_method = form.cleaned_data['payment_method']
#             order_notes = form.cleaned_data['order_notes']
#
#             for item in cart_items:
#                 item.order_first_name = first_name
#                 item.order_last_name = last_name
#                 item.order_address = address
#                 item.order_city = city
#                 item.order_country = country
#                 item.order_postcode = postcode
#                 item.order_mobile = mobile
#                 item.order_email = email
#                 item.shipping_method = shipping_method
#                 item.payment_method = payment_method
#                 item.order_notes = order_notes
#                 item.save()
#
#             cart_items.delete()
#
#             return redirect('order_placed')
#
#     else:
#         form = CheckoutForm()
#
#     total_price = subtotal + shipping_price
#     print('aaa', subtotal, 'selected', selected_shipping_method, 'method', shipping_methods, 'price', shipping_price)
#
#     context = {
#         'form': form,
#         'cart_items': cart_items,
#         'subtotal': subtotal,
#         'payment': payment_methods,
#         'total_price': total_price,
#         'shipping_methods': shipping_methods,
#         'selected_shipping_method': selected_shipping_method,
#     }
#
#     return render(request, 'chackout.html', context)


def update_quantity(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        action = request.POST.get('action')

        cart_item = AddCart.objects.get(pk=product_id)

        if action == 'increment':
            cart_item.quantity += 1
        elif action == 'decrement':
            if cart_item.quantity > 1:
                cart_item.quantity -= 1

        cart_item.save()
        messages.success(request, 'Cart updated successfully.')
        return redirect('view_cart')


def remove_from_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        cart_item = AddCart.objects.get(pk=product_id)
        cart_item.delete()
        messages.success(request, 'Item removed from cart.')
        return redirect('view_cart')


class AddToCartView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'view_cart'

    def get_redirect_url(self, *args, **kwargs):
        product_id = self.kwargs.get('product_id')
        product_type = self.kwargs.get('product_type')

        try:
            if product_type == 'shop':
                product = ShopModel.objects.get(id=product_id)
            elif product_type == 'home':
                product = ProductModel.objects.get(id=product_id)

            cart_item, created = AddCart.objects.get_or_create(product_shop=product if product_type == 'shop' else None,

                                                               product_home=product if product_type == 'home' else None)

        except (ShopModel.DoesNotExist, ProductModel.DoesNotExist):
            pass

        return reverse(self.pattern_name)

