# Soporte Multilingüe / Multilingual Support

PhantomFit Studio incluye soporte completo para múltiples idiomas con detección automática del idioma del sistema.

PhantomFit Studio includes full support for multiple languages with automatic system language detection.

## Idiomas Soportados / Supported Languages

- 🇪🇸 **Español (es)** - Spanish
- 🇬🇧 **English (en)** - English
- 🇫🇷 **Français (fr)** - French
- 🇩🇪 **Deutsch (de)** - German
- 🇧🇷 **Português (pt)** - Portuguese
- 🇮🇹 **Italiano (it)** - Italian

## Detección Automática / Automatic Detection

El sistema detecta automáticamente el idioma del sistema operativo al iniciar:

The system automatically detects the operating system language on startup:

```python
from phantomfit_studio import PhantomFitStudio

# Detección automática del idioma
# Automatic language detection
studio = PhantomFitStudio()

print(f"Idioma detectado / Detected language: {studio.get_language()}")
```

## Especificar Idioma / Specify Language

Puedes especificar un idioma manualmente al crear el estudio:

You can manually specify a language when creating the studio:

```python
from phantomfit_studio import PhantomFitStudio

# Crear estudio en inglés
# Create studio in English
studio_en = PhantomFitStudio(language='en')

# Crear estudio en francés
# Create studio in French
studio_fr = PhantomFitStudio(language='fr')

# Crear estudio en alemán
# Create studio in German
studio_de = PhantomFitStudio(language='de')
```

## Cambio Dinámico de Idioma / Dynamic Language Change

Puedes cambiar el idioma en tiempo de ejecución:

You can change the language at runtime:

```python
studio = PhantomFitStudio(language='es')

# Trabajar en español
pattern = studio.generate_pattern("blouse", measurements)

# Cambiar a inglés
studio.set_language('en')

# Continuar en inglés
info = studio.get_pattern_info()
```

## Listar Idiomas Disponibles / List Available Languages

```python
studio = PhantomFitStudio()

# Obtener idiomas disponibles
# Get available languages
languages = studio.get_available_languages()

for code, name in languages.items():
    print(f"[{code}] {name}")
```

Salida / Output:
```
[es] Español
[en] English
[fr] Français
[de] Deutsch
[pt] Português
[it] Italiano
```

## Ejemplos por Idioma / Examples by Language

### Español

```python
studio = PhantomFitStudio(language='es')

measurements = {"bust": 90, "waist": 70, "hip": 95, "height": 165}
pattern = studio.generate_pattern("blouse", measurements)

print(f"Piezas: {len(pattern['pieces'])}")
print(f"Tela requerida: {pattern['fabric_required']['linear_meters']:.2f} metros")
```

### English

```python
studio = PhantomFitStudio(language='en')

measurements = {"bust": 90, "waist": 70, "hip": 95, "height": 165}
pattern = studio.generate_pattern("blouse", measurements)

print(f"Pieces: {len(pattern['pieces'])}")
print(f"Fabric required: {pattern['fabric_required']['linear_meters']:.2f} meters")
```

### Français

```python
studio = PhantomFitStudio(language='fr')

measurements = {"bust": 90, "waist": 70, "hip": 95, "height": 165}
pattern = studio.generate_pattern("blouse", measurements)

print(f"Pièces: {len(pattern['pieces'])}")
print(f"Tissu requis: {pattern['fabric_required']['linear_meters']:.2f} mètres")
```

### Deutsch

```python
studio = PhantomFitStudio(language='de')

measurements = {"bust": 90, "waist": 70, "hip": 95, "height": 165}
pattern = studio.generate_pattern("blouse", measurements)

print(f"Teile: {len(pattern['pieces'])}")
print(f"Benötigter Stoff: {pattern['fabric_required']['linear_meters']:.2f} Meter")
```

### Português

```python
studio = PhantomFitStudio(language='pt')

measurements = {"bust": 90, "waist": 70, "hip": 95, "height": 165}
pattern = studio.generate_pattern("blouse", measurements)

print(f"Peças: {len(pattern['pieces'])}")
print(f"Tecido necessário: {pattern['fabric_required']['linear_meters']:.2f} metros")
```

### Italiano

```python
studio = PhantomFitStudio(language='it')

measurements = {"bust": 90, "waist": 70, "hip": 95, "height": 165}
pattern = studio.generate_pattern("blouse", measurements)

print(f"Pezzi: {len(pattern['pieces'])}")
print(f"Tessuto richiesto: {pattern['fabric_required']['linear_meters']:.2f} metri")
```

## API de Traducción / Translation API

Para desarrolladores que desean usar el sistema de traducción:

For developers who want to use the translation system:

```python
from phantomfit_studio.i18n import LanguageManager

# Crear gestor de idiomas
lang = LanguageManager('es')

# Traducir claves
print(lang.t('welcome'))  # "Bienvenido a PhantomFit Studio"
print(lang.t('pattern_generated'))  # "Patrón generado"

# Cambiar idioma
lang.set_language('en')
print(lang.t('welcome'))  # "Welcome to PhantomFit Studio"
```

## Detección Manual del Idioma del Sistema / Manual System Language Detection

```python
from phantomfit_studio.i18n import detect_system_language

# Detectar idioma del sistema
system_lang = detect_system_language()
print(f"Sistema configurado en / System configured in: {system_lang}")
```

## Variables de Entorno / Environment Variables

El sistema detecta el idioma desde:

The system detects the language from:

1. Variable de entorno `LANG`
2. Configuración de locale del sistema
3. Por defecto: español (es)

Ejemplos / Examples:

```bash
# Linux/Mac
export LANG=en_US.UTF-8
python my_script.py

# Windows PowerShell
$env:LANG="en_US.UTF-8"
python my_script.py
```

## Mensajes Traducidos / Translated Messages

Todos los mensajes del sistema están completamente traducidos:

All system messages are fully translated:

- Nombres de tipos de prendas
- Mensajes de estado y progreso
- Descripciones de medidas corporales
- Información de módulos LED
- Información de materiales reflectantes
- Mensajes de error
- Nombres de poses
- Controles de visualización 3D

## Ejemplo Completo / Complete Example

```python
from phantomfit_studio import PhantomFitStudio

# Crear estudio con idioma del sistema
studio = PhantomFitStudio()

# Mostrar información en el idioma configurado
print(f"{studio.lang.t('studio_name')}")
print(f"{studio.lang.t('studio_description')}")

# Generar patrón
measurements = {
    "bust": 90,
    "waist": 70,
    "hip": 95,
    "shoulder": 40,
    "height": 165
}

print(f"\n{studio.lang.t('generating_pattern')} {studio.lang.t('blouse')}...")
pattern = studio.generate_pattern("blouse", measurements)
print(f"✓ {studio.lang.t('pattern_generated')}")

# Cargar modelo
print(f"\n{studio.lang.t('loading_model')}...")
studio.load_phantom_model(measurements, pose="default")
print(f"✓ {studio.lang.t('model_loaded')}")

# Información
info = studio.get_pattern_info()
print(f"\n{studio.lang.t('pattern_info')}:")
print(f"  - {studio.lang.t('status')}: {studio.lang.t(info['status'])}")
print(f"  - {studio.lang.t('type')}: {studio.lang.t(info['type'])}")
print(f"  - {studio.lang.t('pieces')}: {info['pieces']}")
```

## Demo Interactiva / Interactive Demo

Ejecuta la demo multilingüe para ver todas las características:

Run the multilingual demo to see all features:

```bash
python examples/multilingual_demo.py
```

Esta demo muestra:

This demo shows:

- Detección automática de idioma
- Funcionamiento en todos los idiomas soportados
- Cambio dinámico de idioma
- Traducción completa de mensajes

---

**PhantomFit Studio** - Diseño textil inteligente multilingüe 🌍
