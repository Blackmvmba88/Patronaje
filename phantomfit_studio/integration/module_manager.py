"""
Gestor de módulos LED y materiales reflectantes
"""

import uuid
from typing import Dict, List, Any, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from ..i18n import LanguageManager


class ModuleManager:
    """
    Gestor de integración para módulos LED y materiales reflectantes.
    
    Proporciona funcionalidades para:
    - Agregar y configurar módulos LED
    - Gestionar materiales reflectantes
    - Controlar patrones de iluminación
    - Simular comportamiento de componentes tecnológicos
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None, language_manager: Optional['LanguageManager'] = None):
        """
        Inicializa el gestor de módulos.
        
        Args:
            config: Configuración opcional del gestor
            language_manager: Gestor de idiomas
        """
        self.config = config or {}
        self.lang = language_manager
        self.led_modules = {}
        self.reflective_materials = {}
        self.lighting_patterns = self._default_patterns()
    
    def add_led_module(self, module_config: Dict[str, Any]) -> str:
        """
        Agrega un módulo LED al diseño.
        
        Args:
            module_config: Configuración del módulo LED con:
                - position: Posición en el patrón (x, y, z)
                - color: Color RGB (0-255)
                - intensity: Intensidad (0-100)
                - pattern: Patrón de iluminación
                - size: Tamaño del módulo
                
        Returns:
            ID único del módulo
        """
        module_id = str(uuid.uuid4())
        
        led_module = {
            "id": module_id,
            "type": "led",
            "position": module_config.get("position", [0, 0, 0]),
            "color": module_config.get("color", [255, 255, 255]),
            "intensity": module_config.get("intensity", 100),
            "pattern": module_config.get("pattern", "static"),
            "size": module_config.get("size", "small"),
            "power_consumption": self._calculate_power_consumption(module_config),
            "status": "active"
        }
        
        self.led_modules[module_id] = led_module
        return module_id
    
    def add_reflective_material(self, material_config: Dict[str, Any]) -> str:
        """
        Agrega un material reflectante al diseño.
        
        Args:
            material_config: Configuración del material con:
                - area: Área de aplicación [(x1, y1), (x2, y2), ...]
                - reflectivity: Coeficiente de reflectividad (0-1)
                - color: Color base del material
                - pattern: Patrón reflectante (uniform, stripe, geometric)
                
        Returns:
            ID único del material
        """
        material_id = str(uuid.uuid4())
        
        reflective_material = {
            "id": material_id,
            "type": "reflective",
            "area": material_config.get("area", []),
            "reflectivity": material_config.get("reflectivity", 0.8),
            "color": material_config.get("color", [200, 200, 200]),
            "pattern": material_config.get("pattern", "uniform"),
            "surface_area": self._calculate_surface_area(material_config.get("area", [])),
            "status": "active"
        }
        
        self.reflective_materials[material_id] = reflective_material
        return material_id
    
    def get_active_modules(self) -> Dict[str, List[str]]:
        """
        Obtiene los módulos activos.
        
        Returns:
            Diccionario con listas de IDs de módulos activos
        """
        active_leds = [
            module_id for module_id, module in self.led_modules.items()
            if module["status"] == "active"
        ]
        
        active_reflective = [
            material_id for material_id, material in self.reflective_materials.items()
            if material["status"] == "active"
        ]
        
        return {
            "led_modules": active_leds,
            "reflective_materials": active_reflective
        }
    
    def update_led_pattern(self, module_id: str, pattern: str) -> None:
        """
        Actualiza el patrón de iluminación de un módulo LED.
        
        Args:
            module_id: ID del módulo
            pattern: Nuevo patrón (static, blink, fade, pulse, rainbow, wave)
        """
        if module_id not in self.led_modules:
            raise ValueError(f"Módulo LED no encontrado: {module_id}")
        
        if pattern not in self.lighting_patterns:
            raise ValueError(f"Patrón no soportado: {pattern}")
        
        self.led_modules[module_id]["pattern"] = pattern
        self.led_modules[module_id]["pattern_config"] = self.lighting_patterns[pattern]
    
    def update_led_color(self, module_id: str, color: List[int]) -> None:
        """
        Actualiza el color de un módulo LED.
        
        Args:
            module_id: ID del módulo
            color: Color RGB [r, g, b] (0-255)
        """
        if module_id not in self.led_modules:
            raise ValueError(f"Módulo LED no encontrado: {module_id}")
        
        if len(color) != 3 or not all(0 <= c <= 255 for c in color):
            raise ValueError("Color debe ser RGB con valores 0-255")
        
        self.led_modules[module_id]["color"] = color
    
    def update_led_intensity(self, module_id: str, intensity: float) -> None:
        """
        Actualiza la intensidad de un módulo LED.
        
        Args:
            module_id: ID del módulo
            intensity: Intensidad (0-100)
        """
        if module_id not in self.led_modules:
            raise ValueError(f"Módulo LED no encontrado: {module_id}")
        
        if not 0 <= intensity <= 100:
            raise ValueError("Intensidad debe estar entre 0 y 100")
        
        self.led_modules[module_id]["intensity"] = intensity
    
    def get_module_info(self, module_id: str) -> Dict[str, Any]:
        """
        Obtiene información de un módulo.
        
        Args:
            module_id: ID del módulo
            
        Returns:
            Información del módulo
        """
        if module_id in self.led_modules:
            return self.led_modules[module_id].copy()
        elif module_id in self.reflective_materials:
            return self.reflective_materials[module_id].copy()
        else:
            raise ValueError(f"Módulo no encontrado: {module_id}")
    
    def remove_module(self, module_id: str) -> None:
        """
        Elimina un módulo.
        
        Args:
            module_id: ID del módulo a eliminar
        """
        if module_id in self.led_modules:
            del self.led_modules[module_id]
        elif module_id in self.reflective_materials:
            del self.reflective_materials[module_id]
        else:
            raise ValueError(f"Módulo no encontrado: {module_id}")
    
    def get_power_requirements(self) -> Dict[str, float]:
        """
        Calcula los requisitos de energía para todos los módulos LED.
        
        Returns:
            Diccionario con información de consumo de energía
        """
        total_power = sum(
            module["power_consumption"]
            for module in self.led_modules.values()
            if module["status"] == "active"
        )
        
        return {
            "total_power_mw": total_power,
            "total_power_w": total_power / 1000,
            "num_modules": len([m for m in self.led_modules.values() if m["status"] == "active"]),
            "average_per_module_mw": total_power / max(1, len(self.led_modules))
        }
    
    def get_material_coverage(self) -> Dict[str, float]:
        """
        Calcula la cobertura de materiales reflectantes.
        
        Returns:
            Información sobre cobertura de materiales
        """
        total_area = sum(
            material["surface_area"]
            for material in self.reflective_materials.values()
            if material["status"] == "active"
        )
        
        return {
            "total_area_cm2": total_area,
            "num_materials": len([m for m in self.reflective_materials.values() if m["status"] == "active"]),
            "average_reflectivity": self._calculate_average_reflectivity()
        }
    
    def simulate_lighting_effect(self, module_id: str, 
                                 duration: float = 1.0) -> List[Dict[str, Any]]:
        """
        Simula el efecto de iluminación de un módulo LED.
        
        Args:
            module_id: ID del módulo
            duration: Duración de la simulación en segundos
            
        Returns:
            Lista de estados del LED a lo largo del tiempo
        """
        if module_id not in self.led_modules:
            raise ValueError(f"Módulo LED no encontrado: {module_id}")
        
        module = self.led_modules[module_id]
        pattern = module["pattern"]
        pattern_config = self.lighting_patterns[pattern]
        
        # Generar frames de la animación
        fps = 30
        num_frames = int(duration * fps)
        frames = []
        
        for frame in range(num_frames):
            time = frame / fps
            state = self._calculate_led_state(module, pattern_config, time)
            frames.append({
                "time": time,
                "color": state["color"],
                "intensity": state["intensity"]
            })
        
        return frames
    
    def _default_patterns(self) -> Dict[str, Dict[str, Any]]:
        """Define los patrones de iluminación por defecto."""
        return {
            "static": {
                "type": "constant",
                "description": "Luz constante"
            },
            "blink": {
                "type": "toggle",
                "frequency": 2.0,  # Hz
                "duty_cycle": 0.5,
                "description": "Parpadeo regular"
            },
            "fade": {
                "type": "sine_wave",
                "frequency": 0.5,
                "min_intensity": 0,
                "max_intensity": 100,
                "description": "Desvanecimiento suave"
            },
            "pulse": {
                "type": "triangle_wave",
                "frequency": 1.0,
                "min_intensity": 20,
                "max_intensity": 100,
                "description": "Pulso de intensidad"
            },
            "rainbow": {
                "type": "color_cycle",
                "frequency": 0.2,
                "description": "Ciclo de colores"
            },
            "wave": {
                "type": "wave",
                "frequency": 0.3,
                "phase_shift": 0,
                "description": "Onda de luz"
            }
        }
    
    def _calculate_power_consumption(self, config: Dict[str, Any]) -> float:
        """Calcula el consumo de energía de un módulo LED (en mW)."""
        size_power = {
            "small": 20,   # 20mW
            "medium": 50,  # 50mW
            "large": 100   # 100mW
        }
        
        base_power = size_power.get(config.get("size", "small"), 20)
        intensity_factor = config.get("intensity", 100) / 100
        
        return base_power * intensity_factor
    
    def _calculate_surface_area(self, area_points: List[List[float]]) -> float:
        """Calcula el área superficial de un material reflectante."""
        if len(area_points) < 3:
            return 0
        
        # Cálculo aproximado usando el método del trapecio
        total_area = 0
        for i in range(len(area_points)):
            j = (i + 1) % len(area_points)
            total_area += area_points[i][0] * area_points[j][1]
            total_area -= area_points[j][0] * area_points[i][1]
        
        return abs(total_area) / 2
    
    def _calculate_average_reflectivity(self) -> float:
        """Calcula la reflectividad promedio de todos los materiales activos."""
        active_materials = [
            m for m in self.reflective_materials.values()
            if m["status"] == "active"
        ]
        
        if not active_materials:
            return 0
        
        total_reflectivity = sum(m["reflectivity"] for m in active_materials)
        return total_reflectivity / len(active_materials)
    
    def _calculate_led_state(self, module: Dict[str, Any], 
                            pattern_config: Dict[str, Any],
                            time: float) -> Dict[str, Any]:
        """Calcula el estado del LED en un momento dado."""
        import math
        
        pattern_type = pattern_config["type"]
        base_color = module["color"]
        base_intensity = module["intensity"]
        
        if pattern_type == "constant":
            return {
                "color": base_color,
                "intensity": base_intensity
            }
        
        elif pattern_type == "toggle":
            frequency = pattern_config["frequency"]
            duty_cycle = pattern_config["duty_cycle"]
            phase = (time * frequency) % 1.0
            
            intensity = base_intensity if phase < duty_cycle else 0
            return {
                "color": base_color,
                "intensity": intensity
            }
        
        elif pattern_type == "sine_wave":
            frequency = pattern_config["frequency"]
            min_intensity = pattern_config["min_intensity"]
            max_intensity = pattern_config["max_intensity"]
            
            value = math.sin(2 * math.pi * frequency * time)
            intensity = min_intensity + (max_intensity - min_intensity) * (value + 1) / 2
            
            return {
                "color": base_color,
                "intensity": intensity
            }
        
        elif pattern_type == "triangle_wave":
            frequency = pattern_config["frequency"]
            min_intensity = pattern_config["min_intensity"]
            max_intensity = pattern_config["max_intensity"]
            
            phase = (time * frequency) % 1.0
            if phase < 0.5:
                value = phase * 2
            else:
                value = (1 - phase) * 2
            
            intensity = min_intensity + (max_intensity - min_intensity) * value
            
            return {
                "color": base_color,
                "intensity": intensity
            }
        
        elif pattern_type == "color_cycle":
            frequency = pattern_config["frequency"]
            phase = (time * frequency) % 1.0
            
            # Ciclo de colores RGB
            if phase < 0.33:
                color = [255, int(255 * (phase / 0.33)), 0]
            elif phase < 0.66:
                color = [int(255 * (1 - (phase - 0.33) / 0.33)), 255, 0]
            else:
                color = [0, int(255 * (1 - (phase - 0.66) / 0.34)), 255]
            
            return {
                "color": color,
                "intensity": base_intensity
            }
        
        elif pattern_type == "wave":
            frequency = pattern_config["frequency"]
            phase_shift = pattern_config.get("phase_shift", 0)
            
            value = math.sin(2 * math.pi * frequency * time + phase_shift)
            intensity = base_intensity * (value + 1) / 2
            
            return {
                "color": base_color,
                "intensity": intensity
            }
        
        return {
            "color": base_color,
            "intensity": base_intensity
        }
