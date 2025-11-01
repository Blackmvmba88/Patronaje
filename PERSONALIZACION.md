# Guía de Personalización - PhantomFit Studio

## 🎨 Opciones de Personalización de Colores y Cuadros de Datos

PhantomFit Studio ahora permite personalizar completamente los colores de las piezas y la posición de los cuadros de información en los patrones exportados.

---

## 📋 Opciones de Colores por Prenda

### Calcetines (Sock)

Personaliza los colores de cada pieza del calcetín:

```python
sock_pattern = studio.generate_pattern(
    garment_type="sock",
    measurements={...},
    style_options={
        "style": "crew",
        "ease": 1,
        "colors": {
            "body": "#FF6B6B",      # Cuerpo del calcetín (rojo coral)
            "heel": "#4ECDC4",      # Talón (turquesa)
            "toe": "#FFE66D"        # Punta (amarillo brillante)
        }
    }
)
```

**Piezas personalizables:**
- `body`: Cuerpo principal del calcetín
- `heel`: Refuerzo del talón
- `toe`: Refuerzo de la punta

---

### Boxers (Boxer Shorts)

Personaliza los colores de cada pieza del boxer:

```python
boxer_pattern = studio.generate_pattern(
    garment_type="boxer",
    measurements={...},
    style_options={
        "ease": 5,
        "colors": {
            "front": "#95E1D3",     # Delantero (verde menta)
            "back": "#F38181",      # Trasero (rosa salmón)
            "waistband": "#AA96DA"  # Pretina (lavanda)
        }
    }
)
```

**Piezas personalizables:**
- `front`: Panel delantero
- `back`: Panel trasero
- `waistband`: Pretina elástica

---

## 📦 Opciones de Exportación SVG

### Posición del Cuadro de Datos

Controla dónde aparece el cuadro con información del patrón:

```python
studio.export_pattern(
    "patron.svg",
    format="svg",
    export_options={
        "show_data_box": True,
        "data_box_position": "top-right",  # Opciones: top-right, top-left, bottom-right, bottom-left
        "show_measurements": True,
        "show_fabric_info": True
    }
)
```

**Posiciones disponibles:**
- `top-right`: Esquina superior derecha ⬈
- `top-left`: Esquina superior izquierda ⬉
- `bottom-right`: Esquina inferior derecha ⬊
- `bottom-left`: Esquina inferior izquierda ⬋

---

### Opciones Completas de Exportación

```python
export_options = {
    # Cuadro de datos
    "show_data_box": True,              # Mostrar/ocultar cuadro de información
    "data_box_position": "top-right",   # Posición del cuadro
    "show_measurements": True,          # Mostrar medidas en el cuadro
    "show_fabric_info": True,           # Mostrar información de tela
    
    # Estilos visuales
    "stroke_color": "#333333",          # Color de las líneas del patrón
    "stroke_width": 2,                  # Grosor de las líneas (en píxeles)
    "text_color": "#1a1a1a",           # Color del texto
    "font_family": "Arial",             # Fuente del texto
    "font_size": 12                     # Tamaño de fuente
}

studio.export_pattern("patron.svg", format="svg", export_options=export_options)
```

---

## 💡 Ejemplos Completos

### Ejemplo 1: Calcetín Colorido con Datos Arriba

```python
from phantomfit_studio import PhantomFitStudio

studio = PhantomFitStudio()

# Generar patrón con colores personalizados
sock_pattern = studio.generate_pattern(
    garment_type="sock",
    measurements={
        "foot_length": 25,
        "foot_width": 10,
        "ankle_circumference": 22,
        "calf_circumference": 35,
        "sock_height": 20
    },
    style_options={
        "style": "crew",
        "ease": 1,
        "colors": {
            "body": "#FF6B6B",
            "heel": "#4ECDC4",
            "toe": "#FFE66D"
        }
    }
)

# Exportar con cuadro de datos personalizado
studio.export_pattern(
    "calcetin_colorido.svg",
    format="svg",
    export_options={
        "show_data_box": True,
        "data_box_position": "top-right",
        "stroke_color": "#333333",
        "stroke_width": 2
    }
)
```

---

### Ejemplo 2: Boxer sin Cuadro de Datos

```python
# Generar boxer con colores vibrantes
boxer_pattern = studio.generate_pattern(
    garment_type="boxer",
    measurements={
        "waist": 75,
        "hip": 95,
        "inseam": 10,
        "thigh_circumference": 55,
        "rise": 25
    },
    style_options={
        "ease": 5,
        "colors": {
            "front": "#FFD93D",
            "back": "#6BCB77",
            "waistband": "#4D96FF"
        }
    }
)

# Exportar solo el patrón, sin cuadro de datos
studio.export_pattern(
    "boxer_simple.svg",
    format="svg",
    export_options={
        "show_data_box": False,  # Sin cuadro de información
        "stroke_color": "#000000",
        "stroke_width": 2.5
    }
)
```

---

### Ejemplo 3: Estilo Profesional con Fuente Grande

```python
# Exportar con estilo profesional
studio.export_pattern(
    "patron_profesional.svg",
    format="svg",
    export_options={
        "show_data_box": True,
        "data_box_position": "bottom-left",
        "show_measurements": True,
        "show_fabric_info": True,
        "stroke_color": "#000000",
        "stroke_width": 2.5,
        "text_color": "#000000",
        "font_family": "Courier New",
        "font_size": 14
    }
)
```

---

## 🎨 Paletas de Colores Recomendadas

### Paleta Pastel
```python
colors = {
    "body": "#FFB3BA",    # Rosa pastel
    "heel": "#BAFFC9",    # Verde pastel
    "toe": "#BAE1FF"      # Azul pastel
}
```

### Paleta Vibrante
```python
colors = {
    "front": "#FF6B6B",   # Rojo brillante
    "back": "#4ECDC4",    # Turquesa
    "waistband": "#FFE66D" # Amarillo
}
```

### Paleta Monocromática Azul
```python
colors = {
    "body": "#A8DADC",    # Azul claro
    "heel": "#457B9D",    # Azul medio
    "toe": "#1D3557"      # Azul oscuro
}
```

---

## 🚀 Ejecutar Demos

### Demo de Personalización Completa
```bash
python examples/customization_demo.py
```

Este demo genera 4 archivos SVG diferentes mostrando:
1. Calcetín con colores personalizados y cuadro arriba-derecha
2. Boxer con colores personalizados y cuadro abajo-izquierda
3. Calcetín sin cuadro de datos
4. Boxer con texto grande y fuente Courier New

### Demo Básico con Personalización
```bash
python examples/sock_boxer_demo.py
```

---

## 📝 Notas

- Los colores se especifican en formato hexadecimal (#RRGGBB)
- Los colores por defecto son suaves y pasteles si no se especifican
- El cuadro de datos muestra hasta 4 medidas principales
- Todas las opciones son opcionales y tienen valores por defecto sensatos
- Los archivos SVG generados son compatibles con:
  - Navegadores web
  - Software de diseño (Inkscape, Adobe Illustrator)
  - Máquinas de corte CNC
  - Plotters de impresión

---

## 🔍 Ver También

- `examples/customization_demo.py` - Demo completo de personalización
- `examples/sock_boxer_demo.py` - Ejemplo básico con colores
- `examples/test_sock_boxer.py` - Tests de las nuevas funcionalidades
