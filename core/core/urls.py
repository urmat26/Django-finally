
from django.contrib import admin
from django.urls import path, include
from django.urls import path
# from django.contrib.auth import views as auth_views
from food import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  # <- вот здесь имя index
    path('shop/', views.shop, name='shop'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('admin/', admin.site.urls),
    path('', include('food.urls')),
    # path('login/',  auth_views.LoginView.as_view(template_name='tour/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('signup/', views.signup, name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

