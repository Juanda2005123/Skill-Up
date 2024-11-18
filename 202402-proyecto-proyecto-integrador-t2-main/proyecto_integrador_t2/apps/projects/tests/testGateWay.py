from django.test import TestCase, Client as TestClient  # Importa TestClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from apps.accounts.models import Client, Freelancer, Country,City
from apps.projects.models import Project, ProjectContributor, ProjectComplexity,Transaction
from decimal import Decimal

class TestGateWay(TestCase):

    def setUp(self):
        self.testClient = TestClient()
        # Crear los usuarios para las pruebas
        self.client_user = get_user_model().objects.create_user(username="clientUser", password="testpassword", is_client=True)
        self.freelancer_user = get_user_model().objects.create_user(username="freelancerUser", password="testpassword", is_freelancer=True)
        
        #Instancias que hacen falta de CAÑO                            
        self.country = Country.objects.get(code="US", name="United States")
        self.city = City.objects.get(name="New York", country=self.country)

        # Crear instancias de Client y Freelancer asociadas a los usuarios
        self.client_instance = Client.objects.create(
            user=self.client_user,
            phoneNumber='123456789',
            taxId='1234567890',
            companyName='TestCompany',
            typeOfCompany='Software',
            businessVertical='IT',
            country=self.country,
            city=self.city,
            address='Av. El Dorado',
        )
        
        self.freelancer = Freelancer.objects.create(
            user=self.freelancer_user,
            phoneNumber='987654321',
            identification='0987654321',
            email='freelancer@example.com',
            balance=Decimal("0.00"),
        )
        # Crear una instancia de ProjectComplexity y Project
        self.complexity = ProjectComplexity.objects.create(levelName='Medium')
        self.project = Project.objects.create(
            title='Test Project',
            description='A test project description',
            client=self.client_instance,
            requiredPosition='Developer',
            daysDuration=30,
            budget=Decimal("1000.00"),
            complexity=self.complexity,
        )
        # Crear un ProjectContributor para el freelancer
        self.project_contributor = ProjectContributor.objects.create(
            project=self.project,
            freelancer=self.freelancer,
            title='Contributor',
            requiredPosition='Developer',
            budget=Decimal("1000.00"),
            daysDuration=15,
            finishJob=True,  # Marcar trabajo como terminado para habilitar el pago
            project_status='PENDING',
            approval_status='pending',
            rejectionReason='pending',
            version=1,
        )
        # URLs para las pruebas
        self.gateWay_url = reverse('gateWay', args=[self.project_contributor.id])
        self.confirmed_payment_url = reverse('confirmedPayment', args=[self.project_contributor.id])


    def test_gateWay_access(self):
        """Verifica que se pueda acceder a la página de gateWay cuando el usuario está autenticado."""
        self.client.login(username="clientUser", password="testpassword")
        response = self.client.get(self.gateWay_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Realizar Pago")


    def test_successful_payment_redirects_to_confirmed_payment(self):
        """Verifica que el pago exitoso redirige a la página de confirmedPayment y crea una transacción."""
        self.client.login(username="clientUser", password="testpassword")
        response = self.client.post(self.gateWay_url, {
            'card_number': '1234567890123456',
            'expiry_date': '12/34',
            'cvv': '123',
            'card_name': 'Juan Pérez'
        })
        self.assertRedirects(response, self.confirmed_payment_url)

        # Verificar que la transacción se creó y que el saldo del freelancer se actualizó
        transaction_exists = Transaction.objects.filter(
            project_contributor=self.project_contributor,
            client=self.client_instance,
            freelancer=self.freelancer,
            project=self.project,
            amount=Decimal("1000.00"),
            status='completed'
        ).exists()
        self.assertTrue(transaction_exists)
        

    def test_payment_with_missing_fields(self):
        """Verifica que el formulario de pago emita un error cuando faltan campos requeridos."""
        self.client.login(username="clientUser", password="testpassword")
        response = self.client.post(self.gateWay_url, {
            'card_number': '',
            'expiry_date': '',
            'cvv': '',
            'card_name': ''
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(str(messages[0]), "All the fields are required.")
        
        
    def test_payment_without_finishJob_redirects_back(self):
        """Verifica que el usuario es redirigido cuando intenta pagar un trabajo que no está terminado."""
        self.project_contributor.finishJob = False
        self.project_contributor.save()
        self.client.login(username="clientUser", password="testpassword")
        response = self.client.get(self.gateWay_url)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(str(messages[0]), "Payment not allowed until the job is marked as complete.")
        
        
class TestConfirmedPayment(TestCase):
    def setUp(self):
        # Configurar los mismos usuarios y proyecto para confirmedPayment
        self.client_user = get_user_model().objects.create_user(username="clientUser", password="testpassword", is_client=True)
        self.freelancer_user = get_user_model().objects.create_user(username="freelancerUser", password="testpassword", is_freelancer=True)
        
        self.country = Country.objects.get(code="US", name="United States")
        self.city = City.objects.get(name="New York", country=self.country)

        self.client_instance = Client.objects.create(
            user=self.client_user,
            phoneNumber='123456789',
            taxId='1234567890',
            companyName='TestCompany',
            typeOfCompany='Software',
            businessVertical='IT',
            country=self.country,
            city=self.city,
            address='Av. El Dorado',
        )
        
        self.freelancer = Freelancer.objects.create(
            user=self.freelancer_user,
            phoneNumber='987654321',
            identification='0987654321',
            email='freelancer@example.com',
            balance=Decimal("0.00"),
        )
        self.complexity = ProjectComplexity.objects.create(levelName='Medium')
        self.project = Project.objects.create(
            title='Test Project',
            description='A test project description',
            client=self.client_instance,
            requiredPosition='Developer',
            daysDuration=30,
            budget=Decimal("1000.00"),
            complexity=self.complexity,
        )
        self.project_contributor = ProjectContributor.objects.create(
            project=self.project,
            freelancer=self.freelancer,
            title='Contributor',
            requiredPosition='Developer',
            budget=Decimal("1000.00"),
            daysDuration=15,
            finishJob=True,
            project_status='PENDING',
            approval_status='pending',
            rejectionReason='pending',
            version=1,
        )
        self.confirmed_payment_url = reverse('confirmedPayment', args=[self.project_contributor.id])
        
        
    def test_confirmed_payment_access(self):
        """Verifica que se pueda acceder a la página de confirmedPayment si el trabajo está terminado."""
        self.client.login(username="clientUser", password="testpassword")
        response = self.client.get(self.confirmed_payment_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "¡Pago Confirmado!")
        
    def test_successful_transaction_and_balance_update(self):
        """Verifica que la transacción se crea exitosamente y que el balance del freelancer se actualiza."""
        self.client.login(username="clientUser", password="testpassword")
        self.client.get(self.confirmed_payment_url)
        # Verificar que la transacción fue creada
        transaction = Transaction.objects.get(
            project_contributor=self.project_contributor,
            client=self.client_instance,
            freelancer=self.freelancer,
            project=self.project,
            amount=Decimal("1000.00"),
            status='completed'
        )
        self.assertIsNotNone(transaction)
        # Verificar que el balance del freelancer se actualizó correctamente
        self.freelancer.refresh_from_db()
        self.assertEqual(self.freelancer.balance, Decimal("1000.00"))
        
    def test_confirmed_payment_with_unfinished_job(self):
        """Verifica que el usuario sea redirigido si intenta confirmar el pago cuando el trabajo no está terminado."""
        self.project_contributor.finishJob = False
        self.project_contributor.save()
        self.client.login(username="clientUser", password="testpassword")
        response = self.client.get(self.confirmed_payment_url)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(str(messages[0]), "Payment could not be completed.")