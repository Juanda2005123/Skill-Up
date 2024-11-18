from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.projects.models import Project, ProjectComplexity, ProjectSkillExpertise, ProjectContributor
from apps.accounts.models import Freelancer, Client as ClientModel

User = get_user_model()

class TestBrowseProjects(TestCase):
    """
    Test suite for browsing projects as a freelancer and filtering or sorting them.
    """

    def setUp(self):
        """
        Set up test data including users, freelancer and client profiles, projects, and test authentication.
        """
        # Create freelancer and client users
        self.freelancer_user = User.objects.create_user(username="freelancer1", password="testpassword", is_freelancer=True)
        self.client_user = User.objects.create_user(username="client1", password="clientpassword", is_client=True)

        # Create Freelancer and Client instances
        self.freelancer = Freelancer.objects.create(user=self.freelancer_user, phoneNumber="123456789", identification="1234")
        self.client = ClientModel.objects.create(user=self.client_user, phoneNumber="987654321", taxId="5678", companyName="Test Client Co")

        # Create ProjectComplexity and ProjectSkillExpertise instances
        self.complexity = ProjectComplexity.objects.create(levelName="Intermediate", description="Medium complexity")
        self.skill_expertise = ProjectSkillExpertise.objects.create(name="Python")

        # Create test projects
        self.project1 = Project.objects.create(
            title="Project A",
            description="Description for project A",
            requiredPosition="Developer",
            daysDuration=30,
            budget="1500.00",
            complexity=self.complexity,
            client=self.client,
        )
        self.project1.skillExpertises.add(self.skill_expertise)

        self.project2 = Project.objects.create(
            title="Project B",
            description="Description for project B",
            requiredPosition="Designer",
            daysDuration=60,
            budget="2500.00",
            complexity=self.complexity,
            client=self.client,
        )
        self.project2.skillExpertises.add(self.skill_expertise)

        # Authenticate freelancer in the test client
        self.client = Client()
        self.client.login(username="freelancer1", password="testpassword")

    def test_browse_projects(self):
        """
        Test that the `browseProjects` view lists all available projects for freelancers.
        """
        url = reverse("browseProject")
        response = self.client.get(url)

        # Assert response status and that projects are in context
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.project1, response.context["projects"])
        self.assertIn(self.project2, response.context["projects"])

    def test_browse_projects_with_filtering(self):
        """
        Test filtering or sorting projects in the `browseProjects` view.
        """
        url = reverse("browseProject")
        response = self.client.get(url, {"sort_by": "title"})

        # Assert response status and sorted order
        self.assertEqual(response.status_code, 200)
        projects = response.context["projects"]
        self.assertEqual(projects[0].title, "Project A")
        self.assertEqual(projects[1].title, "Project B")

    def test_browse_own_projects(self):
        """
        Test that the `browseOwnProjects` view lists only approved projects for the freelancer.
        """
        # Create an approved ProjectContributor for `project1`
        ProjectContributor.objects.create(
            title="Contributor for Project A",
            requiredPosition="Developer",
            budget=1200.00,
            complexity=self.complexity,
            project=self.project1,
            freelancer=self.freelancer,
            approval_status="approved",
            version=1
        )

        url = reverse("browseOwnProjects")
        response = self.client.get(url)

        # Assert response status and approved project in context
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.project1, response.context["projects"])
        self.assertNotIn(self.project2, response.context["projects"])

    def test_browse_own_projects_not_approved(self):
        """
        Test that `browseOwnProjects` does not include unapproved projects.
        """
        # Create an unapproved ProjectContributor for `project2`
        ProjectContributor.objects.create(
            title="Contributor for Project B",
            requiredPosition="Developer",
            budget=1200.00,
            complexity=self.complexity,
            project=self.project2,
            freelancer=self.freelancer,
            approval_status="pending",
            version=1
        )

        url = reverse("browseOwnProjects")
        response = self.client.get(url)

        # Assert response status and unapproved project exclusion
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(self.project2, response.context["projects"])

    def test_browse_own_projects_with_sorting(self):
        """
        Test sorting functionality in `browseOwnProjects` view.
        """
        # Create approved ProjectContributors for both projects
        ProjectContributor.objects.create(
            title="Contributor for Project A",
            requiredPosition="Developer",
            budget=1500.00,
            complexity=self.complexity,
            project=self.project1,
            freelancer=self.freelancer,
            approval_status="approved",
            version=1
        )

        ProjectContributor.objects.create(
            title="Contributor for Project B",
            requiredPosition="Designer",
            budget=2000.00,
            complexity=self.complexity,
            project=self.project2,
            freelancer=self.freelancer,
            approval_status="approved",
            version=1
        )

        url = reverse("browseOwnProjects")
        response = self.client.get(url, {"sort_by": "title"})

        # Assert response status and sorted project order
        self.assertEqual(response.status_code, 200)
        projects = response.context["projects"]
        self.assertEqual(projects[0].title, "Project A")
        self.assertEqual(projects[1].title, "Project B")
