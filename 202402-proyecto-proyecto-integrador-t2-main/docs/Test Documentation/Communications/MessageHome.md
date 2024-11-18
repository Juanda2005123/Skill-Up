# Documentación de Pruebas Unitarias: `TestMessageHome`

## Configuración del Escenario para `TestMessageHome`

| **Nombre**              | **Clase**           | **Escenario**                                                                                     |
|-------------------------|---------------------|---------------------------------------------------------------------------------------------------|
| `TestMessageHome`       | `TestCase`          | Pruebas relacionadas con las vistas de inicio de mensajes para clientes y freelancers.           |
| `clientUser`            | `Userk`             | Usuario cliente autenticado para interactuar con la vista de mensajes.                          |
| `freelancerUser`        | `Userk`             | Usuario freelancer autenticado para interactuar con la vista de mensajes.                       |
| `testClientInstance`    | `Client`            | Perfil asociado al usuario cliente.                                                              |
| `freelancer`            | `Freelancer`        | Perfil asociado al usuario freelancer.                                                           |
| `chat`                  | `Chat`              | Instancia del chat inicial entre cliente y freelancer.                                           |

---

## Pruebas

### Test: `test_client_message_home_view`

**Objetivo:** Verificar que el cliente pueda ver la lista de chats y que el chat más reciente se muestre en primer lugar.

**Precondiciones:**
- El usuario debe estar autenticado como cliente.
- Debe existir al menos un chat entre el cliente y un freelancer.

**Datos de Entrada:**
- Usuario autenticado como cliente.

**Pasos Realizados:**
1. Iniciar sesión como cliente.
2. Realizar una solicitud `GET` a la vista `clientMessageHome`.

**Resultados Esperados:**

| **Resultado**               | **Descripción**                                                                 |
|-----------------------------|---------------------------------------------------------------------------------|
| Código HTTP 200             | La respuesta debe tener un código HTTP 200.                                    |
| Contexto `chats` presente   | La respuesta debe incluir una lista de chats en el contexto.                   |
| Contexto `latestChat`       | La respuesta debe incluir el chat más reciente en el contexto.                 |
| Último chat correcto        | El contexto `latestChat` debe coincidir con el chat creado en el escenario.    |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el cliente puede ver sus chats y el último chat.

---

### Test: `test_freelancer_message_home_view`

**Objetivo:** Verificar que el freelancer pueda ver la lista de chats y que el chat más reciente se muestre en primer lugar.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.
- Debe existir al menos un chat entre un cliente y el freelancer.

**Datos de Entrada:**
- Usuario autenticado como freelancer.

**Pasos Realizados:**
1. Iniciar sesión como freelancer.
2. Realizar una solicitud `GET` a la vista `freelancerMessageHome`.

**Resultados Esperados:**

| **Resultado**               | **Descripción**                                                                 |
|-----------------------------|---------------------------------------------------------------------------------|
| Código HTTP 200             | La respuesta debe tener un código HTTP 200.                                    |
| Contexto `chats` presente   | La respuesta debe incluir una lista de chats en el contexto.                   |
| Contexto `latestChat`       | La respuesta debe incluir el chat más reciente en el contexto.                 |
| Último chat correcto        | El contexto `latestChat` debe coincidir con el chat creado en el escenario.    |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el freelancer puede ver sus chats y el último chat.

---
