# Módulo 3 - Material de apoio
## Processamento simples de imagens em Python

## Ideia da atividade

Nesta aula, vamos tratar uma imagem como dado experimental. Em vez de apenas olhar para a fruta, vamos calcular números a partir das imagens.

O procedimento será:

1. abrir uma sequência de imagens;
2. calcular a média dos canais vermelho, verde e azul;
3. salvar os resultados em uma tabela;
4. gerar um gráfico RGB ao longo da sequência.

As imagens foram retiradas de um subconjunto didático do FruitQ, um dataset público do Kaggle voltado ao estudo de qualidade visual de frutas e hortaliças. O banco completo é muito maior e possui várias frutas, como banana, pepino, uva, caqui, mamão, pêssego, pera, pimentão, morango, tomate e melancia, organizadas em classes visuais de qualidade. O dataset completo pode ser acessado em: https://www.kaggle.com/datasets/sholzz/fruitq-dataset.

Nesta aula usamos apenas uma pequena amostra: banana para o exemplo e tomate para a atividade. A sequência não representa uma medição temporal real feita no laboratório. Ela foi organizada por etapa visual de qualidade: fruta boa, intermediária e deteriorada. Por isso, o eixo horizontal do gráfico deve ser interpretado como índice da imagem ou ordem da sequência.

## Organização dos dados

O material possui dois conjuntos pequenos:

```text
003_material_de_apoio/
  dataset_exemplo/
    banana/
      banana_001.png
      ...
      banana_032.png
  dataset_atividade/
    tomate/
      tomate_001.png
      ...
      tomate_032.png
```

O professor usa o conjunto de banana para demonstrar o processamento. Depois, os alunos repetem o procedimento com o conjunto de tomate.

As imagens foram amostradas de forma uniforme a partir da ordem numérica original do dataset. O nome dos arquivos foi padronizado para facilitar o processamento, como ocorreria em uma coleta real automatizada:

```text
banana_001.png
banana_002.png
banana_003.png
...
```

Os arquivos `manifesto_selecao.csv` guardam a origem de cada imagem no dataset bruto. Eles servem para rastreabilidade, mas não são necessários para executar a atividade.

## Para quem nunca programou em Python

Nesta atividade, não é necessário escrever o programa do zero. O script já está pronto. O aluno precisa apenas:

1. abrir o terminal;
2. entrar na pasta correta;
3. executar o comando indicado;
4. conferir se os arquivos de saída foram criados;
5. interpretar a tabela e o gráfico.

O Python será usado como ferramenta de processamento. Nesta aula, a execução será feita no computador Windows do laboratório, usando o PowerShell.

## Por que usar RGB?

Cada pixel colorido possui três componentes principais:

| Canal | Significado |
|---|---|
| R | intensidade de vermelho |
| G | intensidade de verde |
| B | intensidade de azul |

Quando uma fruta muda de aparência, os valores médios desses canais também podem mudar. Em uma banana, por exemplo, o amadurecimento e a deterioração tendem a alterar a relação entre amarelo, marrom e escuro.

## Cuidado com o fundo

Muitas imagens do dataset possuem fundo branco. Se calcularmos a média da imagem inteira, o resultado pode representar mais o fundo do que a fruta.

Por isso, o script fornecido ignora pixels quase brancos por padrão. Essa é uma forma simples de aproximar a análise da região ocupada pela fruta.

Um pixel é ignorado quando:

```text
R >= 220, G >= 220 e B >= 220
```

Essa regra não é perfeita, mas remove quase todo o fundo branco nas imagens de exemplo. Um limiar alto demais, como 245, deixa muito fundo entrar na média e pode fazer as curvas RGB variarem pouco.

## Script de exemplo

O script está em:

```text
003_material_de_apoio/scripts/analise_rgb.py
```

Dependências usadas pelo script:

```text
Pillow
matplotlib
```

No computador Windows do laboratório, se necessário, instale com:

```powershell
python -m pip install -r 003_material_de_apoio/requirements.txt
```

Para executar o exemplo da banana:

```powershell
python 003_material_de_apoio/scripts/analise_rgb.py 003_material_de_apoio/dataset_exemplo/banana
```

O script gera dois arquivos:

```text
resultado_rgb.csv
grafico_rgb.png
```

O CSV contém uma linha para cada imagem:

| Coluna | Descrição |
|---|---|
| indice | ordem da imagem na sequência |
| arquivo | nome do arquivo processado |
| etapa | boa, intermediária ou deteriorada |
| media_r | média do canal vermelho |
| media_g | média do canal verde |
| media_b | média do canal azul |
| pixels_usados | quantidade de pixels considerados no cálculo |

## Leitura esperada do gráfico

O gráfico não deve ser interpretado como uma prova definitiva de maturação ou qualidade. Ele é uma primeira medida quantitativa.

Ao analisar o gráfico, observe:

- qual canal muda mais ao longo da sequência;
- se os canais sobem ou descem;
- se existe diferença visível entre imagens boas, intermediárias e deterioradas;
- se algum ponto parece fora do padrão;
- como o fundo e a iluminação podem influenciar o resultado.

## Variação para comparação

Para comparar com a média da imagem inteira, execute:

```powershell
python 003_material_de_apoio/scripts/analise_rgb.py 003_material_de_apoio/dataset_exemplo/banana --imagem-inteira
```

Depois compare o novo gráfico com o gráfico gerado usando a máscara do fundo branco.

Também é possível testar uma região de interesse retangular fixa com `--roi`. O exemplo abaixo usa um quadrado interno da banana:

```powershell
python 003_material_de_apoio/scripts/analise_rgb.py 003_material_de_apoio/dataset_exemplo/banana --roi 500 445 80 25 --csv banana_roi.csv --grafico banana_roi.png
```

Essa opção ajuda a comparar duas estratégias: medir uma pequena região interna da fruta ou medir uma aproximação da fruta inteira removendo o fundo quase branco.

Para testar outro limiar de fundo branco:

```powershell
python 003_material_de_apoio/scripts/analise_rgb.py 003_material_de_apoio/dataset_exemplo/banana --limite-branco 245 --csv banana_limiar245.csv --grafico banana_limiar245.png
```

Alterar esse valor muda quais pixels são tratados como fundo. Valores maiores removem apenas pixels muito brancos; valores menores removem uma parte maior do fundo.

## Perguntas para discussão

1. O canal vermelho, verde ou azul mudou mais ao longo da sequência?
2. O gráfico separa bem as etapas boa, intermediária e deteriorada?
3. O que acontece quando o fundo branco é incluído no cálculo?
4. Que fatores experimentais poderiam alterar os valores RGB mesmo sem mudança na fruta?
5. Como uma captura automatizada, como a feita nos módulos anteriores, ajudaria a obter dados mais comparáveis?
