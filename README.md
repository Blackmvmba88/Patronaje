# Patronaje - PhantomFit Studio

Plataforma modular para diseño y generación de patrones textiles inteligentes con simulación 3D y soporte para prendas tecnológicas.

## 🎨 PhantomFit Studio

**PhantomFit Studio** es un entorno de diseño textil inteligente que revoluciona la forma de crear patrones de ropa.

### Características principales:

✅ **Generación Inteligente de Patrones**
- Genera automáticamente patrones de blusas, camisas, pantalones, faldas, vestidos y chaquetas
- Basado en medidas corporales reales
- Calcula automáticamente la tela requerida

✅ **Visualización 3D con Muñeca Fantasma**
- Modelo 3D parametrizable basado en medidas
- Múltiples poses (default, arms_up, arms_out, sitting)
- Mapeo de patrones 2D sobre el modelo 3D

✅ **Integración Tecnológica**
- Módulos LED con múltiples patrones de iluminación
- Materiales reflectantes configurables
- Cálculo de consumo energético
- Preparado para integración con hardware real

✅ **Soporte Multilingüe**
- Detección temprana y automática del idioma del sistema
- 6 idiomas soportados: Español, English, Français, Deutsch, Português, Italiano
- Cambio dinámico de idioma en tiempo de ejecución
- API completamente traducida

## 🚀 Inicio Rápido

```bash
# Clonar el repositorio
git clone https://github.com/Blackmvmba88/Patronaje.git
cd Patronaje

# Ejecutar ejemplo básico
python examples/basic_usage.py

# Ejecutar ejemplo avanzado
python examples/advanced_integration.py
```

## 📚 Documentación

Para documentación completa, ver [PHANTOMFIT_STUDIO.md](PHANTOMFIT_STUDIO.md)

## 💻 Ejemplo de Uso

```python
from phantomfit_studio import PhantomFitStudio

# Crear estudio (detección automática de idioma)
studio = PhantomFitStudio()

# O especificar idioma: 'es', 'en', 'fr', 'de', 'pt', 'it'
studio = PhantomFitStudio(language='en')

# Definir medidas
measurements = {
    "bust": 90,
    "waist": 70,
    "hip": 95,
    "height": 165
}

# Generar patrón
pattern = studio.generate_pattern("blouse", measurements)

# Visualizar en 3D
studio.load_phantom_model(measurements)
studio.visualize_pattern()
studio.show_3d_view()

# Cambiar idioma dinámicamente
studio.set_language('fr')
```

## 🔧 Requisitos

- Python 3.7+
- No se requieren dependencias externas para funcionalidad básica

## 📄 Licencia

Ver archivo LICENSE para más detalles.
