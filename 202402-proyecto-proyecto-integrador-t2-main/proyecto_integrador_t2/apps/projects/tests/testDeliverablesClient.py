from django.test import TestCase, Client as TestClient
from django.urls import reverse
from apps.accounts.models import Userk, Freelancer, Client, City, Country
from apps.projects.models import Project, ProjectComplexity, ProjectContributor, Milestone, Deliverable
from django.contrib.auth import get_user_model

class TestDeliverablesClient(TestCase):
    """
    Suite de pruebas para la gestión de entregables y proyectos por parte de los clientes.
    """

    def setUp(self):
        """
        Configuración inicial para las pruebas, creando usuarios, proyectos y datos relacionados.
        """
        self.testClient = TestClient()
        self.clientUser = get_user_model().objects.create_user(username='clientUser', password='testpassword', is_client=True)
        self.freelancerUser = get_user_model().objects.create_user(username='freelancerUser', password='testpassword', is_freelancer=True)

        # Instancias de Client y Freelancer
        self.testCountry = Country.objects.get(code="CO", name="Colombia")
        self.testCity = City.objects.get(name="Bogotá", country=self.testCountry)

        self.clientProfile = Client.objects.create(
            user=self.clientUser,
            phoneNumber='123456789',
            taxId='1234567890',
            companyName='TestCompany',
            typeOfCompany='Software',
            businessVertical='IT',
            country=self.testCountry,
            city=self.testCity,
            address='Av. El Dorado',
        )

        self.freelancerProfile = Freelancer.objects.create(
            user=self.freelancerUser,
            phoneNumber="987654321",
            identification="0987654321",
            email="freelancer@example.com"
        )

        # Crear proyecto, complejidad y colaborador
        self.projectComplexity = ProjectComplexity.objects.create(levelName="Intermediate", description="Intermediate level project")
        self.testProject = Project.objects.create(
            title="Test Project",
            description="A test project description",
            requiredPosition="Developer",
            daysDuration=10,
            budget=1000.00,
            complexity=self.projectComplexity,
            client=self.clientProfile
        )
        self.projectContributor = ProjectContributor.objects.create(
            title="Contributor Test",
            project=self.testProject,
            freelancer=self.freelancerProfile,
            budget=500,
            version=1
        )

        # Crear hito relacionado con el colaborador
        self.testMilestone = Milestone.objects.create(
            name="Milestone Test",
            projectContributor=self.projectContributor
        )

        # Crear un entregable asociado al hito
        self.testDeliverable = Deliverable.objects.create(
            name="Deliverable Test",
            description="This is a test deliverable",
            deadlineInDays=5,
            requiresEvidence=True,
            milestone=self.testMilestone,
        )

        # Iniciar sesión como cliente
        self.testClient.login(username='clientUser', password='testpassword')

    def testClientCanViewOwnProjects(self):
        """
        Verifica que un cliente pueda ver sus propios proyectos.
        """
        url = reverse('clientProject')
        response = self.testClient.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.testProject.title)

    def testClientCannotCreateProjectWithInvalidData(self):
        """
        Verifica que no se pueda crear un proyecto con datos inválidos.
        """
        url = reverse('createProject')
        response = self.testClient.post(url, {
            'title': '',
            'description': 'Invalid Project',
            'requiredPosition': 'Developer',
            'daysDuration': -5,
            'budget': 'invalid_budget',
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Project.objects.filter(description="Invalid Project").exists())

    def testClientCanApproveDeliverable(self):
        """
        Verifica que un cliente pueda aprobar un entregable válido.
        """
        self.testDeliverable.evidenceFile = 'evidence/test_file.pdf'
        self.testDeliverable.save()

        url = reverse('clientDeliverable', args=[self.projectContributor.id])
        response = self.testClient.post(url, {
            'deliverable_id': self.testDeliverable.id,
            'action': 'accept',
        })
        self.assertEqual(response.status_code, 302)
        self.testDeliverable.refresh_from_db()
        self.assertTrue(self.testDeliverable.done)

    def testClientCannotApproveDeliverableWithoutEvidence(self):
        """
        Verifica que un cliente no pueda aprobar un entregable sin evidencia requerida.
        """
        url = reverse('clientDeliverable', args=[self.projectContributor.id])
        response = self.testClient.post(url, {
            'deliverable_id': self.testDeliverable.id,
            'action': 'accept',
        })
        self.assertEqual(response.status_code, 302)
        self.testDeliverable.refresh_from_db()
        self.assertFalse(self.testDeliverable.done)

    def testClientCanRejectDeliverable(self):
        """
        Verifica que un cliente pueda rechazar un entregable.
        """
        url = reverse('clientDeliverable', args=[self.projectContributor.id])
        response = self.testClient.post(url, {
            'deliverable_id': self.testDeliverable.id,
            'action': 'reject',
        })
        self.assertEqual(response.status_code, 302)
        self.testDeliverable.refresh_from_db()
        self.assertFalse(self.testDeliverable.done)
        self.assertFalse(self.testDeliverable.awaiting_approval)

    def testClientCanViewAllDeliverables(self):
        """
        Verifica que un cliente pueda ver todos los entregables de un colaborador.
        """
        url = reverse('clientDeliverable', args=[self.projectContributor.id])
        response = self.testClient.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.testDeliverable.name)

    def testClientSeesErrorWhenAcceptingDeliverableWithoutEvidence(self):
        """
        Verifica que un cliente reciba un mensaje de error al intentar aceptar un entregable sin evidencia requerida.
        """
        url = reverse('clientDeliverable', args=[self.projectContributor.id])
        response = self.testClient.post(url, {
            'deliverable_id': self.testDeliverable.id,
            'action': 'accept',
        })
        self.assertEqual(response.status_code, 302)
        messages = list(response.wsgi_request._messages)
        self.assertGreater(len(messages), 0)
        self.assertIn("cannot be marked as completed without evidence", str(messages[0]))

    def testClientCanMarkJobAsFinished(self):
        """
        Verifica que un cliente pueda marcar un trabajo como terminado si todos los entregables están completados.
        """
        self.testDeliverable.done = True
        self.testDeliverable.save()

        url = reverse('clientDeliverable', args=[self.projectContributor.id])
        response = self.testClient.post(url, {'finish_job': True})
        self.assertEqual(response.status_code, 302)
        self.projectContributor.refresh_from_db()
        self.assertTrue(self.projectContributor.finishJob)

    def testClientCannotMarkJobAsFinishedWithIncompleteDeliverables(self):
        """
        Verifica que un cliente no pueda marcar un trabajo como terminado si hay entregables sin completar.
        """
        url = reverse('clientDeliverable', args=[self.projectContributor.id])
        response = self.testClient.post(url, {'finish_job': True})
        self.assertEqual(response.status_code, 302)
        self.projectContributor.refresh_from_db()
        self.assertFalse(self.projectContributor.finishJob)

    def testClientCanRequestRevisionOnDeliverable(self):
        """
        Verifica que un cliente pueda solicitar revisiones para un entregable.
        """
        url = reverse('clientDeliverable', args=[self.projectContributor.id])
        response = self.testClient.post(url, {
            'deliverable_id': self.testDeliverable.id,
            'action': 'reject',
        })
        self.assertEqual(response.status_code, 302)
        self.testDeliverable.refresh_from_db()
        self.assertFalse(self.testDeliverable.done)
        self.assertFalse(self.testDeliverable.awaiting_approval)
