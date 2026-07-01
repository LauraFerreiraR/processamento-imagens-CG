PROCESSAMENTO BÁSICO DE IMAGENS

Universidade Estadual do Norte do Paraná - CLM
Computação Gráfica

Este repositório contém implementações em Python de diversos filtros de processamento de imagens usando a biblioteca OpenCV.

1. ESTRUTURA
  Cada pasta contém:
    -Código em python
    -Imagem original
    -Imagem resultante com filtro aplicado

2. FILTROS IMPLEMENTADOS
    a - Realce e Ajuste de Intensidade (melhorar contraste e brilho).
        Arquivo: 'realce_ajuste/realce.py'
        Descrição: Ajuste de brilho e contraste usando multiplicação e adição nos valores dos pixels.
        
    b - Redução de Ruído e Suavização (remover imperfeições).
        Arquivo: 'reducao_ruido/ruido.py'
        Descricao: Aplicação de suavização com filtro Gaussiano para remoção de ruídos.
   
    c - Detecção de Bordas (identificar contornos e formas).
        Arquivo: 'deteccao_bordas/bordas.py'
        Descrição: Uso do filtro Canny para detectar contornos de objetos na imagem.
   
    d - Detecção de Formas e Texturas (identificar padrões na imagem).
        Arquivo: 'formas_texturas/formas_texturas.py'
        Descrição: Conversão para escala de cinza e uso de threshold para realçar formas e padrões.
   
    e - Transformações Geométricas (redimensionamento e distorção).
        Arquivo: 'transformacoes_geometricas/transformacoes.py'
        Descrição: Redimensionamento e rotação da imagem.
   
    f - Filtros Morfológicos (processamento de imagens segmentadas).
        Arquivo: 'filtros_morfologicos/morfologicos.py'
        Descrição: Aplicação de erosão e dilatação para refinar contornos em imagens binarizadas.


4. REQUISITOS
   -Python
   -OpenCV (cv2)

   Para rodar os códigos, precisa instalar as seguintes dependências:
     -No terminal: "pip install opencv-python"

5.EXECUÇÃO

  Ativar ambiente virtual (caso esteja usando): "source venv/bin/activate"
  Executar individualmente: "python3 caminho/filtro.py" Ex: python3 reducao_ruido/ruido.py
