# CRUD usando Django e GraphQL

## Instalação

***1. Instale as dependências do projeto:***
~~~cmd
python -m venv venv
.venv\Scripts\activate
pip install -r requirements.txt
~~~

## Execução:

***1. Executar as migrações***
~~~cmd
python manage.py makemigrations
python manage.py migrate
~~~

***2. Popular o banco de dados:***
~~~cmd
python manage.py loaddata data.json
~~~

***3. Execute o servidor de desenvolvimento:***
~~~cmd
python manage.py runserver
~~~

***3. Abra o navegador e vá para:***
  [Teste](http://localhost:8000/graphql)

## Consultas GraphQL

***Todos os livros***
~~~  
   query {
      allBooks {
         id
         title
         author
         yearPublished
         review
      }
   }
~~~

***Livro por ID***
~~~  
   query {
      book(bookId: 2) {
         id
         title
         author
      }
   }
~~~

## Criar Livro
~~~
   mutation createMutation {
      createBook(bookData: {title: "Things Apart", author: "Chinua Achebe", yearPublished: "1985", review: 3}) {
         book {
            title,
            author,
            yearPublished,
            review
         }
      }
   }
~~~

## Atualizar Livro
~~~
   mutation updateMutation {
      updateBook(bookData: {id: 3, title: "Things Fall Apart", author: "Chinua Achebe", yearPublished: "1958", review: 5}) {
         book {
            title,
            author,
            yearPublished,
            review
         }
      }
   }
~~~

## Deletar livro
~~~
   mutation deleteMutation{
      deleteBook(id: 3) {
         book {
            id
         } 
      }
   }
~~~