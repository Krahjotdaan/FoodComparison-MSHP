"""food_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from App import views
from food_django import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('food/creation/', views.food_creation, name='food_creation'),
    path('food/', views.food_list_page, name='food_list'),
    path('food/statistics/', views.statistics, name='food_statistics'),
    path('food/item/', views.food_item_page, name='food_item'),
    path('profile/page.html', views.profile_page, name='profile_page'),
    path("profile/page_deleted.html", views.delete_user, name="remove_user"),
    path('complaint/list/', views.complaint_list, name='complaint_list'),
    path('complaint/add/', views.complaint_add, name='complaint_add'),
    path('like/page/', views.like_page, name='like_page'),
    path('like/add/', views.add_like, name='add_like'),
    path('comprasion/page/', views.comprasion_page, name='comprasion_page'),
    path('comprasion/add/', views.add_comprasion, name='add_comprasion'),
    path('comments/', views.comments_page, name='comments_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
