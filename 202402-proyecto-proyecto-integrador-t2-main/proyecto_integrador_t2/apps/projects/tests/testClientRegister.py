from django.test import TestCase
from django.urls import reverse
from apps.accounts.models import Client, Userk

class ClientRegisterTests(TestCase):
    """
    Suite de pruebas para la funcionalidad de registro de clientes.
    """

    def setUp(self):
        """
        Configura el entorno de pruebas, incluyendo la URL de registro de clientes y los datos de prueba válidos.
        """
        self.client_register_url = reverse('client_register')  # Asegúrate de que este nombre coincide con tu configuración de URL
        self.valid_data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password1': 'StrongPassword123',
            'password2': 'StrongPassword123',
            'phoneNumber': '123456789',
            'taxId': 'TAX12345',
            'companyName': 'Test Company',
            'typeOfCompany': 'SaaS',
            'businessVertical': 'Software',
            'country': 'US',
            'city': 'New York',
            'address': '123 Test Street'
        }

    def testClientRegisterPageLoads(self):
        """
        Verifica que la página de registro de clientes cargue correctamente.
        """
        response = self.client.get(self.client_register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/clientRegister.html')

    def testClientRegisterValidPost(self):
        """
        Prueba que un formulario de registro de cliente válido cree correctamente los objetos Userk y Client.
        """
        response = self.client.post(self.client_register_url, self.valid_data)
        
        # Verifica que se hayan creado los objetos Userk y Client
        self.assertEqual(Userk.objects.count(), 1)
        self.assertEqual(Client.objects.count(), 1)
        
        # Verifica que la respuesta sea una redirección (indicando éxito en el registro)
        self.assertEqual(response.status_code, 302)

        # Valida los datos del objeto Client creado
        client = Client.objects.first()
        self.assertEqual(client.user.username, 'testuser')
        self.assertEqual(client.phoneNumber, '123456789')
        self.assertEqual(client.companyName, 'Test Company')

    def testClientRegisterInvalidPost(self):
        """
        Verifica que los errores de validación sean manejados correctamente.
        Por ejemplo, cuando las contraseñas no coinciden.
        """
        invalid_data = self.valid_data.copy()
        invalid_data['password2'] = 'WrongPassword'
        
        response = self.client.post(self.client_register_url, invalid_data)
        
        # Verifica que no se hayan creado objetos Userk ni Client
        self.assertEqual(Userk.objects.count(), 0)
        self.assertEqual(Client.objects.count(), 0)
        
        # Verifica que el formulario devuelva un error y permanezca en la misma página
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'password2', 'The two password fields didn’t match.')

    def testRequiredFields(self):
        """
        Verifica que todos los campos requeridos en el formulario de registro sean validados correctamente.
        """
        required_fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'phoneNumber', 'taxId', 'companyName', 'typeOfCompany', 'businessVertical', 'country', 'city', 'address']
        
        for field in required_fields:
            data = self.valid_data.copy()
            data[field] = ''  # Elimina el campo requerido
            
            response = self.client.post(self.client_register_url, data)
            
            # Verifica que la respuesta permanezca en la página de registro y muestre un error
            self.assertEqual(response.status_code, 200)
            self.assertFormError(response, 'form', field, 'This field is required.')
