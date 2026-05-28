# Módulo 2 - Roteiro do aluno
## Automação de captura de imagens com systemd

## Objetivo da atividade

Nesta atividade, você vai criar rotinas automatizadas de captura de imagens usando scripts Bash e `systemd`.

Ao final, você deverá entender:

- como testar a captura manualmente;
- como criar um script de captura simples;
- como executar esse script com um serviço;
- como repetir a execução usando um timer;
- como verificar status e logs;
- como criar uma coleta contínua usando apenas um serviço;
- quando usar `service + timer` e quando usar um serviço contínuo.


## Ideia central

Nesta aula, vamos separar a automação em três partes:

| Elemento | Função |
|---|---|
| Script | Define o que será feito |
| Service | Define como o sistema executa a tarefa |
| Timer | Define quando a tarefa será executada |

> Regra importante: se o script não funciona manualmente, ainda não está pronto para virar automação.

## Parte 1 - Preparação e teste manual da câmera

### O que vamos fazer

Antes de usar `systemd`, vamos testar a câmera manualmente. Isso evita confundir erro de câmera com erro de serviço.

### Comandos

Confira o diretório atual:

```bash
pwd
```

Vá para o diretório home:

```bash
cd ~
```

Verifique se a câmera aparece no Linux:

```bash
ls /dev/video*
```

Verifique se `fswebcam` está instalado:

```bash
type fswebcam
```

Crie uma pasta para imagens:

```bash
mkdir -p imagens
```

A opção `-p` evita erro se a pasta já existir.

Capture uma imagem de teste:

```bash
fswebcam -r 1280x720 imagens/teste.jpg
```

Confira se o arquivo foi criado:

```bash
ls -lh imagens
```

A opção `--no-banner` remove a data e hora da imagem, mas pode ser útil para diagnóstico.

```bash
fswebcam --no-banner -r 1280x720 imagens/teste_sem_banner.jpg
```

### Checkpoint

- [ ] Estou no diretório home.
- [ ] A câmera apareceu como `/dev/video0` ou similar.
- [ ] O comando `fswebcam` está disponível.
- [ ] A imagem `teste.jpg` foi criada.
- [ ] A imagem `teste_sem_banner.jpg` foi criada.
### Responda

1. Por que testamos a câmera antes de criar o serviço?
2. Qual comando mostrou se a câmera foi reconhecida?
3. Qual comando mostrou se a imagem foi criada?

## Parte 2 - Script de captura simples

### O que vamos fazer

Vamos criar um script que faz uma única captura e termina. Esse script será usado depois por um serviço e por um timer.

### Criar o script

Use o seguinte comando para criar o arquivo `captura.sh`:

```bash
nano captura.sh
```

Ou crie o arquivo diretamente pelo VS Code (caso esteja usando), conforme a orientação do professor.

Digite o conteúdo abaixo. Troque `g0` pelo usuário do seu grupo, se necessário.

```bash
#!/bin/bash

mkdir -p $HOME/imagens

ts=$(date +%Y%m%d_%H%M%S)
arquivo="$HOME/imagens/foto_${ts}.jpg"

echo "Capturando imagem em $arquivo"
fswebcam -r 1280x720 "$arquivo"
echo "Captura finalizada"
```

No nano, salve com `Ctrl+O`, confirme com `Enter` e saia com `Ctrl+X`.

### Testar manualmente

Adicione permissão de execução:

```bash
chmod +x captura.sh
```
Verifique se o script tem permissão de execução:

```bash
ls -l captura.sh
```

Execute o script:

```bash
./captura.sh
```

```bash
ls -lh imagens
```

Execute novamente:

```bash
./captura.sh
```

```bash
ls -lh imagens
```

Perceba que o script cria uma nova imagem a cada execução, com um nome diferente baseado na data e hora.

O script assume que `fswebcam` está instalado, no PATH do usuário e que a câmera está funcionando. Se algum desses itens falhar, o script pode não criar a imagem.

É possível melhorar i script para verificar esses erros:
```bash
#!/usr/bin/env bash

# Script para capturar uma imagem usando fswebcam
# Requisitos: fswebcam instalado e câmera conectada em /dev/video0

# Faz o Bash tratar variáveis não definidas como erro
set -u

# Verifica se o fswebcam está instalado e guarda o caminho para a variável
if ! caminho_fswebcam=$(command -v fswebcam); then
    echo "Erro: fswebcam não encontrado. Instale com:"
    echo "sudo apt install fswebcam"
    exit 1
fi

# Verifica se a câmera está disponível em /dev/video0
if [ ! -c /dev/video0 ]; then
    echo "Erro: câmera não encontrada em /dev/video0."
    exit 1
fi

# Cria o diretório para salvar as imagens, se não existir
mkdir -p "$HOME/imagens"

# Gera um nome de arquivo com timestamp para evitar sobrescritas
ts=$(date +%Y%m%d_%H%M%S)
arquivo="$HOME/imagens/foto_${ts}.jpg"

echo "Capturando imagem em $arquivo"

# Executa o comando fswebcam para capturar a imagem
if "$caminho_fswebcam" -d /dev/video0 -q -r 1280x720 --no-banner "$arquivo"; then
    echo "Captura finalizada"
else
    echo "Erro: falha ao capturar imagem."
    exit 1
fi
```

### Checkpoint

- [ ] O script `captura.sh` foi criado.
- [ ] O script tem permissão de execução.
- [ ] O script executa manualmente.
- [ ] Duas imagens foram criadas com nomes diferentes.

### Responda

1. Por que o script usa `date` no nome da imagem?
2. Por que usamos caminhos absolutos como `/home/g0/imagens`?
3. O script fica rodando continuamente ou termina depois de uma captura?

## Parte 3 - Serviço para captura simples

### O que vamos fazer

Vamos criar um serviço do `systemd` para executar o script `captura.sh`.

> Atenção: esta parte usa `sudo` e cria arquivo em `/etc/systemd/system`.

### Criar o arquivo do serviço

```bash
sudo nano /etc/systemd/system/captura.service
```

Digite o conteúdo abaixo. Troque `g0` pelo usuário do seu grupo, se necessário.

```ini
[Unit]
Description=Captura de imagem com script do usuario g0
After=network.target

[Service]
Type=oneshot
User=g0
WorkingDirectory=/home/g0
ExecStart=/home/g0/captura.sh

[Install]
WantedBy=multi-user.target
```

Salve e saia do editor.

### Recarregar e testar

Sempre que criar ou modificar arquivos `.service` ou `.timer`, execute:

```bash
sudo systemctl daemon-reload
```

Inicie o serviço:

```bash
sudo systemctl start captura.service
```

Verifique o estado:

```bash
systemctl status captura.service
```

Veja se uma nova imagem foi criada:

```bash
ls -lh imagens
```

Veja os logs:

```bash
journalctl -u captura.service -n 20
```

Pare o serviço:

```bash
sudo systemctl stop captura.service
```

### Checkpoint

- [ ] Criei `captura.service`.
- [ ] Executei `daemon-reload`.
- [ ] Iniciei o serviço.
- [ ] O status não mostrou erro.
- [ ] Uma nova imagem apareceu na pasta.

### Responda

1. Qual campo indica o usuário que executa o serviço?
2. Qual campo indica o script chamado pelo serviço?
3. O que significa `Type=oneshot`?

## Parte 4 - Timer para repetir a captura

### O que vamos fazer

Vamos criar um timer para chamar `captura.service` automaticamente em intervalos definidos.

### Criar o arquivo do timer

```bash
sudo nano /etc/systemd/system/captura.timer
```

Digite:

```ini
[Unit]
Description=Timer para executar captura de imagem periodicamente

[Timer]
OnBootSec=60s
OnUnitActiveSec=1min
Unit=captura.service

[Install]
WantedBy=timers.target
```

Salve e saia do editor.

### Ativar o timer

```bash
sudo systemctl daemon-reload
```

```bash
sudo systemctl enable --now captura.timer
```

Verifique:

```bash
systemctl status captura.timer
```

Liste os timers ativos:

```bash
systemctl list-timers
```

Aguarde cerca de 2 minutos e confira:

```bash
ls -lh imagens
```

Consulte os logs do serviço:

```bash
journalctl -u captura.service -n 30
```

### Gerando uma planilha das capturas

Para gerar uma planilha com os horários das capturas, adicione o seguinte trecho de código ao final do script `captura.sh`:

```bash
# Salva em um csv o caminho da imagem e a data/hora da captura
csv="$HOME/imagens/capturas.csv"

# Verifica se o arquivo CSV existe, se não existir, cria e adiciona o cabeçalho
# Os cochetes são usados para evitar problemas com espaços em branco no nome do arquivo
if [ ! -f "$csv" ]; then
    echo "caminho,data_hora" > "$csv"
fi
echo "$arquivo,$(date +%Y-%m-%d_%H:%M:%S)" >> "$csv"
```
A opção `-f`, do comando `[`, verifica se o arquivo existe. Se não existir, o script cria o arquivo e adiciona um cabeçalho com os nomes das colunas. Em seguida, a linha `echo "$arquivo,$(date +%Y-%m-%d_%H:%M:%S)" >> "$csv"` adiciona uma nova linha ao arquivo CSV com o caminho da imagem e a data/hora da captura.

### Checkpoint

- [ ] Criei `captura.timer`.
- [ ] Executei `daemon-reload`.
- [ ] Ativei o timer com `enable --now`.
- [ ] O timer apareceu em `systemctl list-timers`.
- [ ] Novas imagens foram geradas automaticamente.

### Responda

1. O timer captura a imagem diretamente ou chama um serviço?
2. Qual linha do timer indica o serviço que será chamado?
3. Em qual arquivo está definido o intervalo de 1 minuto?

## Parte 5 - Parando o timer

### O que vamos fazer

Vamos parar e desabilitar o timer para interromper a execução automática.

### Comandos

```bash
sudo systemctl stop captura.timer
```

```bash
sudo systemctl disable captura.timer
```

Ou, em um único comando:

```bash
sudo systemctl disable --now captura.timer
```

Confira:

```bash
systemctl list-timers
```

### Checkpoint

- [ ] O timer foi parado.
- [ ] O timer foi desabilitado.
- [ ] Ele não aparece mais como timer ativo.

## Parte 6 - Comparação antes da coleta contínua

### O que já fizemos

Até aqui usamos este modelo:

```text
captura.sh -> captura.service -> captura.timer
```

Nesse modelo:

- o script faz uma captura e termina;
- o serviço executa o script;
- o timer chama o serviço periodicamente.

### Próximo modelo

Agora vamos criar uma coleta contínua:

```text
captura_continua.sh -> captura-continua.service
```

Nesse modelo:

- o script fica rodando;
- o intervalo fica dentro do script;
- não usamos timer.

### Responda

1. No primeiro modelo, quem define o intervalo?
2. No segundo modelo, quem define o intervalo?
3. Por que a coleta contínua não precisa de timer?

## Parte 7 - Script de captura contínua

### O que vamos fazer

Vamos criar um script que fica capturando imagens continuamente, com pausa de 15 segundos entre capturas.

### Criar o script

```bash
nano captura_continua.sh
```

Digite o conteúdo abaixo. Troque `g0` pelo usuário do seu grupo, se necessário.

```bash
#!/usr/bin/env bash

# Verifica se o fswebcam está instalado e guarda o caminho para a variável
if ! caminho_fswebcam=$(command -v fswebcam); then
    echo "Erro: fswebcam não encontrado. Instale com:"
    echo "sudo apt install fswebcam"
    exit 1
fi

# Verifica se a câmera está disponível em /dev/video0
if [ ! -c /dev/video0 ]; then
    echo "Erro: câmera não encontrada em /dev/video0."
    exit 1
fi

mkdir -p "$HOME/imagens_continuas"

while true; do
    ts=$(date +%Y%m%d_%H%M%S)
    arquivo="$HOME/imagens_continuas/foto_${ts}.jpg"

    echo "Capturando imagem em $arquivo"
    if "$caminho_fswebcam" -d /dev/video0 -q -r 1280x720 --no-banner "$arquivo"; then
	echo "Captura realizada no arquivo $arquivo"
    else
	echo "Erro: falha no fswebcam"
	exit 1
    fi

    # Salva em um csv o caminho da imagem e a data/hora da captura
    csv="$HOME/imagens_continuas/capturas.csv"

    # Verifica se o arquivo CSV existe, se não existir, cria e adiciona o cabeçalho
    # Os cochetes são usados para evitar problemas com espaços em branco no nome do arquivo
    if [ ! -f "$csv" ]; then
        echo "caminho,data_hora" > "$csv"
    fi
    echo "$arquivo,$(date +%Y-%m-%d_%H:%M:%S)" >> "$csv"

    sleep 15

done

```

Salve e saia do editor.

### Testar manualmente

```bash
chmod +x captura_continua.sh
```

```bash
./captura_continua.sh
```

Aguarde duas ou três capturas.

Interrompa com:

```text
Ctrl+C
```

Confira:

```bash
ls -lh imagens_continuas
```

### Checkpoint

- [ ] Criei `captura_continua.sh`.
- [ ] O script executou manualmente.
- [ ] Precisei interromper com `Ctrl+C`.
- [ ] Várias imagens foram criadas.

### Responda

1. Por que esse script não termina sozinho?
2. Qual comando define o intervalo entre capturas?
3. Qual é o intervalo usado neste exemplo?

## Parte 8 - Serviço contínuo

### O que vamos fazer

Vamos criar um serviço para iniciar o script contínuo.

### Criar o serviço

```bash
sudo nano /etc/systemd/system/captura-continua.service
```

Digite:

```ini
[Unit]
Description=Captura continua de imagens com fswebcam
After=network.target

[Service]
Type=simple
User=g0
WorkingDirectory=/home/g0
ExecStart=/home/g0/captura_continua.sh
Restart=always

[Install]
WantedBy=multi-user.target
```

Salve e saia do editor.

### Iniciar e verificar

```bash
sudo systemctl daemon-reload
```

```bash
sudo systemctl start captura-continua.service
```

```bash
systemctl status captura-continua.service
```

Aguarde cerca de 1 minuto.

```bash
ls -lh imagens_continuas
```

Veja os logs:

```bash
journalctl -u captura-continua.service -n 30
```

Pare o serviço:

```bash
sudo systemctl stop captura-continua.service
```

Confira:

```bash
systemctl status captura-continua.service
```

### Checkpoint

- [ ] Criei `captura-continua.service`.
- [ ] Iniciei o serviço contínuo.
- [ ] O serviço ficou ativo.
- [ ] Novas imagens apareceram em `imagens_continuas`.
- [ ] Parei o serviço.

### Responda

1. Por que esse serviço usa `Type=simple`?
2. Para que serve `Restart=always`?
3. Por que não usamos `.timer` neste modelo?

## Parte 9 - Diagnóstico

### Quando algo falhar

Use estes comandos:

```bash
systemctl status captura.service
```

```bash
systemctl status captura.timer
```

```bash
systemctl status captura-continua.service
```

```bash
journalctl -u captura.service -n 30
```

```bash
journalctl -u captura-continua.service -n 30
```

```bash
ls -lh imagens
```

```bash
ls -lh imagens_continuas
```

### Checklist de erro

- [ ] O script roda manualmente?
- [ ] O script tem permissão de execução?
- [ ] O caminho em `ExecStart` está correto?
- [ ] O usuário em `User=` está correto?
- [ ] Executei `sudo systemctl daemon-reload` depois de modificar o arquivo?
- [ ] O log mostra erro de câmera, caminho ou permissão?

## Parte 10 - Comparação final

Preencha a tabela:

| Situação | Melhor modelo |
|---|---|
| Capturar uma imagem a cada 15 minutos | |
| Capturar uma imagem a cada 15 segundos | |
| Executar uma tarefa que termina rapidamente | |
| Manter um processo rodando continuamente | |
| Verificar timers ativos | |
| Investigar erro de execução | |

Responda:

1. Qual é a função do script?
2. Qual é a função do serviço?
3. Qual é a função do timer?
4. Em qual modelo o intervalo fica no `.timer`?
5. Em qual modelo o intervalo fica dentro do script?
6. Onde você deve olhar quando a automação falha?

## Encerramento

Ao final desta atividade, você deve conseguir explicar:

- por que testar manualmente antes de automatizar;
- a diferença entre script, serviço e timer;
- como criar e testar um serviço `oneshot`;
- como criar e verificar um timer;
- como usar `journalctl` para investigar problemas;
- como criar uma coleta contínua com apenas um serviço;
- qual modelo é mais adequado para cada tipo de intervalo de captura.

