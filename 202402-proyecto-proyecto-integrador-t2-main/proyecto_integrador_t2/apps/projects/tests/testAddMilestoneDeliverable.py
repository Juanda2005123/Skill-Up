from apps.projects.models import Deliverable, Project, ProjectContributor, Milestone, ProjectComplexity
from apps.accounts.models import Freelancer, Client, Userk
from django.test import TestCase
from django.urls import reverse

class TestAddMilestoneDeliverable(TestCase):
    """
    Test suite for adding deliverables to milestones within projects.
    """

    def setUp(self):
        """
        Set up the necessary data for testing, including users, project, milestone, and contributor.
        """
        # Create client user and profile
        self.client_user = Userk.objects.create_user(username='clientuser', password='testpass', is_client=True)
        self.client_profile = Client.objects.create(user=self.client_user, phoneNumber="123456789")

        # Create freelancer user and profile
        self.freelancer_user = Userk.objects.create_user(username='freelanceruser', password='testpass', is_freelancer=True)
        self.freelancer_profile = Freelancer.objects.create(user=self.freelancer_user, phoneNumber="987654321")

        # Create project complexity and project
        complexity = ProjectComplexity.objects.create(levelName="Simple", description="Simple project")
        self.project = Project.objects.create(
            title="Project Test",
            client=self.client_profile,
            complexity=complexity,
            budget=1000
        )

        # Create project contributor
        self.project_contributor = ProjectContributor.objects.create(
            title="Contributor Test",
            project=self.project,
            freelancer=self.freelancer_profile,
            budget=500,
            version=1
        )

        # Create milestone associated with the contributor
        self.milestone = Milestone.objects.create(name="Milestone Test", projectContributor=self.project_contributor)

        # Log in as the freelancer
        self.client.login(username='freelanceruser', password='testpass')

    def test_add_deliverable(self):
        """
        Test that a valid deliverable can be successfully added to a milestone.
        """
        url = reverse('addMilestoneDeliverable', args=[self.milestone.id])
        response = self.client.post(url, {
            'name': 'New Deliverable',
            'description': 'Description',
            'deadlineInDays': 5,
            'requiresEvidence': True
        })
        self.assertEqual(response.status_code, 302)  # Redirect to the next step
        self.assertTrue(Deliverable.objects.filter(name="New Deliverable", milestone=self.milestone).exists())

    def test_add_deliverable_not_authenticated(self):
        """
        Test that unauthenticated users cannot add deliverables.
        """
        self.client.logout()
        url = reverse('addMilestoneDeliverable', args=[self.milestone.id])
        response = self.client.post(url, {
            'name': 'Deliverable Unauthenticated',
            'description': 'Should not be added',
            'deadlineInDays': 3,
            'requiresEvidence': True
        })
        self.assertEqual(response.status_code, 302)  # Redirect to login
        self.assertFalse(Deliverable.objects.filter(name="Deliverable Unauthenticated").exists())

    def test_add_deliverable_without_permission(self):
        """
        Test that a user who is not a contributor to the milestone cannot add deliverables.
        """
        other_user = Userk.objects.create_user(username='otheruser', password='testpass', is_freelancer=True)
        self.client.login(username='otheruser', password='testpass')
        url = reverse('addMilestoneDeliverable', args=[self.milestone.id])
        response = self.client.post(url, {
            'name': 'Unauthorized Deliverable',
            'description': 'Should not be added',
            'deadlineInDays': 3,
            'requiresEvidence': True
        })
        self.assertEqual(response.status_code, 403)  # Forbidden
        self.assertFalse(Deliverable.objects.filter(name="Unauthorized Deliverable").exists())

    def test_add_deliverable_without_name(self):
        """
        Test that a deliverable without a name cannot be added.
        """
        url = reverse('addMilestoneDeliverable', args=[self.milestone.id])
        response = self.client.post(url, {
            'name': '',
            'description': 'No name provided',
            'deadlineInDays': 4,
            'requiresEvidence': False
        })
        self.assertEqual(response.status_code, 400)  # Bad Request
        self.assertFalse(Deliverable.objects.filter(description="No name provided").exists())

    def test_add_deliverable_with_negative_deadline(self):
        """
        Test that a deliverable with a negative deadline cannot be added.
        """
        url = reverse('addMilestoneDeliverable', args=[self.milestone.id])
        response = self.client.post(url, {
            'name': 'Negative Deadline Deliverable',
            'description': 'Invalid deadline',
            'deadlineInDays': -5,
            'requiresEvidence': True
        })
        self.assertEqual(response.status_code, 400)  # Bad Request
        self.assertFalse(Deliverable.objects.filter(name="Negative Deadline Deliverable").exists())

    def test_add_duplicate_deliverable(self):
        """
        Test that duplicate deliverables with the same name in the same milestone cannot be added.
        """
        # Create an existing deliverable
        Deliverable.objects.create(
            name="Duplicate Deliverable",
            description="First instance",
            deadlineInDays=7,
            requiresEvidence=True,
            milestone=self.milestone
        )
        url = reverse('addMilestoneDeliverable', args=[self.milestone.id])
        response = self.client.post(url, {
            'name': 'Duplicate Deliverable',
            'description': 'Duplicate instance',
            'deadlineInDays': 7,
            'requiresEvidence': True
        })
        self.assertEqual(response.status_code, 400)  # Bad Request
        self.assertEqual(Deliverable.objects.filter(name="Duplicate Deliverable").count(), 1)
