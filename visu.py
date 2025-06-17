import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from main import vertices, arestas, a_estrela, distancias

# Configurar matplotlib para evitar warnings de fonte
import matplotlib
matplotlib.rcParams['font.family'] = 'DejaVu Sans'

def obter_cor_vertice(nome):
    """Retorna a cor do vértice baseada na categoria"""
    nome_upper = nome.upper()
    
    if 'PONTO INICIAL' in nome_upper:
        return '#FF0000'  # Vermelho
    elif 'PONTO FINAL' in nome_upper:
        return '#FF0000'  # Vermelho
    elif 'LAB' in nome_upper:
        return '#0066CC'  # Azul
    elif 'MESA' in nome_upper:
        return '#FF9900'  # Laranja
    elif 'SALA' in nome_upper:
        return '#00CC66'  # Verde
    elif any(keyword in nome_upper for keyword in ['B. F', 'B. M', 'B. C']):
        return '#9900CC'  # Roxo
    elif 'CORREDOR' in nome_upper:
        return '#666666'  # Cinza
    elif 'ESCADA' in nome_upper:
        return '#CC6600'  # Marrom
    elif 'ELEVAS' in nome_upper:
        return '#FF6699'  # Rosa
    elif any(keyword in nome_upper for keyword in ['A1', 'A2']):
        return '#CCCC00'  # Amarelo
    else:
        return '#000000'  # Preto

def obter_cor_texto(cor_fundo):
    """Retorna cor do texto (branco ou preto) baseado na cor de fundo para melhor contraste"""
    # Converter hex para RGB
    if cor_fundo.startswith('#'):
        hex_color = cor_fundo[1:]
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        
        # Calcular luminância
        luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
        
        # Retornar branco para cores escuras, preto para claras
        return 'white' if luminance < 0.5 else 'black'
    return 'white'

def criar_label_melhorado(nome):
    """Cria label otimizado para melhor visualização"""
    if 'PONTO INICIAL' in nome:
        return 'INÍCIO'
    elif 'PONTO FINAL' in nome:
        return 'FIM'
    elif nome.startswith('LAB'):
        # LAB 01 - 1 → L1.1
        parts = nome.replace('LAB ', '').replace(' - ', '.')
        return f"L{parts}"
    elif nome.startswith('MESA'):
        # MESA 01 - C1 - 1 → M1.C1.1
        parts = nome.replace('MESA ', '').replace(' - ', '.')
        return f"M{parts}"
    elif nome.startswith('SALA'):
        # SALA 01 - 1 → S1.1
        parts = nome.replace('SALA ', '').replace(' - ', '.')
        return f"S{parts}"
    elif nome.startswith('ESCADA'):
        # ESCADA 1 - 1 → E1.1
        parts = nome.replace('ESCADA ', '').replace(' - ', '.')
        return f"E{parts}"
    elif nome.startswith('ELEVAS'):
        # ELEVAS - 1 → EL1
        parts = nome.replace('ELEVAS - ', '')
        return f"EL{parts}"
    elif nome.startswith('CORREDOR'):
        # CORREDOR - 1 → C1
        parts = nome.replace('CORREDOR - ', '')
        return f"C{parts}"
    elif nome.startswith('A1') or nome.startswith('A2'):
        # A1 - 1 → A1.1
        return nome.replace(' - ', '.')
    elif nome.startswith('B.'):
        return nome  # B.F, B.M, B.C já são curtos
    else:
        return nome[:6] + '...' if len(nome) > 6 else nome

def calcular_distancia_total_caminho(caminho):
    """Calcula a distância total do caminho A*"""
    if not caminho or len(caminho) < 2:
        return 0
    
    distancia_total = 0
    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]
        if origem in distancias and destino in distancias[origem]:
            distancia_total += distancias[origem][destino]
    
    return distancia_total

def gerar_visualizacao(G, pos, cores_vertices, caminho=None, distancia_total=0, 
                      mostrar_caminho=True, nome_arquivo="grafo.png", 
                      titulo_base="Mapa Interior", mostrar_grafico=True):
    """
    Gera visualização do grafo com ou sem caminho destacado
    
    Args:
        G: Grafo NetworkX
        pos: Posições dos vértices
        cores_vertices: Lista de cores dos vértices
        caminho: Lista do caminho A* (opcional)
        distancia_total: Distância total do caminho
        mostrar_caminho: Se deve destacar o caminho A*
        nome_arquivo: Nome do arquivo de saída
        titulo_base: Título base do gráfico
        mostrar_grafico: Se deve exibir o gráfico na tela
    """
    
    # Configurar figura
    fig, ax = plt.subplots(figsize=(22, 18))
    
    # Desenhar arestas com melhor visibilidade
    nx.draw_networkx_edges(G, pos, 
                          edge_color='#555555', 
                          width=1.2, 
                          alpha=0.7,
                          ax=ax)
    
    # Destacar caminho A* se solicitado e caminho existir
    caminho_edges = []
    if mostrar_caminho and caminho:
        print(f"Destacando caminho: {len(caminho)} passos")
        
        # Criar lista de arestas do caminho
        for i in range(len(caminho) - 1):
            caminho_edges.append((caminho[i], caminho[i + 1]))
        
        # Desenhar caminho destacado
        nx.draw_networkx_edges(G, pos,
                              edgelist=caminho_edges,
                              edge_color='#FF0000',
                              width=5,
                              alpha=0.95,
                              style='solid',
                              ax=ax)
    
    # Desenhar vértices com tamanhos otimizados
    node_sizes = []
    for vertice in G.nodes():
        # Nós importantes (início/fim) são maiores
        if 'PONTO' in vertice.upper():
            node_sizes.append(1000)
        else:
            node_sizes.append(800)
    
    nx.draw_networkx_nodes(G, pos, 
                          node_color=cores_vertices, 
                          node_size=node_sizes, 
                          alpha=0.9,
                          edgecolors='black',
                          linewidths=2,
                          ax=ax)
    
    # Adicionar labels com cores adaptativas
    labels = {vertice: criar_label_melhorado(vertice) for vertice in G.nodes()}
    
    # Desenhar labels com cores adaptativas
    for vertice, label in labels.items():
        cor_fundo = obter_cor_vertice(vertice)
        cor_texto = obter_cor_texto(cor_fundo)
        
        x, y = pos[vertice]
        
        # Font size baseado no tipo de nó
        font_size = 10 if 'PONTO' in vertice.upper() else 8
        
        ax.text(x, y, label, 
               fontsize=font_size, 
               fontweight='bold',
               color=cor_texto,
               ha='center', 
               va='center',
               bbox=dict(boxstyle="round,pad=0.1", facecolor=cor_fundo, alpha=0.1, edgecolor='none'))
    
    # Configurar layout otimizado
    ax.set_xlim(-3, 27)
    ax.set_ylim(-3, 40)
    ax.invert_yaxis()
    ax.set_aspect('equal', adjustable='box')
    
    # Criar legenda
    legend_elements = [
        mpatches.Patch(color='#FF0000', label='Pontos Inicial/Final'),
        mpatches.Patch(color='#0066CC', label='Laboratórios'),
        mpatches.Patch(color='#FF9900', label='Mesas'),
        mpatches.Patch(color='#00CC66', label='Salas'),
        mpatches.Patch(color='#9900CC', label='Banheiros'),
        mpatches.Patch(color='#666666', label='Corredores'),
        mpatches.Patch(color='#CC6600', label='Escadas'),
        mpatches.Patch(color='#FF6699', label='Elevadores'),
        mpatches.Patch(color='#CCCC00', label='Armários'),
    ]
    
    # Adicionar informações do caminho na legenda apenas se mostrar caminho
    if mostrar_caminho and caminho:
        legend_elements.append(mpatches.Patch(color='red', label=f'Caminho A* ({len(caminho)} passos)'))
        legend_elements.append(mpatches.Patch(color='white', label=f'Distância: {distancia_total:.1f} unidades'))
    
    # Posicionar legenda
    plt.legend(handles=legend_elements, 
              loc='upper left', 
              bbox_to_anchor=(1.01, 1),
              title="Legenda",
              title_fontsize=14,
              fontsize=11,
              frameon=True,
              fancybox=True,
              shadow=True)
    
    # Configurar título
    if mostrar_caminho and caminho:
        titulo = f"{titulo_base} - Navegação com A*"
        titulo += f"\nRota Otimizada: {len(caminho)} passos • {distancia_total:.1f} unidades"
    else:
        titulo = f"{titulo_base} - Estrutura Completa"
        titulo += f"\nTodos os Vértices e Conexões"
    
    plt.suptitle(titulo, fontsize=18, fontweight='bold', y=0.95)
    
    # Configurações visuais finais
    ax.grid(True, linestyle=':', alpha=0.3, color='gray')
    ax.axis('off')
    
    # Adicionar informações no canto
    info_text = f"Vértices: {len(G.nodes())} | Arestas: {len(G.edges())}"
    if mostrar_caminho and caminho:
        info_text += f" | Eficiência: {(distancia_total/len(caminho)):.1f}u/passo"
    else:
        info_text += " | Visualização Completa"
    
    ax.text(0.02, 0.02, info_text, transform=ax.transAxes, 
            fontsize=10, alpha=0.7,
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
    
    plt.tight_layout(rect=[0, 0, 0.83, 0.93])
    
    # Salvar imagem
    print(f"Salvando {nome_arquivo}...")
    fig.savefig(nome_arquivo, 
               dpi=400,
               bbox_inches='tight',
               facecolor='white',
               edgecolor='none',
               format='png')
    print(f"Imagem salva: {nome_arquivo}")
    
    # Mostrar gráfico se solicitado
    if mostrar_grafico:
        # Maximizar janela
        try:
            mng = plt.get_current_fig_manager()
            try:
                mng.window.state('zoomed')  # TkAgg
            except Exception:
                try:
                    mng.window.showMaximized()  # Qt5Agg/Qt6Agg
                except Exception:
                    try:
                        mng.window.wm_state('zoomed')  # Windows
                    except Exception:
                        print("Não foi possível maximizar a janela automaticamente")
        except Exception:
            print("Maximização da janela não suportada neste backend")
        
        print(f"Exibindo {nome_arquivo}...")
        plt.show()
    else:
        plt.close(fig)  # Fechar figura para liberar memória

# ========================= SCRIPT PRINCIPAL =========================

print("=" * 60)
print("          GERADOR DE VISUALIZAÇÕES DO GRAFO")
print("=" * 60)

# Criar o grafo NetworkX
print("\n1. Criando grafo...")
G = nx.Graph()

# Adicionar vértices com posições
for vertice, coord in vertices.items():
    G.add_node(vertice, pos=coord)

# Adicionar arestas
for origem, vizinhos in arestas.items():
    for destino in vizinhos:
        if origem in vertices and destino in vertices:
            G.add_edge(origem, destino)

print(f"   Grafo criado: {len(G.nodes())} vértices, {len(G.edges())} arestas")

# Obter posições e cores
pos = nx.get_node_attributes(G, 'pos')
cores_vertices = [obter_cor_vertice(vertice) for vertice in G.nodes()]

# Executar A* para encontrar caminho
print("\n2. Executando algoritmo A*...")
caminho = a_estrela("PONTO INICIAL - I", "PONTO FINAL - J")

# Calcular estatísticas do caminho
distancia_total = 0
if caminho:
    distancia_total = calcular_distancia_total_caminho(caminho)
    print(f"   Caminho encontrado: {len(caminho)} passos")
    print("   Caminho A*:")
    for i, passo in enumerate(caminho, 1):
        nome_curto = passo.split(' - ')[0] if ' - ' in passo else passo
        print(f"      {i:2d}. {nome_curto}")
    print(f"   Distância total: {distancia_total:.2f} unidades")
else:
    print("   Nenhum caminho encontrado")

# Gerar visualizações
print("\n3. Gerando visualizações...")

# Visualização 1: Grafo completo (sem caminho destacado)
print("\n   → Gerando visualização completa...")
gerar_visualizacao(
    G=G, 
    pos=pos, 
    cores_vertices=cores_vertices,
    caminho=caminho,
    distancia_total=distancia_total,
    mostrar_caminho=False,  # Não destacar caminho
    nome_arquivo="grafo_completo.png",
    titulo_base="Mapa Interior",
    mostrar_grafico=False  # Não exibir na tela ainda | SE QUISER EXIBIR, MUDAR PARA "True"
)

# Visualização 2: Grafo com caminho A* destacado
print("\n   → Gerando visualização com caminho A*...")
gerar_visualizacao(
    G=G, 
    pos=pos, 
    cores_vertices=cores_vertices,
    caminho=caminho,
    distancia_total=distancia_total,
    mostrar_caminho=True,  # Destacar caminho
    nome_arquivo="grafo_com_caminho_destacado.png",
    titulo_base="Mapa Interior",
    mostrar_grafico=True  # Exibir na tela
)

# Estatísticas finais
print("\n" + "=" * 60)
print("                   RELATÓRIO FINAL")
print("=" * 60)
print(f"✓ Total de vértices: {len(G.nodes())}")
print(f"✓ Total de arestas: {len(G.edges())}")
if caminho:
    print(f"✓ Passos no caminho: {len(caminho)}")
    print(f"✓ Distância total: {distancia_total:.2f} unidades")
    print(f"✓ Eficiência: {(distancia_total/len(caminho)):.2f} unidades/passo")

print(f"\n📁 Arquivos gerados:")
print(f"   • grafo_completo.png - Estrutura completa do grafo")
print(f"   • grafo_com_caminho_destacado.png - Caminho A* destacado")

print("\n🎉 Visualizações concluídas com sucesso!")
print("=" * 60)