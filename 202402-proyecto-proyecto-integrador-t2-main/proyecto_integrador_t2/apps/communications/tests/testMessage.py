from django.test import TestCase, Client as TestClient
from django.urls import reverse
from apps.accounts.models import *
from apps.communications.models import Chat, Message
from apps.communications.forms import ChatMessageCreateForm

class TestMessageViews(TestCase):
    """
    Clase para pruebas de vistas relacionadas con mensajes en los chats de clientes y freelancers.
    """

    def setUp(self):
        """
        Configuración inicial para las pruebas:
        - Creación de usuarios cliente y freelancer.
        - Creación de perfiles asociados (Client y Freelancer).
        - Creación de un chat y mensajes iniciales.
        """
        self.testClient = TestClient()

        # Crear usuarios y sus perfiles asociados
        self.clientUser = Userk.objects.create_user(username='clientUser', password='testpassword', is_client=True)
        self.freelancerUser = Userk.objects.create_user(username='freelancerUser', password='testpassword', is_freelancer=True)

        # Instancias de Client y Freelancer
        self.country = Country.objects.get(code="CO")  # Colombia
        self.city = City.objects.get(name="Bogotá", country=self.country)  # Ciudad en Colombia
        
        # Instancias de Client y Freelancer
        self.clientInstance = Client.objects.create(
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

        # Crear un chat entre el cliente y el freelancer con mensajes
        self.chat = Chat.objects.create(chatName='testChat', freelancer=self.freelancer, client=self.clientInstance)
        self.message1 = Message.objects.create(chat=self.chat, author=self.clientUser, body="the prex")
        self.message2 = Message.objects.create(chat=self.chat, author=self.freelancerUser, body="the message")

    def testClientMessageView(self):
        """
        Prueba que el cliente pueda ver los mensajes de un chat y el formulario de creación de mensajes.
        """
        self.testClient.login(username='clientUser', password='testpassword')
        response = self.testClient.get(reverse('clientMessage', args=['testChat']))

        self.assertEqual(response.status_code, 200)
        self.assertIn('chat', response.context)
        self.assertEqual(response.context['chat'], self.chat)
        self.assertIn('chatMessages', response.context)
        self.assertEqual(len(response.context['chatMessages']), 2)
        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], ChatMessageCreateForm)

    def testFreelancerMessageView(self):
        """
        Prueba que el freelancer pueda ver los mensajes de un chat y el formulario de creación de mensajes.
        """
        self.testClient.login(username='freelancerUser', password='testpassword')
        response = self.testClient.get(reverse('freelancerMessage', args=['testChat']))

        self.assertEqual(response.status_code, 200)
        self.assertIn('chat', response.context)
        self.assertEqual(response.context['chat'], self.chat)
        self.assertIn('chatMessages', response.context)
        self.assertEqual(len(response.context['chatMessages']), 2)
        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], ChatMessageCreateForm)

    def testCreateMessageInClientMessage(self):
        """
        Prueba que el cliente pueda crear un mensaje en el chat y que este se guarde correctamente.
        """
        self.testClient.login(username='clientUser', password='testpassword')
        messageData = {'body': 'the prex'}
        response = self.testClient.post(reverse('clientMessage', args=['testChat']), messageData)

        self.assertEqual(Message.objects.count(), 2)
        newMessage = Message.objects.filter(chat=self.chat, author=self.clientUser).order_by('timeCreated').last()
        self.assertEqual(newMessage.body, 'the prex')

    def testCreateMessageInFreelancerMessage(self):
        """
        Prueba que el freelancer pueda crear un mensaje en el chat y que este se guarde correctamente.
        """
        self.testClient.login(username='freelancerUser', password='testpassword')
        messageData = {'body': 'the message'}
        response = self.testClient.post(reverse('freelancerMessage', args=['testChat']), messageData)

        self.assertEqual(Message.objects.count(), 2)
        newMessage = Message.objects.filter(chat=self.chat, author=self.freelancerUser).order_by('timeCreated').last()
        self.assertEqual(newMessage.body, 'the message')

    def testMessageClientFormInTemplate(self):
        """
        Verifica que el formulario de creación de mensaje esté presente en la página de cliente.
        """
        self.testClient.login(username='clientUser', password='testpassword')
        response = self.testClient.get(reverse('clientMessage', args=['testChat']))
        self.assertContains(response, '<form')
        self.assertContains(response, 'name="body"')

    def testMessageFreelancerFormInTemplate(self):
        """
        Verifica que el formulario de creación de mensaje esté presente en la página de freelancer.
        """
        self.testClient.login(username='freelancerUser', password='testpassword')
        response = self.testClient.get(reverse('freelancerMessage', args=['testChat']))
        self.assertContains(response, '<form')
        self.assertContains(response, 'name="body"')
