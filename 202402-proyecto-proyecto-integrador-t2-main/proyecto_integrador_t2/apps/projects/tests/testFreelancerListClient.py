from django.test import TestCase, Client as TestClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.projects.models import Project, ProjectComplexity, ProjectContributor, Milestone, Deliverable
from apps.accounts.models import Freelancer, Client as ClientModel, Country, City


class TestFreelancerListFunctionality(TestCase):
    """
    Pruebas para verificar funcionalidades relacionadas con la lista de freelancers en proyectos.
    """

    def setUp(self):
        """
        Configuración inicial de pruebas.
        """
        self.client = Client()

        # Crear usuarios
        self.clientUser = get_user_model().objects.create_user(
            username="clientUser", password="testpassword", is_client=True
        )
        self.freelancerUser = get_user_model().objects.create_user(
            username="freelancerUser", password="testpassword", is_freelancer=True
        )

        # Crear datos relacionados
        self.country = Country.objects.get(code="US", name="United States")
        self.city = City.objects.get(name="New York", country=self.country)

        self.clientProfile = ClientModel.objects.create(
            user=self.clientUser,
            phoneNumber="123456789",
            taxId="1234567890",
            companyName="Test Company",
            typeOfCompany="Tech",
            businessVertical="Software",
            country=self.country,
            city=self.city,
            address="123 Main St"
        )

        self.freelancerProfile = Freelancer.objects.create(
            user=self.freelancerUser,
            phoneNumber="987654321",
            identification="111111111",
            email="freelancer@example.com"
        )

        self.complexity = ProjectComplexity.objects.create(
            levelName="Medium", description="Medium complexity project"
        )
        self.project = Project.objects.create(
            title="Project X",
            description="Project for testing",
            requiredPosition="Designer",
            daysDuration=15,
            budget=2000.00,
            complexity=self.complexity,
            client=self.clientProfile
        )

        self.projectContributor = ProjectContributor.objects.create(
            title="Freelancer Contributor",
            project=self.project,
            freelancer=self.freelancerProfile,
            budget=1200,
            approval_status="approved",
            is_send=True,
            version=1
        )

        # Crear hitos y entregables
        self.milestone1 = Milestone.objects.create(
            name="Milestone 1", projectContributor=self.projectContributor
        )
        Deliverable.objects.create(
            name="Deliverable 1",
            milestone=self.milestone1,
            done=True,
            deadlineInDays=10,
            requiresEvidence=True  # Se agrega valor explícito
        )
        Deliverable.objects.create(
            name="Deliverable 2",
            milestone=self.milestone1,
            done=False,
            deadlineInDays=15,
            requiresEvidence=False  # Se agrega valor explícito
        )

        # Iniciar sesión como cliente
        self.client.login(username="clientUser", password="testpassword")

    def testFreelancerProfileDisplayed(self):
        """
        Verifica que el perfil del freelancer esté presente en la lista del proyecto, mostrando el nombre completo.
        """
        url = reverse("listFreelancer", args=[self.project.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.freelancerProfile.user.first_name)
        self.assertContains(response, self.freelancerProfile.user.last_name)


    def testFreelancerBudgetShownCorrectly(self):
        """
        Verifica que el presupuesto asignado al freelancer se muestre correctamente.
        """
        url = reverse("listFreelancer", args=[self.project.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "$1200")

    def testFreelancerProgressDisplayed(self):
        """
        Verifica que el progreso del freelancer en el proyecto esté visible.
        """
        # El progreso se calcula automáticamente basado en los entregables
        expected_progress = 50  # 1 de 2 entregables está completo

        url = reverse("listFreelancer", args=[self.project.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f"{expected_progress}%")

    def testProjectTitleVisible(self):
        """
        Verifica que el título del proyecto esté presente en la página.
        """
        url = reverse("listFreelancer", args=[self.project.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.project.title)
