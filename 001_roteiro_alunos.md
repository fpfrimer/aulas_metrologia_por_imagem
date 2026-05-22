# Módulo 1 - Roteiro do aluno
## SSH, Linux, terminal e scripts Bash

## Objetivo da atividade

Nesta atividade, você vai acessar o Orange Pi / Raspberry Pi por SSH e praticar comandos básicos do Linux pelo terminal. Ao final, você deverá entender:

- como acessar uma máquina remota com SSH;
- como identificar usuário, máquina e diretório atual no prompt;
- como navegar pelo sistema de arquivos;
- como criar, copiar, mover, renomear e remover arquivos;
- como usar redirecionamento com `>` e `>>`;
- como diferenciar comandos internos do Bash e comandos externos;
- como criar e executar scripts Bash simples;
- como testar uma captura de imagem com `fswebcam`.


## Parte 1 - Acesso por SSH

### O que vamos fazer

Vamos acessar o Orange Pi / Raspberry Pi pela rede usando SSH. Depois do login, os comandos digitados no terminal serão executados no Orange Pi, não no computador local.

### Comando

Substitua `usuario` pelo usuário do seu grupo e `endereco_ip` pelo IP informado pelo professor.

```bash
ssh usuario@endereco_ip
```

Exemplo:

```bash
ssh g0@192.168.0.100
```
Neste caso, o usuário é `g0` e o endereço IP é `192.168.0.100`. Após digitar o comando, será solicitada a senha do usuário. Digite a senha informada pelo professor e pressione `Enter` para acessar o terminal do Orange Pi / Raspberry Pi. Pode ser necessário confirmar a conexão na primeira vez, digitando `yes` e pressionando `Enter`.

Após o login, o prompt do terminal deve mostrar algo como:

```
g0@raspberrypi:~ $
```
Isso indica que você está logado como usuário `g0` na máquina `raspberrypi`, e o diretório atual é o home (`~`). Esse é o prompt do terminal onde você pode digitar comandos para interagir com o sistema.

### Confira

- [ ] Consegui acessar o Orange Pi / Raspberry Pi por SSH.
- [ ] O prompt apareceu no terminal.
- [ ] Identifiquei meu usuário no prompt.
- [ ] Identifiquei o nome da máquina no prompt.

### Revisão

1. O comando digitado depois do login roda no seu computador local ou no Orange Pi / Raspberry Pi?
2. Qual usuário aparece no seu prompt?
3. Qual é o nome da máquina que aparece no prompt?

## Parte 2 - Localização no sistema

### O que vamos fazer

Vamos entender em qual diretório estamos e como o terminal trabalha sempre a partir de um diretório atual.

### Comandos

```bash
pwd
```

```bash
ls
```

```bash
ls -a
```

```bash
ls -l
```

```bash
ls -lh
```

### Confira

- [ ] Usei `pwd` para ver o diretório atual.
- [ ] Usei `ls` para listar arquivos.
- [ ] Usei `ls -a` para ver arquivos ocultos.
- [ ] Usei `ls -l` ou `ls -lh` para ver detalhes.

### Revisão

1. Qual foi a saída do comando `pwd`?
2. O que o símbolo `~` representa?
3. Qual a diferença entre `ls` e `ls -a`?

## Parte 3 - Criando arquivos e diretórios

### O que vamos fazer

Vamos criar uma pasta e alguns arquivos de teste no diretório home do usuário.

### Comandos

```bash
mkdir pasta1
```

```bash
ls
```

```bash
echo "Texto exemplo" > arquivo2.txt
```

```bash
ls -l
```

```bash
cat arquivo2.txt
```

### Confira

- [ ] Criei o diretório `pasta1`.
- [ ] Criei o arquivo `arquivo2.txt`.
- [ ] Usei `cat` para ver o conteúdo do arquivo.

### Revisão

1. O que o comando `mkdir` faz?
2. O que o comando `echo "Texto exemplo" > arquivo2.txt` fez?
3. O arquivo foi criado em qual diretório?

## Parte 4 - Navegação entre diretórios

### O que vamos fazer

Vamos entrar em uma pasta, criar um arquivo dentro dela e acessar arquivos usando caminhos relativos.

### Comandos

```bash
cd pasta1
```

```bash
pwd
```

```bash
echo "Hello!" > arquivo3
```

```bash
cat arquivo3
```

```bash
cat ../arquivo2.txt
```

```bash
cd ..
```

```bash
pwd
```

### Confira

- [ ] Entrei em `pasta1`.
- [x] Criei `arquivo3`.
- [ ] Usei `..` para acessar um arquivo no diretório acima.
- [ ] Voltei para o diretório anterior com `cd ..`.

### Revisão

1. O que significa `..` em um caminho?
2. Qual a diferença entre `arquivo3` e `../arquivo2.txt`?
3. Por que é importante usar `pwd` durante a navegação?

## Parte 5 - Redirecionamento com `>` e `>>`

### O que vamos fazer

Vamos comparar dois tipos de redirecionamento: sobrescrever e acrescentar.

### Comandos

Entre novamente em `pasta1`, se necessário:

```bash
cd ~/pasta1
```

Agora execute:

```bash
echo "Hello again!" >> arquivo3
```

```bash
cat arquivo3
```

```bash
cat arquivo3 >> ../arquivo2.txt
```

```bash
cat ../arquivo2.txt
```

Note que o comando `cat arquivo3 >> ../arquivo2.txt` acrescenta o conteúdo de `arquivo3` ao final de `arquivo2.txt`, sem apagar o conteúdo anterior. Se usássemos `>`, o conteúdo de `arquivo2.txt` seria sobrescrito, e perderíamos as informações anteriores. Vamos testar isso:

```bash
cat arquivo3 > ../arquivo2.txt
```

```bash
cat ../arquivo2.txt
```

### Confira

- [ ] Usei `>>` para acrescentar texto (append).
- [ ] Vi que o conteúdo anterior não foi apagado.
- [ ] Acrescentei o conteúdo de `arquivo3` em `arquivo2.txt`.
- [ ] Usei `>` para sobrescrever o conteúdo de `arquivo2.txt`.
- [ ] Vi que o conteúdo anterior de `arquivo2.txt` foi perdido.

### Revisão

1. O que `>` faz?
2. O que `>>` faz?
3. Em que situação usar `>>` é mais seguro que `>`?

## Parte 6 - Copiando, movendo e removendo arquivos

### O que vamos fazer

Vamos praticar comandos de manipulação de arquivos e diretórios.

### Comandos

Volte ao diretório home:

```bash
cd ~
```

Crie uma segunda pasta e copie um arquivo:

```bash
mkdir pasta2
```

```bash
cp arquivo2.txt pasta2/arquivo2copiado
```

Veja o conteúdo de `pasta2`:

```bash
ls -l pasta2
```


```bash
cd pasta2
```

```bash
mv arquivo2copiado arquivo.txt
```

```bash
ls -l
```

Volte ao diretório home:

```bash
cd ~
```

### Confira

- [ ] Criei `pasta2`.
- [ ] Copiei um arquivo para `pasta2`.
- [ ] Renomeei o arquivo com `mv`.

### Revisão

1. Qual a função de `cp`?
2. Qual a função de `mv`?
3. O comando `mv` pode ser usado para mover e também para renomear?

## Parte 7 - Permissões

### O que vamos fazer

Vamos observar que usuários comuns não podem escrever em qualquer lugar do sistema.

### Comandos

```bash
ls -l /
```

```bash
echo "testando" > /arquivoRaiz.txt
```
Note que o comando acima deve gerar um erro de permissão, pois usuários comuns não têm permissão para criar arquivos diretamente na raiz do sistema (`/`).

```bash
ls /home
```

### Confira

- [ ] Observei a listagem da raiz `/`.
- [ ] Tentei criar um arquivo diretamente em `/`.
- [ ] Observei a mensagem de erro.

### Revisão

1. O erro aconteceu por causa do comando `echo` ou por causa da permissão de escrita em `/`?
2. Por que usuários comuns não devem escrever diretamente na raiz do sistema?
3. Qual diretório é apropriado para arquivos do seu usuário?

## Parte 8 - Limpeza dos arquivos da prática

### O que vamos fazer

Vamos remover os arquivos e pastas criados durante a prática.

### Comandos

```bash
cd ~
```

```bash
rm arquivo2.txt
```

```bash
rm -r pasta1
```

```bash
rm -r pasta2
```

```bash
ls
```

```bash
clear
```

### Confira

- [ ] Removi os arquivos de teste.
- [ ] Removi as pastas criadas.
- [ ] Conferi com `ls`.

### Atenção

O comando `rm` remove arquivos "permanentemente" sem enviar para a lixeira. Use com cuidado.

## Parte 9 - Comandos internos e externos

### O que vamos fazer

Vamos verificar se alguns comandos são internos do Bash ou programas externos.

Comandos internos são parte do próprio shell (Bash) e são executados diretamente por ele. Comandos externos são programas separados que o shell chama para executar. Saber a diferença ajuda a entender como o sistema processa os comandos.

### Comandos

```bash
type cd
```

```bash
type echo
```

```bash
type ls
```
Note que `cd` e `echo` são comandos internos do Bash, enquanto `ls` é um comando externo, geralmente localizado em `/bin/ls` ou similar.

```bash
type cat
```

```bash
type -a echo
```
Note que `type -a echo` mostra que `echo` é um comando interno, mas também pode haver um comando externo com o mesmo nome (geralmente em `/bin/echo`), embora o shell use o interno por padrão.

```bash
echo $PATH
```
PATH é uma variável de ambiente que contém uma lista de diretórios onde o shell procura por comandos externos. Quando você digita um comando, o shell verifica se é um comando interno. Se não for, ele procura nos diretórios listados em `PATH` para encontrar um programa correspondente.

O `$` antes de `PATH` indica que estamos acessando o valor da variável de ambiente `PATH`. O conteúdo dessa variável é uma lista de diretórios separados por dois pontos (`:`) onde o sistema procura por executáveis quando um comando é digitado.

Podemos usar o comando `which` para verificar onde um comando externo está localizado:

```bash
which ls
```

```bash
which cd
```

Note que `which ls` mostra o caminho para o comando externo `ls`, enquanto `which cd` não retorna nada, pois `cd` é um comando interno do Bash.

Podemos criar uma variável de ambiente com o comando `export`:

```bash
export MINHA_VARIAVEL="Valor de teste"
```

```bash
echo $MINHA_VARIAVEL
```

Essa variável estará disponível para os processos filhos do shell, mas não para outros terminais ou sessões. Para tornar a variável permanente, seria necessário adicioná-la ao arquivo de configuração do shell, como `~/.bashrc` ou `~/.profile`.

Caso não seja inserido em `~/.bashrc` ou similar, a variável `MINHA_VARIAVEL` só existirá na sessão atual do terminal. Se você abrir um novo terminal ou fizer login novamente, essa variável não estará definida.

Vamos tornar a variável permanente:

```bash
echo 'export MINHA_VARIAVEL="Valor de teste no ~/.bashrc"' >> ~/.bashrc
```

```bash
source ~/.bashrc
```
O comando source recarrega o arquivo `~/.bashrc` para que as alterações tenham efeito imediato na sessão atual do terminal. Agora, mesmo se você abrir um novo terminal ou fizer login novamente, a variável `MINHA_VARIAVEL` estará definida.

```bash
echo $MINHA_VARIAVEL
```

Mais ao final, mostraremos como incluir pastas no `PATH` para que o sistema reconheça comandos personalizados.

### Confira

- [ ] Verifiquei comandos internos.
- [ ] Verifiquei comandos externos.
- [ ] Visualizei a variável `PATH`.
- [ ] Criei uma variável de ambiente com `export`.
- [ ] Tornei a variável permanente editando `~/.bashrc`.
- [ ] Usei `source` para recarregar as configurações do shell.
  

### Revisão

1. O comando `cd` é interno ou externo?
2. O comando `ls` é interno ou externo?
3. Para que serve a variável `PATH`?
4. O que é .bashrc?
5. O que o comando `source` faz?
6. Por que razão .bashrc não aparece ao executar `ls`?

## Parte 10 - Criando um script simples

### O que vamos fazer

Vamos criar um script Bash com informações básicas do sistema.

### Comandos

Antes de criar o script, retorne para o diretório home, se necessário:

```bash
cd ~
```

Teste os seguintes comandos para ver as informações do sistema:

```bash
whoami
```

```bash
hostname
```

```bash
grep PRETTY_NAME /etc/os-release
```

```bash
uptime -p
```

Note que cada comando fornece uma informação diferente: `whoami` mostra o usuário atual, `hostname` mostra o nome da máquina, `grep PRETTY_NAME /etc/os-release` mostra a versão do sistema operacional, e `uptime -p` mostra há quanto tempo o sistema está ligado. Vamos juntar essas informações em um script para facilitar a consulta.


Crie uma pasta para os scripts:

```bash
mkdir scripts
```

Crie o arquivo:

```bash
nano scripts/info_sistema.sh
```

Nano é um editor de texto simples que roda no terminal. Ele permite criar e editar arquivos de texto. Para usar o nano, basta digitar o comando `nano` seguido do nome do arquivo que deseja criar ou editar. No caso, estamos criando um script chamado `info_sistema.sh` dentro da pasta `scripts`.

Digite o conteúdo:

```bash
#!/bin/bash

echo "Informacoes do sistema"
echo "Usuario:"
whoami

echo "Maquina:"
hostname

echo "Versao do Linux:"
grep PRETTY_NAME /etc/os-release

echo "Tempo ligado:"
uptime -p
```

Salve com `Ctrl+O`, confirme com `Enter` e saia com `Ctrl+X`.

Verifique o arquivo:

```bash
ls -l scripts/info_sistema.sh
```

```bash
cat scripts/info_sistema.sh
```

Tente executar:

```bash
./scripts/info_sistema.sh
```

Note que o comando acima pode gerar um erro de permissão, pois o script ainda não tem permissão de execução.

Adicione permissão de execução:

```bash
chmod +x scripts/info_sistema.sh
```

O comando `chmod +x scripts/info_sistema.sh` adiciona permissão de execução ao arquivo `scripts/info_sistema.sh`, permitindo que ele seja executado como um programa. O `+x` significa "adicionar permissão de execução" para o proprietário do arquivo, e possivelmente para outros usuários, dependendo das permissões atuais do arquivo.

O `chmod` é um comando usado para alterar as permissões de arquivos e diretórios no Linux. Ele pode ser usado para conceder ou revogar permissões de leitura, escrita e execução para o proprietário do arquivo, o grupo e outros usuários. Para o intuito dessa aula, o `chmod +x` é suficiente para tornar o script executável. Recomendo pesquisar mais sobre `chmod` para entender melhor as permissões no Linux.

Execute novamente:

```bash
./info_sistema.sh
```

Também execute com:

```bash
bash info_sistema.sh
```

### Confira

- [ ] Criei o script.
- [ ] Vi que faltava permissão de execução.
- [ ] Usei `chmod +x`.
- [ ] Executei o script com `./info_sistema.sh`.
- [ ] Executei o script com `bash info_sistema.sh`.

### Responda

1. Para que serve a primeira linha `#!/bin/bash`?
2. Qual a diferença entre `./info_sistema.sh` e `bash info_sistema.sh`?
3. Qual comando adicionou permissão de execução?

## Parte 11 - Captura de imagem com `fswebcam`

### O que vamos fazer

Vamos testar a câmera e transformar o comando de captura em um script simples.

### Comandos

Verifique a câmera:

```bash
ls /dev/video*
```

Note que o comando acima lista os dispositivos de vídeo disponíveis. Se a câmera estiver conectada e reconhecida pelo sistema, você deve ver um dispositivo como `/dev/video0`. Se não aparecer nenhum dispositivo, pode ser necessário verificar a conexão da câmera ou instalar os drivers adequados.

Verifique o comando `date`:

```bash
date
```

Formate a data e hora para usar no nome do arquivo:

```bash
date +%Y%m%d_%H%M%S
```

O arqumentoo `+%Y%m%d_%H%M%S` formata a data e hora no formato "ano mês dia _ hora minuto segundo". Por exemplo, se a data e hora atual for 5 de junho de 2024 às 14:30:45, o comando `date +%Y%m%d_%H%M%S` retornará `20240605_143045`. Esse formato é útil para criar nomes de arquivos únicos com base na data e hora da captura.

Verifique o comando:

```bash
type fswebcam
```

Capture uma imagem:

```bash
fswebcam foto.jpg
```

Confira:

```bash
ls -lh foto.jpg
```

Crie uma pasta:

```bash
mkdir imagens
```

Crie o script:

```bash
nano captura.sh
```

Digite:

```bash
#!/bin/bash

mkdir -p imagens

arquivo="imagens/foto_$(date +%Y%m%d_%H%M%S).jpg"

echo "Capturando imagem..."
fswebcam -r 1280x720 "$arquivo"
echo "Imagem salva em $arquivo"
```

Salve e saia do editor.

Execute:

```bash
chmod +x captura.sh
```

```bash
./captura.sh
```

```bash
./captura.sh
```

```bash
ls -lh imagens
```

### Confira

- [ ] Capturei uma imagem manualmente.
- [ ] Criei `captura.sh`.
- [ ] Executei o script duas vezes.
- [ ] Foram geradas imagens com nomes diferentes.

### Responda

1. Por que usamos `date` no nome do arquivo?
2. O que aconteceria se todas as imagens tivessem o mesmo nome?
3. Como esse script pode ajudar em uma rotina de metrologia por imagem?

## Parte 12 - Tornando o script executável a partir de qualquer lugar

### O que vamos fazer

Vamos adicionar a pasta `scripts` ao `PATH` para que possamos executar o script de captura de qualquer diretório.

### Comandos

Primeiro, insira a pasta `scripts` no `PATH` editando o `~/.bashrc`:

```bash
echo 'export PATH="$HOME/scripts:$PATH"' >> ~/.bashrc
```
Recarregue o `~/.bashrc`:

```bash
source ~/.bashrc
```

Agora, você pode executar o script de captura de qualquer lugar:

```bash
captura.sh
```

Opcionalmente, é possível criar um link simbólico para modificar o nome do comando:


```bash
ln -s ~/scripts/captura.sh ~/scripts/pic
```
Antes de criar o link, certifique-se de que `captura.sh` tem permissão de execução. Também certifique-se de que não existe um outro comando com o mesmo nome. 

O comando `ln -s` cria um link simbólico chamado `pic` que aponta para `captura.sh`. Agora, você pode executar o script usando o comando `pic` de qualquer diretório:

```bash
pic
```

Também é possível criar o link simbólico diretamente em um diretório que já esteja no `PATH`, como `/usr/local/bin`, mas isso geralmente requer permissões de superusuário (root). Para evitar complicações, manter o link simbólico dentro da pasta `scripts` é uma boa prática para uso pessoal.

### Confira

- [ ] Adicionei `scripts` ao `PATH`.
- [ ] Recarreguei o `~/.bashrc`.
- [ ] Executei o script de captura de outro diretório.
- [ ] Criei um link simbólico para o script.

### Revisão

1. O que é o `PATH` e por que adicionamos a pasta `scripts` a ele?
2. O que o comando `ln -s` faz?
3. Qual a vantagem de criar um link simbólico para o script?

## Encerramento

Ao final desta atividade, você deve conseguir explicar:

- como acessar o Orange Pi / Raspberry Pi via SSH;
- como navegar pelo terminal;
- como criar, mover e remover arquivos;
- como permissões afetam o uso do sistema;
- como criar e executar um script Bash;
- como capturar uma imagem com `fswebcam`;
- por que scripts ajudam a tornar uma rotina experimental mais reprodutível.

## Completmento - comandos extras (grep, less, find, etc.), direcionamento de saída e outros

Teste o seguinte comando para ver o conteúdo do arquivo de configuração do shell:

```bash
less ~/.bashrc
```
O comando `less` é um pager que permite visualizar o conteúdo de arquivos longos de forma paginada, facilitando a leitura. Ele é especialmente útil para arquivos de configuração como `~/.bashrc`, que podem conter muitas linhas de código. Com `less`, você pode navegar pelo arquivo usando as setas do teclado, a barra de espaço para avançar uma página e `q` para sair.

Agora tente:

```bash
info_sistema.sh | less
```
O comando `info_sistema.sh | less` executa o script `info_sistema.sh` e redireciona sua saída para o `less`, permitindo que você visualize as informações do sistema de forma paginada. Isso é útil quando a saída do script é longa e não cabe em uma única tela, facilitando a leitura e a navegação pelos resultados.

O simbolo `|` é conhecido como pipe e é usado para conectar a saída de um comando à entrada de outro. No exemplo, a saída do script `info_sistema.sh` é enviada para o `less`, permitindo que você visualize as informações de forma organizada e paginada. O uso de pipes é uma prática comum no Linux para combinar comandos e processar dados de maneira eficiente.

Tente também:

```bash
info_sistema.sh | grep "up"
```
O comando `info_sistema.sh | grep "up"` executa o script `info_sistema.sh` e filtra a saída para mostrar apenas as linhas que contêm a palavra "up". O `grep` é um comando de busca que procura por padrões específicos em um texto. Neste caso, ele está procurando por linhas que mencionem "up", o que pode ser útil para encontrar informações relacionadas ao tempo de atividade do sistema ou outras ocorrências da palavra "up" na saída do script. O uso de pipes permite combinar comandos para processar e filtrar dados de maneira eficiente.

Tente também:

```bash
find ~ -name "*.sh"
```
O comando `find ~ -name "*.sh"` procura por arquivos com a extensão `.sh` (scripts Bash) no diretório home do usuário (`~`) e em seus subdiretórios. O `find` é um comando poderoso para localizar arquivos com base em critérios específicos, como nome, tipo, tamanho, data de modificação, entre outros. Neste caso, ele está buscando por arquivos que terminam com `.sh`, o que é útil para encontrar scripts Bash em seu sistema. O resultado será uma lista de caminhos para os arquivos encontrados.

Tente também:

```bash
find ~ -type f -executable
```

O comando `find ~ -type f -executable` procura por arquivos regulares (`-type f`) que têm permissão de execução (`-executable`) no diretório home do usuário (`~`) e em seus subdiretórios. Isso é útil para localizar scripts ou programas que podem ser executados diretamente. O resultado será uma lista de caminhos para os arquivos executáveis encontrados, o que pode ajudar a identificar scripts personalizados ou programas instalados pelo usuário.

Tente o comando:

```bash
man find
```
Tente o comando

```bash
tree ~
```
O comando `tree ~` exibe a estrutura de diretórios e arquivos do diretório home do usuário em formato de árvore. Ele mostra os arquivos e pastas organizados hierarquicamente, mas essa aplicação não está instalada. Apenas um dos grupos pode instalar com:

```bash
sudo apt update && sudo apt install tree
```

O comando apt é um gerenciador de pacotes usado em distribuições Linux baseadas em Debian, como o Raspberry Pi OS ou armbian. O comando `sudo apt update` atualiza a lista de pacotes disponíveis, garantindo que você tenha as informações mais recentes sobre os pacotes e suas versões. O comando `sudo apt install tree` instala o programa `tree`, que é uma ferramenta para visualizar a estrutura de diretórios em formato de árvore. O uso de `sudo` é necessário para obter permissões de superusuário, permitindo que o sistema instale o software. Após a instalação, você poderá usar o comando `tree ~` para visualizar a estrutura do diretório home do usuário.

Os demais grupos podem agora usar o comando `tree` para visualizar a estrutura de diretórios e arquivos do diretório home do usuário em formato de árvore, facilitando a compreensão da organização dos arquivos e pastas.

Os demais grupos podem instalar esses outros aplicativos, se desejarem:

```bash
sudo apt install cowsay
```

```bash
sudo apt install cmatrix
```

O comando `sudo apt install cowsay` instala o programa `cowsay`, que é um gerador de arte ASCII que exibe uma mensagem em um balão de fala, acompanhado por uma figura de uma vaca ou outros personagens. O comando `sudo apt install cmatrix` instala o programa `cmatrix`, que é um simulador de chuva de caracteres inspirado no filme "Matrix". Ambos os programas são divertidos e podem ser usados para personalizar a saída do terminal, mas não são essenciais para as atividades de metrologia por imagem. A instalação desses aplicativos é opcional e pode ser feita por qualquer grupo que queira experimentar algo diferente no terminal.

Tentem direcionar a saída de info_sistema.sh para o cowsay:

```bash
info_sistema.sh | cowsay
```

Tente também salvar uma arquivo de texto com a saída de info_sistema.sh direcionada para o cowsay:

```bash
info_sistema.sh | cowsay > info_cowsay.txt && nano info_cowsay.txt
```

