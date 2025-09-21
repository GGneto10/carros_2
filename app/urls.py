"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from carros.views import CarrosListView, CarrosDetailView, AddCarroCreateView, AtualizarCarroUpdateView, DeletarCarroDeleteView, HomeView
from motos.views import MotosListView, MotosDetailView, AddMotoCreateView, AtualizarMotoUpdateView, DeletarMotoDeleteView
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from contas.views import cadastro_view, login_view, logout_view

urlpatterns = [
    path('', RedirectView.as_view(url='home/')),
    path('home/', HomeView.as_view(), name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='deslogar'),
    path('admin/', admin.site.urls),

    path('lista/', CarrosListView.as_view(), name='lista_carros'),
    path('lista/motos/', MotosListView.as_view(), name='lista_motos'),
    path('detalhes/motos/<int:pk>/', MotosDetailView.as_view(), name='detalhes_motos'),
    path('carros/detalhes/<int:pk>/', CarrosDetailView.as_view(), name='detalhes_carros'),
    path('add/carros/', AddCarroCreateView.as_view(), name='add_carro'),
    path('add/motos/', AddMotoCreateView.as_view(), name='add_moto'),
    path('cadastro/', cadastro_view, name='cadastro'),
    path('carros/<int:pk>/update/', AtualizarCarroUpdateView.as_view(), name='atualizar_carro'),
    path('motos/<int:pk>/update/', AtualizarMotoUpdateView.as_view(), name='atualizar_moto'),
    path('carros/<int:pk>/delete/', DeletarCarroDeleteView.as_view(), name='deletar_carro'),
    path('motos/<int:pk>/delete/', DeletarMotoDeleteView.as_view(), name='deletar_moto'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
