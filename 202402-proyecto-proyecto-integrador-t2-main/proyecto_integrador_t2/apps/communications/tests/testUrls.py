from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apps.communications.views import (
    freelancerMessageHome,
    clientMessageHome,
    freelancerMessage,
    clientMessage,
    clientCreateComprobateChat,
    freelancerCreateComprobateChat,
)

class TestUrls(SimpleTestCase):
    """
    Pruebas para verificar que las URLs de la aplicación 'communications' se resuelven correctamente
    a las vistas correspondientes.
    """

    def testUrlFreelancerMessageHome(self):
        """
        Prueba que la URL 'freelancerMessageHome' resuelve correctamente a la vista freelancerMessageHome.
        """
        url = reverse('freelancerMessageHome')
        self.assertEqual(resolve(url).func, freelancerMessageHome)

    def testUrlClientMessageHome(self):
        """
        Prueba que la URL 'clientMessageHome' resuelve correctamente a la vista clientMessageHome.
        """
        url = reverse('clientMessageHome')
        self.assertEqual(resolve(url).func, clientMessageHome)

    def testUrlFreelancerMessage(self):
        """
        Prueba que la URL 'freelancerMessage' resuelve correctamente a la vista freelancerMessage.
        """
        url = reverse('freelancerMessage', args=['testChatName'])
        self.assertEqual(resolve(url).func, freelancerMessage)

    def testUrlClientMessage(self):
        """
        Prueba que la URL 'clientMessage' resuelve correctamente a la vista clientMessage.
        """
        url = reverse('clientMessage', args=['testChatName'])
        self.assertEqual(resolve(url).func, clientMessage)

    def testUrlClientCreateComprobateChat(self):
        """
        Prueba que la URL 'clientCreateComprobateChat' resuelve correctamente a la vista clientCreateComprobateChat.
        """
        url = reverse('clientCreateComprobateChat', args=['testUsername'])
        self.assertEqual(resolve(url).func, clientCreateComprobateChat)

    def testUrlFreelancerCreateComprobateChat(self):
        """
        Prueba que la URL 'freelancerCreateComprobateChat' resuelve correctamente a la vista freelancerCreateComprobateChat.
        """
        url = reverse('freelancerCreateComprobateChat', args=['testUsername'])
        self.assertEqual(resolve(url).func, freelancerCreateComprobateChat)
