from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Residue, Profile, Collection

class PontuacaoTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.profile = Profile.objects.create(user=self.user, user_type='C')
        self.residue = Residue.objects.create(
            citizen=self.user,
            residue_type='Plástico',
            weight=1.5,
            location='Rua Teste, 123'
        )

    def test_pontuacao_apos_processamento(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('core:recycler_process', args=[self.residue.id]))
        self.assertEqual(response.status_code, 302)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.points, 10)
        self.residue.refresh_from_db()
        self.assertEqual(self.residue.status, 'F')

class FluxoCompletoTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.cidadao = User.objects.create_user(username='cidadao', password='password')
        self.coletor = User.objects.create_user(username='coletor', password='password')
        self.recicladora = User.objects.create_user(username='recicladora', password='password')
        self.profile_cidadao = Profile.objects.create(user=self.cidadao, user_type='C')

    def test_fluxo_completo(self):
        # 1. Cidadão cria resíduo
        self.client.login(username='cidadao', password='password')
        residue = Residue.objects.create(
            citizen=self.cidadao,
            residue_type='Vidro',
            units=10,
            location='Rua Nova, 456'
        )

        # 2. Coletor aceita a coleta
        self.client.login(username='coletor', password='password')
        collection = Collection.objects.create(residue=residue, collector=self.coletor)
        collection.status = 'C' # Coletada
        collection.save()

        # 3. Recicladora processa o resíduo
        self.client.login(username='recicladora', password='password')
        response = self.client.post(reverse('core:recycler_process', args=[residue.id]))

        # 4. Verificar se os pontos foram creditados
        self.assertEqual(response.status_code, 302)
        self.profile_cidadao.refresh_from_db()
        self.assertEqual(self.profile_cidadao.points, 10)
        residue.refresh_from_db()
        self.assertEqual(residue.status, 'F')
