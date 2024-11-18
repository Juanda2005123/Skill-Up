from apps.projects.models import Deliverable, Project, ProjectContributor, Milestone, ProjectComplexity
from apps.accounts.models import Freelancer, Client, Userk
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class TestDeleteDeliverable(TestCase):
    def setUp(self):
        """
        Configuración inicial para las pruebas:
        - Crea un usuario cliente y freelancer.
        - Asocia un cliente a un proyecto con un contributor.
        - Crea un milestone y un deliverable para las pruebas.
        """
        # Crear usuario y cliente
        self.client_user = Userk.objects.create_user(username='clientuser', password='testpass', is_client=True)
        self.client_profile = Client.objects.create(user=self.client_user, phoneNumber="123456789")

        # Crear freelancer y proyecto
        self.freelancer_user = Userk.objects.create_user(username='freelanceruser', password='testpass', is_freelancer=True)
        self.freelancer_profile = Freelancer.objects.create(user=self.freelancer_user, phoneNumber="987654321")

        # Crear complejidad del proyecto
        complexity = ProjectComplexity.objects.create(levelName="Simple", description="Simple project")

        # Crear proyecto y contributor
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
        self.milestone = Milestone.objects.create(name="Milestone Test", projectContributor=self.project_contributor)

        # Crear Deliverable
        self.deliverable = Deliverable.objects.create(
            name="Deliverable to Delete",
            description="To be deleted",
            deadlineInDays=10,
            requiresEvidence=True,
            milestone=self.milestone
        )

    def test_delete_deliverable(self):
        """
        Prueba que un deliverable existente se puede eliminar correctamente.
        """
        url = reverse('deleteDeliverable', args=[self.deliverable.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Redirige correctamente
        self.assertFalse(Deliverable.objects.filter(id=self.deliverable.id).exists())

    def test_delete_deliverable_not_authenticated(self):
        """
        Prueba que un usuario no autenticado no pueda eliminar un deliverable.
        El sistema debe redirigir al usuario a la página de inicio de sesión.
        """
        # Cerrar sesión
        self.client.logout()
        url = reverse('deleteDeliverable', args=[self.deliverable.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Deliverable.objects.filter(id=self.deliverable.id).exists())

    def test_delete_deliverable_different_user(self):
        """
        Prueba que un usuario diferente al asociado al proyecto no pueda eliminar un deliverable.
        """
        # Crear un usuario diferente
        other_user = Userk.objects.create_user(username='otheruser', password='testpass', is_freelancer=True)
        self.client.login(username='otheruser', password='testpass')
        url = reverse('deleteDeliverable', args=[self.deliverable.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Deliverable.objects.filter(id=self.deliverable.id).exists())

    def test_delete_nonexistent_deliverable(self):
        """
        Prueba que el sistema devuelve un error 404 al intentar eliminar un deliverable inexistente.
        """
        nonexistent_id = 9999
        url = reverse('deleteDeliverable', args=[nonexistent_id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 404)

    def test_deliverable_association_with_milestone(self):
        """
        Prueba que un deliverable está correctamente asociado a un milestone antes de ser eliminado.
        """
        self.assertEqual(self.deliverable.milestone, self.milestone)
        url = reverse('deleteDeliverable', args=[self.deliverable.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Deliverable.objects.filter(id=self.deliverable.id).exists())

    def test_delete_deliverable_no_evidence_required(self):
        """
        Prueba que se pueda eliminar un deliverable que no requiere evidencia.
        """
        deliverable_no_evidence = Deliverable.objects.create(
            name="No Evidence Deliverable",
            description="No evidence required",
            deadlineInDays=5,
            requiresEvidence=False,
            milestone=self.milestone
        )
        url = reverse('deleteDeliverable', args=[deliverable_no_evidence.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Deliverable.objects.filter(id=deliverable_no_evidence.id).exists())
