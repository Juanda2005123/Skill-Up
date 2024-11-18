from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apps.projects import views

class TestUrls(SimpleTestCase):
    """
    Clase para probar las URLs y su resolución a las vistas correspondientes
    en la aplicación `projects`.
    """

    def test_create_project_url(self):
        """
        Prueba que la URL `createProject` resuelve correctamente a la vista `createProject`.
        """
        url = reverse('createProject')
        self.assertEqual(resolve(url).func, views.createProject)

    def test_update_project_url(self):
        """
        Prueba que la URL `updateProject` resuelve correctamente a la vista `updateProject`.
        """
        url = reverse('updateProject', args=['test_pk'])
        self.assertEqual(resolve(url).func, views.updateProject)

    def test_client_project_url(self):
        """
        Prueba que la URL `clientProject` resuelve correctamente a la vista `clientProject`.
        """
        url = reverse('clientProject')
        self.assertEqual(resolve(url).func, views.clientProject)

    def test_client_deliverable_url(self):
        """
        Prueba que la URL `clientDeliverable` resuelve correctamente a la vista `clientDeliverable`.
        """
        url = reverse('clientDeliverable', args=['test_pk'])
        self.assertEqual(resolve(url).func, views.clientDeliverable)

    def test_list_freelancer_url(self):
        """
        Prueba que la URL `listFreelancer` resuelve correctamente a la vista `listFreelancer`.
        """
        url = reverse('listFreelancer', args=['test_pk'])
        self.assertEqual(resolve(url).func, views.listFreelancer)

    def test_list_of_freelancers_project_client_url(self):
        """
        Prueba que la URL `listOfFreelancersProjectClient` resuelve correctamente a la vista `listOfFreelancersProjectClient`.
        """
        url = reverse('listOfFreelancersProjectClient')
        self.assertEqual(resolve(url).func, views.listOfFreelancersProjectClient)

    def test_client_financial_control_url(self):
        """
        Prueba que la URL `clientFinancialControl` resuelve correctamente a la vista `financial_control`.
        """
        url = reverse('clientFinancialControl')
        self.assertEqual(resolve(url).func, views.financial_control)

    def test_gateway_url(self):
        """
        Prueba que la URL `gateWay` resuelve correctamente a la vista `gateWay`.
        """
        url = reverse('gateWay', args=[1])
        self.assertEqual(resolve(url).func, views.gateWay)

    def test_confirmed_payment_url(self):
        """
        Prueba que la URL `confirmedPayment` resuelve correctamente a la vista `confirmedPayment`.
        """
        url = reverse('confirmedPayment', args=[1])
        self.assertEqual(resolve(url).func, views.confirmedPayment)

    def test_apply_project_freelancer_url(self):
        """
        Prueba que la URL `applyProjectFreelancer` resuelve correctamente a la vista `applyProjectFreelancer`.
        """
        url = reverse('applyProjectFreelancer', args=['test_pk'])
        self.assertEqual(resolve(url).func, views.applyProjectFreelancer)

    def test_approve_freelancer_url(self):
        """
        Prueba que la URL `approveFreelancer` resuelve correctamente a la vista `approveFreelancer`.
        """
        url = reverse('approveFreelancer', args=['test_pk'])
        self.assertEqual(resolve(url).func, views.approveFreelancer)

    def test_browse_project_url(self):
        """
        Prueba que la URL `browseProject` resuelve correctamente a la vista `browseProjects`.
        """
        url = reverse('browseProject')
        self.assertEqual(resolve(url).func, views.browseProjects)

    def test_browse_own_projects_url(self):
        """
        Prueba que la URL `browseOwnProjects` resuelve correctamente a la vista `browseOwnProjects`.
        """
        url = reverse('browseOwnProjects')
        self.assertEqual(resolve(url).func, views.browseOwnProjects)

    def test_add_deliverables_project_url(self):
        """
        Prueba que la URL `addDeliverablesProject` resuelve correctamente a la vista `addDeliverablesProject`.
        """
        url = reverse('addDeliverablesProject', args=['test_pk'])
        self.assertEqual(resolve(url).func, views.addDeliverablesProject)

    def test_add_milestone_deliverable_url(self):
        """
        Prueba que la URL `addMilestoneDeliverable` resuelve correctamente a la vista `addMilestoneDeliverable`.
        """
        url = reverse('addMilestoneDeliverable', args=['test_pk'])
        self.assertEqual(resolve(url).func, views.addMilestoneDeliverable)
