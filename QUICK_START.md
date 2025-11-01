# PhantomFit Studio - Guía de Inicio Rápido

## Instalación

```bash
git clone https://github.com/Blackmvmba88/Patronaje.git
cd Patronaje
```

No se requieren dependencias externas. Python 3.7+ es suficiente.

## Uso Básico en 5 Minutos

### 1. Crear un patrón simple

```python
from phantomfit_studio import PhantomFitStudio

# Inicializar
studio = PhantomFitStudio()

# Definir medidas (en cm)
medidas = {
    "bust": 90,
    "waist": 70,
    "hip": 95,
    "shoulder": 40,
    "height": 165
}

# Generar patrón
patron = studio.generate_pattern("blouse", medidas)

print(f"Piezas: {len(patron['pieces'])}")
print(f"Tela: {patron['fabric_required']['linear_meters']:.2f}m")
```

### 2. Visualizar en 3D

```python
# Cargar modelo fantasma
studio.load_phantom_model(medidas, pose="default")

# Visualizar patrón
studio.visualize_pattern()
studio.show_3d_view()
```

### 3. Agregar tecnología

```python
# Agregar LED
led_id = studio.add_led_module({
    "position": [0, 150, 5],
    "color": [255, 100, 0],
    "intensity": 80,
    "pattern": "pulse",
    "size": "small"
})

# Agregar material reflectante
reflective_id = studio.add_reflective_material({
    "area": [[0, 0], [30, 0], [30, 5], [0, 5]],
    "reflectivity": 0.9,
    "pattern": "stripe"
})
```

### 4. Exportar patrón

```python
studio.export_pattern("mi_patron.svg", format="svg")
```

## Ejemplos Incluidos

```bash
# Ejemplo básico
python examples/basic_usage.py

# Integración tecnológica
python examples/advanced_integration.py

# Flujo de trabajo completo
python examples/complete_workflow.py

# Ver todos los tipos de prendas
python examples/showcase_all_garments.py

# Demo de exportación
python examples/export_demo.py

# Suite de tests
python examples/test_all_features.py
```

## Tipos de Prendas Disponibles

- `blouse` - Blusa
- `shirt` - Camisa
- `pants` - Pantalón
- `skirt` - Falda
- `dress` - Vestido
- `jacket` - Chaqueta

## Poses del Modelo Fantasma

- `default` - Brazos a los lados
- `arms_up` - Brazos levantados
- `arms_out` - Brazos extendidos
- `sitting` - Sentado

## Patrones de LED

- `static` - Luz constante
- `blink` - Parpadeo
- `fade` - Desvanecimiento
- `pulse` - Pulso
- `rainbow` - Ciclo de colores
- `wave` - Onda

## Medidas Requeridas

### Básicas (todas las prendas)
- `bust` - Busto/pecho
- `waist` - Cintura
- `hip` - Cadera
- `height` - Altura

### Adicionales según prenda
- `shoulder` - Ancho de hombros (prendas superiores)
- `back_length` - Largo de espalda (prendas superiores)
- `sleeve_length` - Largo de manga (prendas con mangas)
- `inseam` - Entrepierna (pantalones)
- `outseam` - Costura lateral (pantalones)
- `skirt_length` - Largo de falda (faldas)
- `dress_length` - Largo de vestido (vestidos)

## Soporte

Ver documentación completa en [PHANTOMFIT_STUDIO.md](PHANTOMFIT_STUDIO.md)

Para preguntas o problemas, abrir un issue en GitHub.

---
**PhantomFit Studio** - Diseño textil inteligente 🎨
