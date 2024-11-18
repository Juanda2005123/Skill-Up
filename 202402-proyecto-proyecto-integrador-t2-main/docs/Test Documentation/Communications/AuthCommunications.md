# Documentación de Pruebas Unitarias: `TestSecurity`

## Configuración del Escenario para `TestSecurity`

| **Nombre**               | **Clase**         | **Escenario**                                                                                       |
|--------------------------|-------------------|-----------------------------------------------------------------------------------------------------|
| `TestClient`              | `TestSecurity`    | Pruebas de seguridad y acceso para las vistas de mensajes de cliente y freelancer.                  |

---

## Pruebas

### Test: `testClientAccessToClientMessageHome`

**Objetivo:** Verificar que un cliente autenticado pueda acceder a la vista `clientMessageHome`.

**Precondiciones:**
- El usuario debe estar autenticado como cliente.

**Datos de Entrada:**
- Usuario autenticado como cliente.

**Pasos Realizados:**
1. Iniciar sesión como cliente.
2. Acceder a la URL de `clientMessageHome`.

**Resultados Esperados:**

| **Resultado**        | **Descripción**                                             |
|----------------------|------------------------------------------------------------|
| Código de estado HTTP | La respuesta debe tener un código de estado `200`.         |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el cliente puede acceder a `clientMessageHome`.

---

### Test: `testFreelancerAccessToClientMessageHome`

**Objetivo:** Verificar que un freelancer autenticado no pueda acceder a la vista `clientMessageHome`.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.

**Datos de Entrada:**
- Usuario autenticado como freelancer.

**Pasos Realizados:**
1. Iniciar sesión como freelancer.
2. Acceder a la URL de `clientMessageHome`.

**Resultados Esperados:**

| **Resultado**              | **Descripción**                                                       |
|----------------------------|----------------------------------------------------------------------|
| Mensaje de error en HTML   | Debe mostrar el mensaje `You are not God to view this page bro`.     |
| Código de estado HTTP      | La respuesta debe tener un código de estado `200`.                   |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que los freelancers no pueden acceder a `clientMessageHome`.

---

### Test: `testUnauthenticatedUserAccessToClientMessageHome`

**Objetivo:** Verificar que un usuario no autenticado sea redirigido al login al intentar acceder a `clientMessageHome`.

**Precondiciones:**
- Usuario no autenticado.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Intentar acceder a la URL de `clientMessageHome` sin autenticarse.

**Resultados Esperados:**

| **Resultado**              | **Descripción**                                                       |
|----------------------------|----------------------------------------------------------------------|
| Redirección                | El usuario debe ser redirigido a la página de login.                 |
| Código de estado HTTP      | La respuesta debe tener un código de estado `302`.                   |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando la redirección para usuarios no autenticados.

---

### Test: `testAccessToMessageClientViewAsClient`

**Objetivo:** Verificar que un cliente autenticado pueda acceder a un chat específico.

**Precondiciones:**
- Usuario autenticado como cliente.
- Chat asociado al cliente.

**Datos de Entrada:**
- Usuario autenticado como cliente.
- `chatName` del chat asociado al cliente.

**Pasos Realizados:**
1. Iniciar sesión como cliente.
2. Acceder a la URL del chat mediante `chatName`.

**Resultados Esperados:**

| **Resultado**              | **Descripción**                                                       |
|----------------------------|----------------------------------------------------------------------|
| Código de estado HTTP      | La respuesta debe tener un código de estado `200`.                   |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el cliente puede acceder al chat.

---

### Test: `testAccessToMessageClientViewAsFreelancer`

**Objetivo:** Verificar que un freelancer autenticado no pueda acceder a un chat de cliente.

**Precondiciones:**
- Usuario autenticado como freelancer.
- Chat asociado al cliente.

**Datos de Entrada:**
- Usuario autenticado como freelancer.
- `chatName` del chat asociado al cliente.

**Pasos Realizados:**
1. Iniciar sesión como freelancer.
2. Acceder a la URL del chat mediante `chatName`.

**Resultados Esperados:**

| **Resultado**              | **Descripción**                                                       |
|----------------------------|----------------------------------------------------------------------|
| Mensaje de error en HTML   | Debe mostrar el mensaje `You are not God to view this page bro`.     |
| Código de estado HTTP      | La respuesta debe tener un código de estado `200`.                   |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que los freelancers no pueden acceder al chat de cliente.

---

### Test: `testAccessToMessageClientViewAsUnauthenticated`

**Objetivo:** Verificar que un usuario no autenticado sea redirigido al login al intentar acceder a un chat de cliente.

**Precondiciones:**
- Usuario no autenticado.
- Chat asociado al cliente.

**Datos de Entrada:**
- `chatName` del chat asociado al cliente.

**Pasos Realizados:**
1. Intentar acceder a la URL del chat mediante `chatName` sin autenticarse.

**Resultados Esperados:**

| **Resultado**              | **Descripción**                                                       |
|----------------------------|----------------------------------------------------------------------|
| Redirección                | El usuario debe ser redirigido a la página de login.                 |
| Código de estado HTTP      | La respuesta debe tener un código de estado `302`.                   |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando la redirección para usuarios no autenticados.

---

### Test: `testAccessToFreelancerCreateComprobateChatAsClient`

**Objetivo:** Verificar que un cliente autenticado no pueda crear un chat de freelancer.

**Precondiciones:**
- Usuario autenticado como cliente.

**Datos de Entrada:**
- Usuario autenticado como cliente.
- `username` del freelancer.

**Pasos Realizados:**
1. Iniciar sesión como cliente.
2. Intentar acceder a la URL de creación de chat de freelancer.

**Resultados Esperados:**

| **Resultado**              | **Descripción**                                                       |
|----------------------------|----------------------------------------------------------------------|
| Mensaje de error en HTML   | Debe mostrar el mensaje `You are not God to view this page bro`.     |
| Código de estado HTTP      | La respuesta debe tener un código de estado `200`.                   |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que los clientes no pueden crear chats de freelancer.

---
