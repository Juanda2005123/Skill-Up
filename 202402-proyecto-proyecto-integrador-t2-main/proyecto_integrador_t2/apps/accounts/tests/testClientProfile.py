from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.storage import default_storage
from django.contrib.auth import get_user_model
from apps.accounts.models import Client

User = get_user_model()

class ClientProfileTest(TestCase):
    def setUp(self):
        """
        Configura los datos iniciales para las pruebas.
        Crea un usuario cliente para las pruebas de perfil.
        """
        self.client_user = User.objects.create_user(username='clientuser', password='testpass', is_client=True)
        self.client_profile = Client.objects.create(user=self.client_user, phoneNumber="987654321", taxId="123101")

        self.client_url = reverse('clientProfile')

        self.client.login(username='clientuser', password='testpass')

    def testGetClientProfile(self):
        """
        Verifica que la página de configuración del perfil de freelancer se carga correctamente.
        """
        response = self.client.get(self.client_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/clientProfile.html')

    def testRedirectUnauthenticatedUser(self):
        """Prueba que los usuarios no autenticados sean redirigidos a la página de inicio de sesión."""
        self.client.logout()
        response = self.client.get(self.client_url)
        self.assertRedirects(response, f"{reverse('login')}?next={self.client_url}")

    def testUpdateClientProfile(self):
        """Verifica que se puedan actualizar los datos del perfil del cliente."""
        new_data = {
            "phoneNumber": "111222333",  # Enviado como cadena (lo que hace el formulario)
            "description_company": "Updated description",
        }
        response = self.client.post(self.client_url, new_data)
        self.assertEqual(response.status_code, 302)  # Redirección después de guardar

        # Refresca el objeto de la base de datos
        self.client_profile.refresh_from_db()

        # Convierte a entero para comparar con el modelo
        self.assertEqual(self.client_profile.phoneNumber, int(new_data["phoneNumber"]))
        self.assertEqual(self.client_profile.description_company, new_data["description_company"])

    def testInvalidFileUpload(self):
        """Prueba que no se permita subir un archivo no válido."""
        invalid_file = SimpleUploadedFile("test.txt", b"invalid content", content_type="text/plain")
        response = self.client.post(self.client_url, {"profile_pic": invalid_file})
        self.assertEqual(response.status_code, 200)
        self.assertIn("profile_pic", response.context["form"].errors)

