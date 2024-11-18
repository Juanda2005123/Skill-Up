from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apps.notifications.views import NotificationList, MarkAsReadView, NotificationDetailView

class TestUrls(SimpleTestCase):
    """
    Clase para probar la resolución de URLs relacionadas con las notificaciones.
    """

    def testUrlNotificationList(self):
        """
        Verifica que la URL de la lista de notificaciones resuelve a la clase `NotificationList`.
        """
        url = reverse('notifications')
        self.assertEqual(resolve(url).func.view_class, NotificationList)

    def testUrlMarkAsRead(self):
        """
        Verifica que la URL para marcar una notificación como leída resuelve a la clase `MarkAsReadView`.
        """
        url = reverse('mark_as_read', args=[1])  # Usa un ID de ejemplo (1)
        self.assertEqual(resolve(url).func.view_class, MarkAsReadView)

    def testUrlNotificationDetail(self):
        """
        Verifica que la URL del detalle de la notificación resuelve a la clase `NotificationDetailView`.
        """
        url = reverse('notification_detail', args=[1])  # Usa un ID de ejemplo (1)
        self.assertEqual(resolve(url).func.view_class, NotificationDetailView)
