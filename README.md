# Metrologia por imagem

Materiais didáticos para atividades práticas de metrologia por imagem com sistemas Linux embarcados, acesso remoto, captura de imagens e automação de rotinas experimentais.

O repositório está organizado em módulos progressivos. O primeiro módulo apresenta o uso do terminal Linux, SSH e scripts Bash. O segundo módulo usa essa base para automatizar a captura de imagens com `systemd`.

## Objetivos

- Introduzir o acesso remoto a Orange Pi / Raspberry Pi por SSH.
- Praticar comandos básicos de Linux no terminal.
- Criar e executar scripts Bash simples.
- Testar captura de imagens com webcam usando `fswebcam`.
- Automatizar rotinas de captura com serviços e timers do `systemd`.
- Relacionar automação, organização de dados e repetibilidade em experimentos de metrologia por imagem.

## Estrutura do repositório

| Caminho | Descrição |
|---|---|
| `001_apresentacao_dia1.pptx` | Slides do primeiro encontro. |
| `001_roteiro_alunos.md` | Roteiro prático do módulo 1 para os alunos. |
| `001_material_de_apoio/` | Apostila em LaTeX e PDF do módulo 1, além de imagem de apoio. |
| `002_apresentacao_dia2.pptx` | Slides do segundo encontro. |
| `002_roteiro_alunos.md` | Roteiro prático do módulo 2 para os alunos. |
| `002_material_de_apoio/` | Apostila em LaTeX e PDF do módulo 2. |
| `002_sugestao_slides_systemd.txt` | Texto de apoio/sugestão para elaboração dos slides sobre `systemd`. |
| `pipeline.odg` | Diagrama do fluxo de trabalho. |
| `Planejamento.docx` | Documento de planejamento da atividade/disciplina. |
| `Lista de participantes externos/` | Planilha de participantes externos. |

## Módulos

### Módulo 1 - SSH, Linux, terminal e Bash

Arquivos principais:

- `001_roteiro_alunos.md`
- `001_apresentacao_dia1.pptx`
- `001_material_de_apoio/apostila.pdf`
- `001_material_de_apoio/apostila.tex`

Conteúdos abordados:

- acesso remoto por SSH;
- interpretação do prompt do terminal;
- navegação no sistema de arquivos com `pwd`, `ls` e `cd`;
- criação, cópia, movimentação e remoção de arquivos;
- redirecionamento com `>` e `>>`;
- permissões de arquivos;
- comandos internos e externos do Bash;
- variáveis de ambiente e `PATH`;
- criação de scripts Bash;
- captura de imagem com `fswebcam`.

### Módulo 2 - Automação de captura com systemd

Arquivos principais:

- `002_roteiro_alunos.md`
- `002_apresentacao_dia2.pptx`
- `002_material_de_apoio/apostila.pdf`
- `002_material_de_apoio/apostila.tex`

Conteúdos abordados:

- teste manual de câmera antes da automação;
- criação de script de captura com `fswebcam`;
- criação de serviço `systemd` do tipo `oneshot`;
- criação de timer para repetição periódica;
- uso de `systemctl` para iniciar, parar, habilitar e verificar unidades;
- uso de `journalctl` para consultar logs;
- comparação entre `service + timer` e serviço contínuo;
- criação de script de coleta contínua com `while true` e `sleep`.

## Como usar os materiais

Para cada módulo, recomenda-se seguir esta ordem:

1. Apresentar os conceitos com os slides (`.pptx`).
2. Usar a apostila em PDF como material de apoio.
3. Executar o roteiro dos alunos (`.md`) durante a prática.
4. Ao final, revisar as perguntas e checklists do roteiro.

Os roteiros foram escritos para uso em laboratório, com grupos acessando Orange Pi / Raspberry Pi por SSH e executando os comandos diretamente no dispositivo.

## Requisitos para as práticas

Para executar as atividades em laboratório, são necessários:

- Orange Pi, Raspberry Pi ou outro dispositivo Linux acessível por rede;
- usuário e senha para cada grupo;
- endereço IP do dispositivo;
- câmera reconhecida pelo Linux como `/dev/video0` ou similar;
- `fswebcam` instalado no dispositivo;
- acesso ao terminal local, como PowerShell, CMD, terminal Linux ou terminal macOS;
- permissões de `sudo` para as atividades com `systemd` no módulo 2.

Exemplo de instalação do `fswebcam` em distribuições baseadas em Debian:

```bash
sudo apt update
sudo apt install fswebcam
```

## Comandos centrais

Exemplo de acesso por SSH:

```bash
ssh usuario@endereco_ip
```

Exemplo de captura manual:

```bash
fswebcam -r 1280x720 imagens/teste.jpg
```

Exemplo de verificação de serviço:

```bash
systemctl status captura.service
```

Exemplo de consulta aos logs:

```bash
journalctl -u captura.service -n 30
```

## Observações

- Os comandos dos roteiros usam nomes de usuário como `g0` apenas como exemplo. Substitua pelo usuário correto de cada grupo.
- Em arquivos do `systemd`, prefira caminhos absolutos, como `/home/g0/captura.sh`.
- Sempre teste scripts manualmente antes de transformá-los em serviços ou timers.
- Após criar ou alterar arquivos `.service` ou `.timer`, execute `sudo systemctl daemon-reload`.
- Serviços contínuos devem ser parados ao final da prática para evitar capturas indefinidas.

## Autor

Material organizado por Prof. Felipe Walter Dafico Pfrimer para atividades de metrologia por imagem.
