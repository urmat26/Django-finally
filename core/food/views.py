from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Category, Product
# from .forms import PhotoForm

def index(request):
    return render(request, 'food/index.html')

def about(request):
    return render(request, 'food/about.html')

def contact(request):
    return render(request, 'food/contact.html')



def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    q = request.GET.get('q')
    category_id = request.GET.get('category')

    if q:
        products = products.filter(name__icontains=q)

    if category_id:
        products = products.filter(category_id=category_id)

    return render(request, 'food/shop.html', {
        'products': products,
        'categories': categories
    })

# @login_required(login_url='login')
# def add_photo_to_category(request, category_id):
#     category = get_object_or_404(Category, id=category_id)
#     if request.method == 'POST':
#         form = PhotoForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_photo = form.save(commit=False)
#             new_photo.category = category
#             # author в базе сейчас строка — подставим имя вошедшего пользователя
#             new_photo.author = request.user.username
#             new_photo.save()
#     return redirect('category_gallery', category_id=category_id)
#
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()          # создаёт пользователя
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'tour/signup.html', {'form': form})