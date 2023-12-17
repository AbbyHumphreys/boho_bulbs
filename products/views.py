from django.shortcuts import render, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, LampType, Colour

def all_products(request):
    """ A view to show all products, including sorting and searching """

    products = Product.objects.all()
    query = None
    lamptype = None
    colour = None

    if request.GET:

        if 'lamptype' in request.GET:
            lamptype = request.GET['lamptype'].split(',')
            products = products.filter(lamptype__name__in=lamptype)
            lamptype = LampType.objects.filter(name__in=lamptype)

        if 'colour' in request.GET:
            colour = request.GET['colour'].split(',')
            products = products.filter(colour__name__in=colour)
            colour = Colour.objects.filter(name__in=colour)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter any search criteria")
                return redirect(reverse('products'))
            
            queries = Q(lamptitle__icontains=query) | Q(description1__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_lamptype': lamptype,
        'current_colour':colour,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)