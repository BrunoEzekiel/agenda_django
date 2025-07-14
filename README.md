# 📱 Agenda de Contatos Django

Uma aplicação web completa para gerenciamento de contatos pessoais, desenvolvida com Django e Bootstrap.

## ✨ Funcionalidades

### 📋 CRUD Completo
- ✅ **Criar** novos contatos
- 👁️ **Visualizar** detalhes dos contatos
- ✏️ **Editar** informações existentes
- 🗑️ **Excluir** contatos com confirmação

### 🔍 Busca Inteligente
- Busca por nome, telefone ou email
- Resultados em tempo real
- Filtros mantidos na paginação

### 👤 Autenticação
- Sistema de login/logout
- Cada usuário vê apenas seus contatos
- Proteção de rotas com `LoginRequiredMixin`

### 📄 Paginação
- Lista paginada (10 contatos por página)
- Navegação entre páginas
- Busca mantida na paginação

### 🎨 Interface Moderna
- Design responsivo com Bootstrap 5
- Ícones Font Awesome
- Cards interativos
- Alertas e mensagens de feedback

## 🚀 Como Executar

### 1. Ativar o ambiente virtual
```bash
# O ambiente já deve estar ativado
```

### 2. Instalar dependências (já feito)
```bash
pip install django
```

### 3. Executar migrações (já feito)
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Criar superusuário (já feito)
```bash
python manage.py createsuperuser --username admin --email admin@example.com
# Senha: admin
```

### 5. Criar contatos de exemplo (já feito)
```bash
python manage.py criar_contatos_exemplo
```

### 6. Executar o servidor
```bash
python manage.py runserver
```

### 7. Acessar a aplicação
- **URL:** http://127.0.0.1:8000/
- **Login:** admin
- **Senha:** admin

## 📁 Estrutura do Projeto

```
agenda-django/
├── agenda_contatos/          # Configurações do projeto
│   ├── settings.py          # Configurações (apps, DB, templates)
│   ├── urls.py              # URLs principais
│   └── wsgi.py              # WSGI config
├── contatos/                # App principal
│   ├── models.py            # Modelo Contato
│   ├── views.py             # Views baseadas em classe
│   ├── forms.py             # Formulários com validação
│   ├── urls.py              # URLs do app
│   ├── admin.py             # Configuração do admin
│   └── management/          # Comandos personalizados
│       └── commands/
│           └── criar_contatos_exemplo.py
├── templates/               # Templates HTML
│   ├── base.html           # Template base
│   ├── contatos/           # Templates do app
│   │   ├── lista.html      # Lista de contatos
│   │   ├── detail.html     # Detalhes do contato
│   │   ├── form.html       # Formulário criar/editar
│   │   └── confirm_delete.html # Confirmação de exclusão
│   └── registration/       # Templates de auth
│       └── login.html      # Página de login
└── manage.py               # Script de gerenciamento Django
```

## 🎯 Conceitos Django Implementados

### 🏗️ Models
- **Model Contato** com relacionamento ForeignKey para User
- Campos: nome, telefone, email, usuario, timestamps
- Meta class para configuração de ordenação e verbose names
- Método `__str__` e `get_absolute_url`

### 👁️ Views Genéricas
- **ListView**: Lista paginada com busca
- **DetailView**: Visualização de detalhes
- **CreateView**: Criação de novos contatos
- **UpdateView**: Edição de contatos existentes
- **DeleteView**: Exclusão com confirmação

### 🔐 Autenticação
- **LoginRequiredMixin**: Proteção de todas as views
- Filtragem automática por usuário logado
- URLs de login/logout configuradas
- Redirecionamentos após login/logout

### 📝 Formulários
- **ModelForm** com validação personalizada
- Widgets Bootstrap customizados
- Validação de campos obrigatórios
- Tratamento de erros por campo

### 🌐 URLs
- URLs nomeadas para navegação
- Parâmetros de URL para views baseadas em classe
- Inclusão de URLs de apps
- URLs de autenticação integradas

### 🎨 Templates
- Template de herança com `base.html`
- Sistema de blocos para conteúdo específico
- Bootstrap 5 para estilização
- Font Awesome para ícones
- Paginação personalizada
- Formulários estilizados

### 💾 ORM
- Queries otimizadas com `filter()`
- Busca com `Q objects` para múltiplos campos
- Relacionamentos ForeignKey
- Criação automática de timestamps

## 🔧 Funcionalidades Avançadas

### 🔍 Sistema de Busca
```python
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
```

### 📄 Paginação com Busca
- Paginação mantém parâmetros de busca
- Navegação entre páginas preserva filtros
- Contagem total de resultados

### 🛡️ Segurança
- Cada usuário vê apenas seus contatos
- CSRF protection em todos os formulários
- Validação de dados no backend
- LoginRequired em todas as views

### 📱 Responsividade
- Layout adaptativo para mobile/desktop
- Cards responsivos com Bootstrap Grid
- Formulários otimizados para touch
- Navegação mobile-friendly

## 🎉 Como Testar

1. **Acesse:** http://127.0.0.1:8000/
2. **Faça login** com: admin/admin
3. **Explore as funcionalidades:**
   - ➕ Adicione novos contatos
   - 🔍 Use a busca
   - ✏️ Edite contatos existentes
   - 👁️ Visualize detalhes
   - 🗑️ Exclua contatos
   - 📄 Navegue pelas páginas

## 📊 Dados de Teste

O sistema já vem com 12 contatos de exemplo criados para o usuário admin, permitindo testar:
- Paginação (10 contatos por página)
- Busca por diferentes critérios
- Listagem e navegação
- Todas as operações CRUD

## 🎨 Capturas de Tela

A aplicação possui:
- **Interface moderna** com Bootstrap 5
- **Ícones intuitivos** do Font Awesome
- **Cores harmoniosas** e layout profissional
- **Responsividade completa** para todos os dispositivos
- **Feedback visual** com alerts e mensagens
