# Documentación de Pruebas Unitarias: `TestUrls`

## Configuración del Escenario para `TestUrls`

| **Nombre**           | **Clase**         | **Escenario**                                                   |
|----------------------|-------------------|-----------------------------------------------------------------|
| `TestUrls`           | `SimpleTestCase` | Pruebas unitarias para garantizar que las URLs del dashboard resuelvan correctamente. |

---

## Pruebas

### Test: `testUrlDashboardFreelancer`

**Objetivo:** Verificar que la URL `dashboardFreelancer` resuelva hacia la función `dashboardFreelancer`.

**Precondiciones:**
- La URL `dashboardFreelancer` debe estar definida en el archivo de URLs del proyecto.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Utilizar la función `reverse` para obtener la URL de `dashboardFreelancer`.
2. Resolver la URL utilizando `resolve` y verificar que apunte a la función `dashboardFreelancer`.

**Resultados Esperados:**

| **Resultado**             | **Descripción**                                   |
|---------------------------|--------------------------------------------------|
| Resolución correcta       | La URL debe resolver hacia la función esperada.   |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la URL de `dashboardFreelancer` resuelve correctamente.

---

### Test: `testUrlDashboardClient`

**Objetivo:** Verificar que la URL `dashboardClient` resuelva hacia la función `dashboardClient`.

**Precondiciones:**
- La URL `dashboardClient` debe estar definida en el archivo de URLs del proyecto.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Utilizar la función `reverse` para obtener la URL de `dashboardClient`.
2. Resolver la URL utilizando `resolve` y verificar que apunte a la función `dashboardClient`.

**Resultados Esperados:**

| **Resultado**             | **Descripción**                                   |
|---------------------------|--------------------------------------------------|
| Resolución correcta       | La URL debe resolver hacia la función esperada.   |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la URL de `dashboardClient` resuelve correctamente.

---

### Test: `testUrlClientAnalysis`

**Objetivo:** Verificar que la URL `clientAnalysis` resuelva hacia la función `clientAnalysis`.

**Precondiciones:**
- La URL `clientAnalysis` debe estar definida en el archivo de URLs del proyecto.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Utilizar la función `reverse` para obtener la URL de `clientAnalysis`.
2. Resolver la URL utilizando `resolve` y verificar que apunte a la función `clientAnalysis`.

**Resultados Esperados:**

| **Resultado**             | **Descripción**                                   |
|---------------------------|--------------------------------------------------|
| Resolución correcta       | La URL debe resolver hacia la función esperada.   |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la URL de `clientAnalysis` resuelve correctamente.

---

### Test: `testUrlFreelancerAnalysis`

**Objetivo:** Verificar que la URL `freelancerAnalysis` resuelva hacia la función `freelancerAnalysis`.

**Precondiciones:**
- La URL `freelancerAnalysis` debe estar definida en el archivo de URLs del proyecto.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Utilizar la función `reverse` para obtener la URL de `freelancerAnalysis`.
2. Resolver la URL utilizando `resolve` y verificar que apunte a la función `freelancerAnalysis`.

**Resultados Esperados:**

| **Resultado**             | **Descripción**                                   |
|---------------------------|--------------------------------------------------|
| Resolución correcta       | La URL debe resolver hacia la función esperada.   |

**Resultados Obtenidos:**
- El test pasa exitosamente, confirmando que la URL de `freelancerAnalysis` resuelve correctamente.

---
