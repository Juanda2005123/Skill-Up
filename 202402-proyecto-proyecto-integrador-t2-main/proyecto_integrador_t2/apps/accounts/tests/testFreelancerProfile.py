from django.test import TestCase
from django.urls import reverse
from datetime import date
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.storage import default_storage
from django.contrib.auth import get_user_model
from apps.accounts.models import Freelancer, Portfolio, Experience, FreelancerSkillExpertise, Client, Rating
from apps.projects.models import Deliverable, Project, ProjectContributor, ProjectComplexity

User = get_user_model()

class FreelancerProfileTests(TestCase):

    def setUp(self):
        """
        Configuración inicial para los tests. Crea los usuarios, perfiles y contribuyentes necesarios.
        """
        # Crear un cliente
        self.client_user = get_user_model().objects.create_user(username='clientuser', password='testpass', is_client=True)
        self.client_profile = Client.objects.create(user=self.client_user, phoneNumber="123456789", taxId="321321")
    
        # Crear un freelancer para que el cliente lo vea
        self.freelancer_user = get_user_model().objects.create_user(username='freelanceruser', password='testpass', is_freelancer=True)
        self.resume_file = SimpleUploadedFile("resume.pdf", b"PDF content", content_type="application/pdf")
        self.freelancer_profile = Freelancer.objects.create(
            user=self.freelancer_user,
            phoneNumber="987654321",
            identification="123456789",
            resume=self.resume_file
        )
        
        # Crear un segundo freelancer para las pruebas
        self.second_freelancer_user = get_user_model().objects.create_user(username='freelancer2', password='testpass', is_freelancer=True)
        self.second_freelancer_profile = Freelancer.objects.create(user=self.second_freelancer_user, phoneNumber="987654321", identification="987654321")

        # Crear complejidad del proyecto
        complexity = ProjectComplexity.objects.create(levelName="Simple", description="Simple project")

        # Crear un proyecto y asociar a los freelancers como contributors
        self.project = Project.objects.create(
            title="Project Test",
            client=self.client_profile,
            complexity=complexity,
            budget=1000
        )
    
        # Crear un ProjectContributor para el freelancer
        self.project_contributor = ProjectContributor.objects.create(
            title="Contributor Test",
            project=self.project,
            freelancer=self.freelancer_profile,
            budget=500,
            version=1,
            rejectionReason="pending"
        )
    
        # Crear otro ProjectContributor para el segundo freelancer
        self.project_contributor = ProjectContributor.objects.create(
            title="Contributor Test",
            project=self.project,
            freelancer=self.second_freelancer_profile,
            budget=500,
            version=1
        )

        self.portfolio1 = Portfolio.objects.create(
            freelancer=self.freelancer_profile,
            project_name="Testing",
            project_description="This project is a test",
            project_duration_months="50",
            project_link="https://github.com/freelancer_test"
        )

        # Obtener el contributorId para usarlo en las pruebas
        self.contributor_id = self.project_contributor.id  # Este es el ID que usarás en las pruebas


    def testFreelancerCannotViewAnotherFreelancerProfile(self):
        """
        Verifica que un freelancer no pueda ver el perfil de otro freelancer.
        """
        # Iniciar sesión como el primer freelancer
        self.client.login(username='freelanceruser', password='testpass')

        # Intentar acceder al perfil de otro freelancer (segundo freelancer)
        url = reverse('freelancerProfile', args=[self.second_freelancer_profile.pk])  # Usamos el pk del segundo freelancer
        response = self.client.get(url)

        # Comprobamos que el contenido de la respuesta no contiene el nombre o datos del segundo freelancer
        self.assertNotContains(response, self.second_freelancer_profile.phoneNumber)
        self.assertNotContains(response, self.second_freelancer_profile.identification)

    def testRedirectUnauthenticatedUserToLogin(self):
        """
        Verifica que un usuario no autenticado sea redirigido al login al intentar ver el perfil de un freelancer.
        """
        # Realizar la petición GET para ver el perfil del freelancer sin estar autenticado
        url = reverse('freelancerProfile', args=[self.second_freelancer_profile.pk])  # Usamos el pk del segundo freelancer
        response = self.client.get(url)

        # Verificar que el usuario no autenticado es redirigido a la página de login
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('freelancerProfile', args=[self.second_freelancer_profile.pk])}")

    def testClientCanViewFreelancerProfile(self):
        """
        Verifica que un cliente autenticado pueda acceder al perfil de un freelancer.
        """
        # Iniciar sesión como cliente
        self.client.login(username='clientuser', password='testpass')

        # Generar la URL correcta para acceder al perfil del freelancer
        url = reverse('fprofileRequest', args=[self.freelancer_profile.user.pk, self.contributor_id])
        response = self.client.get(url)

        # Verificar que la respuesta sea 200
        self.assertEqual(response.status_code, 200)

        # Verificar que el contenido incluye datos del freelancer
        self.assertEqual(self.portfolio1.freelancer, self.freelancer_profile)
        self.assertContains(response, self.freelancer_profile.resume.url)

    def testMultiplePortfoliosDisplayed(self):
        """
        Verifica que se muestren todos los portafolios del freelancer en su perfil.
        """
        # Crear un segundo portafolio
        Portfolio.objects.create(
            freelancer=self.freelancer_profile,
            project_name="Another Project",
            project_description="Another test project",
            project_duration_months="12",
            project_link="https://github.com/another_project"
        )

        self.client.login(username='clientuser', password='testpass')

        # Realizar la solicitud
        url = reverse('fprofileRequest', args=[self.freelancer_profile.user.pk, self.contributor_id])
        response = self.client.get(url)

        # Verificar que ambos portafolios están presentes en la respuesta
        self.assertContains(response, "Testing")
        self.assertContains(response, "Another Project")

    def testFreelancerSkillsDisplayed(self):
        """
        Verifica que las habilidades del freelancer se muestren en su perfil.
        """
        # Crear habilidades para el freelancer
        skill_python = FreelancerSkillExpertise.objects.create(name="Python")
        skill_django = FreelancerSkillExpertise.objects.create(name="Django")
        self.freelancer_profile.skillExpertises.add(skill_python, skill_django)

        self.client.login(username='clientuser', password='testpass')

        # Realizar la solicitud
        url = reverse('fprofileRequest', args=[self.freelancer_profile.user.pk, self.contributor_id])
        response = self.client.get(url)

        # Verificar que las habilidades están en la respuesta
        self.assertContains(response, "Python")
        self.assertContains(response, "Django")

    def testNonexistentFreelancerProfile(self):
        """
        Verifica que la vista maneja perfiles inexistentes correctamente.
        """
        self.client.login(username='clientuser', password='testpass')

        # Intentar acceder a un perfil que no existe
        url = reverse('fprofileRequest', args=[9999, self.contributor_id])  # ID no existente
        response = self.client.get(url)

        # Verificar que la respuesta es 404 Not Found
        self.assertEqual(response.status_code, 404)

    def testClientSeesFreelancerDetails(self):
        """
        Verifica que un cliente pueda ver detalles específicos del freelancer en su perfil.
        """
        self.client.login(username='clientuser', password='testpass')

        # Realizar la solicitud
        url = reverse('fprofileRequest', args=[self.freelancer_profile.user.pk, self.contributor_id])
        response = self.client.get(url)

        # Verificar que los detalles específicos están en la respuesta
        self.assertContains(response, self.portfolio1.project_name)
        self.assertContains(response, self.portfolio1.project_description)