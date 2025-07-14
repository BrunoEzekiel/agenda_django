from django.contrib import admin
from .models import Contato

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'email', 'usuario', 'criado_em']
    list_filter = ['usuario', 'criado_em']
    search_fields = ['nome', 'telefone', 'email']
    ordering = ['nome']
    date_hierarchy = 'criado_em'
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario=request.user)
