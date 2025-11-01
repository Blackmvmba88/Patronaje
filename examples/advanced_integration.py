#!/usr/bin/env python3
"""
Ejemplo avanzado: Integración con módulos LED y materiales reflectantes
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from phantomfit_studio import PhantomFitStudio


def main():
    """Ejemplo de integración con módulos LED y materiales reflectantes."""
    
    print("="*60)
    print("PhantomFit Studio - Integración Tecnológica")
    print("="*60)
    print()
    
    # Crear estudio
    studio = PhantomFitStudio()
    
    # Generar una chaqueta deportiva
    measurements = {
        "bust": 95,
        "waist": 80,
        "hip": 100,
        "shoulder": 45,
        "back_length": 42,
        "sleeve_length": 60,
        "height": 170
    }
    
    print("1. Generando patrón de chaqueta deportiva...")
    pattern = studio.generate_pattern(
        garment_type="jacket",
        measurements=measurements,
        style_options={"ease": 10}
    )
    print(f"   ✓ Patrón generado")
    print()
    
    # Cargar modelo
    print("2. Cargando modelo fantasma...")
    studio.load_phantom_model(measurements, pose="default")
    print("   ✓ Modelo cargado")
    print()
    
    # Agregar módulos LED
    print("3. Agregando módulos LED...")
    
    # LED en hombros
    led1 = studio.add_led_module({
        "position": [-20, 150, 5],
        "color": [255, 100, 0],
        "intensity": 80,
        "pattern": "pulse",
        "size": "small"
    })
    print(f"   ✓ LED hombro izquierdo: {led1[:8]}...")
    
    led2 = studio.add_led_module({
        "position": [20, 150, 5],
        "color": [255, 100, 0],
        "intensity": 80,
        "pattern": "pulse",
        "size": "small"
    })
    print(f"   ✓ LED hombro derecho: {led2[:8]}...")
    
    # LED en espalda
    led3 = studio.add_led_module({
        "position": [0, 100, -10],
        "color": [0, 255, 255],
        "intensity": 100,
        "pattern": "rainbow",
        "size": "medium"
    })
    print(f"   ✓ LED espalda: {led3[:8]}...")
    print()
    
    # Agregar materiales reflectantes
    print("4. Agregando materiales reflectantes...")
    
    # Franjas reflectantes en mangas
    reflective1 = studio.add_reflective_material({
        "area": [[0, 0], [30, 0], [30, 5], [0, 5]],
        "reflectivity": 0.9,
        "color": [220, 220, 220],
        "pattern": "stripe"
    })
    print(f"   ✓ Franja manga izquierda: {reflective1[:8]}...")
    
    reflective2 = studio.add_reflective_material({
        "area": [[0, 0], [30, 0], [30, 5], [0, 5]],
        "reflectivity": 0.9,
        "color": [220, 220, 220],
        "pattern": "stripe"
    })
    print(f"   ✓ Franja manga derecha: {reflective2[:8]}...")
    
    # Material reflectante en la espalda
    reflective3 = studio.add_reflective_material({
        "area": [[0, 0], [20, 0], [20, 30], [0, 30]],
        "reflectivity": 0.95,
        "color": [230, 230, 230],
        "pattern": "geometric"
    })
    print(f"   ✓ Panel reflectante espalda: {reflective3[:8]}...")
    print()
    
    # Visualizar
    print("5. Visualizando diseño completo...")
    studio.visualize_pattern()
    studio.show_3d_view()
    print()
    
    # Información del diseño
    print("6. Información del diseño:")
    info = studio.get_pattern_info()
    print(f"   - Piezas del patrón: {info['pieces']}")
    print(f"   - Módulos LED: {len(info['modules']['led_modules'])}")
    print(f"   - Materiales reflectantes: {len(info['modules']['reflective_materials'])}")
    print()
    
    # Requisitos de energía
    power_req = studio.module_manager.get_power_requirements()
    print("7. Requisitos de energía:")
    print(f"   - Consumo total: {power_req['total_power_w']:.2f} W")
    print(f"   - Promedio por módulo: {power_req['average_per_module_mw']:.1f} mW")
    print()
    
    # Cobertura de materiales
    coverage = studio.module_manager.get_material_coverage()
    print("8. Cobertura reflectante:")
    print(f"   - Área total: {coverage['total_area_cm2']:.1f} cm²")
    print(f"   - Reflectividad promedio: {coverage['average_reflectivity']:.2f}")
    print()
    
    print("="*60)
    print("Diseño tecnológico completado!")
    print("="*60)


if __name__ == "__main__":
    main()
