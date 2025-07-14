from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from contatos.models import Contato

class Command(BaseCommand):
    help = 'Cria contatos de exemplo para o usuário admin'

    def handle(self, *args, **options):
        try:
            admin_user = User.objects.get(username='admin')
        except User.DoesNotExist:
            self.stdout.write(
                self.style.ERROR('Usuário admin não encontrado. Execute: python manage.py createsuperuser')
            )
            return

        contatos_exemplo = [
            {
                'nome': 'João Silva',
                'telefone': '(11) 99999-1234',
                'email': 'joao.silva@email.com'
            },
            {
                'nome': 'Maria Oliveira',
                'telefone': '(11) 88888-5678',
                'email': 'maria.oliveira@email.com'
            },
            {
                'nome': 'Pedro Santos',
                'telefone': '(11) 77777-9876',
                'email': 'pedro.santos@email.com'
            },
            {
                'nome': 'Ana Costa',
                'telefone': '(11) 66666-5432',
                'email': 'ana.costa@email.com'
            },
            {
                'nome': 'Carlos Ferreira',
                'telefone': '(11) 55555-1111',
                'email': 'carlos.ferreira@email.com'
            },
            {
                'nome': 'Lucia Pereira',
                'telefone': '(11) 44444-2222',
                'email': 'lucia.pereira@email.com'
            },
            {
                'nome': 'Roberto Lima',
                'telefone': '(11) 33333-3333',
                'email': 'roberto.lima@email.com'
            },
            {
                'nome': 'Fernanda Rocha',
                'telefone': '(11) 22222-4444',
                'email': 'fernanda.rocha@email.com'
            },
            {
                'nome': 'Marcos Alves',
                'telefone': '(11) 11111-5555',
                'email': 'marcos.alves@email.com'
            },
            {
                'nome': 'Juliana Souza',
                'telefone': '(11) 99999-6666',
                'email': 'juliana.souza@email.com'
            },
            {
                'nome': 'Ricardo Martins',
                'telefone': '(11) 88888-7777',
                'email': 'ricardo.martins@email.com'
            },
            {
                'nome': 'Patrícia Gomes',
                'telefone': '(11) 77777-8888',
                'email': 'patricia.gomes@email.com'
            }
        ]

        contatos_criados = 0
        for dados_contato in contatos_exemplo:
            contato, criado = Contato.objects.get_or_create(
                nome=dados_contato['nome'],
                usuario=admin_user,
                defaults={
                    'telefone': dados_contato['telefone'],
                    'email': dados_contato['email']
                }
            )
            if criado:
                contatos_criados += 1
                self.stdout.write(f'Contato criado: {contato.nome}')

        if contatos_criados > 0:
            self.stdout.write(
                self.style.SUCCESS(f'{contatos_criados} contatos de exemplo criados com sucesso!')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Todos os contatos já existem.')
            )
