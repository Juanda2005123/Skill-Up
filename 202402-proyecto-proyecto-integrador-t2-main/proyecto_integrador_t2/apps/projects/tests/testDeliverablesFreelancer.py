from django.test import TestCase, Client as TestClient
from django.urls import reverse
from apps.accounts.models import Userk, Freelancer, Client, City, Country
from apps.projects.models import Project, ProjectComplexity, ProjectContributor, Milestone, Deliverable
from django.contrib.auth import get_user_model

class TestDeliverablesFreelancer(TestCase):
    """
    Suite de pruebas para la gestión de entregables y hitos por parte de los freelancers.
    """

    def setUp(self):
        """
        Configuración inicial para las pruebas, creando usuarios, proyectos y datos relacionados.
        """
        self.client = TestClient()
        self.clientUser = get_user_model().objects.create_user(username='clientUser', password='testpassword', is_client=True)
        self.freelancerUser = get_user_model().objects.create_user(username='freelancerUser', password='testpassword', is_freelancer=True)

        # Instancias de Client y Freelancer
        self.country = Country.objects.get(code="CO", name="Colombia")
        self.city = City.objects.get(name="Bogotá", country=self.country)

        self.clientProfile = Client.objects.create(
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

        self.freelancerProfile = Freelancer.objects.create(
            user=self.freelancerUser,
            phoneNumber="987654321",
            identification="0987654321",
            email="freelancer@example.com"
        )

        # Crear proyecto, complejidad y colaborador
        self.complexity = ProjectComplexity.objects.create(levelName="Intermediate", description="Intermediate level project")
        self.project = Project.objects.create(
            title="Test Project",
            description="A test project description",
            requiredPosition="Developer",
            daysDuration=10,
            budget=1000.00,
            complexity=self.complexity,
            client=self.clientProfile
        )
        self.contributor = ProjectContributor.objects.create(
            title="Contributor Test",
            project=self.project,
            freelancer=self.freelancerProfile,
            budget=500,
            version=1
        )

        # Crear hito relacionado con el colaborador
        self.milestone = Milestone.objects.create(
            name="Milestone Test",
            projectContributor=self.contributor
        )

        # Iniciar sesión como freelancer
        self.client.login(username='freelancerUser', password='testpassword')

    def testAddValidDeliverable(self):
        """
        Verifica que un freelancer pueda agregar un entregable válido a un hito.
        """
        url = reverse('addMilestoneDeliverable', args=[self.milestone.id])
        self.client.post(url, {
            'name': 'Valid Deliverable',
            'description': 'This is a valid deliverable',
            'deadlineInDays': 3,
            'requiresEvidence': True,
        })

        deliverable = Deliverable.objects.filter(name="Valid Deliverable", milestone=self.milestone).first()
        self.assertIsNotNone(deliverable)
        self.assertEqual(deliverable.description, "This is a valid deliverable")
        self.assertEqual(deliverable.deadlineInDays, 3)
        self.assertTrue(deliverable.requiresEvidence)

    def testAddDeliverableWithoutName(self):
        """
        Verifica que no se pueda agregar un entregable sin nombre.
        """
        url = reverse('addMilestoneDeliverable', args=[self.milestone.id])
        self.client.post(url, {
            'name': '',
            'description': 'Deliverable without name',
            'deadlineInDays': 5,
            'requiresEvidence': False,
        })

        deliverables = Deliverable.objects.filter(description="Deliverable without name")
        self.assertEqual(deliverables.count(), 0)

    def testAddDeliverableNegativeDeadline(self):
        """
        Verifica que no se pueda agregar un entregable con un deadline negativo.
        """
        url = reverse('addMilestoneDeliverable', args=[self.milestone.id])
        self.client.post(url, {
            'name': 'Invalid Deadline Deliverable',
            'description': 'This deliverable has a negative deadline',
            'deadlineInDays': -3,
            'requiresEvidence': True,
        })

        deliverables = Deliverable.objects.filter(name="Invalid Deadline Deliverable")
        self.assertEqual(deliverables.count(), 0)

    def testDeleteDeliverable(self):
        """
        Verifica que un freelancer pueda eliminar un entregable que haya creado.
        """
        deliverable = Deliverable.objects.create(
            name="Deletable Deliverable",
            description="This deliverable will be deleted",
            deadlineInDays=5,
            requiresEvidence=True,
            milestone=self.milestone
        )
        url = reverse('deleteDeliverable', args=[deliverable.id])
        self.client.post(url)

        deliverables = Deliverable.objects.filter(name="Deletable Deliverable")
        self.assertEqual(deliverables.count(), 0)

    def testMilestoneTotalDeliverablesCount(self):
        """
        Verifica que se calcule correctamente el número total de entregables asociados a un hito.
        """
        # Crear algunos entregables asociados al hito
        Deliverable.objects.create(
            name="Deliverable 1",
            description="Description 1",
            deadlineInDays=5,
            requiresEvidence=True,
            milestone=self.milestone
        )
        Deliverable.objects.create(
            name="Deliverable 2",
            description="Description 2",
            deadlineInDays=7,
            requiresEvidence=False,
            milestone=self.milestone
        )
        Deliverable.objects.create(
            name="Deliverable 3",
            description="Description 3",
            deadlineInDays=3,
            requiresEvidence=True,
            milestone=self.milestone
        )

        # Verificar el número total de entregables asociados al hito
        totalDeliverables = Deliverable.objects.filter(milestone=self.milestone).count()
        self.assertEqual(totalDeliverables, 3)

