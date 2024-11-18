from django.test import TestCase
from django.urls import reverse
from apps.accounts.models import Freelancer, Userk
from apps.accounts.forms import SignUpFormFreelancer

class FreelancerRegisterTests(TestCase):
    """
    Clase de pruebas para el registro de freelancers.
    Esta clase verifica que el formulario de registro funcione correctamente, maneje validaciones y cree los objetos necesarios.
    """

    def setUp(self):
        """
        Configuración inicial para las pruebas.
        Define la URL del registro y un conjunto de datos válidos para un freelancer.
        """
        self.freelancer_register_url = reverse('freelancerRegister')  # URL para el registro de freelancers
        self.valid_data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password1': 'TestPass123#',
            'password2': 'TestPass123#',
            'phoneNumber': '123456789',
            'identification': '1005967728',
        }

    def testFreelancerRegisterPageLoads(self):
        """
        Verifica que la página de registro de freelancers carga correctamente.
        Comprueba que:
        - El código de estado HTTP es 200.
        - La plantilla usada es 'accounts/freelancerRegister.html'.
        - El formulario en el contexto es una instancia de `SignUpFormFreelancer`.
        """
        response = self.client.get(self.freelancer_register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/freelancerRegister.html')
        self.assertTrue(isinstance(response.context['form'], SignUpFormFreelancer))

    def testFreelancerRegisterValidPost(self):
        """
        Verifica que un freelancer válido se registre correctamente.
        Comprueba que:
        - Se crea un objeto `Userk` y un objeto `Freelancer`.
        - El código de estado HTTP después del registro es 302 (redirección).
        - Los datos del freelancer se guardan correctamente.
        - El usuario asociado tiene `is_freelancer=True`.
        """
        response = self.client.post(self.freelancer_register_url, self.valid_data)
        
        # Verificar creación de objetos
        self.assertEqual(Userk.objects.count(), 1)
        self.assertEqual(Freelancer.objects.count(), 1)
        
        # Verificar redirección tras registro
        self.assertEqual(response.status_code, 302)

        # Verificar que los datos se guardaron correctamente
        freelancer = Freelancer.objects.first()
        self.assertEqual(freelancer.user.username, self.valid_data['username'])
        self.assertEqual(freelancer.user.first_name, self.valid_data['first_name'])
        self.assertEqual(freelancer.user.last_name, self.valid_data['last_name'])
        self.assertEqual(freelancer.user.email, self.valid_data['email'])
        self.assertEqual(freelancer.phoneNumber, self.valid_data['phoneNumber'])
        self.assertEqual(freelancer.identification, self.valid_data['identification'])
        self.assertTrue(freelancer.user.is_freelancer)

    def testFreelancerRegisterInvalidPasswordPost(self):
        """
        Verifica que los errores de validación se manejen correctamente en caso de contraseñas no coincidentes.
        Comprueba que:
        - No se crea ningún objeto `Userk` ni `Freelancer`.
        - Se retorna el código de estado HTTP 200 (misma página con errores).
        - Se utiliza la plantilla 'accounts/freelancerRegister.html'.
        """
        invalid_data = self.valid_data.copy()
        invalid_data['password2'] = 'WrongPassword'
        
        response = self.client.post(self.freelancer_register_url, invalid_data)
        
        # Verificar que no se crearon objetos
        self.assertEqual(Userk.objects.count(), 0)
        self.assertEqual(Freelancer.objects.count(), 0)
        
        # Verificar que se muestran errores en el formulario
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/freelancerRegister.html')
