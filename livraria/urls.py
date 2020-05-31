from django.urls import path, include
from django.contrib.auth import views
from django.contrib import admin


#View
from .views import livraria_base, livraria_cadastrar_produto,livraria_cadastrar_editora
from .views import livraria_exibir_livros, livraria_detalhe_livro , livraria_editar_livro, livraria_deletar_livro

from .views import livraria_realizar_emprestimo, livraria_devolver_livro


app_name = 'livraria'

urlpatterns = [
    path('', livraria_base, name='home'),
    #Cadastros
    
    path('/livraria_cadastrar_produto/', livraria_cadastrar_produto, name='livrariacadastrarproduto'),

    path('/livraria_cadastrar_editora/', livraria_cadastrar_editora, name='livrariacadastrareditora'),

    #Exibição de livros cadastrados
    path('/livraria_exibir_livros/', livraria_exibir_livros,name='livrariaexibirlivros'),

    #Detalhes do livros
    path('/livraria_detalhe_livro/<int:pk>', livraria_detalhe_livro,name='livrariadetalhelivro'),

    #Editar livors
    path('/livraria_editarlivro/<int:pk>',livraria_editar_livro, name='livrariaeditarlivro'),

    #Deletar livro
    path('/livraria_deletarlivro/<int:pk>', livraria_deletar_livro, name='livrariadeletarlivro'),

    #Realizar emprestimo
    path('/livraria_emprestimo_livro/<int:pk>', livraria_realizar_emprestimo, name='livrariaemprestimolivro'),

    #Devolver Livro
    path('/livraria_devolver_livro/<int:pk>',livraria_devolver_livro, name='livrariadevolverlivro')

]
