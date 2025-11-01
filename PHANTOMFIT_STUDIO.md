# PhantomFit Studio

## Entorno de Diseño Textil Inteligente

PhantomFit Studio es una plataforma modular para diseño y generación de patrones textiles inteligentes con simulación 3D y soporte para prendas tecnológicas.

## Características Principales

### 1. Generación Inteligente de Patrones
- ✅ Generación automática de patrones basada en medidas corporales
- ✅ Soporte para múltiples tipos de prendas:
  - Blusas y camisas
  - Pantalones
  - Faldas (rectas, A-line, circulares)
  - Vestidos
  - Chaquetas
- ✅ Cálculo automático de tela requerida
- ✅ Exportación de patrones a SVG (PDF y DXF disponibles para implementación futura)

### 2. Visualización 3D con Muñeca Fantasma
- ✅ Modelo 3D parametrizable basado en medidas corporales
- ✅ Muñeca fantasma semi-transparente para mejor visualización
- ✅ Múltiples poses disponibles (default, arms_up, arms_out, sitting)
- ✅ Mapeo de patrones 2D sobre el modelo 3D
- ✅ Sistema de cámara configurable
- ✅ Iluminación configurable para mejor renderizado

### 3. Integración con Tecnología Wearable
- ✅ Sistema de gestión de módulos LED
  - Múltiples patrones de iluminación (static, blink, fade, pulse, rainbow, wave)
  - Control de color RGB (0-255)
  - Control de intensidad (0-100%)
  - Simulación de efectos de iluminación
  - Cálculo de consumo energético
  
- ✅ Gestión de materiales reflectantes
  - Configuración de áreas reflectantes
  - Control de coeficiente de reflectividad
  - Patrones reflectantes (uniform, stripe, geometric)
  - Cálculo de cobertura superficial

## Arquitectura del Sistema

```
phantomfit_studio/
├── core/
│   ├── studio.py              # Clase principal del estudio
│   └── pattern_generator.py   # Generador de patrones
├── visualization/
│   └── phantom_viewer.py      # Visualizador 3D
├── integration/
│   └── module_manager.py      # Gestor de módulos LED y reflectantes
├── config/
│   └── config_loader.py       # Cargador de configuración
└── patterns/                  # Directorio para patrones guardados
```

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/Blackmvmba88/Patronaje.git
cd Patronaje

# No se requieren dependencias externas para la funcionalidad básica
# El sistema funciona con Python 3.7+
```

## Uso Básico

### Ejemplo 1: Generar un Patrón Simple

```python
from phantomfit_studio import PhantomFitStudio

# Crear instancia del estudio
studio = PhantomFitStudio()

# Definir medidas corporales (en cm)
measurements = {
    "bust": 90,
    "waist": 70,
    "hip": 95,
    "shoulder": 40,
    "back_length": 40,
    "sleeve_length": 58,
    "height": 165
}

# Generar patrón de blusa
pattern = studio.generate_pattern(
    garment_type="blouse",
    measurements=measurements,
    style_options={"ease": 5}
)

# Mostrar información
print(f"Piezas generadas: {len(pattern['pieces'])}")
print(f"Tela requerida: {pattern['fabric_required']['linear_meters']:.2f} metros")

# Exportar patrón a SVG
studio.export_pattern("mi_blusa.svg", format="svg")
```

### Ejemplo 2: Visualización 3D

```python
from phantomfit_studio import PhantomFitStudio

studio = PhantomFitStudio()

measurements = {
    "bust": 90,
    "waist": 70,
    "hip": 95,
    "height": 165
}

# Generar patrón
pattern = studio.generate_pattern("dress", measurements)

# Cargar modelo fantasma
studio.load_phantom_model(measurements, pose="default")

# Visualizar patrón en 3D
studio.visualize_pattern(pattern)
studio.show_3d_view()
```

### Ejemplo 3: Integración con Módulos LED

```python
from phantomfit_studio import PhantomFitStudio

studio = PhantomFitStudio()

# Generar patrón de chaqueta
pattern = studio.generate_pattern("jacket", measurements)

# Agregar módulos LED
led_id = studio.add_led_module({
    "position": [0, 150, 5],
    "color": [255, 100, 0],      # RGB: Naranja
    "intensity": 80,              # 80%
    "pattern": "pulse",           # Patrón de pulso
    "size": "small"
})

# Obtener requisitos de energía
power_req = studio.module_manager.get_power_requirements()
print(f"Consumo total: {power_req['total_power_w']} W")
```

### Ejemplo 4: Materiales Reflectantes

```python
from phantomfit_studio import PhantomFitStudio

studio = PhantomFitStudio()

# Agregar material reflectante en manga
reflective_id = studio.add_reflective_material({
    "area": [[0, 0], [30, 0], [30, 5], [0, 5]],
    "reflectivity": 0.9,
    "color": [220, 220, 220],
    "pattern": "stripe"
})

# Obtener cobertura
coverage = studio.module_manager.get_material_coverage()
print(f"Área reflectante: {coverage['total_area_cm2']} cm²")
```

## Ejecución de Ejemplos

```bash
# Ejemplo básico
python examples/basic_usage.py

# Ejemplo avanzado con integración tecnológica
python examples/advanced_integration.py
```

## API Reference

### PhantomFitStudio

Clase principal del estudio.

#### Métodos principales:

- `generate_pattern(garment_type, measurements, style_options)`: Genera un patrón de ropa
- `load_phantom_model(body_measurements, pose)`: Carga el modelo 3D fantasma
- `visualize_pattern(pattern)`: Visualiza un patrón en 3D
- `show_3d_view()`: Muestra la vista 3D interactiva
- `add_led_module(module_config)`: Agrega un módulo LED
- `add_reflective_material(material_config)`: Agrega material reflectante
- `export_pattern(filepath, format)`: Exporta el patrón actual
- `get_pattern_info()`: Obtiene información del patrón actual

### PatternGenerator

Generador inteligente de patrones.

#### Tipos de prenda soportados:
- `blouse`: Blusa
- `shirt`: Camisa
- `pants`: Pantalón
- `skirt`: Falda
- `dress`: Vestido
- `jacket`: Chaqueta

### PhantomViewer

Visualizador 3D del modelo fantasma.

#### Poses disponibles:
- `default`: Brazos a los lados
- `arms_up`: Brazos levantados
- `arms_out`: Brazos extendidos
- `sitting`: Sentado

### ModuleManager

Gestor de módulos tecnológicos.

#### Patrones de LED disponibles:
- `static`: Luz constante
- `blink`: Parpadeo
- `fade`: Desvanecimiento suave
- `pulse`: Pulso de intensidad
- `rainbow`: Ciclo de colores
- `wave`: Onda de luz

## Configuración

El sistema utiliza una configuración por defecto que puede ser personalizada:

```python
from phantomfit_studio.config import ConfigLoader

# Cargar configuración personalizada
config = ConfigLoader.load_config("mi_config.json")

# Crear estudio con configuración personalizada
studio = PhantomFitStudio(config=config)
```

Ejemplo de archivo de configuración JSON:

```json
{
  "viewer": {
    "resolution": [1920, 1080],
    "camera": {
      "position": [0, 0, 300],
      "fov": 45
    }
  },
  "modules": {
    "led": {
      "max_modules": 100,
      "default_intensity": 80
    }
  }
}
```

## Roadmap de Funcionalidades Futuras

### Visualización 3D Avanzada
- [ ] Integración con OpenGL para renderizado en tiempo real
- [ ] Soporte para VR/AR
- [ ] Animaciones de movimiento del modelo
- [ ] Simulación de física de telas

### Exportación Avanzada
- [ ] Exportación a PDF con reportlab
- [ ] Exportación a DXF con ezdxf
- [ ] Exportación a formatos 3D (OBJ, STL, GLTF completos)

### Integración Hardware
- [ ] Control real de módulos LED vía Arduino/Raspberry Pi
- [ ] Integración con sensores de movimiento
- [ ] Sincronización con música/sonido
- [ ] API REST para control remoto

### IA y Machine Learning
- [ ] Generación de patrones asistida por IA
- [ ] Recomendaciones de estilo personalizadas
- [ ] Ajuste automático de patrones basado en retroalimentación

### Colaboración
- [ ] Modo colaborativo multi-usuario
- [ ] Biblioteca de patrones compartidos
- [ ] Integración con plataformas de e-commerce

## Contribuir

Este es un proyecto de código abierto. Las contribuciones son bienvenidas!

## Licencia

Ver archivo LICENSE para más detalles.

## Soporte

Para preguntas, sugerencias o reportar problemas, por favor abrir un issue en GitHub.

---

**PhantomFit Studio** - Diseño textil inteligente del futuro 🚀
