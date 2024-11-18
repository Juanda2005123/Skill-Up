# Test Suite: `TestDeleteDeliverable`

## Objetivo
Este conjunto de pruebas garantiza que los **Deliverables** (entregables) asociados a **Milestones** dentro de un proyecto se gestionen correctamente y que solo los usuarios autorizados puedan eliminarlos bajo condiciones válidas.

---

## Casos de Prueba

### 1. `test_delete_deliverable`
**Objetivo**: Verificar que un entregable puede eliminarse exitosamente por un usuario autenticado y autorizado.
- **Pasos**:
  1. Enviar una solicitud `POST` para eliminar el entregable.
  2. Verificar que el entregable ya no exista en la base de datos.
- **Resultado Esperado**:
  - **Código de Estado**: `302` (Redirección después de la eliminación).
  - El entregable se elimina de la base de datos.

---

### 2. `test_delete_deliverable_not_authenticated`
**Objetivo**: Asegurarse de que los usuarios no autenticados no puedan eliminar un entregable.
- **Pasos**:
  1. Cerrar sesión del usuario actual.
  2. Intentar eliminar el entregable.
  3. Verificar que el entregable siga existiendo en la base de datos.
- **Resultado Esperado**:
  - **Código de Estado**: `302` (Redirección a la página de inicio de sesión).
  - El entregable permanece en la base de datos.

---

### 3. `test_delete_deliverable_different_user`
**Objetivo**: Garantizar que un usuario no asociado al proyecto no pueda eliminar un entregable.
- **Pasos**:
  1. Iniciar sesión con una cuenta de usuario diferente.
  2. Intentar eliminar el entregable.
  3. Verificar que el entregable siga existiendo en la base de datos.
- **Resultado Esperado**:
  - **Código de Estado**: `302` (Eliminación no permitida).
  - El entregable permanece en la base de datos.

---

### 4. `test_delete_nonexistent_deliverable`
**Objetivo**: Verificar que intentar eliminar un entregable inexistente devuelve un error `404`.
- **Pasos**:
  1. Intentar eliminar un entregable con un ID inválido.
- **Resultado Esperado**:
  - **Código de Estado**: `404` (Entregable no encontrado).

---

### 5. `test_deliverable_association_with_milestone`
**Objetivo**: Confirmar que un entregable está correctamente asociado a un **Milestone** antes de ser eliminado.
- **Pasos**:
  1. Verificar la asociación del entregable con el **Milestone**.
  2. Eliminar el entregable.
  3. Comprobar que ya no existe en la base de datos.
- **Resultado Esperado**:
  - El entregable está correctamente asociado al **Milestone**.
  - **Código de Estado**: `302` (Eliminación exitosa).

---

### 6. `test_delete_deliverable_no_evidence_required`
**Objetivo**: Asegurarse de que un entregable sin requisitos de evidencia pueda ser eliminado.
- **Pasos**:
  1. Crear un entregable con `requiresEvidence=False`.
  2. Intentar eliminar el entregable.
  3. Comprobar que ya no existe en la base de datos.
- **Resultado Esperado**:
  - **Código de Estado**: `302` (Eliminación exitosa).
  - El entregable se elimina de la base de datos.

---

## Funcionalidades Cubiertas

### 1. **Autenticación y Autorización**
- Solo los usuarios autorizados (contribuyentes al proyecto) pueden eliminar entregables.
- Los usuarios no autenticados o no autorizados son redirigidos o bloqueados.

### 2. **Manejo de Errores**
- Gestión adecuada de IDs inválidos (errores `404` para entregables inexistentes).

### 3. **Validación de Datos**
- Verifica que los entregables estén correctamente asociados a **Milestones** antes de eliminarlos.

### 4. **Casos Extremos**
- Manejo de casos como entregables que no requieren evidencia.

---

## Resumen

Este conjunto de pruebas garantiza que la funcionalidad de eliminación de entregables sea:
- Robusta.
- Respetuosa de los permisos del usuario.
- Capaz de manejar casos extremos y errores.

Al implementar estas pruebas, se asegura la integridad y seguridad de los datos relacionados con los proyectos y sus entregables.
