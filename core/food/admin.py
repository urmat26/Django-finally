from django.contrib import admin

from .models import Product, Category

from django.contrib import admin
from .models import Product, Category


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     exclude = ("author",)
#     list_display = ("name", "price", "category", "author")
#
#     def save_model(self, request, obj, form, change):
#         if not obj.pk:
#             obj.author = request.user
#         super().save_model(request, obj, form, change)
#
#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ("name",)