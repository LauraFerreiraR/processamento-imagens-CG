# Processamento de Imagens com OpenCV

Projeto desenvolvido para a disciplina de **Computação Gráfica** da Universidade Estadual do Norte do Paraná (UENP).

O objetivo do projeto é demonstrar a aplicação de técnicas básicas de **Processamento Digital de Imagens** utilizando Python e OpenCV.

---

## Sobre o Projeto

Foram implementados diferentes algoritmos de processamento de imagens, permitindo aplicar filtros e transformações para melhoria, análise e extração de características das imagens.

Cada técnica possui uma pasta própria contendo:

- Código-fonte
- Imagem original
- Resultado obtido após o processamento

---

## Tecnologias Utilizadas

- Python
- OpenCV
- NumPy

---

## Estrutura do Projeto

```text
processamento-imagens-CG/

├── realce_ajuste/
├── reducao_ruido/
├── deteccao_bordas/
├── formas_texturas/
├── transformacoes_geometricas/
├── filtros_morfologicos/
└── README.md
```

---

*Funcionalidades

### Realce e Ajuste de Intensidde

- Ajuste de brilho
- Ajuste de contraste

---

### Redução de Ruído

- Filtro Gaussiano
- Suavização da imagem

---

### Detecção de Bordas

- Algoritmo de Canny

---

### Detecção de Formas e Texturas

- Conversão para tons de cinza
- Threshold
- Identificação de padrões

---

### Transformações Geométricas

- Rotação
- Redimensionamento

---

### Operações Morfológicas

- Erosão
- Dilatação

---

## Como executar

Clone o projeto

```bash
git clone https://github.com/LauraFerreiraR/processamento-imagens-CG.git
```

Instale as dependências

```bash
pip install opencv-python numpy
```

Execute qualquer módulo, por exemplo:

```bash
python reducao_ruido/ruido.py
```

---

## Conceitos Aplicados

- Processamento Digital de Imagens
- Visão Computacional
- Filtros Espaciais
- Operações Morfológicas
- Detecção de Bordas
- Transformações Geométricas

---

## Melhorias Futuras

- Comparação entre algoritmos
- Processamento em vídeo
- Detecção automática de objetos
- Aplicação de filtros em tempo real

---

Projeto desenvolvido para a disciplina de Computação Gráfica.
