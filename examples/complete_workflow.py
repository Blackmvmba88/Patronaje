#!/usr/bin/env python3
"""
Flujo de trabajo completo: Desde medidas hasta prenda tecnológica
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from phantomfit_studio import PhantomFitStudio


def print_section(title):
    """Imprime un separador de sección."""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)


def main():
    """Demuestra el flujo de trabajo completo."""
    
    print("\n" + "🎨 "*20)
    print("\n" + " "*15 + "PHANTOMFIT STUDIO")
    print(" "*10 + "Flujo de Trabajo Completo")
    print("\n" + "🎨 "*20)
    
    # PASO 1: Inicialización
    print_section("PASO 1: Inicialización del Estudio")
    
    studio = PhantomFitStudio()
    print("✓ PhantomFit Studio inicializado")
    print("✓ Generador de patrones listo")
    print("✓ Visualizador 3D listo")
    print("✓ Gestor de módulos listo")
    
    # PASO 2: Tomar medidas
    print_section("PASO 2: Medidas Corporales")
    
    measurements = {
        "bust": 92,
        "waist": 72,
        "hip": 96,
        "shoulder": 42,
        "back_length": 41,
        "sleeve_length": 59,
        "height": 167
    }
    
    print("Medidas ingresadas:")
    for key, value in measurements.items():
        print(f"  {key:15s}: {value:6.1f} cm")
    
    # PASO 3: Diseñar la prenda
    print_section("PASO 3: Diseño de Prenda Base")
    
    print("Generando chaqueta deportiva...")
    pattern = studio.generate_pattern(
        garment_type="jacket",
        measurements=measurements,
        style_options={
            "ease": 10,  # Holgura adicional para prenda deportiva
        }
    )
    
    print(f"✓ Patrón generado exitosamente")
    print(f"  - Tipo: {pattern['garment_type']}")
    print(f"  - Piezas: {len(pattern['pieces'])}")
    print(f"  - Tela requerida: {pattern['fabric_required']['linear_meters']:.2f}m")
    print(f"  - Ancho de tela: {pattern['fabric_required']['fabric_width_cm']}cm")
    
    # PASO 4: Visualización 3D
    print_section("PASO 4: Visualización 3D")
    
    print("Cargando modelo fantasma...")
    studio.load_phantom_model(measurements, pose="default")
    print("✓ Modelo fantasma cargado")
    
    print("\nMapeando patrón al modelo 3D...")
    studio.visualize_pattern()
    print("✓ Patrón mapeado exitosamente")
    
    # PASO 5: Integración tecnológica
    print_section("PASO 5: Integración Tecnológica")
    
    print("\n[A] Agregando módulos LED...")
    
    # LED en hombros para visibilidad
    led_configs = [
        {
            "name": "Hombro Izquierdo",
            "config": {
                "position": [-20, 150, 5],
                "color": [0, 150, 255],  # Azul
                "intensity": 85,
                "pattern": "pulse",
                "size": "small"
            }
        },
        {
            "name": "Hombro Derecho",
            "config": {
                "position": [20, 150, 5],
                "color": [0, 150, 255],
                "intensity": 85,
                "pattern": "pulse",
                "size": "small"
            }
        },
        {
            "name": "Espalda Central",
            "config": {
                "position": [0, 100, -10],
                "color": [255, 50, 0],  # Rojo
                "intensity": 100,
                "pattern": "blink",
                "size": "medium"
            }
        },
        {
            "name": "Manga Izquierda",
            "config": {
                "position": [-30, 120, 0],
                "color": [0, 255, 100],  # Verde
                "intensity": 70,
                "pattern": "wave",
                "size": "small"
            }
        },
        {
            "name": "Manga Derecha",
            "config": {
                "position": [30, 120, 0],
                "color": [0, 255, 100],
                "intensity": 70,
                "pattern": "wave",
                "size": "small"
            }
        }
    ]
    
    led_ids = []
    for led in led_configs:
        led_id = studio.add_led_module(led["config"])
        led_ids.append(led_id)
        print(f"  ✓ {led['name']}: {led['config']['color']} @ {led['config']['intensity']}%")
    
    print(f"\nTotal LEDs instalados: {len(led_ids)}")
    
    print("\n[B] Agregando materiales reflectantes...")
    
    # Franjas reflectantes en mangas
    reflective_configs = [
        {
            "name": "Franja Manga Izquierda",
            "config": {
                "area": [[-30, 100], [-28, 100], [-28, 115], [-30, 115]],
                "reflectivity": 0.95,
                "color": [230, 230, 230],
                "pattern": "stripe"
            }
        },
        {
            "name": "Franja Manga Derecha",
            "config": {
                "area": [[28, 100], [30, 100], [30, 115], [28, 115]],
                "reflectivity": 0.95,
                "color": [230, 230, 230],
                "pattern": "stripe"
            }
        },
        {
            "name": "Panel Espalda",
            "config": {
                "area": [[-10, 90], [10, 90], [10, 120], [-10, 120]],
                "reflectivity": 0.90,
                "color": [240, 240, 240],
                "pattern": "geometric"
            }
        },
        {
            "name": "Franja Inferior",
            "config": {
                "area": [[-20, 50], [20, 50], [20, 55], [-20, 55]],
                "reflectivity": 0.85,
                "color": [235, 235, 235],
                "pattern": "stripe"
            }
        }
    ]
    
    reflective_ids = []
    for material in reflective_configs:
        material_id = studio.add_reflective_material(material["config"])
        reflective_ids.append(material_id)
        print(f"  ✓ {material['name']}: reflectividad {material['config']['reflectivity']}")
    
    print(f"\nTotal materiales reflectantes: {len(reflective_ids)}")
    
    # PASO 6: Análisis técnico
    print_section("PASO 6: Análisis Técnico")
    
    print("\n[A] Requisitos de energía:")
    power_req = studio.module_manager.get_power_requirements()
    print(f"  - Consumo total: {power_req['total_power_w']:.3f} W")
    print(f"  - Consumo por módulo: {power_req['average_per_module_mw']:.1f} mW")
    print(f"  - Módulos activos: {power_req['num_modules']}")
    
    battery_capacity = 2000  # mAh típico para batería portátil
    battery_voltage = 3.7    # V típico para Li-ion
    battery_wh = battery_capacity * battery_voltage / 1000
    runtime_hours = battery_wh / power_req['total_power_w']
    
    print(f"\n  Autonomía estimada:")
    print(f"  - Batería: {battery_capacity}mAh @ {battery_voltage}V")
    print(f"  - Capacidad: {battery_wh:.2f}Wh")
    print(f"  - Duración: ~{runtime_hours:.1f} horas")
    
    print("\n[B] Cobertura reflectante:")
    coverage = studio.module_manager.get_material_coverage()
    print(f"  - Área total: {coverage['total_area_cm2']:.1f} cm²")
    print(f"  - Reflectividad promedio: {coverage['average_reflectivity']:.2%}")
    print(f"  - Materiales activos: {coverage['num_materials']}")
    
    # PASO 7: Visualización final
    print_section("PASO 7: Visualización Final")
    
    print("\nGenerando vista 3D completa...")
    studio.show_3d_view()
    
    # PASO 8: Exportación
    print_section("PASO 8: Exportación")
    
    output_dir = "/tmp/phantomfit_workflow"
    os.makedirs(output_dir, exist_ok=True)
    
    svg_path = os.path.join(output_dir, "tech_jacket_pattern.svg")
    studio.export_pattern(svg_path, format="svg")
    
    if os.path.exists(svg_path):
        print(f"✓ Patrón exportado a: {svg_path}")
        print(f"  Tamaño: {os.path.getsize(svg_path)} bytes")
    
    # Información del diseño
    info = studio.get_pattern_info()
    
    # RESUMEN FINAL
    print_section("RESUMEN DEL PROYECTO")
    
    print(f"""
Chaqueta Deportiva Tecnológica
{'─'*60}

📐 PATRÓN:
  • Tipo: {info['type']}
  • Piezas: {info['pieces']}
  • Tela: {pattern['fabric_required']['linear_meters']:.2f}m

💡 TECNOLOGÍA LED:
  • Módulos: {len(info['modules']['led_modules'])}
  • Patrones: pulse, blink, wave
  • Consumo: {power_req['total_power_w']:.3f}W
  • Autonomía: ~{runtime_hours:.1f}h

✨ REFLECTANTES:
  • Áreas: {len(info['modules']['reflective_materials'])}
  • Cobertura: {coverage['total_area_cm2']:.1f}cm²
  • Reflectividad: {coverage['average_reflectivity']:.0%}

📁 ARCHIVOS:
  • Patrón SVG: {svg_path}
    """)
    
    print("="*60)
    print("✓ PROYECTO COMPLETADO EXITOSAMENTE")
    print("="*60)
    print()
    print("La prenda está lista para fabricación!")
    print("Características ideales para:")
    print("  • Ciclismo urbano nocturno")
    print("  • Running en condiciones de baja luz")
    print("  • Actividades deportivas con requisitos de visibilidad")
    print("  • Moda tecnológica / wearables")
    print()


if __name__ == "__main__":
    main()
