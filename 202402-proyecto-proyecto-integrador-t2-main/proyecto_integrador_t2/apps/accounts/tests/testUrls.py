from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apps.accounts.views import *
from django.contrib.auth import views as auth_views

class TestUrls(SimpleTestCase):
    """
    Clase de pruebas para verificar el correcto mapeo de URLs a las vistas correspondientes.
    Esta clase valida que cada URL definida en el proyecto se resuelva correctamente 
    y apunte a la función de vista o clase esperada.
    """

    def testUrlLogin(self):
        """
        Verifica que la URL para el login ('login') resuelve a la función de vista `loginPage`.
        """
        url = reverse('login')
        self.assertEqual(resolve(url).func, loginPage)

    def testUrlLandpage(self):
        """
        Verifica que la URL para la página de inicio ('landpage') resuelve a la función de vista `landpage`.
        """
        url = reverse('landpage')
        self.assertEqual(resolve(url).func, landpage)

    def testUrlFreelancerRegister(self):
        """
        Verifica que la URL para el registro de freelancers ('freelancerRegister') resuelve a la función de vista `freelancerRegister`.
        """
        url = reverse('freelancerRegister')
        self.assertEqual(resolve(url).func, freelancerRegister)

    def testUrlClientRegister(self):
        """
        Verifica que la URL para el registro de clientes ('clientRegister') resuelve a la función de vista `clientRegister`.
        """
        url = reverse('clientRegister')
        self.assertEqual(resolve(url).func, clientRegister)

    def testUrlLogout(self):
        """
        Verifica que la URL para el logout ('logout') resuelve a la función de vista `logout`.
        """
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout)

    def testUrlClientProfile(self):
        """
        Verifica que la URL para el perfil de clientes ('clientProfile') resuelve a la función de vista `client_profile`.
        """
        url = reverse('clientProfile')
        self.assertEqual(resolve(url).func, client_profile)

    def testUrlFreelancerProfile(self):
        """
        Verifica que la URL para el perfil de freelancers ('freelancerProfile') resuelve a la función de vista `freelancer_profile`.
        """
        url = reverse('freelancerProfile', args=[1])
        self.assertEqual(resolve(url).func, freelancer_profile)
    
    def testUrlfprofileRequest(self):
        """
        Verifica que la URL para solicitar perfiles de freelancers ('fprofileRequest') 
        resuelve a la función de vista `fprofileRequest`.
        """
        url = reverse('fprofileRequest', args=[1, 2])
        self.assertEqual(resolve(url).func, fprofileRequest)

    def testUrlfreelancerProfileSettings(self):
        """
        Verifica que la URL para configurar el perfil de freelancers ('freelancerProfileSettings') 
        resuelve a la función de vista `freelancer_profile_settings`.
        """
        url = reverse('freelancerProfileSettings')
        self.assertEqual(resolve(url).func, freelancer_profile_settings)
    
    def test_recoverPassword_url_resolves(self):
        """
        Verifica que la URL para la recuperación de contraseña ('recoverPassword') 
        resuelve a la clase de vista `PasswordResetView`.
        """
        url = reverse('recoverPassword')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordResetView)

    def test_recoverPasswordSent_url_resolves(self):
        """
        Verifica que la URL para la confirmación del envío de recuperación de contraseña ('password_reset_done') 
        resuelve a la clase de vista `PasswordResetDoneView`.
        """
        url = reverse('password_reset_done')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordResetDoneView)

    def test_recoverPasswordConfirm_url_resolves(self):
        """
        Verifica que la URL para confirmar el restablecimiento de contraseña ('password_reset_confirm') 
        resuelve a la clase de vista `PasswordResetConfirmView`.
        """
        url = reverse('password_reset_confirm', args=['uidb64', 'token'])
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordResetConfirmView)

    def test_recoverPasswordDone_url_resolves(self):
        """
        Verifica que la URL para la finalización del restablecimiento de contraseña ('password_reset_complete') 
        resuelve a la clase de vista `PasswordResetCompleteView`.
        """
        url = reverse('password_reset_complete')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordResetCompleteView)
