# Navegação Interior com Algoritmo A*

Este projeto implementa um sistema de navegação interior utilizando o algoritmo A* para encontrar o caminho mais eficiente entre dois pontos em um mapa de ambiente interno.

## 📋 Descrição

O sistema mapeia um ambiente interior (laboratórios, salas, corredores, etc.) e utiliza o algoritmo A* para calcular a rota otimizada entre um ponto inicial e final, considerando as distâncias euclidianas entre os pontos conectados.

## 🏗️ Estrutura do Projeto

```
📁 Projeto/
├── main.py                              # Lógica principal e algoritmo A*
├── visu.py                             # Script principal de visualização
├── grafo_completo.png                  # Visualização do grafo completo
├── grafo_com_caminho_destacado.png     # Visualização com caminho A*
└── __pycache__/                        # Cache do Python
```

## 🚀 Como Executar

### Pré-requisitos

Certifique-se de ter Python 3.7+ instalado e as seguintes bibliotecas:

```bash
pip install networkx matplotlib numpy
```

### Executando a Aplicação

Para executar a visualização completa:

```bash
python visu.py
```

Para executar apenas o algoritmo A* (sem visualização):

```bash
python main.py
```

## 📊 Funcionalidades

### 🗺️ Mapeamento do Ambiente

O sistema mapeia diferentes tipos de locais:
- **🔴 Pontos Inicial/Final** - Origem e destino
- **🔵 Laboratórios** - LAB 01, LAB 02
- **🟠 Mesas** - Áreas de trabalho organizadas
- **🟢 Salas** - SALA 01, SALA 02
- **🟣 Banheiros** - Masculino, Feminino, Comum
- **⚫ Corredores** - Áreas de passagem
- **🟤 Escadas** - Conexões verticais
- **🩷 Elevadores** - Transporte vertical
- **🟡 Armários** - Áreas de armazenamento

### 🧭 Algoritmo A*

- Calcula o caminho mais eficiente entre dois pontos
- Utiliza distância euclidiana como heurística
- Considera as conexões reais entre os ambientes
- Otimiza tanto distância quanto número de passos

### 📈 Visualizações Geradas

1. **Grafo Completo** (`grafo_completo.png`)
   - Mostra toda a estrutura do ambiente
   - Todos os vértices e conexões
   - Legenda com categorização por cores

2. **Caminho A*** (`grafo_com_caminho_destacado.png`)
   - Destaca o caminho otimizado em vermelho
   - Mostra estatísticas da rota
   - Informações de eficiência

## 🔧 Arquivos Principais

### `main.py`
- Define a estrutura do grafo (vértices e arestas)
- Implementa o algoritmo A*
- Calcula matriz de distâncias euclidianas
- Executa a busca de caminho

### `visu.py`
- Script principal de visualização
- Gera duas imagens: grafo completo e com caminho
- Interface rica com legendas e estatísticas
- Funcões de otimização visual

## 📊 Exemplo de Saída

```
==========================================
          GERADOR DE VISUALIZAÇÕES DO GRAFO
==========================================

1. Criando grafo...
   Grafo criado: 55 vértices, 142 arestas

2. Executando algoritmo A*...
   Caminho encontrado: 6 passos
   Caminho A*:
       1. PONTO INICIAL
       2. A2 - 1
       3. SALA 02 - 1
       4. SALA 01 - 1
       5. SALA 01 - 2
       6. PONTO FINAL
   Distância total: 23.45 unidades

3. Gerando visualizações...
   → Gerando visualização completa...
   → Gerando visualização com caminho A*...

🎉 Visualizações concluídas com sucesso!
```

## 🎯 Características Técnicas

- **Algoritmo**: A* com heurística euclidiana
- **Grafo**: 55 vértices, ~142 arestas
- **Visualização**: NetworkX + Matplotlib
- **Resolução**: 400 DPI para imagens de alta qualidade
- **Layout**: Coordenadas fixas baseadas na planta real

## 🛠️ Personalização

Para modificar o ambiente:

1. **Adicionar novos pontos**: Edite o dicionário `vertices` em `main.py`
2. **Modificar conexões**: Atualize o dicionário `arestas` em `main.py`
3. **Alterar cores**: Modifique a função `obter_cor_vertice()` em `visu.py`
4. **Mudar pontos inicial/final**: Ajuste a chamada da função `a_estrela()` em `main.py`

## 🔍 Métricas de Performance

O sistema fornece métricas detalhadas:
- **Número de passos** no caminho otimizado
- **Distância total** em unidades
- **Eficiência** (unidades por passo)
- **Estatísticas do grafo** (vértices/arestas)

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais e de demonstração do algoritmo A* em navegação interior.
