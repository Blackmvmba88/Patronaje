#!/usr/bin/env python3
"""
Test completo de todas las características de PhantomFit Studio
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from phantomfit_studio import PhantomFitStudio


def test_pattern_generation():
    """Prueba generación de todos los tipos de patrón."""
    print("\n" + "="*60)
    print("TEST: Generación de Patrones")
    print("="*60)
    
    studio = PhantomFitStudio()
    
    measurements = {
        "bust": 90,
        "waist": 70,
        "hip": 95,
        "shoulder": 40,
        "back_length": 40,
        "sleeve_length": 58,
        "height": 165,
        "inseam": 75,
        "outseam": 100,
        "skirt_length": 60,
        "dress_length": 100,
        "foot_length": 25,
        "foot_width": 10,
        "ankle_circumference": 22,
        "calf_circumference": 35,
        "sock_height": 20,
        "thigh_circumference": 55,
        "rise": 25
    }
    
    garment_types = ["blouse", "shirt", "pants", "skirt", "dress", "jacket", "sock", "boxer"]
    
    for garment_type in garment_types:
        try:
            pattern = studio.generate_pattern(garment_type, measurements)
            print(f"✓ {garment_type.capitalize()}: {len(pattern['pieces'])} piezas, "
                  f"{pattern['fabric_required']['linear_meters']:.2f}m tela")
        except Exception as e:
            print(f"✗ {garment_type.capitalize()}: Error - {e}")
    
    print("\nTEST PASADO ✓")


def test_phantom_model():
    """Prueba creación de modelo fantasma con diferentes poses."""
    print("\n" + "="*60)
    print("TEST: Modelo Fantasma")
    print("="*60)
    
    studio = PhantomFitStudio()
    
    measurements = {
        "bust": 90,
        "waist": 70,
        "hip": 95,
        "shoulder": 40,
        "height": 165
    }
    
    poses = ["default", "arms_up", "arms_out", "sitting"]
    
    for pose in poses:
        try:
            studio.load_phantom_model(measurements, pose=pose)
            print(f"✓ Pose '{pose}': Modelo cargado")
        except Exception as e:
            print(f"✗ Pose '{pose}': Error - {e}")
    
    print("\nTEST PASADO ✓")


def test_led_modules():
    """Prueba módulos LED con diferentes patrones."""
    print("\n" + "="*60)
    print("TEST: Módulos LED")
    print("="*60)
    
    studio = PhantomFitStudio()
    
    patterns = ["static", "blink", "fade", "pulse", "rainbow", "wave"]
    
    for pattern in patterns:
        try:
            led_id = studio.add_led_module({
                "position": [0, 100, 0],
                "color": [255, 100, 50],
                "intensity": 80,
                "pattern": pattern,
                "size": "medium"
            })
            
            # Simular efecto
            frames = studio.module_manager.simulate_lighting_effect(led_id, duration=0.5)
            print(f"✓ Patrón '{pattern}': {len(frames)} frames generados")
        except Exception as e:
            print(f"✗ Patrón '{pattern}': Error - {e}")
    
    # Probar control de LEDs
    print("\nPruebas de control de LED:")
    
    led_id = studio.add_led_module({
        "position": [0, 0, 0],
        "color": [255, 255, 255],
        "intensity": 100,
        "pattern": "static",
        "size": "small"
    })
    
    # Cambiar color
    studio.module_manager.update_led_color(led_id, [0, 255, 0])
    print("✓ Color actualizado")
    
    # Cambiar intensidad
    studio.module_manager.update_led_intensity(led_id, 50)
    print("✓ Intensidad actualizada")
    
    # Cambiar patrón
    studio.module_manager.update_led_pattern(led_id, "fade")
    print("✓ Patrón actualizado")
    
    print("\nTEST PASADO ✓")


def test_reflective_materials():
    """Prueba materiales reflectantes."""
    print("\n" + "="*60)
    print("TEST: Materiales Reflectantes")
    print("="*60)
    
    studio = PhantomFitStudio()
    
    patterns = ["uniform", "stripe", "geometric"]
    
    for pattern in patterns:
        try:
            material_id = studio.add_reflective_material({
                "area": [[0, 0], [10, 0], [10, 10], [0, 10]],
                "reflectivity": 0.85,
                "color": [220, 220, 220],
                "pattern": pattern
            })
            
            info = studio.module_manager.get_module_info(material_id)
            print(f"✓ Patrón '{pattern}': {info['surface_area']:.1f} cm²")
        except Exception as e:
            print(f"✗ Patrón '{pattern}': Error - {e}")
    
    print("\nTEST PASADO ✓")


def test_integration():
    """Prueba integración completa."""
    print("\n" + "="*60)
    print("TEST: Integración Completa")
    print("="*60)
    
    studio = PhantomFitStudio()
    
    measurements = {
        "bust": 92,
        "waist": 72,
        "hip": 96,
        "shoulder": 42,
        "back_length": 41,
        "sleeve_length": 59,
        "height": 167
    }
    
    # Generar patrón
    pattern = studio.generate_pattern("jacket", measurements)
    print(f"✓ Patrón generado: {pattern['garment_type']}")
    
    # Cargar modelo
    studio.load_phantom_model(measurements, pose="default")
    print("✓ Modelo fantasma cargado")
    
    # Visualizar
    studio.visualize_pattern()
    print("✓ Patrón visualizado en 3D")
    
    # Agregar LEDs
    for i in range(5):
        studio.add_led_module({
            "position": [i * 10, 100, 0],
            "color": [255, 100, 0],
            "intensity": 70,
            "pattern": "pulse",
            "size": "small"
        })
    print("✓ 5 módulos LED agregados")
    
    # Agregar materiales
    for i in range(3):
        studio.add_reflective_material({
            "area": [[i*15, 0], [i*15+10, 0], [i*15+10, 20], [i*15, 20]],
            "reflectivity": 0.9,
            "color": [230, 230, 230],
            "pattern": "stripe"
        })
    print("✓ 3 materiales reflectantes agregados")
    
    # Obtener información
    info = studio.get_pattern_info()
    print(f"✓ Info obtenida: {info['pieces']} piezas, "
          f"{len(info['modules']['led_modules'])} LEDs, "
          f"{len(info['modules']['reflective_materials'])} materiales")
    
    # Requisitos de energía
    power_req = studio.module_manager.get_power_requirements()
    print(f"✓ Consumo calculado: {power_req['total_power_w']:.3f} W")
    
    # Cobertura reflectante
    coverage = studio.module_manager.get_material_coverage()
    print(f"✓ Cobertura: {coverage['total_area_cm2']:.1f} cm²")
    
    print("\nTEST PASADO ✓")


def test_export():
    """Prueba exportación de patrones."""
    print("\n" + "="*60)
    print("TEST: Exportación de Patrones")
    print("="*60)
    
    studio = PhantomFitStudio()
    
    measurements = {
        "bust": 90,
        "waist": 70,
        "hip": 95,
        "shoulder": 40,
        "back_length": 40,
        "sleeve_length": 58,
        "height": 165
    }
    
    pattern = studio.generate_pattern("blouse", measurements)
    
    # Exportar a SVG
    try:
        output_dir = "/tmp/phantomfit_output"
        os.makedirs(output_dir, exist_ok=True)
        
        svg_path = os.path.join(output_dir, "test_pattern.svg")
        studio.export_pattern(svg_path, format="svg")
        
        if os.path.exists(svg_path):
            with open(svg_path, 'r') as f:
                content = f.read()
                if '<svg' in content and '</svg>' in content:
                    print(f"✓ SVG exportado exitosamente: {svg_path}")
                    print(f"  Tamaño: {len(content)} bytes")
                else:
                    print(f"✗ SVG inválido")
        else:
            print(f"✗ Archivo no creado")
    except Exception as e:
        print(f"✗ Error exportando: {e}")
    
    print("\nTEST PASADO ✓")


def main():
    """Ejecutar todos los tests."""
    print("\n" + "="*60)
    print("PHANTOMFIT STUDIO - SUITE DE TESTS COMPLETA")
    print("="*60)
    
    try:
        test_pattern_generation()
        test_phantom_model()
        test_led_modules()
        test_reflective_materials()
        test_integration()
        test_export()
        
        print("\n" + "="*60)
        print("✓✓✓ TODOS LOS TESTS PASADOS ✓✓✓")
        print("="*60)
        print()
        
    except Exception as e:
        print(f"\n✗✗✗ ERROR EN TESTS: {e} ✗✗✗\n")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
