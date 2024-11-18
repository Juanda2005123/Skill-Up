from django.contrib.contenttypes.models import ContentType
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.notifications.models import Notification
from apps.projects.models import Project, ProjectContributor, ProjectComplexity
from apps.accounts.models import Freelancer, Client as ClientModel, Country, City

User = get_user_model()

class TestFreelancerNotificationViews(TestCase):
    def setUp(self):
        self.client = Client()

        # Crear usuarios y datos relacionados
        self.clientUser = get_user_model().objects.create_user(
            username="clientUser", password="testpassword", is_client=True
        )
        self.freelancerUser = get_user_model().objects.create_user(
            username="freelancerUser", password="testpassword", is_freelancer=True
        )

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

        complexity = ProjectComplexity.objects.create(levelName="Simple", description="Simple project")
        self.project = Project.objects.create(
            title="Test Project",
            client=self.clientProfile,
            complexity=complexity,
            budget=1000
        )
        
        self.project_contributor = ProjectContributor.objects.create(
            title="Test Contributor",
            project=self.project,
            freelancer=self.freelancerProfile,
            budget=500,
            version=1,
            is_send=True
        )

    def create_notification(self, destinity, verb):
        actor_content_type = ContentType.objects.get_for_model(User)
        return Notification.objects.create(
            actor_content_type=actor_content_type,
            object_id_actor=self.clientUser.id,
            destinity=destinity,
            verb=verb,
        )

    def test_send_request_notification(self):
        self.create_notification(
            destinity=self.freelancerUser,
            verb=f"The client accepted your proposal for {self.project_contributor.title}"
        )
        notification = Notification.objects.filter(
            destinity=self.freelancerUser, verb__contains="accepted your proposal"
        ).first()
        self.assertIsNotNone(notification)

    def test_add_milestone_notification(self):
        self.create_notification(
            destinity=self.freelancerUser,
            verb=f"A new milestone was added for {self.project.title}"
        )
        notification = Notification.objects.filter(
            destinity=self.freelancerUser, verb__contains="milestone was added"
        ).first()
        self.assertIsNotNone(notification)
    def test_reject_proposal_notification(self):
        """
        Verifica que se envíe una notificación al freelancer cuando el cliente rechaza su propuesta.
        """
        self.create_notification(
            destinity=self.freelancerUser,
            verb=f"The client rejected your proposal for {self.project_contributor.title}"
        )
        notification = Notification.objects.filter(
            destinity=self.freelancerUser, verb__contains="rejected your proposal"
        ).first()
        self.assertIsNotNone(notification)

    def test_assign_deliverable_notification(self):
        """
        Verifica que se envíe una notificación al freelancer cuando se le asigna un entregable.
        """
        self.create_notification(
            destinity=self.freelancerUser,
            verb=f"A deliverable for {self.project.title} has been assigned to you"
        )
        notification = Notification.objects.filter(
            destinity=self.freelancerUser, verb__contains="has been assigned"
        ).first()
        self.assertIsNotNone(notification)

    def test_proposal_submitted_notification(self):
        """
        Verifica que se envíe una notificación al cliente cuando un freelancer envía una propuesta.
        """
        self.create_notification(
            destinity=self.clientUser,
            verb=f"The freelancer has submitted a proposal for {self.project.title}"
        )
        notification = Notification.objects.filter(
            destinity=self.clientUser, verb__contains="submitted a proposal"
        ).first()
        self.assertIsNotNone(notification)

    def test_milestone_completed_notification(self):
        """
        Verifica que se envíe una notificación al cliente cuando un freelancer completa un entregable.
        """
        self.create_notification(
            destinity=self.clientUser,
            verb=f"The freelancer has completed a milestone for {self.project.title}"
        )
        notification = Notification.objects.filter(
            destinity=self.clientUser, verb__contains="completed a milestone"
        ).first()
        self.assertIsNotNone(notification)

    def test_project_cancellation_notification(self):
        """
        Verifica que se envíe una notificación al freelancer cuando un cliente cancela el proyecto.
        """
        self.create_notification(
            destinity=self.freelancerUser,
            verb=f"The project {self.project.title} has been canceled by the client"
        )
        notification = Notification.objects.filter(
            destinity=self.freelancerUser, verb__contains="has been canceled"
        ).first()
        self.assertIsNotNone(notification)
