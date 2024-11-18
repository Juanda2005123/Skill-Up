from django.test import TestCase, Client as TestClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.accounts.models import Client, Freelancer, City, Country
from apps.projects.models import Project, ProjectContributor, ProjectComplexity
from apps.communications.models import Chat, Message

class TestDashboard(TestCase):
    """
    Pruebas unitarias para las vistas del dashboard de freelancer y cliente.
    Estas pruebas verifican los accesos y contenidos mostrados en cada tipo de dashboard.
    """

    def setUp(self):
        """
        Configuración inicial para las pruebas.
        Crea usuarios cliente y freelancer, sus perfiles y un proyecto asociado.
        """
        self.testClient = TestClient()
        self.clientUser = get_user_model().objects.create_user(username='clientUser', password='testpassword', is_client=True)
        self.freelancerUser = get_user_model().objects.create_user(username='freelancerUser', password='testpassword', is_freelancer=True)

        # Instancias de Client y Freelancer
        self.country = Country.objects.get(code="CO")  # Colombia
        self.city = City.objects.get(name="Bogotá", country=self.country)  # Ciudad en Colombia
        
        # Crear instancias de Client y Freelancer asociadas a los usuarios
        self.testClientInstance = Client.objects.create(
            user=self.clientUser,
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
            user=self.freelancerUser,
            phoneNumber='987654321',
            identification='0987654321',
            email='freelancer@example.com',
        )

        # Crear una instancia de ProjectComplexity
        self.complexity = ProjectComplexity.objects.create(levelName='Medium')

        # Crear un proyecto
        self.project = Project.objects.create(
            title='Test Project',
            description='A description of the test project',
            client=self.testClientInstance,
            requiredPosition='Developer',
            daysDuration=30,
            budget=1000.00,
            complexity=self.complexity,
        )

        # Crear un ProjectContributor
        self.projectContributor = ProjectContributor.objects.create(
            project=self.project,
            freelancer=self.freelancer,
            title='Contributor',
            requiredPosition='Developer',
            budget=500.00,
            daysDuration=15,
            project_status='PENDING',
            approval_status='pending',
            rejectionReason='pending',
            version=1,
        )

        # URLs para las pruebas
        self.dashboard_freelancer_url = reverse('dashboardFreelancer')
        self.dashboard_client_url = reverse('dashboardClient')

    def testFreelancerAccessToDashboard(self):
        """
        Verifica que un freelancer autenticado puede acceder a su dashboard.
        """
        self.client.login(username='freelancerUser', password='testpassword')
        response = self.client.get(self.dashboard_freelancer_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome')
        self.assertContains(response, 'My Projects')

    def testClientAccessToDashboard(self):
        """
        Verifica que un cliente autenticado puede acceder a su dashboard.
        """
        self.client.login(username='clientUser', password='testpassword')
        response = self.client.get(self.dashboard_client_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome')
        self.assertContains(response, 'My projects')

    def testUnauthenticatedUserAccessToFreelancerDashboard(self):
        """
        Verifica que un usuario no autenticado es redirigido al login cuando intenta acceder al dashboard del freelancer.
        """
        response = self.client.get(self.dashboard_freelancer_url)
        self.assertRedirects(response, '/login/?next=/dashboardFreelancer/')
        self.assertEqual(response.status_code, 302)

    def testUnauthenticatedUserAccessToClientDashboard(self):
        """
        Verifica que un usuario no autenticado es redirigido al login cuando intenta acceder al dashboard del cliente.
        """
        response = self.client.get(self.dashboard_client_url)
        self.assertRedirects(response, '/login/?next=/dashboardClient/')
        self.assertEqual(response.status_code, 302)

    def testFreelancerDashboardShowsProjects(self):
        """
        Verifica que el dashboard del freelancer muestra los proyectos asociados.
        """
        self.client.login(username='freelancerUser', password='testpassword')
        response = self.client.get(self.dashboard_freelancer_url)
        self.assertContains(response, 'Test Project')

    def testClientDashboardShowsProjects(self):
        """
        Verifica que el dashboard del cliente muestra los proyectos creados por el cliente.
        """
        self.client.login(username='clientUser', password='testpassword')
        response = self.client.get(self.dashboard_client_url)
        self.assertContains(response, 'Test Project')

    def testFreelancerDashboardShowsBalance(self):
        """
        Verifica que el dashboard del freelancer muestra el balance disponible.
        """
        self.client.login(username='freelancerUser', password='testpassword')
        response = self.client.get(self.dashboard_freelancer_url)
        self.assertContains(response, 'Available Balance')

    def testClientDashboardShowsFinances(self):
        """
        Verifica que el dashboard del cliente muestra las finanzas.
        """
        self.client.login(username='clientUser', password='testpassword')
        response = self.client.get(self.dashboard_client_url)
        self.assertContains(response, 'My Finances')

    def testFreelancerDashboardShowsMessages(self):
        """
        Verifica que el dashboard del freelancer muestra la sección de mensajes.
        """
        self.client.login(username='freelancerUser', password='testpassword')
        response = self.client.get(self.dashboard_freelancer_url)
        self.assertContains(response, 'Messages')

    def testClientDashboardShowsMessages(self):
        """
        Verifica que el dashboard del cliente muestra la sección de mensajes.
        """
        self.client.login(username='clientUser', password='testpassword')
      
