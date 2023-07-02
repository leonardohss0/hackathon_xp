# Projeto Hackathon - OrganizAI 
keywords: Inteligência Artificial, Finanças, 
### Este projeto foi desenvolvido como parte de um hackathon do setor financeiro, com o objetivo de criar uma plataforma web completa para ajudar os usuários a economizarem dinheiro, gerenciarem suas finanças e melhorarem seus investimentos. A plataforma utiliza tecnologias como Dash, Plotly e Python, além de integração com o ChatGPT API para fornecer um planejamento financeiro totalmente personalizado para cada usuário.


## Funcionalidades
* **Chatbot de coleta de informações**: A plataforma inclui um chatbot que coleta informações financeiras dos usuários, como renda mensal, gastos, objetivos financeiros, entre outros.
* **Análise dos dados coletados**: Os dados coletados pelo chatbot são enviados para a API do ChatGPT, onde são analisados para criar um perfil financeiro personalizado para cada usuário.
* **Planejamento financeiro personalizado**: Com base nas informações coletadas e na análise realizada pela API do ChatGPT, a plataforma gera um planejamento financeiro completo e personalizado para cada usuário. Isso inclui sugestões de orçamento, estratégias de economia, investimentos recomendados, entre outros.
* **Interface de usuário interativa**: A plataforma oferece uma interface de usuário intuitiva e interativa, onde os usuários podem visualizar seu planejamento financeiro, ajustar as configurações, visualizar gráficos e receber recomendações personalizadas.


## Estrutura do projeto

A estrutura do projeto é organizada da seguinte maneira:

├── assets: Esta pasta contém recursos estáticos, como imagens, folhas de estilo CSS, arquivos de fonte, etc.
├── pages: Aqui estão as páginas da plataforma, cada página é responsável por um aspecto específico, como a página inicial, página de configurações, página de visualização do planejamento financeiro, etc.
├── resources: Essa pasta contém recursos adicionais utilizados pelo projeto, como arquivos de dados ou modelos pré-treinados.
├── utils: Esta pasta contém utilitários e módulos auxiliares para o projeto.
├── .gitignore: Arquivo que especifica quais arquivos e pastas devem ser ignorados pelo controle de versão Git.
├── LICENSE: Arquivo de licença que especifica os termos e condições para o uso deste projeto.
├── README.md: Este arquivo que você está lendo agora, contendo informações detalhadas sobre o projeto.
├── app.py: Arquivo principal do aplicativo Dash, que inicia o servidor e define as rotas e layouts das páginas.
├── create_database.py: Script em Python para criar o banco de dados SQLite que armazena os dados dos usuários.
├── data.sqlite: Arquivo do banco de dados SQLite que armazena os dados dos usuários.
├── index.py: Arquivo de entrada do aplicativo Dash, importa e inicia o arquivo app.py.
├── requirements.txt: Arquivo que lista todas as dependências do projeto, permitindo uma fácil instalação.


## Configuração e Instalação
1. Certifique-se de ter o Python 3 instalado corretamente em sua máquina.
2. Clone este repositório para o seu ambiente local.
3. No terminal, navegue até a pasta raiz do projeto.
4. Crie um ambiente virtual (opcional) para isolar as dependências do projeto. Você pode usar o seguinte comando:

`python -m venv myenv`

5. Ative o ambiente virtual. Dependendo do seu sistema operacional, use um dos comandos a seguir:
* No Windows: `myenv\Scripts\activate`
* No Linux/macOS: `source myenv/bin/activate`

6. Instale as dependências do projeto usando o arquivo requirements.txt. Execute o seguinte comando:
`pip install -r requirements.txt
   
Isso instalará todas as bibliotecas necessárias para executar o projeto.

7. Antes de executar o aplicativo, é necessário criar o banco de dados SQLite. No terminal, execute o seguinte comando:
`python create_database.py`

Isso criará o arquivo data.sqlite que será usado para armazenar os dados dos usuários.

## Executando o aplicativo
Após concluir a configuração e instalação, você pode iniciar o aplicativo. No terminal, navegue até a pasta raiz do projeto e execute o seguinte comando:
`python index.py`

Isso iniciará o servidor e o aplicativo estará disponível no endereço http://localhost:8050.

Acesse o endereço no seu navegador para utilizar o OrganizAI.

## Contribuição
Se você deseja contribuir para este projeto, fique à vontade para enviar pull requests ou relatar problemas na seção de issues. Sua contribuição é muito bem-vinda!

## Licença
Este projeto está licenciado nos termos da licença MIT.
