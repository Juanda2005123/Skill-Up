from django.test import TestCase, Client
from django.urls import reverse
from apps.accounts.models import Userk
from apps.accounts.forms import SignUpFormFreelancer


class testViews(TestCase):
    """
    Clase de prueba para las vistas y formularios en la aplicación de cuentas.
    """

    def setUp(self):
        """
        Configuración inicial para las pruebas:
        - Crea un cliente para simular solicitudes HTTP.
        - Crea un usuario de prueba con credenciales específicas.
        """
        self.client = Client()
        self.user = Userk.objects.create_user(username='testuser', password='password123')

    def test_login_view_GET(self):
        """
        Verifica que la vista de inicio de sesión sea accesible con una solicitud GET.
        - Comprueba que la respuesta tenga un código de estado 200.
        - Verifica que se cargue la plantilla correcta ('accounts/login.html').
        """
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_login_invalid_user_view_POST(self):
        """
        Simula un intento de inicio de sesión con credenciales incorrectas.
        - Comprueba que la respuesta tenga un código de estado 200 (no redirige).
        - Verifica que se siga mostrando la plantilla de inicio de sesión ('accounts/login.html').
        """
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_login_view_POST(self):
        """
        Simula un intento de inicio de sesión con credenciales válidas.
        - Verifica que el usuario sea redirigido a la vista correspondiente ('clientProject').
        - Comprueba que la respuesta tenga un código de redirección 302.
        """
        response = self.client.post(reverse('login'), {
            'username': 'c',
            'password': 'client0105'
        })
        print(response.content)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('clientProject'))
    
    def test_signup_form_not_valid_data(self):
        """
        Verifica que el formulario de registro no sea válido con una contraseña común.
        - Utiliza el formulario 'SignUpFormFreelancer' con datos de prueba.
        - Comprueba que el formulario no pase la validación debido a la contraseña común.
        """
        form = SignUpFormFreelancer(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password1': 'password123',
            'password2': 'password123',
            'identification': '123456789',
            'phoneNumber': '555-5555'
        })
        print("Is not valid cos password is too common")
        self.assertFalse(form.is_valid())

    def test_signup_form_valid_data(self):
        """
        Verifica que el formulario de registro sea válido con datos correctos.
        - Utiliza el formulario 'SignUpFormFreelancer' con datos de prueba válidos.
        - Comprueba que el formulario pase la validación correctamente.
        """
        form = SignUpFormFreelancer(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password1': 'EySiMrJohn095',
            'password2': 'EySiMrJohn095',
            'identification': '123456789',
            'phoneNumber': '555-5555'
        })
        print("It should be valid")
        self.assertTrue(form.is_valid())
