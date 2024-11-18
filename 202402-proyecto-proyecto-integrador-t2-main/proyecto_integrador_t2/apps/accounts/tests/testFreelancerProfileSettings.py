from django.test import TestCase
from django.urls import reverse
from datetime import date
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from apps.accounts.models import Freelancer, Portfolio, Experience, FreelancerSkillExpertise, Client, Rating

User = get_user_model()

class FreelancerProfileSettingsTest(TestCase):
    """
    Clase de pruebas para verificar la funcionalidad de configuración del perfil de freelancers.
    Cubre pruebas para la edición del perfil, manejo de habilidades, experiencia, portafolio y ratings.
    """

    def setUp(self):
        """
        Configura los datos iniciales necesarios para las pruebas.
        Crea un usuario freelancer y un cliente, así como sus perfiles asociados.
        """
        self.freelancer_user = User.objects.create_user(username='freelanceruser', password='testpass', is_freelancer=True)
        self.freelancer_profile = Freelancer.objects.create(user=self.freelancer_user, phoneNumber="987654321", identification="123456789")

        self.client_user = User.objects.create_user(username='clientuser', password='testpass', is_client=True)
        self.client_profile = Client.objects.create(user=self.client_user, phoneNumber="123456789", taxId="321321")

        self.freelancer_url = reverse('freelancerProfileSettings')

        self.client.login(username='freelanceruser', password='testpass')

        # Archivo de prueba para simulación de subida de un currículum
        self.resume_file = SimpleUploadedFile("resume.pdf", b"PDF content", content_type="application/pdf")

    def testGetFreelancerProfile(self):
        """
        Verifica que la página de configuración del perfil de freelancer se carga correctamente.
        - Código de estado HTTP esperado: 200.
        - Plantilla utilizada: 'accounts/freelancerProfileSettings.html'.
        """
        response = self.client.get(self.freelancer_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/freelancerProfileSettings.html')

    def test_redirect_unauthenticated_user(self):
        """
        Prueba que los usuarios no autenticados son redirigidos a la página de inicio de sesión.
        - Código de estado HTTP esperado: 302 (redirección).
        """
        self.client.logout()
        response = self.client.get(self.freelancer_url)
        self.assertRedirects(response, f"{reverse('login')}?next={self.freelancer_url}")

    def testUpdateFreelancerProfile(self):
        """
        Verifica que se puede actualizar el perfil del freelancer correctamente.
        - Datos probados incluyen descripción, nivel de experiencia, enlaces sociales, habilidades, y un currículum.
        """
        # Crear habilidades para añadir al perfil
        expertise_1 = FreelancerSkillExpertise.objects.create(name="Javascript")
        expertise_2 = FreelancerSkillExpertise.objects.create(name="SQL")

        form_data = {
            "description": "Experienced SQL and noSQL developer",
            "experience_level": "Senior",
            "linkedin_url": "https://linkedin.com/in/freelancer_test",
            "github_url": "https://github.com/freelancer_test",
            "resume": self.resume_file,
            "skillExpertises": [expertise_1.id, expertise_2.id]
        }

        response = self.client.post(self.freelancer_url, form_data)

        # Verificar que los datos fueron actualizados correctamente
        self.freelancer_profile.refresh_from_db()
        self.assertEqual(self.freelancer_profile.description, "Experienced SQL and noSQL developer")
        self.assertIn(expertise_1, self.freelancer_profile.skillExpertises.all())

    def testAddExperienceFreelancerProfile(self):
        """
        Verifica que se puede añadir experiencia laboral al perfil del freelancer.
        """
        experience = Experience.objects.create(
            freelancer=self.freelancer_profile,
            job="Tester",
            company="Amazonas",
            start_date=date(2020, 5, 1),
            end_date=date(2023, 5, 1),
            job_description="Unitary and automated testing"
        )
        self.assertEqual(experience.freelancer, self.freelancer_profile)

    def testAddPortfolioFreelancerProfile(self):
        """
        Verifica que se puede añadir un proyecto al portafolio del freelancer.
        """
        portfolio = Portfolio.objects.create(
            freelancer=self.freelancer_profile,
            project_name="Testing Project",
            project_description="Description of a testing project",
            project_duration_months="12",
            project_link="https://github.com/freelancer_test"
        )
        self.assertEqual(portfolio.freelancer, self.freelancer_profile)

    def testAddRatingFreelancerProfile(self):
        """
        Verifica que se puede añadir una calificación al perfil del freelancer.
        - Calificación incluye un comentario y puntuación (rating).
        """
        rating = Rating.objects.create(
            freelancer=self.freelancer_profile,
            client=self.client_profile,
            rating=5,
            comment="Excellent work.",
            date_posted=timezone.now()
        )
        self.assertEqual(rating.freelancer, self.freelancer_profile)
        self.assertEqual(rating.client, self.client_profile)
        self.assertEqual(rating.rating, 5)
