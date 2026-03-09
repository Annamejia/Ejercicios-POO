# 🐍 Ejercicios de Programación Orientada a Objetos - Python

Repositorio con ejercicios prácticos de **Programación Orientada a Objetos (POO)** en Python, aplicando conceptos como herencia, encapsulación, polimorfismo y composición.

---

## 📚 Conceptos Aplicados

- **Encapsulación** → atributos privados con `__` y acceso mediante getters/setters
- **Herencia** → clases hijas que reutilizan y extienden clases padre
- **Polimorfismo** → mismo método con comportamiento diferente según la clase
- **Composición** → clases que contienen objetos de otras clases
- **Abstracción** → métodos base que las subclases implementan a su manera

---

## 📁 Estructura del Repositorio

```
Ejercicios-POO/
│
├── Ejercicio1/          # Sistema de Biblioteca
│   ├── Libro.py
│   └── main.py
│
├── Ejercicio2/          # Sistema de Cuenta Bancaria
│   ├── Cuenta_bancaria.py
│   └── main.py
│
├── Ejercicio3/          # Sistema de Estudiantes y Cursos
│   ├── Curso.py
│   ├── Estudiante.py
│   └── main.py
│
├── Ejercicio4/          # Sistema de Automóviles
│   ├── Motor.py
│   ├── Automovil.py
│   └── main.py
│
├── Ejercicio5/          # Sistema de Equipo de Fútbol
│   ├── Jugador.py
│   ├── EquipoFut.py
│   └── main.py
│
├── Ejercicio6/          # Sistema de Formas Geométricas
│   ├── FormaGeometrica.py
│   ├── Circulo.py
│   ├── Rectangulo.py
│   └── main.py
│
├── Ejercicio7/          # Sistema de Empleados
│   ├── Empleado.py
│   ├── EmpleadoFijo.py
│   ├── Contratista.py
│   └── main.py
│
├── Ejercicio8/          # Sistema de Vehículos
│   ├── Vehiculo.py
│   ├── Terrestres.py
│   ├── Acuaticos.py
│   └── main.py
│
├── Ejercicio9/          # Sistema de Pedidos
│   ├── Cliente.py
│   ├── Producto.py
│   ├── Pedido.py
│   └── main.py
│
└── Ejercicio10/         # Sistema de Zoológico
    ├── Animal.py
    ├── Mamifero.py
    ├── Aves.py
    ├── Cuidador.py
    ├── Jaula.py
    └── main.py
```

---

## 🔎 Descripción de cada Ejercicio

### Ejercicio 1 - Sistema de Biblioteca
Gestión de libros con control de disponibilidad y préstamos.

| Clase | Atributos | Métodos |
|-------|-----------|---------|
| `Libro` | titulo, autor, anio_publicacion, isbn, disponible, veces_prestado | `cambiar_disponibilidad()` |

---

### Ejercicio 2 - Sistema de Cuenta Bancaria
Gestión de cuentas con operaciones de depósito y retiro con validaciones.

| Clase | Atributos | Métodos |
|-------|-----------|---------|
| `cuenta_bancaria` | Num_cuenta, Titular, Saldo, Fecha_apertura | `depositar()`, `retirar()` |

---

### Ejercicio 3 - Sistema de Estudiantes y Cursos
Matriculación de estudiantes en cursos con composición.

| Clase | Atributos | Métodos |
|-------|-----------|---------|
| `Curso` | id, nombre, codigo, num_creditos | getters/setters |
| `Estudiante` | id, nombre, codigo_estudiantil, carrera, cursos | `Matricular()` |

**Relación:** `Estudiante` ◆→ `Curso`

---

### Ejercicio 4 - Sistema de Automóviles
Gestión de autos con composición del motor.

| Clase | Atributos | Métodos |
|-------|-----------|---------|
| `Motor` | cilindrada, tipo_combustible, potencia | `mostrar_info()` |
| `Automovil` | marca, modelo, anio, color, motor | `mostrar_info()` |

**Relación:** `Automovil` ◆→ `Motor`

---

### Ejercicio 5 - Sistema de Equipo de Fútbol
Gestión de equipos y jugadores con transferencias.

| Clase | Atributos | Métodos |
|-------|-----------|---------|
| `Jugador` | id, nombre, edad, posicion, numeroCamisa | `transferir()` |
| `EquipoFut` | nombre, ciudad, entrenador, jugadores | `agregar()`, `remover()`, `mostrar_plantilla()` |

**Relación:** `EquipoFut` ◆→ `Jugador`

---

### Ejercicio 6 - Sistema de Formas Geométricas
Cálculo de áreas usando herencia y polimorfismo.

| Clase | Atributos | Métodos |
|-------|-----------|---------|
| `FormaGeometrica` | color, formula, area | `calcular_area()`, `mostrarInformacion()` |
| `Circulo` | radio, pi | `calcular_area()`, `mostrarInformacion()` |
| `Rectangulo` | largo, ancho | `calcular_area()`, `mostrarInformacion()` |

**Diagrama:** `FormaGeometrica` ← `Circulo` / `Rectangulo`

---

### Ejercicio 7 - Sistema de Empleados
Gestión de empleados con dos tipos de contratación.

| Clase | Atributos | Métodos |
|-------|-----------|---------|
| `Empleado` | nombre, id, salario_base | getters/setters |
| `EmpleadoFijo` | hereda de Empleado | `Calcular_Salario()` → retorna salario base |
| `Contratista` | tarifa_hora, horas_trabajadas | `Calcular_Salario()` → tarifa × horas |

**Diagrama:** `Empleado` ← `EmpleadoFijo` / `Contratista`

---

### Ejercicio 8 - Sistema de Vehículos
Clasificación de vehículos según su medio de transporte.

| Clase | Atributos | Métodos |
|-------|-----------|---------|
| `Vehiculo` | marca, modelo, capacidad_pasajeros | `Mover()` |
| `Terrestres` | num_ruedas | `Frenar()`, `Mover()` |
| `Acuaticos` | tipo_propulsion | `Anclar()`, `Mover()` |

**Diagrama:** `Vehiculo` ← `Terrestres` / `Acuaticos`

---

### Ejercicio 9 - Sistema de Pedidos
Gestión de pedidos de una tienda con relaciones de composición.

| Clase | Atributos | Métodos |
|-------|-----------|---------|
| `Cliente` | nombre, email, telefono | getters/setters |
| `Producto` | codigo, nombre, precio | getters/setters |
| `Pedido` | cliente, fecha, total, items | `agregar_producto()`, `eliminar_producto()`, `mostrar_resumen()` |

**Relación:** `Pedido` ◆→ `Cliente` / `Producto`

---

### Ejercicio 10 - Sistema de Zoológico
Gestión de animales, jaulas y cuidadores con herencia y composición.

| Clase | Atributos | Métodos |
|-------|-----------|---------|
| `Animal` | nombre, edad, especie | `hacerSonido()`, `comer()` |
| `Mamifero` | tipo_pelaje | `amamantan()`, `hacerSonido()` |
| `Aves` | envergadura_alas | `volar()`, `hacerSonido()` |
| `Cuidador` | nombre, anios_experiencia | getters/setters |
| `Jaula` | numero, capacidad, cuidador, animales | `agregar_animal()`, `mostrar_info()` |

**Diagrama:** `Animal` ← `Mamifero` / `Aves` | `Jaula` ◆→ `Cuidador` / `Animal`

---

## ▶️ Cómo ejecutar cada ejercicio

```bash
# Ejercicio 1
cd Ejercicio1 && py main.py

# Ejercicio 2
cd Ejercicio2 && py main.py

# Ejercicio 3
cd Ejercicio3 && py main.py

# Ejercicio 4
cd Ejercicio4 && py main.py

# Ejercicio 5
cd Ejercicio5 && py main.py

# Ejercicio 6
cd Ejercicio6 && py main.py

# Ejercicio 7
cd Ejercicio7 && py main.py

# Ejercicio 8
cd Ejercicio8 && py main.py

# Ejercicio 9
cd Ejercicio9 && py main.py

# Ejercicio 10
cd Ejercicio10 && py main.py
```

---

## 🛠️ Requisitos

- Python 3.x
- No requiere librerías externas

---

## 👩‍💻 Autora

**Ana Maria Mejia**  
Curso de Programación Orientada a Objetos
