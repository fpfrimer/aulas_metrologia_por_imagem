# Módulo 3 - Roteiro do aluno
## Processamento de imagens e gráfico RGB

## Objetivo da atividade

Nesta atividade, você vai processar uma sequência de imagens usando Python. Ao final, você deverá entender:

- como uma imagem pode ser tratada como dado numérico;
- como calcular médias dos canais R, G e B;
- como salvar resultados em uma tabela CSV;
- como gerar um gráfico simples a partir de imagens;
- por que iluminação, fundo e enquadramento afetam medições por imagem.

## Ideia central

Nos módulos anteriores, vimos como capturar imagens de forma manual e automatizada. Agora vamos analisar imagens já coletadas. Esta atividade será executada no computador Windows do laboratório, usando o PowerShell.

O objetivo é gerar um gráfico das componentes RGB ao longo de uma sequência de imagens de uma fruta.

A atividade foi inspirada no trabalho de Valesan sobre controle de maturação por imagem. Esse trabalho está disponível no repositório em `referencias/dispositivocontrolematuracao.pdf`.

## Parte 1 - Entrar na pasta da atividade

### O que vamos fazer

Vamos acessar a pasta do material e conferir os arquivos disponíveis.

### Comandos

Abra o PowerShell na pasta do material. Se necessário, entre na pasta com:

```powershell
cd caminho\para\aulas_metrologia_por_imagem
```

Liste os arquivos:

```powershell
dir
```

```powershell
dir 003_material_de_apoio
```

### Confira

- [ ] Encontrei a pasta `003_material_de_apoio`.
- [ ] Encontrei o script `analise_rgb.py`.
- [ ] Encontrei os datasets pequenos do módulo 3.

Se o professor solicitar a instalação das bibliotecas Python, use:

```powershell
python -m pip install -r 003_material_de_apoio/requirements.txt
```

Você não precisa saber programar em Python para executar esta atividade. O script já está pronto; nesta aula, o mais importante é saber executar o comando, conferir os arquivos gerados e interpretar os resultados.

Confira se o Python está disponível:

```powershell
python --version
```

Se aparecer uma versão, como `Python 3.11.2`, o Python está instalado.

Se o script reclamar da falta das bibliotecas `PIL` ou `matplotlib`, avise o professor ou execute novamente o comando de instalação com `pip`.

## Parte 2 - Observar o dataset de exemplo

### O que vamos fazer

Antes de processar as imagens, vamos conferir a organização dos arquivos.

As imagens vieram de um recorte pequeno do FruitQ, um banco de imagens do Kaggle com várias frutas e classes de qualidade. O banco completo é grande demais para a atividade em laboratório, não está neste repositório e pode ser acessado em: https://www.kaggle.com/datasets/sholzz/fruitq-dataset. Por isso, vamos usar apenas 32 imagens de banana no exemplo e 32 imagens de tomate na atividade.

### Comandos

```powershell
dir 003_material_de_apoio/dataset_exemplo/banana
```

Veja que os nomes seguem uma ordem:

```text
banana_001.png
banana_002.png
...
banana_012.png
...
banana_032.png
```

Essa ordem será usada como eixo horizontal do gráfico.

No conjunto de exemplo, as imagens `banana_001.png` até `banana_011.png` representam a etapa boa, `banana_012.png` até `banana_021.png` representam a etapa intermediária, e `banana_022.png` até `banana_032.png` representam a etapa deteriorada.

### Confira

- [ ] Entendi que a sequência não é tempo real de laboratório.
- [ ] Entendi que a ordem representa uma sequência visual de qualidade.
- [ ] Identifiquei imagens boas, intermediárias e deterioradas.

## Parte 3 - Executar o exemplo da banana

### O que vamos fazer

Vamos executar um script pronto que calcula a média dos canais RGB nas imagens de banana.

### Comando

```powershell
python 003_material_de_apoio/scripts/analise_rgb.py 003_material_de_apoio/dataset_exemplo/banana
```

Se o comando funcionar, devem aparecer mensagens parecidas com:

```text
Imagens processadas: 32
CSV salvo em: resultado_rgb.csv
Grafico salvo em: grafico_rgb.png
```

### Confira

```powershell
dir
```

- [ ] O arquivo `resultado_rgb.csv` foi criado.
- [ ] O arquivo `grafico_rgb.png` foi criado.

## Parte 4 - Abrir a tabela de resultados

### O que vamos fazer

Vamos visualizar as primeiras linhas do CSV.

### Comando

```powershell
Get-Content resultado_rgb.csv -TotalCount 10
```

Cada linha representa uma imagem processada.

### Observe

- o nome do arquivo;
- a etapa da imagem;
- a média do canal vermelho;
- a média do canal verde;
- a média do canal azul;
- a quantidade de pixels usados.

### Confira

- [ ] Consegui visualizar a tabela.
- [ ] Entendi que cada imagem virou uma linha de dados.
- [ ] Localizei as colunas `media_r`, `media_g` e `media_b`.

## Parte 5 - Interpretar o gráfico

### O que vamos fazer

Vamos analisar o gráfico `grafico_rgb.png`.

Abra o arquivo `grafico_rgb.png` no computador do laboratório, clicando duas vezes nele pelo Explorador de Arquivos ou usando o visualizador de imagens do Windows.

### Perguntas

1. Qual canal apresenta maior variação?
2. O gráfico muda quando a sequência passa de boa para intermediária?
3. O gráfico muda quando a sequência passa de intermediária para deteriorada?
4. Algum ponto parece diferente dos demais?
5. A média RGB sozinha seria suficiente para dizer se uma fruta está boa ou deteriorada?

## Parte 6 - Repetir com outra fruta

### O que vamos fazer

Agora cada grupo vai repetir o procedimento com o conjunto de tomate.

### Comando

```powershell
python 003_material_de_apoio/scripts/analise_rgb.py 003_material_de_apoio/dataset_atividade/tomate --csv tomate_rgb.csv --grafico tomate_rgb.png
```

### Confira

```powershell
dir
```

- [ ] O arquivo `tomate_rgb.csv` foi criado.
- [ ] O arquivo `tomate_rgb.png` foi criado.

## Parte 7 - Comparar banana e tomate

### O que vamos fazer

Compare os resultados do exemplo com os resultados da atividade.

### Perguntas

1. A fruta analisada pelo grupo teve comportamento parecido com a banana?
2. Qual canal RGB foi mais importante no tomate?
3. O fundo branco atrapalharia a análise?
4. Como a iluminação poderia alterar o gráfico?
5. Que melhoria você faria no processamento?

## Parte 8 - Teste extra: imagem inteira

### O que vamos fazer

Por padrão, o script ignora pixels quase brancos para reduzir o efeito do fundo. Agora vamos testar a imagem inteira.

### Comando

```powershell
python 003_material_de_apoio/scripts/analise_rgb.py 003_material_de_apoio/dataset_atividade/tomate --imagem-inteira --csv tomate_inteiro.csv --grafico tomate_inteiro.png
```

### Perguntas

1. O gráfico mudou muito?
2. A diferença entre as etapas ficou maior ou menor?
3. Qual resultado parece representar melhor a fruta?

## Parte 9 - Teste extra: limiar do fundo

### O que vamos fazer

O script descarta pixels quase brancos usando um limiar. Por padrão, o valor é `220`. Agora vamos testar um valor maior, `245`, para observar o que acontece quando pouco fundo é removido.

### Comando

```powershell
python 003_material_de_apoio/scripts/analise_rgb.py 003_material_de_apoio/dataset_atividade/tomate --limite-branco 245 --csv tomate_limiar245.csv --grafico tomate_limiar245.png
```

### Perguntas

1. O gráfico mudou?
2. O número de pixels usados mudou?
3. O valor `245` parece deixar mais fundo na média do que o valor padrão `220`?

## Entrega da atividade

Ao final, cada grupo deve apresentar:

- o arquivo CSV da fruta analisada;
- o gráfico RGB gerado;
- uma breve interpretação dos canais RGB;
- uma sugestão de melhoria para tornar a medição mais confiável.

## Revisão final

- [ ] Processei as imagens de banana.
- [ ] Processei as imagens de tomate.
- [ ] Gerei CSV e gráfico.
- [ ] Comparei os resultados.
- [ ] Entendi que processamento de imagem depende da captura, iluminação, fundo e escolha da região analisada.
