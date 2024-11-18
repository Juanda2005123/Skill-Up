# Documentación de Pruebas Unitarias: `TestUrls`

## Configuración del Escenario para `TestUrls`

| **Nombre**                      | **Clase**          | **Escenario**                                                                                     |
|---------------------------------|--------------------|---------------------------------------------------------------------------------------------------|
| `TestUrls`                      | `SimpleTestCase`   | Pruebas para verificar que las URLs de la aplicación `communications` resuelven correctamente.   |

---

## Pruebas

### Test: `testUrlFreelancerMessageHome`

**Objetivo:** Verificar que la URL `freelancerMessageHome` se resuelva correctamente a la vista `freelancerMessageHome`.

**Precondiciones:**
- La URL `freelancerMessageHome` debe estar correctamente configurada en el archivo `urls.py`.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Utilizar la función `reverse` para obtener la URL de `freelancerMessageHome`.
2. Resolver la URL con la función `resolve`.
3. Comparar el resultado con la función `freelancerMessageHome`.

**Resultados Esperados:**

| **Resultado**            | **Descripción**                                   |
|--------------------------|-------------------------------------------------|
| Resuelve correctamente   | La URL debe resolverse correctamente a la vista `freelancerMessageHome`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la URL se resuelve correctamente.

---

### Test: `testUrlClientMessageHome`

**Objetivo:** Verificar que la URL `clientMessageHome` se resuelva correctamente a la vista `clientMessageHome`.

**Precondiciones:**
- La URL `clientMessageHome` debe estar correctamente configurada en el archivo `urls.py`.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Utilizar la función `reverse` para obtener la URL de `clientMessageHome`.
2. Resolver la URL con la función `resolve`.
3. Comparar el resultado con la función `clientMessageHome`.

**Resultados Esperados:**

| **Resultado**            | **Descripción**                                   |
|--------------------------|-------------------------------------------------|
| Resuelve correctamente   | La URL debe resolverse correctamente a la vista `clientMessageHome`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la URL se resuelve correctamente.

---

### Test: `testUrlFreelancerMessage`

**Objetivo:** Verificar que la URL `freelancerMessage` se resuelva correctamente a la vista `freelancerMessage`.

**Precondiciones:**
- La URL `freelancerMessage` debe estar correctamente configurada en el archivo `urls.py`.

**Datos de Entrada:**
- Argumento: `testChatName`.

**Pasos Realizados:**
1. Utilizar la función `reverse` para obtener la URL de `freelancerMessage`.
2. Resolver la URL con la función `resolve`.
3. Comparar el resultado con la función `freelancerMessage`.

**Resultados Esperados:**

| **Resultado**            | **Descripción**                                   |
|--------------------------|-------------------------------------------------|
| Resuelve correctamente   | La URL debe resolverse correctamente a la vista `freelancerMessage`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la URL se resuelve correctamente.

---

### Test: `testUrlClientMessage`

**Objetivo:** Verificar que la URL `clientMessage` se resuelva correctamente a la vista `clientMessage`.

**Precondiciones:**
- La URL `clientMessage` debe estar correctamente configurada en el archivo `urls.py`.

**Datos de Entrada:**
- Argumento: `testChatName`.

**Pasos Realizados:**
1. Utilizar la función `reverse` para obtener la URL de `clientMessage`.
2. Resolver la URL con la función `resolve`.
3. Comparar el resultado con la función `clientMessage`.

**Resultados Esperados:**

| **Resultado**            | **Descripción**                                   |
|--------------------------|-------------------------------------------------|
| Resuelve correctamente   | La URL debe resolverse correctamente a la vista `clientMessage`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la URL se resuelve correctamente.

---

### Test: `testUrlClientCreateComprobateChat`

**Objetivo:** Verificar que la URL `clientCreateComprobateChat` se resuelva correctamente a la vista `clientCreateComprobateChat`.

**Precondiciones:**
- La URL `clientCreateComprobateChat` debe estar correctamente configurada en el archivo `urls.py`.

**Datos de Entrada:**
- Argumento: `testUsername`.

**Pasos Realizados:**
1. Utilizar la función `reverse` para obtener la URL de `clientCreateComprobateChat`.
2. Resolver la URL con la función `resolve`.
3. Comparar el resultado con la función `clientCreateComprobateChat`.

**Resultados Esperados:**

| **Resultado**            | **Descripción**                                   |
|--------------------------|-------------------------------------------------|
| Resuelve correctamente   | La URL debe resolverse correctamente a la vista `clientCreateComprobateChat`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la URL se resuelve correctamente.

---

### Test: `testUrlFreelancerCreateComprobateChat`

**Objetivo:** Verificar que la URL `freelancerCreateComprobateChat` se resuelva correctamente a la vista `freelancerCreateComprobateChat`.

**Precondiciones:**
- La URL `freelancerCreateComprobateChat` debe estar correctamente configurada en el archivo `urls.py`.

**Datos de Entrada:**
- Argumento: `testUsername`.

**Pasos Realizados:**
1. Utilizar la función `reverse` para obtener la URL de `freelancerCreateComprobateChat`.
2. Resolver la URL con la función `resolve`.
3. Comparar el resultado con la función `freelancerCreateComprobateChat`.

**Resultados Esperados:**

| **Resultado**            | **Descripción**                                   |
|--------------------------|-------------------------------------------------|
| Resuelve correctamente   | La URL debe resolverse correctamente a la vista `freelancerCreateComprobateChat`. |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la URL se resuelve correctamente.

---
