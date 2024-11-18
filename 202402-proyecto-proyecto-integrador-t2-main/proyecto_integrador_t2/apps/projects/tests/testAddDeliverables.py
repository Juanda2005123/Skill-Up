from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.projects.models import Project, ProjectContributor, Milestone, ProjectComplexity
from apps.accounts.models import Freelancer, Client

User = get_user_model()

class TestAddDeliverablesProject(TestCase):
    """
    Test suite for the 'addDeliverablesProject' view to handle milestones creation
    for project contributors.
    """

    def setUp(self):
        """
        Set up users, project, and project contributor for testing.
        """
        # Create a client user and profile
        self.client_user = User.objects.create_user(username='clientuser', password='testpass', is_client=True)
        self.client_profile = Client.objects.create(user=self.client_user, phoneNumber="123456789")

        # Create a freelancer user and profile
        self.freelancer_user = User.objects.create_user(username='freelanceruser', password='testpass', is_freelancer=True)
        self.freelancer_profile = Freelancer.objects.create(user=self.freelancer_user, phoneNumber="987654321")

        # Create project complexity and project
        complexity = ProjectComplexity.objects.create(levelName="Simple", description="Simple project")
        self.project = Project.objects.create(
            title="Project Test",
            client=self.client_profile,
            complexity=complexity,
            budget=1000
        )

        # Create a project contributor (freelancer assigned to the project)
        self.project_contributor = ProjectContributor.objects.create(
            title="Contributor Test",
            project=self.project,
            freelancer=self.freelancer_profile,
            budget=500,
            version=1
        )

        # Authenticate freelancer for testing
        self.client.login(username='freelanceruser', password='testpass')

    def test_add_milestone_via_htmx(self):
        """
        Test creating a milestone via HTMX request.
        """
        url = reverse('addDeliverablesProject', args=[self.project_contributor.id])
        response = self.client.post(url, {'name': 'New Milestone'}, HTTP_HX_REQUEST='true')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Milestone.objects.filter(name="New Milestone", projectContributor=self.project_contributor).exists())

    def test_add_deliverable_with_empty_name(self):
        """
        Test that milestones with an empty name are not created.
        """
        url = reverse('addDeliverablesProject', args=[self.project_contributor.id])
        response = self.client.post(url, {'name': '', 'description': 'Test description', 'deadlineInDays': 5, 'requiresEvidence': True}, HTTP_HX_REQUEST='true')
        self.assertEqual(response.status_code, 200)  # Expect validation error response
        self.assertFalse(Milestone.objects.filter(name="").exists())

    def test_add_deliverable_with_negative_deadline(self):
        """
        Test that milestones with a negative deadline are not created.
        """
        url = reverse('addDeliverablesProject', args=[self.project_contributor.id])
        response = self.client.post(url, {'name': 'Negative Deadline', 'description': 'Test description', 'deadlineInDays': -5, 'requiresEvidence': True}, HTTP_HX_REQUEST='true')
        self.assertEqual(response.status_code, 200)  # Expect validation error
        self.assertFalse(Milestone.objects.filter(name="Negative Deadline").exists())

    def test_add_deliverable_not_authenticated(self):
        """
        Test that unauthenticated users cannot create milestones.
        """
        self.client.logout()
        url = reverse('addDeliverablesProject', args=[self.project_contributor.id])
        response = self.client.post(url, {'name': 'Unauthenticated Milestone'}, HTTP_HX_REQUEST='true')
        self.assertEqual(response.status_code, 302)  # Redirect to login
        self.assertFalse(Milestone.objects.filter(name="Unauthenticated Milestone").exists())

    def test_add_deliverable_not_contributor(self):
        """
        Test that freelancers not assigned to the project cannot create milestones.
        """
        # Create another freelancer
        other_freelancer_user = User.objects.create_user(username='otherfreelancer', password='testpass', is_freelancer=True)
        self.client.login(username='otherfreelancer', password='testpass')
        url = reverse('addDeliverablesProject', args=[self.project_contributor.id])
        response = self.client.post(url, {'name': 'Unauthorized Milestone'}, HTTP_HX_REQUEST='true')
        self.assertEqual(response.status_code, 403)  # Forbidden
        self.assertFalse(Milestone.objects.filter(name="Unauthorized Milestone").exists())

    def test_add_deliverable_duplicate(self):
        """
        Test that duplicate milestones cannot be created for the same project contributor.
        """
        # Create an existing milestone
        Milestone.objects.create(name='Duplicate Milestone', projectContributor=self.project_contributor)
        url = reverse('addDeliverablesProject', args=[self.project_contributor.id])
        response = self.client.post(url, {'name': 'Duplicate Milestone'}, HTTP_HX_REQUEST='true')
        self.assertEqual(response.status_code, 200)  # Expect validation error
        self.assertEqual(Milestone.objects.filter(name="Duplicate Milestone").count(), 1)
