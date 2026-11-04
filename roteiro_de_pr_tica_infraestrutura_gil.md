# Roteiro Passo a Passo: Infraestrutura Ágil (CI/CD)

Este é um guia estruturado para a execução do trabalho prático. Siga cada etapa com atenção e **faça pausas para tirar os prints** nos momentos indicados para compor o seu relatório final.

## Etapa 1: Preparação do Ambiente
1. Crie uma conta no [GitLab](https://gitlab.com/users/).
2. Crie uma conta no [Docker Hub](https://hub.docker.com/).
3. Instale o Git no seu computador através do site [oficial](https://git-scm.com/downloads).

> 📸 **PAUSE PARA PRINT:** Tire um print das telas de perfil do GitLab, do Docker Hub e do seu terminal comprovando que o Git está instalado (usando o comando `git --version`).

## Etapa 2: Organização dos Arquivos
1. Descompacte o arquivo "devops-master" em uma pasta local no seu computador.
2. Verifique se os arquivos necessários estão presentes na pasta (`.gitlab-ci.yml`, `Dockerfile`, scripts `.sh` e arquivos `.py`).

> 📸 **PAUSE PARA PRINT:** Tire um print do seu explorador de arquivos (Windows Explorer, Finder, etc.) mostrando a pasta do projeto com todos os arquivos descompactados e listados.

## Etapa 3: Configuração do Repositório Local (Git)
1. Abra o seu terminal (Git Bash, CMD ou PowerShell).
2. Navegue até a pasta onde você descompactou os arquivos (exemplo: `cd caminho/para/a/pasta`).
3. Inicialize o repositório local com o comando: 
   ```bash
   git init
   ```
4. *(Opcional, mas recomendado)* Mude o nome da branch principal para `main`:
   ```bash
   git branch -M main
   ```

> 📸 **PAUSE PARA PRINT:** Tire um print do terminal mostrando a execução do comando `git init` dentro da pasta correta.

## Etapa 4: Conectando com o GitLab e Enviando os Arquivos (Push)
1. No GitLab, crie um novo projeto/repositório em branco chamado **"UNOPAR_CI_CD"**.
2. No seu terminal, vincule o repositório local ao remoto do GitLab:
   ```bash
   git remote add origin https://gitlab.com/seu-usuario/unopar_ci_cd.git
   ```
   *(Lembre-se de substituir "seu-usuario" pelo seu nome de usuário real do GitLab)*
3. Adicione todos os arquivos da pasta para o envio:
   ```bash
   git add .
   ```
4. Crie o commit inicial salvando as alterações:
   ```bash
   git commit -m "Initial commit"
   ```
5. Envie os arquivos para o servidor do GitLab:
   ```bash
   git push -u origin main
   ```

> 📸 **PAUSE PARA PRINT:** Tire **dois** prints nesta etapa: 
> 1. Um do terminal mostrando que o comando `git push` foi concluído com sucesso e transferiu os arquivos.
> 2. Outro da tela principal do seu repositório no GitLab mostrando que os arquivos já aparecem carregados lá na web.

## Etapa 5: Monitoramento do Pipeline (Integração Contínua)
1. No site do GitLab, abra o seu repositório "UNOPAR_CI_CD" e acesse no menu lateral a aba **"Build"** > **"Pipelines"** (ou "CI/CD" > "Pipelines", dependendo da versão visual do GitLab).
2. O arquivo `.gitlab-ci.yml` que você enviou iniciará o pipeline automaticamente, definindo a ordem de execução dos "jobs" e utilizando a imagem do Docker Hub.
3. Acompanhe a execução do script e a construção da aplicação.

> 📸 **PAUSE PARA PRINT:** Tire prints da tela do pipeline em execução no GitLab, mostrando os "jobs". Capture as telas para comprovar o cenário de **sucesso** (job aprovado, geralmente com um check verde) e simule ou registre também um cenário de **falha** (job reprovado/vermelho, caso consiga forçar um erro no script para demonstrar a notificação de falha).

## Etapa 6: Elaboração do Relatório Final
1. Reúna todos os prints capturados nas etapas 1 a 5.
2. Crie um documento (Word, Google Docs, etc.) com a seguinte estrutura obrigatória requerida pelo roteiro:
   - **Introdução**
   - **Métodos**
   - **Resultados**
   - **Conclusão**
3. Insira os seus prints ao longo das seções de *Métodos* e *Resultados* para documentar o seu passo a passo, descrevendo brevemente o que está acontecendo em cada imagem para provar que você compreendeu o funcionamento do pipeline de entrega contínua.