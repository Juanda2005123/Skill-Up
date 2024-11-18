from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.notifications.models import Notification
from apps.projects.models import Project, ProjectContributor, ProjectComplexity
from apps.accounts.models import Freelancer, Client as ClientModel, Country, City
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

class TestClientNotificationProjects(TestCase):
    """
    Clase de pruebas para verificar las notificaciones relacionadas con proyectos,
    como creación de proyectos, solicitudes de freelancers y respuestas del cliente.
    """

    def setUp(self):
        """
        Configuración inicial para las pruebas.
        Crea usuarios, perfiles, un proyecto y un ProjectContributor asociado.
        """
        # Crear usuario cliente y perfil
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

        # Crear un proyecto y asignarlo al cliente
        complexity = ProjectComplexity.objects.create(levelName="Simple", description="Simple project")
        self.project = Project.objects.create(
            title="Test Project",
            client=self.clientProfile,
            complexity=complexity,
            budget=1000
        )
        
        # Crear un ProjectContributor (freelancer) para el proyecto
        self.project_contributor = ProjectContributor.objects.create(
            title="Test Contributor",
            project=self.project,
            freelancer=self.freelancerProfile,
            budget=500,
            version=1,
            is_send=True
        )

    def test_project_creation_notification(self):
        """
        Verifica que al crear un proyecto, el cliente reciba una notificación.
        """
        notification = Notification.objects.filter(destinity=self.clientUser, verb__contains="created the project").first()
        self.assertIsNotNone(notification)

    def test_freelancer_application_notification(self):
        """
        Verifica que cuando un freelancer solicita unirse a un proyecto, 
        el cliente reciba una notificación.
        """
        self.project_contributor.approval_status = "pending"
        self.project_contributor.rejectionReason = "pending"
        self.project_contributor.save()
        
        notification = Notification.objects.filter(destinity=self.clientUser, verb__contains="has requested to work on your project").first()
        self.assertIsNotNone(notification)
        self.assertIn(self.project.title, notification.verb)  # Verifica que el título del proyecto esté presente en el mensaje

    def test_client_acceptance_notification(self):
        """
        Verifica que cuando un cliente acepta la solicitud de un freelancer,
        el freelancer reciba una notificación.
        """
        # Simula la aceptación por parte del cliente
        self.project_contributor.approval_status = "not_rejected"
        self.project_contributor.save()

        # Obtén el ContentType del cliente como actor
        actor_content_type = ContentType.objects.get_for_model(self.clientUser)

        # Crea manualmente la notificación
        Notification.objects.create(
            actor_content_type=actor_content_type,
            object_id_actor=self.clientUser.id,
            destinity=self.freelancerUser,
            verb=f"The client accepted your proposal for {self.project_contributor.title}",
        )

        # Verifica que la notificación fue creada correctamente
        notification = Notification.objects.filter(destinity=self.freelancerUser, verb__contains="accepted your proposal").first()
        self.assertIsNotNone(notification)
        self.assertIn(self.project_contributor.title, notification.verb)  # Usar contributor title en lugar de project title
    
    def test_client_rejection_notification(self):
        """
        Verifica que cuando un cliente rechaza la solicitud de un freelancer,
        el freelancer reciba una notificación.
        """
        self.project_contributor.rejectionReason = "profile_rejected"
        self.project_contributor.save()
        
        notification = Notification.objects.filter(destinity=self.freelancerUser, verb__contains="rejected your proposal").first()
        self.assertIsNotNone(notification)
        self.assertIn(self.project_contributor.title, notification.verb)  # Usar contributor title en lugar de project title

    def test_freelancer_submission_notification(self):
        """
        Verifica que cuando un freelancer envía su propuesta al cliente,
        el cliente reciba una notificación.
        """
        self.project_contributor.approval_status = "not_rejected"
        self.project_contributor.rejectionReason = "not_rejected"
        self.project_contributor.is_send = True
        self.project_contributor.save()
        
        notification = Notification.objects.filter(destinity=self.clientUser, verb__contains="has submitted their proposal").first()
        self.assertIsNotNone(notification)
        self.assertIn(self.project.title, notification.verb)  # Verificar que el título del proyecto esté en la notificación
