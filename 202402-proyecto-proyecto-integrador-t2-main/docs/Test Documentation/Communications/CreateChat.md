# Documentación de Pruebas Unitarias: `TestCreateChat`

## Configuración del Escenario para `TestCreateChat`

| **Nombre**                  | **Clase**          | **Escenario**                                                                                     |
|-----------------------------|--------------------|---------------------------------------------------------------------------------------------------|
| `TestCreateChat`            | `TestSecurity`     | Pruebas para la creación y redirección de chats entre clientes y freelancers.                     |
| `clientUser`                | `Userk`            | Usuario cliente autenticado para iniciar los chats.                                               |
| `freelancerUser`            | `Userk`            | Usuario freelancer autenticado para iniciar los chats.                                            |
| `testClientInstance`        | `Client`           | Perfil asociado al usuario cliente.                                                               |
| `freelancer`                | `Freelancer`       | Perfil asociado al usuario freelancer.                                                            |
| `chat`                      | `Chat`             | Instancia inicial de chat entre el cliente y el freelancer.                                       |

---

## Pruebas

### Test: `testCreateNewChatForClient`

**Objetivo:** Verificar que un cliente pueda crear un nuevo chat con un freelancer si no existe un chat previo.

**Precondiciones:**
- El usuario debe estar autenticado como cliente.
- No debe existir un chat previo entre el cliente y el freelancer.

**Datos de Entrada:**
- Usuario autenticado como cliente.

**Pasos Realizados:**
1. Iniciar sesión como cliente.
2. Realizar una solicitud `GET` a la URL de creación de chat con el freelancer.

**Resultados Esperados:**

| **Resultado**              | **Descripción**                                                       |
|----------------------------|----------------------------------------------------------------------|
| Creación de chat           | Se debe crear un nuevo chat en la base de datos.                    |
| Redirección                | El cliente debe ser redirigido a la vista `clientMessage`.          |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que un cliente puede crear un nuevo chat con un freelancer.

---

### Test: `testRedirectToExistingChatForClient`

**Objetivo:** Verificar que un cliente sea redirigido a un chat existente si ya hay un chat entre el cliente y el freelancer.

**Precondiciones:**
- El usuario debe estar autenticado como cliente.
- Debe existir un chat previo entre el cliente y el freelancer.

**Datos de Entrada:**
- Usuario autenticado como cliente.
- Chat existente entre cliente y freelancer.

**Pasos Realizados:**
1. Iniciar sesión como cliente.
2. Realizar una solicitud `GET` a la URL de creación de chat con el freelancer.

**Resultados Esperados:**

| **Resultado**              | **Descripción**                                                       |
|----------------------------|----------------------------------------------------------------------|
| No creación de nuevo chat  | No se debe crear un nuevo chat en la base de datos.                  |
| Redirección                | El cliente debe ser redirigido a la vista `clientMessage`.          |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que los clientes son redirigidos a chats existentes.

---

### Test: `testCreateNewChatForFreelancer`

**Objetivo:** Verificar que un freelancer pueda crear un nuevo chat con un cliente si no existe un chat previo.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.
- No debe existir un chat previo entre el freelancer y el cliente.

**Datos de Entrada:**
- Usuario autenticado como freelancer.

**Pasos Realizados:**
1. Iniciar sesión como freelancer.
2. Realizar una solicitud `GET` a la URL de creación de chat con el cliente.

**Resultados Esperados:**

| **Resultado**              | **Descripción**                                                       |
|----------------------------|----------------------------------------------------------------------|
| Creación de chat           | Se debe crear un nuevo chat en la base de datos.                    |
| Redirección                | El freelancer debe ser redirigido a la vista `freelancerMessage`.   |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que un freelancer puede crear un nuevo chat con un cliente.

---

### Test: `testRedirectToExistingChatForFreelancer`

**Objetivo:** Verificar que un freelancer sea redirigido a un chat existente si ya hay un chat entre el freelancer y el cliente.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.
- Debe existir un chat previo entre el freelancer y el cliente.

**Datos de Entrada:**
- Usuario autenticado como freelancer.
- Chat existente entre freelancer y cliente.

**Pasos Realizados:**
1. Iniciar sesión como freelancer.
2. Realizar una solicitud `GET` a la URL de creación de chat con el cliente.

**Resultados Esperados:**

| **Resultado**              | **Descripción**                                                       |
|----------------------------|----------------------------------------------------------------------|
| No creación de nuevo chat  | No se debe crear un nuevo chat en la base de datos.                  |
| Redirección                | El freelancer debe ser redirigido a la vista `freelancerMessage`.   |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que los freelancers son redirigidos a chats existentes.

---
