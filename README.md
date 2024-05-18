# CRUD usando Django e GraphQL

## Instalação

***1. Instale as dependências do projeto:***
   `code`
   pip install -r requirements.txt

## Execução:

***1. Execute o servidor de desenvolvimento:***
   python manage.py runserver

***3. Abra o navegador e vá para:***
   http://localhost:8000/graphql

## Consultas GraphQL

### Consulta de todos os livros

***Todos os livros***
   query {
      allBooks {
         id
         title
         author
         yearPublished
         review
      }
   }

***Livro por ID***
   query {
      book(bookId: 2) {
         id
         title
         author
      }
   }
