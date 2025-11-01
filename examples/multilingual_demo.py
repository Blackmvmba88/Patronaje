#!/usr/bin/env python3
"""
Demostración de soporte multilingüe con detección temprana de idioma
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from phantomfit_studio import PhantomFitStudio
from phantomfit_studio.i18n import detect_system_language


def test_language(lang_code: str, lang_name: str):
    """Prueba el estudio en un idioma específico."""
    print(f"\n{'='*60}")
    print(f"Testing in {lang_name} ({lang_code})")
    print('='*60)
    
    # Crear estudio con idioma específico
    studio = PhantomFitStudio(language=lang_code)
    
    # Mostrar información en el idioma seleccionado
    print(f"\n{studio.lang.t('studio_name')}")
    print(f"{studio.lang.t('studio_description')}")
    print(f"{studio.lang.t('version')}: 1.0.0")
    print()
    
    # Generar patrón
    measurements = {
        "bust": 90,
        "waist": 70,
        "hip": 95,
        "shoulder": 40,
        "height": 165
    }
    
    print(f"1. {studio.lang.t('generating_pattern')} {studio.lang.t('blouse')}...")
    pattern = studio.generate_pattern("blouse", measurements)
    print(f"   ✓ {studio.lang.t('pattern_generated')}")
    print(f"   - {studio.lang.t('pieces')}: {len(pattern['pieces'])}")
    print(f"   - {studio.lang.t('fabric_required')}: {pattern['fabric_required']['linear_meters']:.2f} {studio.lang.t('linear_meters')}")
    print()
    
    # Cargar modelo
    print(f"2. {studio.lang.t('loading_model')}...")
    studio.load_phantom_model(measurements, pose="default")
    print(f"   ✓ {studio.lang.t('model_loaded')}")
    print()
    
    # Agregar LED
    print(f"3. {studio.lang.t('adding_led')}...")
    led_id = studio.add_led_module({
        "position": [0, 150, 5],
        "color": [255, 100, 0],
        "intensity": 80,
        "pattern": "pulse",
        "size": "small"
    })
    print(f"   ✓ {studio.lang.t('led_added')}: {led_id[:8]}...")
    print()
    
    # Agregar material reflectante
    print(f"4. {studio.lang.t('adding_reflective')}...")
    reflective_id = studio.add_reflective_material({
        "area": [[0, 0], [30, 0], [30, 5], [0, 5]],
        "reflectivity": 0.9,
        "pattern": "stripe"
    })
    print(f"   ✓ {studio.lang.t('reflective_added')}: {reflective_id[:8]}...")
    print()
    
    # Información
    info = studio.get_pattern_info()
    print(f"5. {studio.lang.t('pattern_info')}:")
    print(f"   - {studio.lang.t('status')}: {studio.lang.t(info['status'])}")
    print(f"   - {studio.lang.t('type')}: {studio.lang.t(info['type'])}")
    print(f"   - {studio.lang.t('pieces')}: {info['pieces']}")
    print(f"   - {studio.lang.t('led_modules')}: {len(info['modules']['led_modules'])}")
    print(f"   - {studio.lang.t('reflective_materials')}: {len(info['modules']['reflective_materials'])}")
    print()


def main():
    """Demuestra el soporte multilingüe."""
    
    print("\n" + "🌍 "*20)
    print("\n" + " "*10 + "PHANTOMFIT STUDIO")
    print(" "*5 + "Multilingual Support Demonstration")
    print(" "*8 + "Demostración Multilingüe")
    print("\n" + "🌍 "*20)
    
    # Detección automática de idioma
    print(f"\n{'='*60}")
    print("Detección Temprana de Idioma / Early Language Detection")
    print('='*60)
    
    detected_lang = detect_system_language()
    print(f"\nIdioma del sistema detectado / System language detected: {detected_lang}")
    print()
    
    # Crear estudio con detección automática
    print("Creando estudio con detección automática...")
    print("Creating studio with automatic detection...")
    studio_auto = PhantomFitStudio()
    print(f"✓ Idioma configurado / Language configured: {studio_auto.get_language()}")
    print()
    
    # Mostrar idiomas disponibles
    print(f"{'='*60}")
    print("Idiomas Disponibles / Available Languages")
    print('='*60)
    available = studio_auto.get_available_languages()
    for code, name in available.items():
        print(f"  [{code}] {name}")
    print()
    
    # Probar cada idioma
    languages = [
        ('es', 'Español'),
        ('en', 'English'),
        ('fr', 'Français'),
        ('de', 'Deutsch'),
        ('pt', 'Português'),
        ('it', 'Italiano')
    ]
    
    for lang_code, lang_name in languages:
        test_language(lang_code, lang_name)
    
    # Demostración de cambio dinámico de idioma
    print(f"\n{'='*60}")
    print("Cambio Dinámico de Idioma / Dynamic Language Change")
    print('='*60)
    print()
    
    studio = PhantomFitStudio(language='es')
    print(f"Idioma inicial: {studio.get_language()}")
    print(f"Mensaje: {studio.lang.t('welcome')}")
    print()
    
    print("Cambiando a inglés...")
    studio.set_language('en')
    print(f"Current language: {studio.get_language()}")
    print(f"Message: {studio.lang.t('welcome')}")
    print()
    
    print("Wechseln zu Deutsch...")
    studio.set_language('de')
    print(f"Aktuelle Sprache: {studio.get_language()}")
    print(f"Nachricht: {studio.lang.t('welcome')}")
    print()
    
    # Resumen
    print(f"\n{'='*60}")
    print("RESUMEN / SUMMARY")
    print('='*60)
    print()
    print("✓ Detección temprana de idioma del sistema")
    print("  Early detection of system language")
    print()
    print("✓ 6 idiomas soportados:")
    print("  - Español (es)")
    print("  - English (en)")
    print("  - Français (fr)")
    print("  - Deutsch (de)")
    print("  - Português (pt)")
    print("  - Italiano (it)")
    print()
    print("✓ Cambio dinámico de idioma en tiempo de ejecución")
    print("  Dynamic language switching at runtime")
    print()
    print("✓ Traducción completa de todos los mensajes")
    print("  Complete translation of all messages")
    print()
    print("✓ API multilingüe para desarrolladores")
    print("  Multilingual API for developers")
    print()
    print('='*60)
    print()


if __name__ == "__main__":
    main()
