"""
Visualizador 3D de muñeca fantasma
"""

import json
from typing import Dict, List, Tuple, Any, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from ..i18n import LanguageManager


class PhantomViewer:
    """
    Visualizador 3D para la muñeca fantasma y patrones de ropa.
    
    Proporciona visualización interactiva en 3D de:
    - Modelo de muñeca fantasma parametrizable
    - Patrones de ropa mapeados sobre el modelo
    - Módulos LED y materiales reflectantes
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None, language_manager: Optional['LanguageManager'] = None):
        """
        Inicializa el visualizador.
        
        Args:
            config: Configuración del visualizador
            language_manager: Gestor de idiomas
        """
        self.config = config or {}
        self.lang = language_manager
        self.phantom_model = None
        self.current_pattern = None
        self.camera_position = (0, 0, 300)
        self.lighting_setup = self._default_lighting()
        self.materials = []
        
    def create_phantom(self, 
                      measurements: Dict[str, float],
                      pose: str = "default") -> Dict[str, Any]:
        """
        Crea un modelo de muñeca fantasma basado en medidas.
        
        Args:
            measurements: Medidas corporales
            pose: Pose del modelo
            
        Returns:
            Modelo 3D de la muñeca fantasma
        """
        # Extraer medidas principales
        bust = measurements.get("bust", 90)
        waist = measurements.get("waist", 70)
        hip = measurements.get("hip", 95)
        height = measurements.get("height", 165)
        shoulder = measurements.get("shoulder", 40)
        
        # Crear geometría del modelo
        self.phantom_model = {
            "type": "phantom_mannequin",
            "measurements": measurements,
            "pose": pose,
            "geometry": {
                "head": self._create_head(height),
                "torso": self._create_torso(bust, waist, hip, height),
                "arms": self._create_arms(shoulder, height, pose),
                "legs": self._create_legs(hip, height, pose)
            },
            "material": {
                "type": "translucent",
                "color": [0.8, 0.8, 0.9, 0.3],  # RGBA - semi-transparente
                "wireframe": True,
                "opacity": 0.3
            },
            "joints": self._create_joints(pose)
        }
        
        return self.phantom_model
    
    def _create_head(self, height: float) -> Dict[str, Any]:
        """Crea la geometría de la cabeza."""
        head_height = height * 0.13  # ~13% de la altura
        head_width = head_height * 0.7
        
        return {
            "type": "ellipsoid",
            "position": [0, height * 0.94, 0],
            "dimensions": [head_width, head_height, head_width * 0.8],
            "segments": 32
        }
    
    def _create_torso(self, bust: float, waist: float, hip: float, 
                      height: float) -> Dict[str, Any]:
        """Crea la geometría del torso."""
        # Torso desde cuello hasta cadera
        torso_start = height * 0.87
        torso_end = height * 0.54
        torso_height = torso_start - torso_end
        
        # Crear segmentos del torso con diferentes circunferencias
        segments = [
            {"y": torso_start, "circumference": bust * 0.4, "label": "shoulders"},
            {"y": torso_start - torso_height * 0.3, "circumference": bust, "label": "bust"},
            {"y": torso_start - torso_height * 0.6, "circumference": waist, "label": "waist"},
            {"y": torso_end, "circumference": hip, "label": "hip"}
        ]
        
        return {
            "type": "lofted_surface",
            "segments": segments,
            "smooth": True
        }
    
    def _create_arms(self, shoulder: float, height: float, 
                     pose: str) -> Dict[str, Any]:
        """Crea la geometría de los brazos."""
        arm_length = height * 0.35
        shoulder_y = height * 0.87
        
        if pose == "arms_up":
            # Brazos levantados
            left_angle = 135
            right_angle = 45
        elif pose == "arms_out":
            # Brazos extendidos
            left_angle = 90
            right_angle = 90
        else:
            # Pose por defecto - brazos a los lados
            left_angle = 15
            right_angle = 15
        
        return {
            "left": {
                "type": "cylinder",
                "start": [-shoulder * 0.55, shoulder_y, 0],
                "length": arm_length,
                "radius": 3.5,
                "angle": left_angle
            },
            "right": {
                "type": "cylinder",
                "start": [shoulder * 0.55, shoulder_y, 0],
                "length": arm_length,
                "radius": 3.5,
                "angle": right_angle
            }
        }
    
    def _create_legs(self, hip: float, height: float, pose: str) -> Dict[str, Any]:
        """Crea la geometría de las piernas."""
        leg_length = height * 0.54
        hip_y = height * 0.54
        
        if pose == "sitting":
            # Piernas dobladas
            upper_angle = 90
            lower_angle = 90
        else:
            # Piernas rectas
            upper_angle = 0
            lower_angle = 0
        
        leg_separation = hip * 0.15
        
        return {
            "left": {
                "type": "cylinder",
                "start": [-leg_separation, hip_y, 0],
                "length": leg_length,
                "radius": 4.5,
                "angle": upper_angle
            },
            "right": {
                "type": "cylinder",
                "start": [leg_separation, hip_y, 0],
                "length": leg_length,
                "radius": 4.5,
                "angle": upper_angle
            }
        }
    
    def _create_joints(self, pose: str) -> List[Dict[str, Any]]:
        """Crea los puntos de articulación."""
        return [
            {"name": "neck", "type": "ball"},
            {"name": "left_shoulder", "type": "ball"},
            {"name": "right_shoulder", "type": "ball"},
            {"name": "left_elbow", "type": "hinge"},
            {"name": "right_elbow", "type": "hinge"},
            {"name": "waist", "type": "ball"},
            {"name": "left_hip", "type": "ball"},
            {"name": "right_hip", "type": "ball"},
            {"name": "left_knee", "type": "hinge"},
            {"name": "right_knee", "type": "hinge"}
        ]
    
    def display_pattern(self, pattern: Dict[str, Any]) -> None:
        """
        Visualiza un patrón sobre la muñeca fantasma.
        
        Args:
            pattern: Patrón a visualizar
        """
        if self.phantom_model is None:
            raise ValueError("Primero debe crear un modelo fantasma")
        
        self.current_pattern = pattern
        
        # Mapear piezas del patrón sobre el modelo 3D
        garment_type = pattern.get("garment_type")
        pieces = pattern.get("pieces", [])
        
        mapped_pieces = []
        for piece in pieces:
            mapped_piece = self._map_pattern_to_3d(piece, garment_type)
            mapped_pieces.append(mapped_piece)
        
        pattern["mapped_3d"] = mapped_pieces
    
    def _map_pattern_to_3d(self, piece: Dict[str, Any], 
                           garment_type: str) -> Dict[str, Any]:
        """
        Mapea una pieza de patrón 2D al modelo 3D.
        
        Args:
            piece: Pieza del patrón
            garment_type: Tipo de prenda
            
        Returns:
            Pieza mapeada en 3D
        """
        piece_type = piece.get("type")
        piece_name = piece.get("name")
        points_2d = piece.get("points", [])
        
        # Determinar la superficie del modelo donde mapear
        if "front" in piece_name:
            surface = "torso_front"
        elif "back" in piece_name:
            surface = "torso_back"
        elif "sleeve" in piece_name:
            if "left" in piece_name:
                surface = "arm_left"
            else:
                surface = "arm_right"
        elif "leg" in piece_name or "pants" in piece_name:
            if "left" in piece_name:
                surface = "leg_left"
            else:
                surface = "leg_right"
        else:
            surface = "torso_front"
        
        # Convertir puntos 2D a malla 3D
        mesh_3d = self._create_3d_mesh(points_2d, surface)
        
        return {
            "name": piece_name,
            "type": piece_type,
            "surface": surface,
            "mesh": mesh_3d,
            "material": {
                "type": "fabric",
                "color": [0.9, 0.9, 0.95, 0.8],
                "texture": "fabric_weave"
            }
        }
    
    def _create_3d_mesh(self, points_2d: List[Tuple[float, float]], 
                       surface: str) -> Dict[str, Any]:
        """Crea una malla 3D a partir de puntos 2D."""
        # Convertir puntos 2D en vertices 3D
        vertices = []
        for i, (x, y) in enumerate(points_2d):
            # Proyectar sobre la superficie correspondiente
            vertex_3d = self._project_to_surface(x, y, surface)
            vertices.append(vertex_3d)
        
        # Crear triángulos para la malla
        triangles = self._triangulate_points(len(vertices))
        
        return {
            "vertices": vertices,
            "triangles": triangles,
            "normals": self._calculate_normals(vertices, triangles)
        }
    
    def _project_to_surface(self, x: float, y: float, 
                           surface: str) -> List[float]:
        """Proyecta un punto 2D sobre una superficie 3D."""
        if "torso" in surface:
            # Proyectar sobre el torso (cilindro aproximado)
            if "front" in surface:
                z = 8  # Adelante
            else:
                z = -8  # Atrás
            return [x, y + 80, z]
        elif "arm" in surface:
            # Proyectar sobre el brazo
            offset = 20 if "left" in surface else -20
            return [offset, y + 50, x / 2]
        elif "leg" in surface:
            # Proyectar sobre la pierna
            offset = 8 if "left" in surface else -8
            return [offset, y, x / 2]
        else:
            return [x, y, 0]
    
    def _triangulate_points(self, num_points: int) -> List[List[int]]:
        """Triangula un conjunto de puntos."""
        triangles = []
        if num_points < 3:
            return triangles
        
        # Triangulación simple en abanico
        for i in range(1, num_points - 1):
            triangles.append([0, i, i + 1])
        
        return triangles
    
    def _calculate_normals(self, vertices: List[List[float]], 
                          triangles: List[List[int]]) -> List[List[float]]:
        """Calcula las normales de la superficie."""
        normals = [[0, 0, 1] for _ in vertices]  # Normales por defecto
        return normals
    
    def _default_lighting(self) -> Dict[str, Any]:
        """Configuración de iluminación por defecto."""
        return {
            "ambient": {
                "color": [0.3, 0.3, 0.3],
                "intensity": 0.5
            },
            "directional": [
                {
                    "position": [100, 200, 100],
                    "color": [1.0, 1.0, 1.0],
                    "intensity": 0.8
                },
                {
                    "position": [-100, 150, 50],
                    "color": [0.9, 0.9, 1.0],
                    "intensity": 0.4
                }
            ]
        }
    
    def show(self) -> None:
        """
        Muestra la visualización 3D interactiva.
        
        En una implementación completa, esto abriría una ventana con:
        - Modelo 3D de la muñeca fantasma
        - Patrón mapeado sobre el modelo
        - Controles de cámara interactivos
        - Opciones de visualización (wireframe, sólido, etc.)
        """
        if self.phantom_model is None:
            raise ValueError("No hay modelo fantasma para mostrar")
        
        # Generar representación en consola
        print("\n" + "="*60)
        print("PHANTOMFIT STUDIO - VISTA 3D")
        print("="*60)
        print(f"\nModelo Fantasma:")
        print(f"  Pose: {self.phantom_model['pose']}")
        print(f"  Medidas: {json.dumps(self.phantom_model['measurements'], indent=4)}")
        
        if self.current_pattern:
            print(f"\nPatrón Actual:")
            print(f"  Tipo: {self.current_pattern['garment_type']}")
            print(f"  Piezas: {len(self.current_pattern['pieces'])}")
            
            if "mapped_3d" in self.current_pattern:
                print(f"\n  Piezas Mapeadas en 3D:")
                for piece in self.current_pattern["mapped_3d"]:
                    print(f"    - {piece['name']}: {piece['surface']}")
        
        print(f"\nCámara: {self.camera_position}")
        print(f"Iluminación: {len(self.lighting_setup['directional'])} luces direccionales")
        print("\n" + "="*60)
        print("CONTROLES:")
        print("  [En una implementación completa]")
        print("  - Ratón: Rotar cámara")
        print("  - Rueda: Zoom")
        print("  - Teclas: W/A/S/D para mover")
        print("="*60 + "\n")
    
    def add_led_visualization(self, led_config: Dict[str, Any]) -> None:
        """
        Agrega visualización de módulo LED.
        
        Args:
            led_config: Configuración del LED
        """
        led_visual = {
            "type": "led_module",
            "position": led_config.get("position", [0, 0, 0]),
            "color": led_config.get("color", [1.0, 1.0, 1.0]),
            "intensity": led_config.get("intensity", 1.0),
            "radius": led_config.get("radius", 0.5),
            "animation": led_config.get("animation", "static")
        }
        self.materials.append(led_visual)
    
    def add_reflective_visualization(self, material_config: Dict[str, Any]) -> None:
        """
        Agrega visualización de material reflectante.
        
        Args:
            material_config: Configuración del material
        """
        reflective_visual = {
            "type": "reflective_material",
            "area": material_config.get("area", []),
            "reflectivity": material_config.get("reflectivity", 0.8),
            "color": material_config.get("color", [0.9, 0.9, 0.9]),
            "pattern": material_config.get("pattern", "uniform")
        }
        self.materials.append(reflective_visual)
    
    def export_3d_model(self, filepath: str, format: str = "obj") -> None:
        """
        Exporta el modelo 3D a un archivo.
        
        Args:
            filepath: Ruta del archivo
            format: Formato (obj, stl, gltf)
        """
        if self.phantom_model is None:
            raise ValueError("No hay modelo para exportar")
        
        if format == "obj":
            self._export_obj(filepath)
        elif format == "stl":
            self._export_stl(filepath)
        elif format == "gltf":
            self._export_gltf(filepath)
        else:
            raise ValueError(f"Formato no soportado: {format}")
    
    def _export_obj(self, filepath: str) -> None:
        """Exporta a formato OBJ."""
        with open(filepath, 'w') as f:
            f.write("# PhantomFit Studio - Phantom Model\n")
            f.write(f"# Pose: {self.phantom_model['pose']}\n")
            f.write("# Generated by PhantomFit Studio\n\n")
            
            # En una implementación completa, escribir vertices y faces
            f.write("# Model data would be here\n")
    
    def _export_stl(self, filepath: str) -> None:
        """Exporta a formato STL."""
        raise NotImplementedError("Exportación STL requiere implementación completa de geometría")
    
    def _export_gltf(self, filepath: str) -> None:
        """Exporta a formato GLTF."""
        raise NotImplementedError("Exportación GLTF requiere implementación completa de geometría")
