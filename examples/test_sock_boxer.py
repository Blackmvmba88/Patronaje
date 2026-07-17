#!/usr/bin/env python3
"""
Ejemplo de uso de PhantomFit Studio para calcetines y boxers
"""

import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from phantomfit_studio import PhantomFitStudio


def test_sock_generation():
    """Prueba generación de patrón de calcetín."""
    print("\n" + "="*60)
    print("TEST: Generación de Patrón de Calcetín")
    print("="*60)
    
    studio = PhantomFitStudio()
    
    # Medidas para calcetín
    measurements = {
        "foot_length": 25,
        "foot_width": 10,
        "ankle_circumference": 22,
        "calf_circumference": 35,
        "sock_height": 20
    }
    
    # Probar diferentes estilos
    styles = ["ankle", "crew", "knee-high"]
    
    for style in styles:
        print(f"\n  Generando calcetín estilo '{style}'...")
        pattern = studio.generate_pattern(
            garment_type="calcetín",
            measurements=measurements,
            style_options={"style": style, "ease": 1}
        )
        
        print(f"    ✓ Patrón generado con {len(pattern['pieces'])} piezas")
        print(f"    ✓ Tipo: {pattern['garment_type']}")
        print(f"    ✓ Piezas:")
        for piece in pattern['pieces']:
            print(f"      - {piece['name']} ({piece['type']})")
        print(f"    ✓ Tela requerida: {pattern['fabric_required']['linear_meters']:.2f} metros")
    
    print("\n  ✓ TEST PASADO")
    return True


def test_boxer_generation():
    """Prueba generación de patrón de boxer."""
    print("\n" + "="*60)
    print("TEST: Generación de Patrón de Boxer")
    print("="*60)
    
    studio = PhantomFitStudio()
    
    # Medidas para boxer
    measurements = {
        "waist": 75,
        "hip": 95,
        "inseam": 10,
        "thigh_circumference": 55,
        "rise": 25
    }
    
    # Probar diferentes opciones
    print(f"\n  Generando boxer...")
    pattern = studio.generate_pattern(
        garment_type="boxer",
        measurements=measurements,
        style_options={"ease": 5, "leg_opening": "loose"}
    )
    
    print(f"    ✓ Patrón generado con {len(pattern['pieces'])} piezas")
    print(f"    ✓ Tipo: {pattern['garment_type']}")
    print(f"    ✓ Piezas:")
    for piece in pattern['pieces']:
        print(f"      - {piece['name']} ({piece['type']})")
    print(f"    ✓ Tela requerida: {pattern['fabric_required']['linear_meters']:.2f} metros")
    
    print("\n  ✓ TEST PASADO")
    return True


def test_combined_measurements():
    """Prueba con medidas combinadas para ambos."""
    print("\n" + "="*60)
    print("TEST: Generación con Medidas Personalizadas")
    print("="*60)
    
    studio = PhantomFitStudio()
    
    # Medidas personalizadas
    sock_measurements = {
        "foot_length": 27,
        "foot_width": 11,
        "ankle_circumference": 24,
        "calf_circumference": 38,
        "sock_height": 15
    }
    
    boxer_measurements = {
        "waist": 80,
        "hip": 100,
        "inseam": 12,
        "thigh_circumference": 60,
        "rise": 28
    }
    
    print("\n  Generando calcetín con medidas grandes...")
    sock_pattern = studio.generate_pattern("calcetín", sock_measurements)
    print(f"    ✓ Calcetín: {len(sock_pattern['pieces'])} piezas, "
          f"{sock_pattern['fabric_required']['linear_meters']:.2f}m tela")
    
    print("\n  Generando boxer con medidas grandes...")
    boxer_pattern = studio.generate_pattern("boxer", boxer_measurements)
    print(f"    ✓ Boxer: {len(boxer_pattern['pieces'])} piezas, "
          f"{boxer_pattern['fabric_required']['linear_meters']:.2f}m tela")
    
    print("\n  ✓ TEST PASADO")
    return True


def test_export():
    """Prueba exportación de patrones."""
    print("\n" + "="*60)
    print("TEST: Exportación de Patrones")
    print("="*60)
    
    studio = PhantomFitStudio()
    
    # Generar calcetín
    sock_measurements = {
        "foot_length": 25,
        "foot_width": 10,
        "ankle_circumference": 22,
        "calf_circumference": 35,
        "sock_height": 20
    }
    
    sock_pattern = studio.generate_pattern("calcetín", sock_measurements)
    
    # Exportar a SVG
    output_dir = "/tmp/phantomfit_output"
    os.makedirs(output_dir, exist_ok=True)
    
    sock_svg = os.path.join(output_dir, "sock_pattern.svg")
    studio.export_pattern(sock_svg, format="svg")
    
    if os.path.exists(sock_svg):
        with open(sock_svg, 'r') as f:
            content = f.read()
            print(f"    ✓ Calcetín exportado: {sock_svg}")
            print(f"      Tamaño: {len(content)} bytes")
    
    # Generar boxer
    boxer_measurements = {
        "waist": 75,
        "hip": 95,
        "inseam": 10,
        "thigh_circumference": 55,
        "rise": 25
    }
    
    boxer_pattern = studio.generate_pattern("boxer", boxer_measurements)
    
    boxer_svg = os.path.join(output_dir, "boxer_pattern.svg")
    studio.export_pattern(boxer_svg, format="svg")
    
    if os.path.exists(boxer_svg):
        with open(boxer_svg, 'r') as f:
            content = f.read()
            print(f"    ✓ Boxer exportado: {boxer_svg}")
            print(f"      Tamaño: {len(content)} bytes")
    
    print("\n  ✓ TEST PASADO")
    return True


def main():
    """Ejecutar todos los tests."""
    print("\n" + "="*60)
    print("PHANTOMFIT STUDIO - TESTS DE CALCETÍN Y BOXER")
    print("="*60)
    
    try:
        test_sock_generation()
        test_boxer_generation()
        test_combined_measurements()
        test_export()
        
        print("\n" + "="*60)
        print("✓✓✓ TODOS LOS TESTS PASADOS ✓✓✓")
        print("="*60)
        print()
        
        return True
        
    except Exception as e:
        print(f"\n✗✗✗ ERROR EN TESTS: {e} ✗✗✗\n")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
