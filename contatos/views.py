from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Contato
from .forms import ContatoForm

class ContatoListView(LoginRequiredMixin, ListView):
    model = Contato
    template_name = 'contatos/lista.html'
    context_object_name = 'contatos'
    paginate_by = 10

    def get_queryset(self):
        queryset = Contato.objects.filter(usuario=self.request.user)
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(nome__icontains=search) | 
                Q(telefone__icontains=search) | 
                Q(email__icontains=search)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

class ContatoDetailView(LoginRequiredMixin, DetailView):
    model = Contato
    template_name = 'contatos/detail.html'
    context_object_name = 'contato'

    def get_queryset(self):
        return Contato.objects.filter(usuario=self.request.user)

class ContatoCreateView(LoginRequiredMixin, CreateView):
    model = Contato
    form_class = ContatoForm
    template_name = 'contatos/form.html'
    success_url = reverse_lazy('contato_list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class ContatoUpdateView(LoginRequiredMixin, UpdateView):
    model = Contato
    form_class = ContatoForm
    template_name = 'contatos/form.html'
    success_url = reverse_lazy('contato_list')

    def get_queryset(self):
        return Contato.objects.filter(usuario=self.request.user)

class ContatoDeleteView(LoginRequiredMixin, DeleteView):
    model = Contato
    template_name = 'contatos/confirm_delete.html'
    success_url = reverse_lazy('contato_list')
    context_object_name = 'contato'

    def get_queryset(self):
        return Contato.objects.filter(usuario=self.request.user)
