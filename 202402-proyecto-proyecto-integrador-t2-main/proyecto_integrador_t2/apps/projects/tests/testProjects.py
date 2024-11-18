import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from apps.projects.models import Project
from apps.accounts.models import Client

@pytest.mark.django_db
def test_create_project(client):
    """
    Prueba que un cliente autenticado puede crear un proyecto exitosamente.
    """

    # Paso 1: Crear un cliente
    user = User.objects.create_user(username='testuser', password='12345')
    client_profile = Client.objects.create(user=user)

    # Paso 2: Autenticar al cliente
    client.login(username='testuser', password='12345')

    # Paso 3: Preparar los datos del proyecto
    project_data = {
        'name': 'Test Project',
        'description': 'This is a test project',
        'client': client_profile.id,
    }

    # Paso 4: Enviar una solicitud POST para crear el proyecto
    response = client.post(reverse('create_project'), project_data)

    # Paso 5: Validar el resultado
    # Verificar que la solicitud redirige correctamente
    assert response.status_code == 302  # Redirección después de la creación

    # Verificar que el proyecto se creó en la base de datos
    assert Project.objects.filter(name='Test Project').exists()
