# Documentación de Pruebas Unitarias: `TestSecurity`

## Configuración del Escenario para `TestSecurity`

| **Nombre**           | **Clase**         | **Escenario**                                                   |
|----------------------|-------------------|-----------------------------------------------------------------|
| `TestSecurity`       | `TestCase`       | Pruebas de seguridad para garantizar el acceso adecuado a las notificaciones según el rol del usuario. |

---

## Pruebas

### Test: `testClientAccessToNotifications`

**Objetivo:** Verificar que un cliente autenticado puede acceder a la vista de notificaciones.

**Precondiciones:**
- El usuario debe estar autenticado como cliente (`is_client=True`).
- La vista `notifications` debe estar configurada para permitir acceso a clientes.

**Datos de Entrada:**
- Usuario `clientUser` con rol de cliente.

**Pasos Realizados:**
1. Iniciar sesión como el usuario `clientUser`.
2. Acceder a la vista de notificaciones mediante una solicitud HTTP GET.
3. Verificar el código de respuesta HTTP.

**Resultados Esperados:**

| **Resultado**             | **Descripción**                                   |
|---------------------------|--------------------------------------------------|
| Código HTTP 200           | El cliente puede acceder a la vista de notificaciones. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que los clientes autenticados pueden acceder a las notificaciones.

---

### Test: `testFreelancerAccessToNotifications`

**Objetivo:** Verificar que un freelancer autenticado puede acceder a la vista de notificaciones.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer (`is_freelancer=True`).
- La vista `notifications` debe estar configurada para permitir acceso a freelancers.

**Datos de Entrada:**
- Usuario `freelancerUser` con rol de freelancer.

**Pasos Realizados:**
1. Iniciar sesión como el usuario `freelancerUser`.
2. Acceder a la vista de notificaciones mediante una solicitud HTTP GET.
3. Verificar el código de respuesta HTTP.

**Resultados Esperados:**

| **Resultado**             | **Descripción**                                   |
|---------------------------|--------------------------------------------------|
| Código HTTP 200           | El freelancer puede acceder a la vista de notificaciones. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que los freelancers autenticados pueden acceder a las notificaciones.

---

## Resumen de Configuración

| **Entidad**      | **Tipo**              | **Descripción**                                                     |
|------------------|-----------------------|---------------------------------------------------------------------|
| `clientUser`     | `Userk`              | Usuario con rol de cliente para verificar acceso a las notificaciones. |
| `freelancerUser` | `Userk`              | Usuario con rol de freelancer para verificar acceso a las notificaciones. |
| `testClient`     | `TestClient`         | Cliente HTTP utilizado para realizar solicitudes en las pruebas.   |
