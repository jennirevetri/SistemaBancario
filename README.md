# README - Sistema Bancario Simulado

Este proyecto de Python simula un sistema bancario básico que permite a los usuarios realizar operaciones bancarias como crear cuentas, consultar el estado de cuentas, depositar fondos, retirar fondos y transferir dinero entre cuentas. A continuación, se proporciona una descripción general del código y cómo utilizarlo.

## Descripción General

El código consta de una clase llamada `cuenta`, que representa una cuenta bancaria. Cada instancia de esta clase tiene atributos como el cliente titular de la cuenta, el saldo actual, un número de cuenta único y la fecha de apertura. Además, se proporcionan métodos para realizar operaciones bancarias como depositar, retirar y transferir dinero.

## Uso del Sistema Bancario Simulado

Para usar este sistema bancario simulado, siga estos pasos:

1. Ejecute el programa.

2. Se le presentará un menú con varias opciones:
   
   - **Crear cuenta (Opción 1)**: Puede crear una nueva cuenta ingresando el nombre del titular y el saldo inicial.

   - **Estatus cuenta (Opción 2)**: Puede verificar el estado de una cuenta existente ingresando el número de cuenta.

   - **Depositar (Opción 3)**: Puede depositar dinero en una cuenta existente ingresando el número de cuenta y el monto a depositar.

   - **Retirar (Opción 4)**: Puede retirar dinero de una cuenta existente ingresando el número de cuenta y el monto a retirar.

   - **Transferir (Opción 5)**: Puede transferir dinero de una cuenta a otra ingresando el número de su cuenta, el monto y el número de cuenta de destino.

   - **Salir (Opción 6)**: Puede salir del programa.

3. Siga las instrucciones proporcionadas por el programa para realizar la operación deseada.

## Ejemplos de Uso

- **Creación de una cuenta**:
  - Opción: 1
  - Ingrese el nombre del titular: [Nombre del Titular]
  - Ingrese el saldo inicial: [Saldo Inicial]
  
- **Consulta de estado de cuenta**:
  - Opción: 2
  - Ingrese el número de cuenta: [Número de Cuenta]

- **Depósito bancario**:
  - Opción: 3
  - Ingrese el número de cuenta a depositar: [Número de Cuenta]
  - Ingrese el monto a depositar: [Monto]

- **Retiro de fondos**:
  - Opción: 4
  - Ingrese el número de cuenta a retirar: [Número de Cuenta]
  - Ingrese el monto a retirar: [Monto]

- **Transferencia a terceros**:
  - Opción: 5
  - Ingrese el número de su cuenta: [Su Número de Cuenta]
  - Ingrese el monto a transferir: [Monto]
  - Ingrese el número de cuenta de destino: [Número de Cuenta de Destino]

## Consideraciones Importantes

- El sistema bancario simulado no maneja autenticación ni seguridad avanzada, por lo que se asume que los usuarios proporcionarán información precisa y no realizarán acciones maliciosas.

- Las cuentas creadas durante una ejecución del programa no se almacenan de forma persistente. Cuando se cierra el programa, se pierden todas las cuentas y sus datos.

- Las transacciones y operaciones en el sistema bancario simulado se realizan en memoria durante la ejecución del programa y no involucran una base de datos real ni cuentas bancarias reales.

Este sistema bancario simulado es una herramienta básica para comprender los conceptos fundamentales de las operaciones bancarias y la programación en Python. Puede servir como punto de partida para desarrollar un sistema bancario más completo y seguro en el futuro.
