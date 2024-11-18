from django.test import TestCase
from django.test import Client as TestClient
from django.urls import reverse
from apps.accounts.models import Userk
from django.core import mail

class TestRecoverMyAccount(TestCase):
    """
    Clase de pruebas para verificar el proceso de recuperación de contraseñas.
    Incluye pruebas para la recuperación, confirmación y finalización del restablecimiento.
    """

    def setUp(self):
        """
        Configuración inicial para las pruebas.
        Crea un cliente de prueba y un usuario para verificar la recuperación de contraseña.
        """
        self.client = TestClient()
        self.landPage = reverse('recoverPassword')
        self.passwordResetDone = reverse('password_reset_done')
        self.passwordResetConfirm = reverse('password_reset_confirm', kwargs={'uidb64': 'testuid', 'token': 'testtoken'})
        self.passwordResetComplete = reverse('password_reset_complete')
        self.user = Userk.objects.create_user(username='testuser', email='testuser@example.com', password='password123')

    def testRecoverPasswordPageAccess(self):
        """
        Verifica que la página de recuperación de contraseña se cargue correctamente.
        """
        response = self.client.get(self.landPage)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/recoverPassword.html')

    def testRecoverPasswordSentPageAccess(self):
        """
        Verifica que la página de confirmación de envío de recuperación de contraseña se cargue correctamente.
        """
        response = self.client.get(self.passwordResetDone)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/recoverPasswordSent.html')

    def testRecoverPasswordEmailSent(self):
        """
        Verifica que se envíe un correo electrónico después de solicitar el restablecimiento de contraseña.
        """
        response = self.client.post(self.landPage, {'email': 'testuser@example.com'})
        self.assertEqual(response.status_code, 302)  # Redirección después de enviar el correo
        self.assertRedirects(response, self.passwordResetDone)
        self.assertEqual(len(mail.outbox), 1)  # Comprueba que se ha enviado un correo
        self.assertIn('Password reset', mail.outbox[0].subject)

    def testPasswordResetConfirmPageAccess(self):
        """
        Verifica que la página de confirmación de restablecimiento de contraseña se cargue correctamente.
        """
        response = self.client.get(self.passwordResetConfirm)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/recoverPasswordForm.html')

    def testPasswordResetCompletePageAccess(self):
        """
        Verifica que la página de finalización del restablecimiento de contraseña se cargue correctamente.
        """
        response = self.client.get(self.passwordResetComplete)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/recoverPasswordDone.html')

    def testValidPasswordReset(self):
        """
        Verifica el proceso completo de restablecimiento de contraseña.
        Incluye:
        - Solicitud de restablecimiento.
        - Confirmación del enlace recibido por correo.
        - Restablecimiento exitoso de la contraseña.
        """
        # Solicita la recuperación de contraseña
        response = self.client.post(self.landPage, {'email': 'testuser@example.com'})
        
        # Comprueba que se haya enviado el correo de restablecimiento
        self.assertEqual(len(mail.outbox), 1)
        resetEmail = mail.outbox[0]
        
        # Extrae el enlace de restablecimiento de contraseña del cuerpo del correo
        resetLink = None
        for line in resetEmail.body.splitlines():
            if "http" in line:
                resetLink = line
                break

        # Verifica que se haya encontrado el enlace
        self.assertIsNotNone(resetLink)
        
        # Extrae uidb64 y token del enlace
        path = resetLink.split('/')[-2:]  # Debería devolver [uidb64, token]
        if len(path) != 2:
            self.fail("No se pudieron extraer correctamente el uidb64 y el token del enlace")

        uidb64, token = path
        
        # Simula el restablecimiento de la contraseña con el token
        resetUrl = reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
        response = self.client.post(resetUrl, {'new_password1': 'password123', 'new_password2': 'password123'})
        
        # Verifica redirección tras el restablecimiento
        self.assertEqual(response.status_code, 302)

        # Comprueba que el usuario pueda iniciar sesión con la nueva contraseña
        user = Userk.objects.get(username='testuser')
        self.assertTrue(user.check_password('password123'))
