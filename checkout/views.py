from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LRSjYGg4BpUsp5D5kJqxadDjW64t7xzSQshpH9UBEbzHHYK71gHmt2L6A6QNwrCWS3LMiZHEqdguKNnj8fV681P00dxo6Pztx',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
