# Documentación de Pruebas Unitarias: Resolución de URLs (`TestUrls`)

## Descripción General
Esta suite de pruebas asegura que las URLs definidas en la aplicación `projects` se resuelvan correctamente a las vistas correspondientes.

---

## Configuración del Escenario

| **Nombre de la URL**                    | **Vista**                       | **Parámetros**       |
|-----------------------------------------|----------------------------------|----------------------|
| `createProject`                         | `views.createProject`           | Ninguno              |
| `updateProject`                         | `views.updateProject`           | `test_pk`            |
| `clientProject`                         | `views.clientProject`           | Ninguno              |
| `clientDeliverable`                     | `views.clientDeliverable`       | `test_pk`            |
| `listFreelancer`                        | `views.listFreelancer`          | `test_pk`            |
| `listOfFreelancersProjectClient`        | `views.listOfFreelancersProjectClient` | Ninguno     |
| `clientFinancialControl`                | `views.financial_control`       | Ninguno              |
| `gateWay`                               | `views.gateWay`                 | `1`                  |
| `confirmedPayment`                      | `views.confirmedPayment`        | `1`                  |
| `applyProjectFreelancer`                | `views.applyProjectFreelancer`  | `test_pk`            |
| `approveFreelancer`                     | `views.approveFreelancer`       | `test_pk`            |
| `browseProject`                         | `views.browseProjects`          | Ninguno              |
| `browseOwnProjects`                     | `views.browseOwnProjects`       | Ninguno              |
| `addDeliverablesProject`                | `views.addDeliverablesProject`  | `test_pk`            |
| `addMilestoneDeliverable`               | `views.addMilestoneDeliverable` | `test_pk`            |

---

## Pruebas

### Test: `test_create_project_url`

**Objetivo:** Verificar que la URL `createProject` resuelve correctamente a la vista `views.createProject`.

**Pasos Realizados:**
1. Llamar a la función `reverse` para obtener la URL de `createProject`.
2. Verificar que la función `resolve` retorna `views.createProject`.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                          |
|------------------------------|------------------------------------------|
| Resolución exitosa           | La URL resuelve correctamente a la vista.|

---

### Test: `test_update_project_url`

**Objetivo:** Verificar que la URL `updateProject` resuelve correctamente a la vista `views.updateProject`.

**Parámetros:** `test_pk`

**Pasos Realizados:**
1. Llamar a la función `reverse` con el parámetro `test_pk`.
2. Verificar que la función `resolve` retorna `views.updateProject`.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                          |
|------------------------------|------------------------------------------|
| Resolución exitosa           | La URL resuelve correctamente a la vista.|

---

### Test: `test_client_project_url`

**Objetivo:** Verificar que la URL `clientProject` resuelve correctamente a la vista `views.clientProject`.

**Pasos Realizados:**
1. Llamar a la función `reverse` para obtener la URL de `clientProject`.
2. Verificar que la función `resolve` retorna `views.clientProject`.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                          |
|------------------------------|------------------------------------------|
| Resolución exitosa           | La URL resuelve correctamente a la vista.|

---

### Test: `test_browse_project_url`

**Objetivo:** Verificar que la URL `browseProject` resuelve correctamente a la vista `views.browseProjects`.

**Pasos Realizados:**
1. Llamar a la función `reverse` para obtener la URL de `browseProject`.
2. Verificar que la función `resolve` retorna `views.browseProjects`.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                          |
|------------------------------|------------------------------------------|
| Resolución exitosa           | La URL resuelve correctamente a la vista.|

---

### Test: `test_add_deliverables_project_url`

**Objetivo:** Verificar que la URL `addDeliverablesProject` resuelve correctamente a la vista `views.addDeliverablesProject`.

**Parámetros:** `test_pk`

**Pasos Realizados:**
1. Llamar a la función `reverse` con el parámetro `test_pk`.
2. Verificar que la función `resolve` retorna `views.addDeliverablesProject`.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                          |
|------------------------------|------------------------------------------|
| Resolución exitosa           | La URL resuelve correctamente a la vista.|

---

### Test: `test_add_milestone_deliverable_url`

**Objetivo:** Verificar que la URL `addMilestoneDeliverable` resuelve correctamente a la vista `views.addMilestoneDeliverable`.

**Parámetros:** `test_pk`

**Pasos Realizados:**
1. Llamar a la función `reverse` con el parámetro `test_pk`.
2. Verificar que la función `resolve` retorna `views.addMilestoneDeliverable`.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                          |
|------------------------------|------------------------------------------|
| Resolución exitosa           | La URL resuelve correctamente a la vista.|

---

## Consideraciones
- Estas pruebas son esenciales para garantizar que las rutas configuradas en el archivo `urls.py` están correctamente vinculadas con sus vistas correspondientes.
- Los nombres de las URLs (`name`) deben coincidir exactamente con los definidos en el archivo de configuración.
