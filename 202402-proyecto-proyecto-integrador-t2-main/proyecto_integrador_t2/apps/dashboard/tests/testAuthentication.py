from django.test import TestCase, Client as TestClient  # Importa TestClient
from django.urls import reverse
from apps.dashboard.views import *
from apps.accounts.models import Userk, Client, Freelancer, City, Country


class TestSecurity(TestCase):
    """
    Pruebas de seguridad para las vistas del dashboard.
    Verifica los accesos permitidos y restricciones para diferentes tipos de usuarios.
    """

    def setUp(self):
        """
        Configuración inicial para las pruebas de seguridad.
        Crea usuarios cliente y freelancer junto con sus respectivas instancias.
        """
        self.testClient = TestClient()
        self.clientUser = Userk.objects.create_user(username='clientUser', password='testPassword', is_client=True)
        self.freelancerUser = Userk.objects.create_user(username='freelancerUser', password='testPassword', is_freelancer=True)
        
        # Instancias de Client y Freelancer
        self.country = Country.objects.get(code="CO")  # Colombia
        self.city = City.objects.get(name="Bogotá", country=self.country)  # Ciudad en Colombia
        
        # Instancias de Client y Freelancer
        self.testClientInstance = Client.objects.create(
            user=self.clientUser,
            phoneNumber=123456789,
            taxId=1234567890,
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

    # Tests para acceso al Dashboard Freelancer
    def testFreelancerAccessToDashboardFreelancer(self):
        """Verifica que un freelancer pueda acceder a su dashboard."""
        self.testClient.login(username='freelancerUser', password='testpassword')
        response = self.testClient.get(reverse('dashboardFreelancer'))
        self.assertEqual(response.status_code, 200)

    def testClientAccessToDashboardFreelancer(self):
        """Verifica que un cliente no pueda acceder al dashboard del freelancer."""
        self.testClient.login(username='clientUser', password='testpassword')
        response = self.testClient.get(reverse('dashboardFreelancer'))
        self.assertContains(response, 'You are not God to view this page bro')
        self.assertEqual(response.status_code, 200)

    def testUnauthenticatedUserAccessToDashboardFreelancer(self):
        """Verifica que un usuario no autenticado sea redirigido al login cuando intenta acceder al dashboard del freelancer."""
        response = self.testClient.get(reverse('dashboardFreelancer'))
        self.assertRedirects(response, '/login/?next=/dashboardFreelancer/')
        self.assertEqual(response.status_code, 302)

    # Tests para acceso al Dashboard Cliente
    def testFreelancerAccessToDashboardClient(self):
        """Verifica que un freelancer no pueda acceder al dashboard del cliente."""
        self.testClient.login(username='freelancerUser', password='testpassword')
        response = self.testClient.get(reverse('dashboardClient'))
        self.assertContains(response, 'You are not God to view this page bro')
        self.assertEqual(response.status_code, 200)

    def testClientAccessToDashboardClient(self):
        """Verifica que un cliente pueda acceder a su dashboard."""
        self.testClient.login(username='clientUser', password='testpassword')
        response = self.testClient.get(reverse('dashboardClient'))
        self.assertEqual(response.status_code, 200)

    def testUnauthenticatedUserAccessToDashboardClient(self):
        """Verifica que un usuario no autenticado sea redirigido al login cuando intenta acceder al dashboard del cliente."""
        response = self.testClient.get(reverse('dashboardClient'))
        self.assertRedirects(response, '/login/?next=/dashboardClient/')
        self.assertEqual(response.status_code, 302)

    # Tests para acceso a Client Analysis
    def testFreelancerAccessToClientAnalysis(self):
        """Verifica que un freelancer no pueda acceder a la vista de análisis del cliente."""
        self.testClient.login(username='freelancerUser', password='testpassword')
        response = self.testClient.get(reverse('clientAnalysis'))
        self.assertContains(response, 'You are not God to view this page bro')
        self.assertEqual(response.status_code, 200)

    def testClientAccessToClientAnalysis(self):
        """Verifica que un cliente pueda acceder a la vista de análisis del cliente."""
        self.testClient.login(username='clientUser', password='testpassword')
        response = self.testClient.get(reverse('clientAnalysis'))
        self.assertEqual(response.status_code, 200)

    def testUnauthenticatedUserAccessToClientAnalysis(self):
        """Verifica que un usuario no autenticado sea redirigido al login cuando intenta acceder a la vista de análisis del cliente."""
        response = self.testClient.get(reverse('clientAnalysis'))
        self.assertRedirects(response, '/login/?next=/clientAnalysis/')
        self.assertEqual(response.status_code, 302)

    # Tests para acceso a Freelancer Analysis
    def testFreelancerAccessToFreelancerAnalysis(self):
        """Verifica que un freelancer pueda acceder a la vista de análisis del freelancer."""
        self.testClient.login(username='freelancerUser', password='testpassword')
        response = self.testClient.get(reverse('freelancerAnalysis'))
        self.assertEqual(response.status_code, 200)

    def testClientAccessToFreelancerAnalysis(self):
        """Verifica que un cliente no pueda acceder a la vista de análisis del freelancer."""
        self.testClient.login(username='clientUser', password='testpassword')
        response = self.testClient.get(reverse('freelancerAnalysis'))
        self.assertContains(response, 'You are not God to view this page bro')
        self.assertEqual(response.status_code, 200)

    def testUnauthenticatedUserAccessToFreelancerAnalysis(self):
        """Verifica que un usuario no autenticado sea redirigido al login cuando intenta acceder a la vista de análisis del freelancer."""
        response = self.testClient.get(reverse('freelancerAnalysis'))
        self.assertRedirects(response, '/login/?next=/freelancerAnalysis/')
        self.assertEqual(response.status_code, 302)
