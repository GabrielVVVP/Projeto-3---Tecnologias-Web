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
<br></br>Link do projeto: https://warm-everglades-39735.herokuapp.com/

### Problema
Diversos pacientes com doenças incomuns, raras ou não identificadas, muitas vezes dependem de sorte para receber o diagnóstico e tratamento correto, o que depende de encontrar um médico que tenha conhecimento na área, ou ao mesmo encontrar um médico que conheça algum outro e que o possa recomendar, algo que muitas vezes pode levar a tratamentos sem resultados positivos, acarretando em consequências, ou em casos mais graves, até na morte. 

### Objetivo
O seu principal objetivo é gerar um diagnóstico à partir de inteligência artificial para um usuário paciente a partir de um conjunto de sintomas como tosse ou dores abdominais, e deixar que a plataforma recomende médicos (também cadastrados) à partir das suas especializações individuais e dos resultados deste diagnóstico. Desta forma, os médicos ideais com maiores conhecimentos nas doenças de maior probabilidade mencionadas no resultado do diagnóstico podem ser recomendados diretamente ao paciente e aumentar as chances de um tratamento bem sucedido. Os pacientes apenas precisam selecionar o que estão sentindo (sintomas) e colocar um valor de gravidade (0-10) sendo 0 muito leve e 10 gravíssimo. A plataforma também evoluiu para possibilitar que os médicos também marquem consultas com os seus pacientes, utilizando um calendário interativo.

### Arquitetura
Já que o projeto consiste em diversas partes comunicando entre si, a definição de um diagrama demonstrando como elas se comunicam facilita bastante o entendimento, o funcionamento e os objetivos do projeto.

<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/120945301-e75c7d80-c70e-11eb-887b-50835f5509c1.png" width="600" height="500"></img>
</p>

## Manual da User Interface
Para facilitar a navegação na plataforma, este manual de utilização foi construído.

### Página Principal
A partir da página principal ou da página sobre, o usuário poderá criar uma conta na plataforma, caso seja um médico, deverá selecionar Criar Conta e depois Médico, e caso seja um Paciente, deverá selecionar Criar Conta e depois Paciente e preencher o Cadastro.

<p align="center">
  <img src="https://user-images.githubusercontent.com/60860861/120946953-a2d3e080-c714-11eb-8d86-ef2148e30a67.png" width="800" height="500"></img>
</p>

Após se cadastrar, o usuário é redirecionado para o Menu do Médico ou do Paciente, de acordo com o tipo de conta. Caso retorne posteriormente, para ingressar novamente na conta, basta selecionar login, e utilizar os mesmos dados de cadastro, de login e senha.

### Paciente
Após entrar na conta via Criar Conta ou Login, o usuário do tipo Paciente é redirecionado para o seu menu principal.

#### Menu
Na página principal do Paciente, cinco opções de páginas podem ser selecionadas.
<br></br>Elas estão organizadas na ordem em que a plataforma foi projetada:

<p align="center">
  Criar/Editar Instâncias -> Diagnóstico Inteligente -> Histórico de Diagnósticos (Opcional) -> Médicos Especialistas -> Calendário
</p>

Assim, a ordem de eventos é:
1. Na página de Adicionar Sintomas: Criar uma instância com três sintomas iniciais e suas gravidades de (0-10), e adicionar mais sintomas, caso necessário;
2. Na página de Diagnóstico Inteligente: Selecionar a instância na qual se deseja realizar o diagnóstico e verificar os resultados;
3. Na página de Histórico de Diagnóstico: Caso queira verificar novamente o resultado do diagnóstico obtido. Caso contrário ir para a próxima página/etapa;
4. Na página de Médicos Especialistas: Ao selecionar um diagnóstico recebido, a plataforma irá recomendar um médico baseado na sua especialidade, e o paciente poderá mandar uma requisição de consulta para que o médico selecionado possa lhe avaliar. Após o médico receber esta requisição e aceitar, basta o usuário aguardar a resposta do médico via email;
5. Na página de Calendário: Nesta ferramenta útil, o usuário poderá sempre verificar as datas e características de consultas e cirurgias dos médicos recomendados pela plataforma.

### Médico
Após entrar na conta via Criar Conta ou Login, o usuário do tipo Médico é redirecionado para o seu menu principal.

#### Menu
Na página principal do Médico, cinco opções de páginas podem ser selecionadas.
<br></br>Elas estão organizadas na ordem em que a plataforma foi projetada:

<p align="center">
  Aceitar/Recusar Requisições -> Histórico de Instâncias -> Histórico de Diagnósticos -> Marcar Eventos -> Calendário
</p>

Assim, a ordem de eventos é:
1. Na página de Aceitar/Recusar Requisições: Ver as requisições de acompanhamento médico em aberto feita pelos pacientes e pode aceitar ou recusá-las. Após aceitar a requisição, todos os pacientes aceitos aparecem na lista de pacientes; 
2. Na página de Histórico de Instâncias: Escolher qualquer paciente aceito da lista de pacientes e verificar as suas instâncias (conjunto de sintomas);
3. Na página de Histórico de Diagnóstico: Escolher qualquer paciente aceito da lista de pacientes e verificar os seus diagnósticos e assim avaliar o seu caso;
4. Na página de Marcar Eventos: A partir da análise dos sintomas e diagnósticos, o médico pode marcar um evento, como uma consulta com o paciente para avaliar o seu caso;
5. Na página de Calendário: Todos as consultas ou cirurgias marcados pelo médico na plataforma estarão mostrados neste calendário interativo, para facilitar a organização e evitar conflitos de horários.
