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
            "blouse", "shirt", "pants", "skirt", "dress", "jacket", "sock", "boxer"
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
        elif garment_type == "sock":
            return self._generate_sock(measurements, style_options)
        elif garment_type == "boxer":
            return self._generate_boxer(measurements, style_options)
        
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
    
    def _generate_sock(self, 
                       measurements: Dict[str, float],
                       style_options: Dict[str, Any]) -> Dict[str, Any]:
        """Genera patrón de calcetín."""
        foot_length = measurements.get("foot_length", 25)
        foot_width = measurements.get("foot_width", 10)
        ankle_circumference = measurements.get("ankle_circumference", 22)
        calf_circumference = measurements.get("calf_circumference", 35)
        sock_height = measurements.get("sock_height", 20)
        
        style = style_options.get("style", "ankle")  # ankle, crew, knee-high
        
        # Ajustar altura según estilo
        if style == "ankle":
            sock_height = min(sock_height, 10)
        elif style == "crew":
            sock_height = min(sock_height, 20)
        elif style == "knee-high":
            sock_height = max(sock_height, 35)
        
        ease = style_options.get("ease", 1)  # Elasticidad del calcetín
        
        # Opciones de personalización de colores
        colors = style_options.get("colors", {})
        body_color = colors.get("body", "#87CEEB")  # Azul cielo por defecto
        heel_color = colors.get("heel", "#FFB6C1")  # Rosa claro por defecto
        toe_color = colors.get("toe", "#98FB98")    # Verde claro por defecto
        
        pieces = [
            {
                "name": "sock_body",
                "type": "tubular",
                "points": self._calculate_sock_body(
                    foot_length, foot_width, ankle_circumference, 
                    calf_circumference, sock_height, ease
                ),
                "seam_allowance": 0.5,
                "color": body_color
            },
            {
                "name": "heel",
                "type": "heel_patch",
                "points": self._calculate_sock_heel(foot_length, foot_width, ease),
                "seam_allowance": 0.5,
                "color": heel_color
            },
            {
                "name": "toe",
                "type": "toe_cap",
                "points": self._calculate_sock_toe(foot_width, ease),
                "seam_allowance": 0.5,
                "color": toe_color
            }
        ]
        
        return {
            "garment_type": "sock",
            "measurements": measurements,
            "style_options": style_options,
            "pieces": pieces,
            "fabric_required": self._calculate_fabric_required(pieces)
        }
    
    def _generate_boxer(self, 
                        measurements: Dict[str, float],
                        style_options: Dict[str, Any]) -> Dict[str, Any]:
        """Genera patrón de boxer."""
        waist = measurements.get("waist", 75)
        hip = measurements.get("hip", 95)
        inseam = measurements.get("inseam", 10)  # Entrepierna corta para boxer
        thigh = measurements.get("thigh_circumference", 55)
        rise = measurements.get("rise", 25)  # Altura del tiro
        
        ease = style_options.get("ease", 5)  # Holgura cómoda
        leg_opening = style_options.get("leg_opening", "loose")  # loose, fitted
        
        # Ajustar medida de entrepierna para boxer (más corta que pantalones)
        boxer_inseam = min(inseam, 15)
        
        # Opciones de personalización de colores
        colors = style_options.get("colors", {})
        front_color = colors.get("front", "#FFE4B5")    # Beige claro por defecto
        back_color = colors.get("back", "#F0E68C")      # Amarillo claro por defecto
        waistband_color = colors.get("waistband", "#DDA0DD")  # Ciruela por defecto
        
        pieces = [
            {
                "name": "front",
                "type": "front_panel",
                "points": self._calculate_boxer_front(
                    waist, hip, thigh, boxer_inseam, rise, ease
                ),
                "seam_allowance": 1.0,
                "color": front_color
            },
            {
                "name": "back",
                "type": "back_panel",
                "points": self._calculate_boxer_back(
                    waist, hip, thigh, boxer_inseam, rise, ease
                ),
                "seam_allowance": 1.0,
                "color": back_color
            },
            {
                "name": "waistband",
                "type": "band",
                "points": self._calculate_boxer_waistband(waist, ease),
                "seam_allowance": 0.5,
                "color": waistband_color
            }
        ]
        
        return {
            "garment_type": "boxer",
            "measurements": measurements,
            "style_options": style_options,
            "pieces": pieces,
            "fabric_required": self._calculate_fabric_required(pieces)
        }
    
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
    
    def _calculate_sock_body(self, foot_length: float, foot_width: float,
                             ankle_circ: float, calf_circ: float,
                             height: float, ease: float) -> List[Tuple[float, float]]:
        """Calcula puntos del cuerpo del calcetín (patrón plano para tejido tubular)."""
        # El patrón de calcetín se crea como rectángulo que se enrolla
        ankle_width = (ankle_circ + ease) / 2
        calf_width = (calf_circ + ease) / 2
        foot_flat_width = (foot_width * 2 + ease) / 2
        
        return [
            (0, 0),
            (ankle_width, 0),
            (calf_width, height * 0.3),
            (calf_width, height),
            (0, height),
            (0, height * 0.3),
            (0, 0)
        ]
    
    def _calculate_sock_heel(self, foot_length: float, foot_width: float,
                             ease: float) -> List[Tuple[float, float]]:
        """Calcula puntos del refuerzo del talón."""
        heel_width = foot_width + ease
        heel_height = foot_length * 0.25
        
        return [
            (0, 0),
            (heel_width, 0),
            (heel_width, heel_height),
            (heel_width * 0.5, heel_height * 1.2),
            (0, heel_height),
            (0, 0)
        ]
    
    def _calculate_sock_toe(self, foot_width: float, ease: float) -> List[Tuple[float, float]]:
        """Calcula puntos del refuerzo de la punta."""
        toe_width = foot_width + ease
        toe_height = foot_width * 0.8
        
        return [
            (0, 0),
            (toe_width, 0),
            (toe_width, toe_height),
            (toe_width * 0.5, toe_height * 1.1),
            (0, toe_height),
            (0, 0)
        ]
    
    def _calculate_boxer_front(self, waist: float, hip: float, thigh: float,
                               inseam: float, rise: float, ease: float) -> List[Tuple[float, float]]:
        """Calcula puntos del delantero del boxer."""
        waist_width = (waist + ease) / 4
        hip_width = (hip + ease) / 4
        thigh_width = (thigh + ease) / 4
        
        return [
            (0, 0),
            (waist_width, 0),
            (hip_width, rise * 0.5),
            (thigh_width, rise),
            (thigh_width - 1, rise + inseam),
            (1, rise + inseam),
            (0, rise),
            (0, 0)
        ]
    
    def _calculate_boxer_back(self, waist: float, hip: float, thigh: float,
                              inseam: float, rise: float, ease: float) -> List[Tuple[float, float]]:
        """Calcula puntos de la parte trasera del boxer."""
        waist_width = (waist + ease) / 4 + 2
        hip_width = (hip + ease) / 4 + 2
        thigh_width = (thigh + ease) / 4
        
        return [
            (0, 0),
            (waist_width, 0),
            (hip_width, rise * 0.5),
            (thigh_width, rise),
            (thigh_width - 1, rise + inseam),
            (1, rise + inseam),
            (0, rise),
            (0, 0)
        ]
    
    def _calculate_boxer_waistband(self, waist: float, ease: float) -> List[Tuple[float, float]]:
        """Calcula puntos de la pretina del boxer."""
        band_length = waist + ease
        band_width = 4  # Ancho estándar de pretina elástica
        
        return [
            (0, 0),
            (band_length, 0),
            (band_length, band_width),
            (0, band_width),
            (0, 0)
        ]
    
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
    
    def export(self, pattern: Dict[str, Any], filepath: str, format: str = "svg", 
               export_options: Optional[Dict[str, Any]] = None) -> None:
        """
        Exporta el patrón a un archivo.
        
        Args:
            pattern: Patrón a exportar
            filepath: Ruta del archivo
            format: Formato (svg, pdf, dxf)
            export_options: Opciones de personalización de exportación
        """
        if format == "svg":
            self._export_svg(pattern, filepath, export_options)
        elif format == "pdf":
            self._export_pdf(pattern, filepath)
        elif format == "dxf":
            self._export_dxf(pattern, filepath)
        else:
            raise ValueError(f"Formato no soportado: {format}")
    
    def _export_svg(self, pattern: Dict[str, Any], filepath: str, export_options: Optional[Dict[str, Any]] = None) -> None:
        """Exporta patrón a SVG con opciones de personalización."""
        pieces = pattern.get("pieces", [])
        export_options = export_options or {}
        
        # Opciones de personalización de cuadros de datos
        show_data_box = export_options.get("show_data_box", True)
        data_box_position = export_options.get("data_box_position", "top-right")  # top-right, top-left, bottom-right, bottom-left
        show_measurements = export_options.get("show_measurements", True)
        show_fabric_info = export_options.get("show_fabric_info", True)
        
        # Opciones de colores y estilos
        stroke_color = export_options.get("stroke_color", "black")
        stroke_width = export_options.get("stroke_width", 1)
        text_color = export_options.get("text_color", "black")
        font_family = export_options.get("font_family", "Arial")
        font_size = export_options.get("font_size", 12)
        
        # Crear SVG básico
        svg_content = ['<?xml version="1.0" encoding="UTF-8"?>']
        svg_content.append('<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="1400">')
        
        # Añadir título del patrón
        garment_type = pattern.get("garment_type", "patrón")
        svg_content.append(f'  <text x="500" y="30" text-anchor="middle" ')
        svg_content.append(f'    font-family="{font_family}" font-size="{font_size + 6}" font-weight="bold" fill="{text_color}">')
        svg_content.append(f'    Patrón de {garment_type}</text>')
        
        offset_x = 50
        offset_y = 80
        
        for i, piece in enumerate(pieces):
            points = piece.get("points", [])
            if not points:
                continue
            
            # Obtener color de la pieza (si existe)
            piece_color = piece.get("color", "#FFFFFF")
            
            # Convertir puntos a string SVG
            points_str = " ".join([f"{x + offset_x},{y + offset_y}" for x, y in points])
            
            # Dibujar polígono con color de relleno personalizado
            svg_content.append(f'  <polygon points="{points_str}" ')
            svg_content.append(f'    fill="{piece_color}" fill-opacity="0.3" stroke="{stroke_color}" stroke-width="{stroke_width}"/>')
            
            # Etiqueta de la pieza
            svg_content.append(f'  <text x="{offset_x}" y="{offset_y - 10}" ')
            svg_content.append(f'    font-family="{font_family}" font-size="{font_size}" fill="{text_color}">')
            svg_content.append(f'    {piece["name"]} ({piece["type"]})</text>')
            
            # Margen de costura
            seam = piece.get("seam_allowance", 0)
            svg_content.append(f'  <text x="{offset_x}" y="{offset_y - 25}" ')
            svg_content.append(f'    font-family="{font_family}" font-size="{font_size - 2}" fill="{text_color}" opacity="0.7">')
            svg_content.append(f'    Margen: {seam} cm</text>')
            
            # Ajustar offset para la siguiente pieza
            offset_x += 200
            if offset_x > 800:
                offset_x = 50
                offset_y += 300
        
        # Añadir cuadro de datos si está habilitado
        if show_data_box:
            self._add_data_box(svg_content, pattern, data_box_position, 
                              show_measurements, show_fabric_info, 
                              font_family, font_size, text_color)
        
        svg_content.append('</svg>')
        
        with open(filepath, 'w') as f:
            f.write('\n'.join(svg_content))
    
    def _add_data_box(self, svg_content: List[str], pattern: Dict[str, Any], 
                      position: str, show_measurements: bool, show_fabric_info: bool,
                      font_family: str, font_size: int, text_color: str) -> None:
        """Añade cuadro de datos con información del patrón."""
        # Determinar posición del cuadro
        if position == "top-right":
            box_x, box_y = 700, 80
        elif position == "top-left":
            box_x, box_y = 20, 80
        elif position == "bottom-right":
            box_x, box_y = 700, 1200
        else:  # bottom-left
            box_x, box_y = 20, 1200
        
        # Dibujar fondo del cuadro
        svg_content.append(f'  <rect x="{box_x}" y="{box_y}" width="260" height="180" ')
        svg_content.append(f'    fill="white" stroke="{text_color}" stroke-width="1" opacity="0.9"/>')
        
        y_offset = box_y + 20
        
        # Título del cuadro
        svg_content.append(f'  <text x="{box_x + 10}" y="{y_offset}" ')
        svg_content.append(f'    font-family="{font_family}" font-size="{font_size}" font-weight="bold" fill="{text_color}">')
        svg_content.append(f'    Información del Patrón</text>')
        y_offset += 20
        
        # Información de medidas
        if show_measurements:
            measurements = pattern.get("measurements", {})
            svg_content.append(f'  <text x="{box_x + 10}" y="{y_offset}" ')
            svg_content.append(f'    font-family="{font_family}" font-size="{font_size - 2}" fill="{text_color}">')
            svg_content.append(f'    Medidas (cm):</text>')
            y_offset += 15
            
            for key, value in list(measurements.items())[:4]:  # Mostrar solo 4 medidas principales
                svg_content.append(f'  <text x="{box_x + 15}" y="{y_offset}" ')
                svg_content.append(f'    font-family="{font_family}" font-size="{font_size - 3}" fill="{text_color}">')
                svg_content.append(f'    • {key}: {value}</text>')
                y_offset += 12
        
        # Información de tela
        if show_fabric_info:
            fabric = pattern.get("fabric_required", {})
            y_offset += 10
            svg_content.append(f'  <text x="{box_x + 10}" y="{y_offset}" ')
            svg_content.append(f'    font-family="{font_family}" font-size="{font_size - 2}" fill="{text_color}">')
            svg_content.append(f'    Tela requerida:</text>')
            y_offset += 15
            
            linear_m = fabric.get("linear_meters", 0)
            width = fabric.get("fabric_width_cm", 150)
            svg_content.append(f'  <text x="{box_x + 15}" y="{y_offset}" ')
            svg_content.append(f'    font-family="{font_family}" font-size="{font_size - 3}" fill="{text_color}">')
            svg_content.append(f'    • {linear_m:.2f} metros lineales</text>')
            y_offset += 12
            
            svg_content.append(f'  <text x="{box_x + 15}" y="{y_offset}" ')
            svg_content.append(f'    font-family="{font_family}" font-size="{font_size - 3}" fill="{text_color}">')
            svg_content.append(f'    • Ancho: {width} cm</text>')
    
    def _export_pdf(self, pattern: Dict[str, Any], filepath: str) -> None:
        """Exporta patrón a PDF."""
        # Implementación básica - en producción usar reportlab
        raise NotImplementedError("Exportación PDF requiere dependencia adicional: reportlab")
    
    def _export_dxf(self, pattern: Dict[str, Any], filepath: str) -> None:
        """Exporta patrón a DXF."""
        # Implementación básica - en producción usar ezdxf
        raise NotImplementedError("Exportación DXF requiere dependencia adicional: ezdxf")
