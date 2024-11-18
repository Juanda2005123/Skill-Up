from apps.projects.models import Deliverable, Project, ProjectContributor, Milestone, ProjectComplexity
from apps.accounts.models import Freelancer, Client, Userk
from django.test import TestCase
from django.urls import reverse

class TestDeleteMilestone(TestCase):
    def setUp(self):
        """
        Configuración inicial para las pruebas:
        - Crea un usuario cliente y freelancer.
        - Asocia un cliente a un proyecto con un contribuidor.
        - Crea un milestone para realizar pruebas de eliminación.
        """
        # Crear usuario y cliente
        self.client_user = Userk.objects.create_user(username='clientuser', password='testpass', is_client=True)
        self.client_profile = Client.objects.create(user=self.client_user, phoneNumber="123456789")

        # Crear freelancer y proyecto
        self.freelancer_user = Userk.objects.create_user(username='freelanceruser', password='testpass', is_freelancer=True)
        self.freelancer_profile = Freelancer.objects.create(user=self.freelancer_user, phoneNumber="987654321")

        # Crear complejidad del proyecto
        complexity = ProjectComplexity.objects.create(levelName="Simple", description="Simple project")

        # Crear proyecto y contribuidor
        self.project = Project.objects.create(
            title="Project Test",
            client=self.client_profile,
            complexity=complexity,
            budget=1000
        )
        self.project_contributor = ProjectContributor.objects.create(
            title="Contributor Test",
            project=self.project,
            freelancer=self.freelancer_profile,
            budget=500,
            version=1
        )

        # Iniciar sesión como freelancer
        self.client.login(username='freelanceruser', password='testpass')

        # Crear Milestone
        self.milestone = Milestone.objects.create(name="Milestone to Delete", projectContributor=self.project_contributor)

    def test_delete_milestone(self):
        """
        Prueba que un milestone existente se puede eliminar correctamente.
        """
        url = reverse('deleteMilestone', args=[self.milestone.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Redirige correctamente
        self.assertFalse(Milestone.objects.filter(id=self.milestone.id).exists())

    def test_delete_milestone_not_authenticated(self):
        """
        Prueba que un usuario no autenticado no pueda eliminar un milestone.
        El sistema debe redirigir al usuario a la página de inicio de sesión.
        """
        # Cerrar sesión
        self.client.logout()
        url = reverse('deleteMilestone', args=[self.milestone.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Milestone.objects.filter(id=self.milestone.id).exists())

    def test_delete_milestone_different_user(self):
        """
        Prueba que un usuario diferente al contribuidor asociado no pueda eliminar un milestone.
        """
        # Crear un usuario diferente
        other_user = Userk.objects.create_user(username='otheruser', password='testpass', is_freelancer=True)
        self.client.login(username='otheruser', password='testpass')
        url = reverse('deleteMilestone', args=[self.milestone.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Milestone.objects.filter(id=self.milestone.id).exists())

    def test_delete_milestone_with_associated_deliverables(self):
        """
        Prueba que al eliminar un milestone, también se eliminen sus deliverables asociados.
        """
        # Crear un Deliverable asociado al Milestone
        deliverable = Deliverable.objects.create(
            name="Deliverable for Milestone",
            description="Associated deliverable",
            deadlineInDays=5,
            requiresEvidence=True,
            milestone=self.milestone
        )
        url = reverse('deleteMilestone', args=[self.milestone.id])
        response = self.client.post(url)
        # Verificar que el Milestone y sus Deliverables hayan sido eliminados
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Milestone.objects.filter(id=self.milestone.id).exists())
        self.assertFalse(Deliverable.objects.filter(id=deliverable.id).exists())

    def test_delete_nonexistent_milestone(self):
        """
        Prueba que el sistema devuelve un error 404 al intentar eliminar un milestone inexistente.
        """
        nonexistent_id = 9999
        url = reverse('deleteMilestone', args=[nonexistent_id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 404)

    def test_delete_milestone_different_contributor(self):
        """
        Prueba que un freelancer no pueda eliminar un milestone asociado a otro contribuidor.
        """
        # Crear un segundo contribuidor y milestone asociado
        other_contributor = ProjectContributor.objects.create(
            title="Second Contributor",
            project=self.project,
            freelancer=self.freelancer_profile,
            budget=300,
            version=1
        )
        milestone_other = Milestone.objects.create(name="Other Contributor Milestone", projectContributor=other_contributor)

        # Intentar eliminar el milestone del otro contribuidor usando el freelancer actual
        url = reverse('deleteMilestone', args=[milestone_other.id])
        response = self.client.post(url)
        # Verificar que el freelancer actual no puede eliminar el milestone de otro contribuidor
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Milestone.objects.filter(id=milestone_other.id).exists())
