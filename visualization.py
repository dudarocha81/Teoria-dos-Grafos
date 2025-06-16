import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from typing import Dict, Tuple, List
import math

class GraphVisualizer:
    def __init__(self, vertices: Dict[str, Tuple[int, int]]):
        self.vertices = vertices
        self.fig, self.ax = plt.subplots(figsize=(16, 12))
        self.colors = self._define_colors()


    def _define_colors(self) -> Dict[str, str]:
        """Define cores para diferentes tipos de elementos"""
        return {
            'PONTO INICIAL': '#FF0000',  # Vermelho
            'LAB': '#0066CC',           # Azul
            'MESA': '#FF9900',          # Laranja
            'SALA': '#00CC66',          # Verde
            'BANHEIRO': '#9900CC',      # Roxo
            'CORREDOR': '#666666',      # Cinza
            'ESCADA': '#CC6600',        # Marrom
            'ELEVAS': '#FF6699',        # Rosa
            'AREA': '#CCCC00',          # Amarelo
            'DEFAULT': '#000000'        # Preto
        }
    

    def _get_node_color(self, node_name: str) -> str:
        """Determina a cor do nó baseado no seu nome"""
        name_upper = node_name.upper()

        if 'PONTO INICIAL' in name_upper:
            return self.colors['PONTO INICIAL']
        elif 'LAB' in name_upper:
            return self.colors['LAB']
        elif 'MESA' in name_upper:
            return self.colors['MESA']
        elif 'SALA' in name_upper:
            return self.colors['SALA']
        elif any(keyword in name_upper for keyword in ['B. F', 'B. M', 'B. C']):
            return self.colors['BANHEIRO']
        elif 'CORREDOR' in name_upper:
            return self.colors['CORREDOR']
        elif 'ESCADA' in name_upper:
            return self.colors['ESCADA']
        elif 'ELEVAS' in name_upper:
            return self.colors['ELEVAS']
        elif any(keyword in name_upper for keyword in ['A1', 'A2']):
            return self.colors['AREA']
        else:
            return self.colors['DEFAULT']
        

    def _get_node_size(self, node_name: str) -> int:
        """Determina o tamanho do nó baseado no seu tipo"""
        if 'PONTO INICIAL' in node_name.upper():
            return 200  # Maior para destaque
        elif any(keyword in node_name.upper() for keyword in ['MESA', 'LAB', 'SALA']):
            return 100
        else:
            return 80
        

    def plot_vertices(self, show_labels: bool = True, label_fontsize: int = 8):
        """Plota todos os vértices do grafo"""
        for name, (x, y) in self.vertices.items():
            color = self._get_node_color(name)
            size = self._get_node_size(name)
            
            # Plota o ponto
            self.ax.scatter(x, y, c=color, s=size, alpha=0.8, edgecolors='black', linewidth=1)
            
            # Adiciona label se solicitado
            if show_labels:
                # Abrevia o nome para melhor visualização
                short_name = self._abbreviate_name(name)
                self.ax.annotate(short_name, (x, y), xytext=(5, 5), 
                               textcoords='offset points', fontsize=label_fontsize,
                               bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7))
                

    def _abbreviate_name(self, name: str) -> str:
        """Abrevia nomes longos para melhorar a visualização"""
        if 'PONTO INICIAL' in name:
            return 'I'
        elif 'LAB 01' in name:
            return name.replace('LAB 01 - ', 'L1-')
        elif 'LAB 02' in name:
            return name.replace('LAB 02', 'L2')
        elif 'MESA 01' in name:
            return name.replace('MESA 01 - ', 'M1-')
        elif 'MESA 02' in name:
            return name.replace('MESA 02 - ', 'M2-')
        elif 'SALA 01' in name:
            return name.replace('SALA 01 - ', 'S1-')
        elif 'SALA 02' in name:
            return name.replace('SALA 02 - ', 'S2-')
        elif 'ESCADA 1' in name:
            return name.replace('ESCADA 1 - ', 'E1-')
        elif 'ESCADA 2' in name:
            return name.replace('ESCADA 2 - ', 'E2-')
        elif 'ELEVAS' in name:
            return name.replace('ELEVAS - ', 'EL-')
        elif 'CORREDOR' in name:
            return name.replace('CORREDOR - ', 'C-')
        else:
            return name[:10] + '...' if len(name) > 10 else name
        

    def plot_edges(self, max_distance: float = None, edge_alpha: float = 0.3):
        """Plota as arestas (conexões) entre os vértices"""
        if max_distance is None:
            # Calcula uma distância máxima razoável baseada nos dados
            distances = []
            for name1, coord1 in self.vertices.items():
                for name2, coord2 in self.vertices.items():
                    if name1 != name2:
                        dist = math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)
                        distances.append(dist)
            max_distance = np.percentile(distances, 25)  # Conecta apenas os 25% mais próximos
        
        for name1, coord1 in self.vertices.items():
            for name2, coord2 in self.vertices.items():
                if name1 != name2:
                    dist = math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)
                    if dist <= max_distance:
                        self.ax.plot([coord1[0], coord2[0]], [coord1[1], coord2[1]], 
                                   'k-', alpha=edge_alpha, linewidth=0.5)