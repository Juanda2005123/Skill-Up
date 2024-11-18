from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apps.dashboard.views import *

class TestUrls(SimpleTestCase):
    """
    Pruebas unitarias para garantizar que las URLs de las vistas del dashboard
    resuelvan correctamente hacia las funciones correspondientes.
    """

    def testUrlDashboardFreelancer(self):
        """
        Prueba que la URL de `dashboardFreelancer` resuelve hacia la función `dashboardFreelancer`.
        """
        url = reverse('dashboardFreelancer')
        self.assertEqual(resolve(url).func, dashboardFreelancer)

    def testUrlDashboardClient(self):
        """
        Prueba que la URL de `dashboardClient` resuelve hacia la función `dashboardClient`.
        """
        url = reverse('dashboardClient')
        self.assertEqual(resolve(url).func, dashboardClient)

    def testUrlClientAnalysis(self):
        """
        Prueba que la URL de `clientAnalysis` resuelve hacia la función `clientAnalysis`.
        """
        url = reverse('clientAnalysis')
        self.assertEqual(resolve(url).func, clientAnalysis)

    def testUrlFreelancerAnalysis(self):
        """
        Prueba que la URL de `freelancerAnalysis` resuelve hacia la función `freelancerAnalysis`.
        """
        url = reverse('freelancerAnalysis')
        self.assertEqual(resolve(url).func, freelancerAnalysis)
