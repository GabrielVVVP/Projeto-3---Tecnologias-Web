# Tecnologias Web - Projeto 3 - SmartDoctor

## Integrante
- Gabriel Vieira de Vasconcelos Vilaça Pinto

## Introdução
Este repositório é o Projeto 3 (Final) da Matéria de Tecnologias Web do curso de Engenharia da Computação do Insper. 

## Restrições
Conforme listadas pelo professor, o projeto possui as seguintes restrições:

- O uso de alguma tecnologia web deve ser central para o projeto;
- O resultado do projeto deve ser público (o código fonte não precisa ser público):
- Se for uma página ou serviço, você deve fazer o deploy;
- Se for um tutorial, ele deve estar disponível em algum endereço público (ex: Medium, Dev.to, GitHub Pages);
- Se for um web crawler/scrapper, o resultado da análise deve ser público (ex: escrevendo um post com o resultado, ou publicando um Jupyter Notebook no GitHub).
- Você deve planejar a arquitetura do projeto e adicionar uma imagem com essa arquitetura no seu repositório do GitHub (pode escanear um diagrama desenhado à mão, se preferir). Não é obrigatório seguir nenhum formalismo, mas você deve representar em um diagrama quais são os componentes principais do seu projeto e como eles se comunicam entre si;
- Você deve definir um cronograma, que deve ser apresentado no README do seu repositório. Sugestão: crie uma tasklist no README e vá marcando as tarefas conforme forem cumpridas (https://docs.github.com/en/github/managing-your-work-on-github/about-task-lists). Importante: seu cronograma deve ter entregas bem definidas para cada semana. Elas podem (e devem?) ser atualizadas ao longo das sprints, mas é importante ter algum planejamento.

## Cronograma

Conforme definido nas restrições do projeto, o cronograma de Sprints semanais foi feito ao longo do período de 4 semanas, ou seja, totalizando 4 Sprints.

### Sprint 1 - Semana (16/05-22/05)

Tarefas para Realizar:
- [x] Determinação do Tema do Projeto
- [x] Benchmark de Platarformas Web com Diagnósticos Médicos por AI
- [x] Estudo de APIs de Diagnósticos Médicos por AI em plataformas como RapidAPI
- [x] Teste inicial da API para validar o seu funcionamento
- [x] Boilerplate do Projeto 

### Sprint 2 - Semana (23/05-29/05) 

Tarefas para Realizar:
- [x] Determinação da Arquitetura
- [x] Determinação do Escopo e Entregas
- [x] Desenvolvimento da Feature: Sistema Rudimentar de Sign In e Login (Email e Senha)
- [x] Desenvolvimento da Feature: Criação de Instâncias de Doenças (Conjunto de 3 sintomas com valores de gravidade (0-10) à partir de uma lista de sintomas)
- [x] Desenvolvimento da Feature: Criação de Diagnósticos Inteligentes (A partir de uma instância criada anteriormente, a EndlessMedical API é utilizada para realizar um diagnóstico e retorna um dicionário com as maiores probabilidades de ocorrência de doenças)
- [x] Visualização inicial dos resultados do diagnóstico em uma tabela. 
- [x] Organização dos fluxos de urls e Menus, tanto no header, quanto no menu interativo inferior, para facilitar a movimentação do usuário nas diversas páginas que compõem o projeto.
- [x]  Desenvolvimento da Feature: Histórico de Diagnósticos (Uma vez que a API é consumida a cada chamada de diagnóstico, esta tela armazena e mostra para o usuário os diagnósticos já realizados e os seus resultados, que estão armazenados no banco de dados)
- [x] Desenvolvimento da Feature: Recomendação de Médicos (A partir da escolha de um diagnóstico realizado, o sistema irá recomendar médicos que tenham a sua especialização equivalente a doença de maior probabilidade deste diagnóstico)
- [x] Implementação de um calendário interativo com eventos  

### Sprint 3 - Semana (30/05-05/06)

Tarefas para Realizar:
 - [x] Reorganização do fluxo de menus. Dependendo do tipo de usuário cadastrado (Paciente ou Médico), os menus, as interfaces e as funcionalidades são diferentes.
 - [x] Desenvolvimento da Feature: Indicações e Referências. Assim que o paciente seleciona um médico indicado para tratar de uma doença mencionada em um diagnóstico, uma mensagem é enviada para a página de requisições do Médico cadastrado na plataforma. O médico pode selecionar aceitar a requisição do paciente ou não, e o paciente não pode enviar mais requisições para o mesmo médico (evitando spam) enquanto o médico não selecionar aceitar ou recusar a requisição. Após aceitar, o médico terá acesso ao histórico de instâncias e diagnósticos deste paciente.
- [x] Desenvolvimento da Feature: Visualização de Instâncias e Diagnósticos.  Dos pacientes aceitos anteriormente (Mesmo modelo de visualização do paciente, exceto que o Médico pode visualizar de qualquer paciente atribuído a ele).
- [x] Desenvolvimento da Feature: Criação de Eventos. Um médico pode marcar um evento (consulta ou cirurgia) com um paciente selecionado e adicionar informações a este evento.
- [x] Desenvolvimento da Feature: Calendário Interativo.  O médico tem acesso ao calendário listando todas os eventos marcados por ele (para todos seus pacientes), e o paciente tem acesso ao calendário listando todos os eventos marcados pelos médicos atribuídos a eles (para todos os médicos atribuídos a eles via a referência). 
- [x] Desenvolvimento da Feature: Adicionar e Deletar Sintomas, Deletar e Editar Instâncias, e Editar Dados de Cadastro. A funcionalidade Create do CRUD foi adicionada permitindo adicionar mais sintomas a uma instância. A funcionalidade Delete do CRUD foi criada para permitir os pacientes deletarem sintomas ou instâncias antigas, e os seus diagnósticos atribuídos (Apenas o paciente tem acesso a criar, editar e deletar sintomas, instâncias e diagnósticos, os médicos podem apenas ler os resultados). Já a funcionalidade Update do CRUD foi criada para permitir editar estas instâncias e seus sintomas, e os dados gerais de cadastro (nome, idade, sexo, profissão, especialidade, email, senha e etc) podem ser modificados em qualquer página.    
- [x] Teste geral de funcionamento da plataforma 
- [x] Deploy no Heroku

### Sprint 4 (Final) - Semana (06/06-12/06)

Tarefas para Realizar:
- [x] Desenvolvimento de Feature: Avisos e Alertas. Agora o usuário irá receber avisos e alertas mostrando quando não preencheram os campos de Login, Sign In, e alteração de dados e senha, para que tenha Feedback caso não tenham feito algo correto. As mensagens de erro são personalizadas de acordo com o erro, para induzir o usuário ao preenchimento correto dos formulários.
- [x] Polimento geral da plataforma
- [x] Deploy Final
- [x] Criação da Demo
- [x] Atualização do Readme   


## Projeto

O projeto se chama SmartDoctor e se trata de uma plataforma Web que realiza diagnósticos com inteligência artificial a partir da EndlessMedical API, e recomenda médicos a partir destes diagnósticos. Os médicos recomendados podem ver o histórico dos pacientes e marcar consultas e cirurgias. O projeto está hospedado na plataforma Heroku.
<br></br>
Logo do Smart Doctor:

<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/122309837-6eff7480-cee5-11eb-8a75-3107dd5e4413.jpg" width="300" height="300"></img>
</p>

<br></br>Link do projeto: https://warm-everglades-39735.herokuapp.com/
<br></br>A logo do projeto foi feita na plataforma: https://freelogodesign.org
<br></br>O template do projeto obtido no site: https://colorlib.com/

### Problema
Diversos pacientes com doenças incomuns, raras ou não identificadas, muitas vezes dependem de sorte para receber o diagnóstico e tratamento correto, o que depende de encontrar um médico que tenha conhecimento na área, ou ao mesmo encontrar um médico que conheça algum outro e que o possa recomendar, algo que muitas vezes pode levar a tratamentos sem resultados positivos, acarretando em consequências, ou em casos mais graves, até na morte. 

### Objetivo
O seu principal objetivo é gerar um diagnóstico à partir de inteligência artificial para um usuário paciente a partir de um conjunto de sintomas como tosse ou dores abdominais, e deixar que a plataforma recomende médicos (também cadastrados) à partir das suas especializações individuais e dos resultados deste diagnóstico. Desta forma, os médicos ideais com maiores conhecimentos nas doenças de maior probabilidade mencionadas no resultado do diagnóstico podem ser recomendados diretamente ao paciente e aumentar as chances de um tratamento bem sucedido. Os pacientes apenas precisam selecionar o que estão sentindo (sintomas) e colocar um valor de gravidade (0-10) sendo 0 muito leve e 10 gravíssimo. A plataforma também evoluiu para possibilitar que os médicos também marquem consultas com os seus pacientes, utilizando um calendário interativo.

### Arquitetura
Já que o projeto consiste em diversas partes comunicando entre si, a definição de um diagrama demonstrando como elas se comunicam facilita bastante o entendimento, o funcionamento e os objetivos do projeto.

<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/120945301-e75c7d80-c70e-11eb-887b-50835f5509c1.png" width="600" height="500"></img>
</p>

A comunicação entre as duas partes de Médico e Paciente são dadas da seguinte maneira:
1. O Paciente envia uma requisição para um Médico;
2. O Médico aceita a Requisição;
3. O dados de Instâncias e Diagnósticos do Paciente agora estão disponíveis para este Médico;
4. Qualquer consulta ou cirurgia marcada por este Médico para este Paciente irá aparecer tanto no Calendário do Médico, quanto no Calendário do Paciente.

## Manual da User Interface
Para facilitar a navegação na plataforma, este manual de utilização foi construído.

### Página Principal
A partir da página principal ou da página sobre, o usuário poderá criar uma conta na plataforma, caso seja um médico, deverá selecionar Criar Conta e depois Médico, e caso seja um Paciente, deverá selecionar Criar Conta e depois Paciente e preencher o Cadastro.

<br></br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/120946953-a2d3e080-c714-11eb-8d86-ef2148e30a67.png" width="800" height="500"></img>
</p>

Após se cadastrar, o usuário é redirecionado para o Menu do Médico ou do Paciente, de acordo com o tipo de conta. Caso retorne posteriormente, para ingressar novamente na conta, basta selecionar Login, e utilizar os mesmos dados de cadastro, de email e senha.

### Paciente
Após entrar na conta via Criar Conta ou Login, o usuário do tipo Paciente é redirecionado para o seu menu principal.

#### Menu
Na página principal do Paciente, cinco opções de páginas podem ser selecionadas.

<br></br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/120949534-1f69bd80-c71b-11eb-8486-a89a3d7a887f.png" width="800" height="500"></img>
</p>

<br></br>Elas estão organizadas na ordem em que a plataforma foi projetada:

<p align="center">
  Adicionar Sintomas -> Diagnóstico Inteligente -> Histórico de Diagnósticos -> Médicos Especialistas -> Calendário de Consultas
</p>

Assim, a ordem de eventos é:
1. Na página de Adicionar Sintomas: Criar uma instância com três sintomas iniciais e suas gravidades de (0-10), e adicionar mais sintomas, caso necessário;
2. Na página de Diagnóstico Inteligente: Selecionar a instância na qual se deseja realizar o diagnóstico e verificar os resultados;
3. Na página de Histórico de Diagnóstico: Caso queira verificar novamente o resultado do diagnóstico obtido. Caso contrário ir para a próxima página/etapa;
4. Na página de Médicos Especialistas: Ao selecionar um diagnóstico recebido, a plataforma irá recomendar um médico baseado na sua especialidade, e o paciente poderá mandar uma requisição de consulta para que o médico selecionado possa lhe avaliar. Após o médico receber esta requisição e aceitar, basta o usuário aguardar a resposta do médico via email;
5. Na página de Calendário de Consultas: Nesta ferramenta útil, o usuário poderá sempre verificar as datas e características de consultas e cirurgias dos médicos recomendados pela plataforma.

#### Adicionar Sintomas

Iniciando o percurso seguido nas páginas dos pacientes, o primeiro passo a ser realizado é a criação de uma **Instância**, que representa um conjunto de sintomas dado pelo paciente. Os valores são arbitrários, já que dependem da gravidade percebida pelo próprio paciente, indo de uma escala de 0 até 10. Para isso, basta clicar no botão *Criar Instância*, e inicialmente, três valores de sintomas podem ser inseridos inicialmente. 
<br></br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/122310150-11b7f300-cee6-11eb-9911-85787aa93d80.png" width="800" height="500"></img>
</p>
<br></br>
Mais valores podem ser inseridos ou removidos posteriormente, clicando-se no botão de Editar Instância, que também permite apagar completamente a instância criada.
<br></br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/122310661-29dc4200-cee7-11eb-8e0b-0473d5e46bc3.png" width="1000" height="500"></img>
</p>
<br></br>

#### Diagnóstico Inteligente

Seguindo o percurso seguido nas páginas dos pacientes, o segundo passo a ser realizado é a criação de um **Diagnóstico**, que representa um conjunto de possíveis doenças a partir dos sintomas de uma dada instância.  Para realizar o diagnóstico, basta clicar no botão *Diagnóstico Inteligente*. Os resultados principais aparecerão na página.
<br></br>
<br></br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/122313206-2dbe9300-ceec-11eb-8630-97fa6ada2ee2.png" width="800" height="500"></img>
</p>
Para cada diagnóstico, apenas os 5 resultados com maiores probabilidades de ocorrência são apresentados.
<br></br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/122313311-5ba3d780-ceec-11eb-87a5-a5c75981ea6f.png" width="1000" height="500"></img>
</p>
<br></br>
Uma vez que o diagnóstico é feito para uma instância, o sistema bloqueará a dada instância para a realização do diagnóstico novamente, para evitar reutilização indevida da API EndlessMedical, já que os resultados para uma dada instância serão iguais, caso os sintomas não sejam alterados. Caso necessite rever os resultados do diagnóstico, ver na página Histórico de Diagnósticos.
<br></br>
<br></br>

<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/122313885-6dd24580-ceed-11eb-9faf-109de5cf563a.png" width="1000" height="500"></img>
</p>


#### Histórico de Diagnósticos

Seguindo o percurso seguido nas páginas dos pacientes, o terceiro passo, e também opcional, é verificar os **resultados dos diagnósticos** já realizados. Para isto, basta selecionar o diagnóstico desejado, e ele demonstrará os mesmos resultados de quando foi criado.
<br></br>
<br></br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/122313969-a2de9800-ceed-11eb-8775-9d86148cfa27.png" width="800" height="500"></img>
</p>
<br></br>

#### Médicos Especialistas

Seguindo o percurso seguido nas páginas dos pacientes, o quarto passo a ser realizado é a procura de **Médicos Especialistas** da doença de maior probabilidade de um dado diagnóstico. Primeiramente, basta selecionar um diagnóstico da lista dos já realizados.

<br></br>
<br></br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/122314338-61022180-ceee-11eb-92e3-aa38965eb8a9.png" width="800" height="600"></img>
</p>
Depois, selecionar um médico dentre os resultados, que são *especialistas na doença de maior probabilidade de um dado diagnóstico*.
<br></br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/122314390-79723c00-ceee-11eb-81f7-4222051e2c36.png" width="800" height="600"></img>
</p>
<br></br>
Por fim, clicar Marcar Consulta. O prompt de confirmação irá aparecer, e o Médico selecionado irá ser notificado da sua procura.
<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/122314535-c1915e80-ceee-11eb-82d5-a9a98877108c.png" width="800" height="600"></img>
</p>
<br></br>
Após isso é só esperar o contato do Médico!

#### Calendário de Consultas

Seguindo o percurso seguido nas páginas dos pacientes, o último passo a ser realizado, e que também é opcional, é a utilização do **Calendário de Consultas** da plataforma. Todos as consultas e/ou cirurgias marcadas por qualquer médico associado ao dado paciente irão aparecer no calendário interativo, facilitando a organização do paciente quando utilizar a plataforma.
<br></br>
<br></br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/122314935-7166cc00-ceef-11eb-8074-1a316f7b743c.png" width="1000" height="600"></img>
</p>
<br></br>

### Médico
Após entrar na conta via Criar Conta ou Login, o usuário do tipo Médico é redirecionado para o seu menu principal.

#### Menu
Na página principal do Médico, cinco opções de páginas podem ser selecionadas.

<br></br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/120949747-956e2480-c71b-11eb-810a-46b0ad799d9f.png" width="800" height="600"></img>
</p>

<br></br>Elas estão organizadas na ordem em que a plataforma foi projetada:

<p align="center">
  Requisições de Pacientes -> Histórico de Instâncias -> Histórico de Diagnósticos -> Marcar Consultas ou Cirurgias -> Calendário de Consultas
</p>

Assim, a ordem de eventos é:
1. Na página de Requisições de Pacientes: Ver as requisições de acompanhamento médico em aberto feita pelos pacientes e pode aceitar ou recusá-las. Após aceitar a requisição, todos os pacientes aceitos aparecem na lista de pacientes; 
2. Na página de Histórico de Instâncias: Escolher qualquer paciente aceito da lista de pacientes e verificar as suas instâncias (conjunto de sintomas);
3. Na página de Histórico de Diagnóstico: Escolher qualquer paciente aceito da lista de pacientes e verificar os seus diagnósticos e assim avaliar o seu caso;
4. Na página de Marcar Consultas ou Cirurgias: A partir da análise dos sintomas e diagnósticos, o médico pode marcar um evento, como uma consulta com o paciente para avaliar o seu caso;
5. Na página de Calendário de Consultas: Todos as consultas ou cirurgias marcados pelo médico na plataforma estarão mostrados neste calendário interativo, para facilitar a organização e evitar conflitos de horários.

#### Requisições de Pacientes

Iniciando o percurso seguido nas páginas dos médicos, o primeiro passo a ser realizado é a verificação das **Requisições dos Pacientes**, que representam os pedidos de contato dos pacientes. O médico tem a opção de aceitar ou de recusar as requisições. Caso aceite-as, elas aparecerão na lista de pacientes abaixo.
<br></br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/122319673-513b0b00-cef7-11eb-8e6a-5ca732533b0d.png" width="800" height="500"></img>
</p>
<br></br>

#### Histórico de Instâncias

Seguindo o percurso seguido nas páginas dos médicos, é a página de **Histórico de Instâncias**, na qual o médico pode escolher um paciente aceito pelas requisições, e verificar suas instâncias clicando em *Instâncias*.
<br></br>
<br></br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/122322998-c230f180-cefc-11eb-885c-5cd1606855dd.png" width="800" height="400"></img>
</p>
<br></br>


#### Histórico de Diagnósticos

Seguindo o percurso seguido nas páginas dos médicos, o terceiro passo, é verificar os **Históricos dos Diagnósticos** já realizados. Para isto, basta selecionar o paciente aceito pelas requisições, e o diagnóstico que deseja verificar, clicando em *Diagnósticos*.

<br></br>
<br></br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/122323051-da087580-cefc-11eb-9955-35e9e5a8ace9.png" width="800" height="400"></img>
</p>
<br></br>

#### Eventos

Seguindo o percurso seguido nas páginas dos pacientes, o quarto passo a ser realizado é a criação de **Eventos**, como consultas e cirurgias. Após verificar as instâncias e diagnósticos de um dado paciente, o médico poderá marcar os eventos pela plataforma. Inicialmente, precisará escolher um paciente, para marcar a consulta com ele. 

<br></br>
<br></br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/122323218-1f2ca780-cefd-11eb-83da-f7fe3990fb6a.png" width="800" height="400"></img>
</p>

#### Calendário de Consultas

Seguindo o percurso seguido nas páginas dos médicos, o último passo a ser realizado, e que também é opcional, é a utilização do **Calendário de Consultas** da plataforma. Todos as consultas e/ou cirurgias marcadas por você médico, aos seus pacientes irão aparecer no calendário interativo, facilitando a organização do médico quando utilizar a plataforma.
<br></br>
<br></br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/122323354-5ef38f00-cefd-11eb-83cf-a76f37e3d3ad.png" width="1000" height="600"></img>
</p>
<br></br>

