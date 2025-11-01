"""
Generador de patrones de ropa
"""

import math
from typing import Dict, List, Tuple, Any, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from ..i18n import LanguageManager


class PatternGenerator:
    """
    Generador inteligente de patrones de ropa basado en medidas corporales.
    """
    
    def __init__(self, language_manager: Optional['LanguageManager'] = None):
        self.supported_garments = [
            "blouse", "shirt", "pants", "skirt", "dress", "jacket"
        ]
        self.lang = language_manager
    
    def generate(self, 
                 garment_type: str,
                 measurements: Dict[str, float],
                 style_options: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Genera un patrón de ropa.
        
        Args:
            garment_type: Tipo de prenda
            measurements: Medidas corporales en cm
            style_options: Opciones de estilo
            
        Returns:
            Diccionario con el patrón generado
        """
        if garment_type not in self.supported_garments:
            raise ValueError(f"Tipo de prenda no soportado: {garment_type}")
        
        style_options = style_options or {}
        
        # Generar patrón según el tipo de prenda
        if garment_type == "blouse":
            return self._generate_blouse(measurements, style_options)
        elif garment_type == "shirt":
            return self._generate_shirt(measurements, style_options)
        elif garment_type == "pants":
            return self._generate_pants(measurements, style_options)
        elif garment_type == "skirt":
            return self._generate_skirt(measurements, style_options)
        elif garment_type == "dress":
            return self._generate_dress(measurements, style_options)
        elif garment_type == "jacket":
            return self._generate_jacket(measurements, style_options)
        
        return {}
    
    def _generate_blouse(self, 
                         measurements: Dict[str, float],
                         style_options: Dict[str, Any]) -> Dict[str, Any]:
        """Genera patrón de blusa."""
        bust = measurements.get("bust", 90)
        waist = measurements.get("waist", 70)
        shoulder = measurements.get("shoulder", 40)
        back_length = measurements.get("back_length", 40)
        sleeve_length = measurements.get("sleeve_length", 58)
        
        ease = style_options.get("ease", 5)  # Holgura en cm
        
        # Calcular piezas del patrón
        pieces = [
            {
                "name": "front",
                "type": "body",
                "points": self._calculate_blouse_front(bust, waist, back_length, ease),
                "seam_allowance": 1.5
            },
            {
                "name": "back",
                "type": "body",
                "points": self._calculate_blouse_back(bust, waist, shoulder, back_length, ease),
                "seam_allowance": 1.5
            },
            {
                "name": "sleeve_left",
                "type": "sleeve",
                "points": self._calculate_sleeve(bust, sleeve_length, ease),
                "seam_allowance": 1.5
            },
            {
                "name": "sleeve_right",
                "type": "sleeve",
                "points": self._calculate_sleeve(bust, sleeve_length, ease),
                "seam_allowance": 1.5
            }
        ]
        
        return {
            "garment_type": "blouse",
            "measurements": measurements,
            "style_options": style_options,
            "pieces": pieces,
            "fabric_required": self._calculate_fabric_required(pieces)
        }
    
    def _generate_shirt(self, 
                        measurements: Dict[str, float],
                        style_options: Dict[str, Any]) -> Dict[str, Any]:
        """Genera patrón de camisa."""
        # Similar a blusa pero con estilo más estructurado
        return self._generate_blouse(measurements, style_options)
    
    def _generate_pants(self, 
                        measurements: Dict[str, float],
                        style_options: Dict[str, Any]) -> Dict[str, Any]:
        """Genera patrón de pantalón."""
        waist = measurements.get("waist", 75)
        hip = measurements.get("hip", 95)
        inseam = measurements.get("inseam", 75)
        outseam = measurements.get("outseam", 100)
        
        ease = style_options.get("ease", 3)
        
        pieces = [
            {
                "name": "front_left",
                "type": "leg",
                "points": self._calculate_pants_front(waist, hip, inseam, outseam, ease),
                "seam_allowance": 1.5
            },
            {
                "name": "front_right",
                "type": "leg",
                "points": self._calculate_pants_front(waist, hip, inseam, outseam, ease),
                "seam_allowance": 1.5
            },
            {
                "name": "back_left",
                "type": "leg",
                "points": self._calculate_pants_back(waist, hip, inseam, outseam, ease),
                "seam_allowance": 1.5
            },
            {
                "name": "back_right",
                "type": "leg",
                "points": self._calculate_pants_back(waist, hip, inseam, outseam, ease),
                "seam_allowance": 1.5
            }
        ]
        
        return {
            "garment_type": "pants",
            "measurements": measurements,
            "style_options": style_options,
            "pieces": pieces,
            "fabric_required": self._calculate_fabric_required(pieces)
        }
    
    def _generate_skirt(self, 
                        measurements: Dict[str, float],
                        style_options: Dict[str, Any]) -> Dict[str, Any]:
        """Genera patrón de falda."""
        waist = measurements.get("waist", 70)
        hip = measurements.get("hip", 95)
        length = measurements.get("skirt_length", 60)
        
        style = style_options.get("style", "straight")  # straight, a-line, circle
        
        if style == "circle":
            pieces = [
                {
                    "name": "circle_skirt",
                    "type": "circular",
                    "points": self._calculate_circle_skirt(waist, length),
                    "seam_allowance": 1.5
                }
            ]
        else:
            pieces = [
                {
                    "name": "front",
                    "type": "panel",
                    "points": self._calculate_skirt_panel(waist, hip, length, "front"),
                    "seam_allowance": 1.5
                },
                {
                    "name": "back",
                    "type": "panel",
                    "points": self._calculate_skirt_panel(waist, hip, length, "back"),
                    "seam_allowance": 1.5
                }
            ]
        
        return {
            "garment_type": "skirt",
            "measurements": measurements,
            "style_options": style_options,
            "pieces": pieces,
            "fabric_required": self._calculate_fabric_required(pieces)
        }
    
    def _generate_dress(self, 
                        measurements: Dict[str, float],
                        style_options: Dict[str, Any]) -> Dict[str, Any]:
        """Genera patrón de vestido."""
        # Combina elementos de blusa y falda
        bust = measurements.get("bust", 90)
        waist = measurements.get("waist", 70)
        hip = measurements.get("hip", 95)
        length = measurements.get("dress_length", 100)
        
        pieces = [
            {
                "name": "bodice_front",
                "type": "bodice",
                "points": self._calculate_dress_bodice(bust, waist, "front"),
                "seam_allowance": 1.5
            },
            {
                "name": "bodice_back",
                "type": "bodice",
                "points": self._calculate_dress_bodice(bust, waist, "back"),
                "seam_allowance": 1.5
            },
            {
                "name": "skirt_front",
                "type": "skirt",
                "points": self._calculate_dress_skirt(waist, hip, length, "front"),
                "seam_allowance": 1.5
            },
            {
                "name": "skirt_back",
                "type": "skirt",
                "points": self._calculate_dress_skirt(waist, hip, length, "back"),
                "seam_allowance": 1.5
            }
        ]
        
        return {
            "garment_type": "dress",
            "measurements": measurements,
            "style_options": style_options,
            "pieces": pieces,
            "fabric_required": self._calculate_fabric_required(pieces)
        }
    
    def _generate_jacket(self, 
                         measurements: Dict[str, float],
                         style_options: Dict[str, Any]) -> Dict[str, Any]:
        """Genera patrón de chaqueta."""
        # Similar a blusa pero con más estructura y holgura
        bust = measurements.get("bust", 90)
        measurements_with_ease = measurements.copy()
        measurements_with_ease["bust"] = bust + 10  # Más holgura para chaqueta
        
        return self._generate_blouse(measurements_with_ease, style_options)
    
    # Métodos auxiliares para calcular puntos de patrón
    
    def _calculate_blouse_front(self, bust: float, waist: float, 
                                length: float, ease: float) -> List[Tuple[float, float]]:
        """Calcula puntos del delantero de blusa."""
        width = (bust + ease) / 4
        return [
            (0, 0),
            (width, 0),
            (width + 2, length * 0.4),  # Sisa
            (width, length),
            ((waist + ease) / 4, length),
            (0, length),
            (0, length * 0.4),
            (0, 0)
        ]
    
    def _calculate_blouse_back(self, bust: float, waist: float, shoulder: float,
                               length: float, ease: float) -> List[Tuple[float, float]]:
        """Calcula puntos de la espalda de blusa."""
        width = (bust + ease) / 4
        return [
            (0, 0),
            (shoulder / 2, 0),
            (width, length * 0.4),
            (width, length),
            ((waist + ease) / 4, length),
            (0, length),
            (0, 0)
        ]
    
    def _calculate_sleeve(self, bust: float, length: float, 
                          ease: float) -> List[Tuple[float, float]]:
        """Calcula puntos de la manga."""
        cap_height = bust / 8
        width = bust / 6
        return [
            (0, cap_height),
            (width / 2, 0),
            (width, cap_height),
            (width - 5, length),
            (5, length),
            (0, cap_height)
        ]
    
    def _calculate_pants_front(self, waist: float, hip: float, inseam: float,
                               outseam: float, ease: float) -> List[Tuple[float, float]]:
        """Calcula puntos del delantero del pantalón."""
        return [
            (0, 0),
            ((waist + ease) / 4, 0),
            ((hip + ease) / 4, outseam * 0.25),
            ((hip + ease) / 4 - 2, inseam),
            (2, inseam),
            (0, outseam * 0.25),
            (0, 0)
        ]
    
    def _calculate_pants_back(self, waist: float, hip: float, inseam: float,
                              outseam: float, ease: float) -> List[Tuple[float, float]]:
        """Calcula puntos de la parte trasera del pantalón."""
        return [
            (0, 0),
            ((waist + ease) / 4 + 2, 0),
            ((hip + ease) / 4 + 2, outseam * 0.25),
            ((hip + ease) / 4, inseam),
            (0, inseam),
            (0, outseam * 0.25),
            (0, 0)
        ]
    
    def _calculate_circle_skirt(self, waist: float, 
                                length: float) -> List[Tuple[float, float]]:
        """Calcula puntos de falda circular."""
        radius = waist / (2 * math.pi)
        outer_radius = radius + length
        
        # Generar círculo con puntos
        points = []
        steps = 36
        for i in range(steps + 1):
            angle = (2 * math.pi * i) / steps
            x = outer_radius * math.cos(angle)
            y = outer_radius * math.sin(angle)
            points.append((x, y))
        
        return points
    
    def _calculate_skirt_panel(self, waist: float, hip: float, length: float,
                               panel_type: str) -> List[Tuple[float, float]]:
        """Calcula puntos de panel de falda."""
        waist_width = waist / 4
        hip_width = hip / 4
        
        return [
            (0, 0),
            (waist_width, 0),
            (hip_width, length * 0.3),
            (hip_width - 1, length),
            (1, length),
            (0, length * 0.3),
            (0, 0)
        ]
    
    def _calculate_dress_bodice(self, bust: float, waist: float,
                                panel_type: str) -> List[Tuple[float, float]]:
        """Calcula puntos del corpiño del vestido."""
        width = bust / 4
        waist_width = waist / 4
        length = 40
        
        return [
            (0, 0),
            (width, 0),
            (width, length * 0.5),
            (waist_width, length),
            (0, length),
            (0, 0)
        ]
    
    def _calculate_dress_skirt(self, waist: float, hip: float, length: float,
                               panel_type: str) -> List[Tuple[float, float]]:
        """Calcula puntos de la falda del vestido."""
        return self._calculate_skirt_panel(waist, hip, length, panel_type)
    
    def _calculate_fabric_required(self, pieces: List[Dict[str, Any]]) -> Dict[str, float]:
        """Calcula la cantidad de tela requerida."""
        total_area = 0
        for piece in pieces:
            points = piece.get("points", [])
            if len(points) > 2:
                # Calcular área aproximada usando el método del trapecio
                area = self._calculate_polygon_area(points)
                total_area += area
        
        # Agregar margen para costuras y desperdicio (20%)
        total_area *= 1.2
        
        # Calcular metros lineales asumiendo ancho estándar de tela de 150cm
        fabric_width = 150
        linear_meters = total_area / fabric_width
        
        return {
            "total_area_cm2": total_area,
            "linear_meters": linear_meters,
            "fabric_width_cm": fabric_width
        }
    
    def _calculate_polygon_area(self, points: List[Tuple[float, float]]) -> float:
        """Calcula el área de un polígono usando la fórmula del trapecio."""
        if len(points) < 3:
            return 0
        
        area = 0
        for i in range(len(points)):
            j = (i + 1) % len(points)
            area += points[i][0] * points[j][1]
            area -= points[j][0] * points[i][1]
        
        return abs(area) / 2
    
    def export(self, pattern: Dict[str, Any], filepath: str, format: str = "svg") -> None:
        """
        Exporta el patrón a un archivo.
        
        Args:
            pattern: Patrón a exportar
            filepath: Ruta del archivo
            format: Formato (svg, pdf, dxf)
        """
        if format == "svg":
            self._export_svg(pattern, filepath)
        elif format == "pdf":
            self._export_pdf(pattern, filepath)
        elif format == "dxf":
            self._export_dxf(pattern, filepath)
        else:
            raise ValueError(f"Formato no soportado: {format}")
    
    def _export_svg(self, pattern: Dict[str, Any], filepath: str) -> None:
        """Exporta patrón a SVG."""
        pieces = pattern.get("pieces", [])
        
        # Crear SVG básico
        svg_content = ['<?xml version="1.0" encoding="UTF-8"?>']
        svg_content.append('<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="1400">')
        
        offset_x = 50
        offset_y = 50
        
        for i, piece in enumerate(pieces):
            points = piece.get("points", [])
            if not points:
                continue
            
            # Convertir puntos a string SVG
            points_str = " ".join([f"{x + offset_x},{y + offset_y}" for x, y in points])
            
            svg_content.append(f'  <polygon points="{points_str}" ')
            svg_content.append(f'    fill="none" stroke="black" stroke-width="1"/>')
            svg_content.append(f'  <text x="{offset_x}" y="{offset_y - 10}" ')
            svg_content.append(f'    font-family="Arial" font-size="12">{piece["name"]}</text>')
            
            # Ajustar offset para la siguiente pieza
            offset_x += 200
            if offset_x > 800:
                offset_x = 50
                offset_y += 300
        
        svg_content.append('</svg>')
        
        with open(filepath, 'w') as f:
            f.write('\n'.join(svg_content))
    
    def _export_pdf(self, pattern: Dict[str, Any], filepath: str) -> None:
        """Exporta patrón a PDF."""
        # Implementación básica - en producción usar reportlab
        raise NotImplementedError("Exportación PDF requiere dependencia adicional: reportlab")
    
    def _export_dxf(self, pattern: Dict[str, Any], filepath: str) -> None:
        """Exporta patrón a DXF."""
        # Implementación básica - en producción usar ezdxf
        raise NotImplementedError("Exportación DXF requiere dependencia adicional: ezdxf")
