# Documentación de Pruebas Unitarias: `TestMessageViews`

## Configuración del Escenario para `TestMessageViews`

| **Nombre**              | **Clase**           | **Escenario**                                                                                     |
|-------------------------|---------------------|---------------------------------------------------------------------------------------------------|
| `TestMessageViews`      | `TestCase`          | Pruebas relacionadas con la visualización y creación de mensajes en los chats de clientes y freelancers. |
| `clientUser`            | `Userk`             | Usuario cliente autenticado para interactuar con el chat.                                         |
| `freelancerUser`        | `Userk`             | Usuario freelancer autenticado para interactuar con el chat.                                      |
| `clientInstance`        | `Client`            | Perfil asociado al usuario cliente.                                                              |
| `freelancer`            | `Freelancer`        | Perfil asociado al usuario freelancer.                                                           |
| `chat`                  | `Chat`              | Instancia del chat inicial entre cliente y freelancer.                                           |
| `message1`, `message2`  | `Message`           | Mensajes iniciales en el chat.                                                                   |

---

## Pruebas

### Test: `testClientMessageView`

**Objetivo:** Verificar que el cliente pueda ver los mensajes de un chat y el formulario de creación de mensajes.

**Precondiciones:**
- El usuario debe estar autenticado como cliente.
- Debe existir un chat entre el cliente y el freelancer con mensajes.

**Datos de Entrada:**
- Usuario autenticado como cliente.
- Chat existente.

**Pasos Realizados:**
1. Iniciar sesión como cliente.
2. Realizar una solicitud `GET` a la vista `clientMessage`.

**Resultados Esperados:**

| **Resultado**         | **Descripción**                                                      |
|-----------------------|----------------------------------------------------------------------|
| Carga de mensajes     | Los mensajes del chat deben estar presentes en el contexto.         |
| Formulario presente   | El formulario para crear mensajes debe estar en el contexto.        |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el cliente puede ver los mensajes y el formulario.

---

### Test: `testFreelancerMessageView`

**Objetivo:** Verificar que el freelancer pueda ver los mensajes de un chat y el formulario de creación de mensajes.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.
- Debe existir un chat entre el freelancer y el cliente con mensajes.

**Datos de Entrada:**
- Usuario autenticado como freelancer.
- Chat existente.

**Pasos Realizados:**
1. Iniciar sesión como freelancer.
2. Realizar una solicitud `GET` a la vista `freelancerMessage`.

**Resultados Esperados:**

| **Resultado**         | **Descripción**                                                      |
|-----------------------|----------------------------------------------------------------------|
| Carga de mensajes     | Los mensajes del chat deben estar presentes en el contexto.         |
| Formulario presente   | El formulario para crear mensajes debe estar en el contexto.        |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el freelancer puede ver los mensajes y el formulario.

---

### Test: `testCreateMessageInClientMessage`

**Objetivo:** Verificar que un cliente pueda crear un mensaje en un chat existente.

**Precondiciones:**
- El usuario debe estar autenticado como cliente.
- Debe existir un chat entre el cliente y el freelancer.

**Datos de Entrada:**
- Mensaje a crear: `{'body': 'the prex'}`.

**Pasos Realizados:**
1. Iniciar sesión como cliente.
2. Realizar una solicitud `POST` a la vista `clientMessage` con los datos del mensaje.

**Resultados Esperados:**

| **Resultado**         | **Descripción**                                                      |
|-----------------------|----------------------------------------------------------------------|
| Creación del mensaje  | El mensaje debe guardarse en la base de datos.                      |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el cliente puede crear mensajes.

---

### Test: `testCreateMessageInFreelancerMessage`

**Objetivo:** Verificar que un freelancer pueda crear un mensaje en un chat existente.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.
- Debe existir un chat entre el freelancer y el cliente.

**Datos de Entrada:**
- Mensaje a crear: `{'body': 'the message'}`.

**Pasos Realizados:**
1. Iniciar sesión como freelancer.
2. Realizar una solicitud `POST` a la vista `freelancerMessage` con los datos del mensaje.

**Resultados Esperados:**

| **Resultado**         | **Descripción**                                                      |
|-----------------------|----------------------------------------------------------------------|
| Creación del mensaje  | El mensaje debe guardarse en la base de datos.                      |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que el freelancer puede crear mensajes.

---

### Test: `testMessageClientFormInTemplate`

**Objetivo:** Verificar que el formulario de creación de mensajes esté presente en la página del cliente.

**Precondiciones:**
- El usuario debe estar autenticado como cliente.
- Debe existir un chat entre el cliente y el freelancer.

**Datos de Entrada:**
- Usuario autenticado como cliente.

**Pasos Realizados:**
1. Iniciar sesión como cliente.
2. Realizar una solicitud `GET` a la vista `clientMessage`.

**Resultados Esperados:**

| **Resultado**         | **Descripción**                                                      |
|-----------------------|----------------------------------------------------------------------|
| Formulario presente   | El formulario debe estar visible en el contenido HTML de la respuesta. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando la presencia del formulario.

---

### Test: `testMessageFreelancerFormInTemplate`

**Objetivo:** Verificar que el formulario de creación de mensajes esté presente en la página del freelancer.

**Precondiciones:**
- El usuario debe estar autenticado como freelancer.
- Debe existir un chat entre el freelancer y el cliente.

**Datos de Entrada:**
- Usuario autenticado como freelancer.

**Pasos Realizados:**
1. Iniciar sesión como freelancer.
2. Realizar una solicitud `GET` a la vista `freelancerMessage`.

**Resultados Esperados:**

| **Resultado**         | **Descripción**                                                      |
|-----------------------|----------------------------------------------------------------------|
| Formulario presente   | El formulario debe estar visible en el contenido HTML de la respuesta. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando la presencia del formulario.

---
