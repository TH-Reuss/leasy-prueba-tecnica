# 🚗 LEASY - Sistema de Gestión de Alquiler de Autos

![Django](https://img.shields.io/badge/Django-5.2.3-green.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple.svg)
![Python](https://img.shields.io/badge/Python-3.12+-yellow.svg)

**Leasy** es un sistema completo de gestión de alquiler de vehículos desarrollado en Django, diseñado para administrar contratos, clientes, vehículos y facturación de manera eficiente y profesional.

---

## 📋 **ÍNDICE**

- [Características Principales](#-características-principales)
- [Funcionalidades](#-funcionalidades)
- [Instalación y Configuración](#-instalación-y-configuración)
- [Uso del Sistema](#-uso-del-sistema)
- [Estructura del Proyecto](#-estructura-del-proyecto)

---

## 🌟 **CARACTERÍSTICAS PRINCIPALES**

### ✅ **Sistema de Autenticación Avanzado**

- Autenticación por email en lugar de username
- Sistema de login/logout seguro con CSRF protection
- Redirects automáticos según el estado de autenticación

### 📊 **Dashboard Analítico Completo**

- Gráficos interactivos con Chart.js
- Proyección de ingresos mensuales
- Estadísticas de vehículos con/sin contrato
- Métricas en tiempo real del negocio

### 🚗 **Gestión Integral de Vehículos**

- Registro de marcas, modelos y vehículos
- Control de disponibilidad
- Historial de contratos por vehículo
- Sistema de placas únicas

### 👥 **Administración de Clientes**

- Registro completo de datos personales
- DNI único por cliente
- Historial de contratos
- Búsqueda y filtrado avanzado

### 📝 **Sistema de Contratos Inteligente**

- Creación de contratos con fechas automáticas
- Cálculo automático de cuotas semanales
- Estados activo/inactivo
- Soft-delete para preservar historial

### 💰 **Facturación Automatizada**

- Generación automática de facturas semanales
- Control de pagos pendientes
- Proyecciones de ingresos futuras
- Estados de facturación

### 📤 **Sistema de Importación Masiva**

- Carga de contratos desde archivos CSV/Excel
- Validación automática de datos
- Creación automática de clientes, vehículos y contratos
- Manejo de errores detallado

### 📋 **Reportes y Exportación**

- Exportación a CSV y Excel
- Selector dinámico de columnas
- Filtros y búsqueda avanzada
- Paginación eficiente

---

## 🚀 **FUNCIONALIDADES**

### **Módulo de Usuarios (`users`)**

- ✅ Modelo de usuario personalizado con email
- ✅ Backend de autenticación personalizado
- ✅ Templates de login responsivos
- ✅ Gestión de sesiones segura

### **Módulo de Clientes (`clients`)**

- ✅ CRUD completo de clientes
- ✅ Validación de DNI único
- ✅ Búsqueda por nombre, apellido o DNI
- ✅ Relación con contratos

### **Módulo de Vehículos (`cars`)**

- ✅ Gestión de marcas y modelos
- ✅ Registro de vehículos con placa única
- ✅ Fecha de fabricación
- ✅ Estado de disponibilidad

### **Módulo de Contratos (`contracts`)**

- ✅ Creación de contratos con servicios
- ✅ Cálculo automático de fechas de vencimiento
- ✅ Generación automática de facturas
- ✅ Sistema de soft-delete
- ✅ Validaciones de negocio

### **Módulo de Analytics (`analytics`)**

- ✅ Dashboard principal con métricas
- ✅ Gráficos de área para proyecciones
- ✅ Gráficos de dona para distribución
- ✅ Cards con estadísticas clave

### **Módulo de Importación (`uploads`)**

- ✅ Carga masiva desde CSV/Excel
- ✅ Validación de estructura de archivos
- ✅ Creación automática de registros relacionados
- ✅ Manejo transaccional de errores

### **Módulo Core (`core`)**

- ✅ Clases base para CRUD operations
- ✅ Sistema de soft-delete universal
- ✅ Managers personalizados
- ✅ Template tags personalizados
- ✅ Sistema de exportación

---

## 🏗️ **ARQUITECTURA DEL SISTEMA**

### **Patrón MVT (Model-View-Template)**

```
📁 leasy_app/
├── 🐍 models.py          # Lógica de datos y validaciones
├── 🎯 views.py           # Lógica de presentación
├── 🎨 templates/         # Interfaz de usuario
├── ⚙️  services.py       # Lógica de negocio
└── 🔗 urls.py           # Enrutamiento
```

### **Aplicaciones Modulares**

- **`core`**: Funcionalidades base y reutilizables
- **`users`**: Gestión de autenticación y usuarios
- **`clients`**: Administración de clientes
- **`cars`**: Gestión de vehículos
- **`contracts`**: Sistema de contratos y facturación
- **`analytics`**: Dashboard y reportes
- **`uploads`**: Importación masiva de datos

## 🛠️ **TECNOLOGÍAS UTILIZADAS**

### **Backend**

- **Django 5.2.3** - Framework web principal
- **PostgreSQL** - Base de datos relacional
- **Python 3.12+** - Lenguaje de programación

### **Frontend**

- **Bootstrap 5** - Framework CSS responsivo
- **Chart.js** - Gráficos interactivos
- **FontAwesome** - Iconografía
- **jQuery** - Manipulación DOM

## 🚀 **INSTALACIÓN Y CONFIGURACIÓN**

### **Prerrequisitos**

- GIT
- Docker

### **1. Clonar el Repositorio**

```bash
git clone <repository-url>
cd leasy-prueba
```

### **2. Configurar Variables de Entorno**

Crear archivo `.env` en la raíz del proyecto:

```env
# Configuración de Django
SECRET_KEY=your-secret-key-here
DEBUG=True
LANGUAGE_CODE=es-co
TIME_ZONE=America/Bogota

# Configuración de Base de Datos PostgreSQL
POSTGRES_DB=leasy_dev
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

### **6. Crear Superusuario**

Necesitas conectarte al contenedor para crear un superusuario con el siguiente comando

```bash
docker exec -it [ID-Contenedor] bash
```

Una vez dentro del contenedor el siguiente comando

```bash
python manage.py createsuperuser
```

Ahora ya puedes ingresar al sistema con las credenciales creadas

### **8. Acceder al Sistema**

- **Aplicación**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

---

## 💻 **USO DEL SISTEMA**

### **🔐 Acceso Inicial**

1. Ve a la URL principal del proyecto
2. Serás redirigido al login automáticamente
3. Usa las credenciales del superusuario creado
4. Después del login, accederás al dashboard principal

### **📊 Dashboard Principal**

- **Métricas clave**: Contratos, clientes, vehículos totales
- **Gráfico de área**: Proyección de ingresos mensuales
- **Gráfico de dona**: Distribución de vehículos con/sin contrato

### **👥 Gestión de Clientes**

1. Ve a **"Clientes"** en el menú lateral
2. Usa **"Crear nuevo"** para añadir clientes
3. Utiliza el buscador para encontrar clientes específicos
4. Exporta datos a CSV/Excel según necesites

### **🚗 Gestión de Vehículos**

1. Accede a **"Autos"** → **"Marcas"** para crear marcas
2. Luego **"Modelos"** para asociar modelos a marcas
3. Finalmente **"Autos"** para registrar vehículos específicos

### **📝 Creación de Contratos**

1. Ve a **"Contratos"** → **"Crear nuevo"**
2. Selecciona cliente y vehículo
3. Define monto semanal y duración
4. El sistema generará automáticamente las facturas semanales

### **📤 Importación Masiva**

1. Ve a **"Importación"** en el menú
2. Usa la plantilla CSV de ejemplo que se encuentra en este repositorio
3. Completa los datos siguiendo el formato:
   - Nombres, Apellidos, Número de documento
   - Inicio de contrato, Cuota semanal
   - Marca del auto, Modelo del auto, Placa del auto
4. Sube el archivo y revisa los resultados

### **📋 Reportes**

- **Selector de columnas**: Personaliza qué campos mostrar
- **Búsqueda**: Filtra por cualquier campo visible
- **Exportación**: Descarga datos en CSV o Excel
- **Paginación**: Navega eficientemente por grandes volúmenes

---

## 📁 **ESTRUCTURA DEL PROYECTO**

```
leasy-prueba/
├── 📁 leasy_app/              # Configuración principal de Django
│   ├── settings.py            # Configuración del proyecto
│   ├── urls.py                # URLs principales
│   ├── wsgi.py                # Configuración WSGI
│   └── asgi.py                # Configuración ASGI
├── 📁 templates/              # Templates HTML
│   ├── base.html              # Template base
│   ├── sidebar.html           # Layout con sidebar
│   ├── 📁 users/              # Templates de usuarios
│   ├── 📁 analytics/          # Templates del dashboard
│   └── 📁 core/               # Templates genéricos
├── 📁 static/                 # Archivos estáticos
│   ├── 📁 theme/              # Tema Bootstrap
│   ├── 📁 analytics/          # Scripts de gráficos
│   └── 📁 users/              # Estilos de login
├── 📁 core/                   # App principal con utilidades
│   ├── models.py              # BaseModel con soft-delete
│   ├── classes/base.py        # Clases base para vistas
│   ├── templatetags/          # Template tags personalizados
│   └── migrations/
```

---

### **Funcionalidades por Endpoint**

- **GET + POST**: Formularios de creación/edición
- **Parámetros de consulta**: `?search=`, `?columns=`, `?export=csv`
- **Paginación**: `?page=N`
- **Ordenamiento**: Configurable por vista

### **Añadir Modelo con Soft-Delete**

```python
from core.models import BaseModel

class MiModelo(BaseModel):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Mi Modelo"
        verbose_name_plural = "Mis Modelos"
```

### **Crear Vista CRUD Rápida**

```python
from core.classes.base import CustomListView

class MiModeloListView(LoginRequiredMixin, CustomListView):
    model = MiModelo
    template_name = 'core/list.html'
    available_columns = {
        'Nombre': 'nombre',
        'Fecha': 'created_at',
    }
    default_columns = ['nombre']
```
