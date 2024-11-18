from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import authenticate, get_user
from django.contrib import messages
from apps.accounts.models import Freelancer, Client, Userk

class LoginTests(TestCase):
    """
    Clase de pruebas unitarias para verificar el funcionamiento del sistema de inicio de sesión.
    """

    def setUp(self):
        """
        Configuración inicial para las pruebas.
        Crea usuarios cliente y freelancer con perfiles asociados.
        """
        # Crear un cliente
        self.client_user = Userk.objects.create_user(
            username='clientuser', 
            password='papasFritas123',
            is_active=True
        )
        # Establecer el atributo is_client en True
        self.client_user.is_client = True
        self.client_user.is_freelancer = False
        self.client_user.save()
        
        self.client_profile = Client.objects.create(user=self.client_user)
        
        # Crear un freelancer
        self.freelancer_user = Userk.objects.create_user(
            username='freelanceruser', 
            password='huevosFritos123',
            is_active=True
        )
        # Establecer el atributo is_freelancer en True
        self.freelancer_user.is_freelancer = True
        self.freelancer_user.is_client = False
        self.freelancer_user.save()
        
        self.freelancer_profile = Freelancer.objects.create(user=self.freelancer_user)
        
        # URL de inicio de sesión
        self.login_url = reverse('login')

    def test_login_page_loads_for_unauthenticated(self):
        """
        Verifica que la página de inicio de sesión carga correctamente para usuarios no autenticados.
        """
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_login_redirects_authenticated_client(self):
        """
        Verifica que un cliente autenticado sea redirigido a la página de clientProject.
        """
        self.client.login(username='clientuser', password='papasFritas123')
        response = self.client.get(self.login_url)
        self.assertRedirects(response, reverse('clientProject'))

    def test_client_login_success(self):
        """
        Verifica que un cliente puede iniciar sesión correctamente.
        """
        response = self.client.post(self.login_url, {
            'username': 'clientuser',
            'password': 'papasFritas123',
        })
        self.assertRedirects(response, reverse('dashboardClient'))
        
        # Verifica que el usuario está autenticado
        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)
        self.assertTrue(user.is_client)

    def test_freelancer_login_success(self):
        """
        Verifica que un freelancer puede iniciar sesión correctamente.
        """
        response = self.client.post(self.login_url, {
            'username': 'freelanceruser',
            'password': 'huevosFritos123',
        })
        self.assertRedirects(response, reverse('dashboardFreelancer'))
        
        # Verifica que el usuario está autenticado
        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)
        self.assertTrue(user.is_freelancer)

    def test_login_fail_invalid_credentials(self):
        """
        Verifica que el inicio de sesión falla si se proporcionan credenciales inválidas.
        """
        response = self.client.post(self.login_url, {
            'username': 'clientuser',
            'password': 'contraseñaIncorrecta',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        
        # Verifica que se muestra el mensaje de error correcto
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertTrue(any(message.message == 'Username or password is incorrect' 
                          for message in messages_list))

    def test_login_with_empty_fields(self):
        """
        Verifica que el inicio de sesión falla cuando los campos están vacíos.
        """
        response = self.client.post(self.login_url, {
            'username': '',
            'password': '',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        
        # Verifica que se muestra al menos un mensaje de error
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertTrue(len(messages_list) > 0)
