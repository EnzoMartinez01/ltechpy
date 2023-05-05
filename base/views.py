from django import forms
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView

from .models import *


class ServiceList(ListView):
    model = Servicios
    template_name = 'base/service/list.html'
    context_object_name = 'servicios'

class ServiceDetail(DetailView):
    model = Servicios
    template_name = 'base/service/service_detail.html'
    context_object_name = 'servicio'

class CategoryList(ListView):
    model = Category
    second_model = Cliente
    template_name = 'base/service/list_category.html'
    context_object_name = 'categorias'

    def get_context_data(self, *args, **kwargs):
        category = Category.objects.all()
        clientes = Cliente.objects.all()
        return {'clientes': clientes, 'categorias': category}

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Servicios
        fields = ['name', 'description', 'price', 'category', 'image']
    
    def clean_name(self):
        name = self.cleaned_data('name')
        if Servicios.objects.filter(name=name).exists():
            raise forms.ValidationError('Servicio with this name already exists')
        return name

class ServiceCreate(CreateView):
    model = Servicios
    form_class = ServiceForm
    fields = ['name', 'description', 'price', 'category']
    template_name = 'base/service/service_create.html'
    success_url = '/'

class Index(TemplateView):
    template_name = 'base/service/index.html'

class AboutMe(TemplateView):
    template_name = 'base/service/about_me.html'

class Repo(TemplateView):
    template_name = 'base/service/repo.html'

def clienteCreate(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        description = request.POST.get('description')
        imagencli = request.POST.get('imagencli')
        cliente = Cliente.objects.create(
            name=name,
            last_name=last_name,
            email=email,
            telephone=telephone,
            description=description,
            imagencli=imagencli,
        )
        return redirect('base:index')
    return render(request, 'base/service/contact.html')