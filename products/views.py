from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, LampType, Colour, Brand, IpRating
from .forms import ProductForm

def all_products(request):
    """ A view to show all products, including sorting and searching """

    products = Product.objects.all()
    query = None
    lamptype = None
    colour = None
    brand = None
    iprating = None
    sort = None
    direction = None
    unique_colours = Colour.objects.all()
    unique_types = LampType.objects.all()
    unique_ipratings = IpRating.objects.all()
    unique_brands = Brand.objects.all()

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'brand':
                sortkey = 'brand__name'
            if sortkey == 'lamptype':
                sortkey = 'lamptype__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction =='desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'lamptype' in request.GET:
            lamptype = request.GET['lamptype'].split(',')
            products = products.filter(lamptype__name__in=lamptype)
            lamptype = LampType.objects.filter(name__in=lamptype)

        if 'colour' in request.GET:
            colour = request.GET['colour'].split(',')
            products = products.filter(colour__name__in=colour)
            colour = Colour.objects.filter(name__in=colour)

        if 'brand' in request.GET:
            brand = request.GET['brand'].split(',')
            products = products.filter(brand__name__in=brand)
            brand = Brand.objects.filter(name__in=brand)
        
        if 'iprating' in request.GET:
            iprating = request.GET['iprating'].split(',')
            products = products.filter(iprating__name__in=iprating)
            iprating = IpRating.objects.filter(name__in=iprating)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter any search criteria")
                return redirect(reverse('products'))
            
            queries = Q(lamptitle__icontains=query) | Q(description1__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    sorting_name = {
        'price_desc': 'Price, high to low',
        'price_asc': 'Price, low to high',
        'lamptype_desc': 'Lamp Type, A-Z',
        'lamptype_asc': 'Lamp Type, Z-A',
        'brand_asc': 'Brand, A-Z',
        'brand_desc': 'Brand Type, Z-A',
    }
    
    current_sorting_name = ''
    if current_sorting in sorting_name:
        current_sorting_name = sorting_name[current_sorting]

    context = {
        'products': products,
        'search_term': query,
        'current_lamptype': lamptype,
        'current_lamptypes': unique_types,
        'current_colour': colour,
        'current_colours': unique_colours,
        'current_brand': brand,
        'current_brands': unique_brands,
        'current_iprating': iprating,
        'current_ipratings': unique_ipratings,
        'current_sorting': current_sorting,
        'current_sorting_name': current_sorting_name,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.lamptitle}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

