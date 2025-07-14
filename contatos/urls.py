from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContatoListView.as_view(), name='contato_list'),
    path('contato/<int:pk>/', views.ContatoDetailView.as_view(), name='contato_detail'),
    path('novo/', views.ContatoCreateView.as_view(), name='contato_create'),
    path('contato/<int:pk>/editar/', views.ContatoUpdateView.as_view(), name='contato_update'),
    path('contato/<int:pk>/excluir/', views.ContatoDeleteView.as_view(), name='contato_delete'),
]
