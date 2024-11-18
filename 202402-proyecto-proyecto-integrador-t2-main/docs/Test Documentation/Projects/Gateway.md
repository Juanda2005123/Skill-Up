# Documentación de Pruebas Unitarias: `gateWay`

## Descripción General
Este conjunto de pruebas verifica la funcionalidad de la vista de inicio de pagos (`gateWay`) y la redirección tras un pago exitoso. También valida la creación de transacciones relacionadas con los proyectos y los freelancers.

---

## Configuración del Escenario

| **Nombre**              | **Clase**                  | **Escenario**                                                         |
|-------------------------|----------------------------|------------------------------------------------------------------------|
| `client_user`           | `Userk`                   | Usuario autenticado como cliente.                                     |
| `freelancer_user`       | `Userk`                   | Usuario autenticado como freelancer.                                  |
| `client_instance`       | `Client`                  | Perfil del cliente propietario del proyecto.                          |
| `freelancer`            | `Freelancer`              | Freelancer asignado como contribuidor al proyecto.                    |
| `project`               | `Project`                 | Proyecto asociado al cliente y al freelancer.                         |
| `project_contributor`   | `ProjectContributor`       | Relación entre freelancer y proyecto.                                 |
| `gateWay_url`           | `URL`                     | URL de la vista `gateWay`.                                            |
| `confirmed_payment_url` | `URL`                     | URL de la vista `confirmedPayment` tras un pago exitoso.              |

---

## Pruebas

### Test: `test_gateWay_access`

**Objetivo:** Verificar que la vista de `gateWay` sea accesible para el cliente.

**Precondiciones:**
- El cliente debe estar autenticado.
- El proyecto debe estar asociado al cliente.

**Pasos Realizados:**
1. Iniciar sesión como cliente.
2. Realizar una solicitud GET a la URL `gateWay`.
3. Verificar el código de estado de la respuesta.
4. Confirmar que la página contiene texto relacionado con el pago.

**Resultados Esperados:**

| **Resultado**            | **Descripción**                                 |
|--------------------------|------------------------------------------------|
| Código de estado 200     | La página de inicio de pagos se carga correctamente. |
| Texto "Realizar Pago"    | La página contiene el mensaje de inicio de pago. |

---

### Test: `test_successful_payment_redirects_to_confirmed_payment`

**Objetivo:** Verificar que un pago exitoso redirige correctamente a la vista de confirmación de pago y crea una transacción.

**Precondiciones:**
- El cliente debe estar autenticado.
- El proyecto debe estar asociado al cliente.
- Los datos de la tarjeta deben ser válidos.

**Datos de Entrada:**
- `card_number`: "1234"
- `expiry_date`: "12/34"
- `cvv`: "123"

**Pasos Realizados:**
1. Iniciar sesión como cliente.
2. Realizar una solicitud POST con los datos de la tarjeta.
3. Verificar que la solicitud redirige a la URL `confirmedPayment`.

**Resultados Esperados:**

| **Resultado**                | **Descripción**                                             |
|------------------------------|------------------------------------------------------------|
| Redirección a `confirmedPayment` | La solicitud POST redirige correctamente a la confirmación. |
| Transacción creada           | La transacción está registrada en la base de datos.        |

---

## Consideraciones
- Estas pruebas aseguran que solo los usuarios autenticados puedan realizar pagos.
- Se validan los flujos de redirección y creación de transacciones en la base de datos.
- Las pruebas podrían extenderse para incluir validaciones de errores en los datos de la tarjeta.
