# Documentación de Pruebas Unitarias: Resolución de URLs de Notificaciones

## Descripción General
Este conjunto de pruebas asegura que las URLs relacionadas con las notificaciones resuelvan correctamente hacia las vistas asociadas en la aplicación.

---

## Configuración del Escenario

| **Nombre**          | **Clase**          | **Escenario**                                                                 |
|---------------------|--------------------|-------------------------------------------------------------------------------|
| `notifications`     | `NotificationList` | Vista para listar todas las notificaciones de un usuario.                    |
| `mark_as_read`      | `MarkAsReadView`   | Vista para marcar una notificación específica como leída.                    |
| `notification_detail` | `NotificationDetailView` | Vista para mostrar el detalle de una notificación específica.              |

---

## Pruebas

### Test: `testUrlNotificationList`

**Objetivo:** Verificar que la URL de la lista de notificaciones resuelve correctamente a la vista `NotificationList`.

**Precondiciones:**
- La URL debe estar configurada en el archivo `urls.py` de la aplicación.

**Datos de Entrada:**
- Ninguno.

**Pasos Realizados:**
1. Utilizar la función `reverse` para obtener la URL de la lista de notificaciones.
2. Resolver la URL utilizando `resolve`.
3. Comparar el resultado con la clase `NotificationList`.

**Resultados Esperados:**

| **Resultado**            | **Descripción**                                                       |
|--------------------------|----------------------------------------------------------------------|
| Resolución Correcta       | La URL resuelve correctamente hacia la vista `NotificationList`.     |

**Resultados Obtenidos:**
- La URL resuelve correctamente a la vista `NotificationList`.

---

### Test: `testUrlMarkAsRead`

**Objetivo:** Verificar que la URL para marcar una notificación como leída resuelve correctamente a la vista `MarkAsReadView`.

**Precondiciones:**
- La URL debe aceptar un parámetro de ID correspondiente a la notificación.

**Datos de Entrada:**
- ID de ejemplo: `1`.

**Pasos Realizados:**
1. Utilizar la función `reverse` con un ID para generar la URL.
2. Resolver la URL utilizando `resolve`.
3. Comparar el resultado con la clase `MarkAsReadView`.

**Resultados Esperados:**

| **Resultado**            | **Descripción**                                                     |
|--------------------------|---------------------------------------------------------------------|
| Resolución Correcta       | La URL resuelve correctamente hacia la vista `MarkAsReadView`.     |

**Resultados Obtenidos:**
- La URL resuelve correctamente a la vista `MarkAsReadView`.

---

### Test: `testUrlNotificationDetail`

**Objetivo:** Verificar que la URL para ver el detalle de una notificación resuelve correctamente a la vista `NotificationDetailView`.

**Precondiciones:**
- La URL debe aceptar un parámetro de ID correspondiente a la notificación.

**Datos de Entrada:**
- ID de ejemplo: `1`.

**Pasos Realizados:**
1. Utilizar la función `reverse` con un ID para generar la URL.
2. Resolver la URL utilizando `resolve`.
3. Comparar el resultado con la clase `NotificationDetailView`.

**Resultados Esperados:**

| **Resultado**            | **Descripción**                                                       |
|--------------------------|-----------------------------------------------------------------------|
| Resolución Correcta       | La URL resuelve correctamente hacia la vista `NotificationDetailView`. |

**Resultados Obtenidos:**
- La URL resuelve correctamente a la vista `NotificationDetailView`.

---
