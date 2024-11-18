from django.test import TestCase, Client as TestClient  # Importa TestClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.accounts.models import *
from apps.communications.models import *

class TestCreateChat(TestCase):
    """
    Clase de pruebas para la creación y redirección de chats entre clientes y freelancers.
    """

    def setUp(self):
        """
        Configuración inicial de las pruebas:
        - Creación de usuarios cliente y freelancer.
        - Creación de instancias de perfil de cliente y freelancer.
        - Creación de un chat inicial para pruebas.
        """
        self.testClient = TestClient()
        self.clientUser = Userk.objects.create_user(username='clientUser', password='testPassword', is_client=True)
        self.freelancerUser = Userk.objects.create_user(username='freelancerUser', password='testPassword', is_freelancer=True)
        
        # Instancias de Client y Freelancer
        self.country = Country.objects.get(code="CO")  # Colombia
        self.city = City.objects.get(name="Bogotá", country=self.country)  # Ciudad en Colombia
        
        # Instancias de Client y Freelancer
        self.testClientInstance = Client.objects.create(
            user=self.clientUser,
            phoneNumber=123456789,
            taxId=1234567890,
            companyName='TestCompany',
            typeOfCompany='Software',
            businessVertical='IT',
            country=self.country,
            city=self.city,
            address='Av. El Dorado',
        )
        
        self.freelancer = Freelancer.objects.create(
            user=self.freelancerUser,
            phoneNumber='987654321',
            identification='0987654321',
            email='freelancer@example.com',
        )
        
        # Crear chat inicial
        self.chat = Chat.objects.create(
            chatName='testChat',
            freelancer=self.freelancer,
            client=self.testClientInstance
        )
        
        self.freelancerCreateChatUrl = reverse('freelancerCreateComprobateChat', args=[self.clientUser.username])
        self.clientCreateChatUrl = reverse('clientCreateComprobateChat', args=[self.freelancerUser.username])

    def testCreateNewChatForClient(self):
        """
        Prueba que un cliente cree un nuevo chat con un freelancer si no existe un chat previo.
        """
        self.testClient.login(username='clientUser', password='testPassword')  # Inicia sesión como cliente
        
        response = self.testClient.get(self.clientCreateChatUrl)  # Solicitar creación de chat
        
        chat = Chat.objects.filter(client=self.testClientInstance, freelancer=self.freelancer).first()
        self.assertIsNotNone(chat)  # Verifica que el chat se haya creado
        self.assertRedirects(response, reverse('clientMessage', args=[chat.chatName]))  # Redirección al chat

    def testRedirectToExistingChatForClient(self):
        """
        Prueba que un cliente sea redirigido a un chat existente sin crear uno nuevo.
        """
        existingChat = Chat.objects.filter(client=self.testClientInstance, freelancer=self.freelancer).first()
        
        self.testClient.login(username='clientUser', password='testPassword')  # Inicia sesión como cliente
        
        response = self.testClient.get(self.clientCreateChatUrl)  # Solicitar redirección al chat existente
        
        self.assertEqual(Chat.objects.filter(client=self.testClientInstance, freelancer=self.freelancer).count(), 1)  # Verifica que solo existe un chat
        self.assertRedirects(response, reverse('clientMessage', args=[existingChat.chatName]))  # Redirección al chat existente

    def testCreateNewChatForFreelancer(self):
        """
        Prueba que un freelancer cree un nuevo chat con un cliente si no existe un chat previo.
        """
        self.testClient.login(username='freelancerUser', password='testPassword')  # Inicia sesión como freelancer
        
        response = self.testClient.get(self.freelancerCreateChatUrl)  # Solicitar creación de chat
        
        chat = Chat.objects.filter(client=self.testClientInstance, freelancer=self.freelancer).first()
        self.assertIsNotNone(chat)  # Verifica que el chat se haya creado
        self.assertRedirects(response, reverse('freelancerMessage', args=[chat.chatName]))  # Redirección al chat

    def testRedirectToExistingChatForFreelancer(self):
        """
        Prueba que un freelancer sea redirigido a un chat existente sin crear uno nuevo.
        """
        existingChat = Chat.objects.filter(client=self.testClientInstance, freelancer=self.freelancer).first()
        
        self.testClient.login(username='freelancerUser', password='testPassword')  # Inicia sesión como freelancer
        
        response = self.testClient.get(self.freelancerCreateChatUrl)  # Solicitar redirección al chat existente
        
        self.assertEqual(Chat.objects.filter(client=self.testClientInstance, freelancer=self.freelancer).count(), 1)  # Verifica que solo existe un chat
        self.assertRedirects(response, reverse('freelancerMessage', args=[existingChat.chatName]))  # Redirección al chat existente
