#
#from livraria.models import Livro, Editora, Endereco, Autor, EmprestimoLivro
#from django.utils import timezone
#from datetime import date

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUsuario, Livro, Editora, Categoria, Autor

class DateInput(forms.DateInput):
    input_type = 'date'


CATEGORIA_CHOICES = (
    ('Filosofia', 'Filosofia'),
    ('Religiao','Religiao'),
    ('Ciencia','Ciencia'),
    ('Romance','Romance'),
    ('Historia','Historia'),
    ('Terror', 'Terror'),
    ('Suspense', 'Suspense'),
    )


class CustomUsuarioCreationForm(UserCreationForm):
    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone', 'email')


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.username = self.cleaned_data['email']
        

        if commit:
            user.save()

        return user


class CustomUsuarioChangeForm(UserChangeForm):

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone', 'email')



class LivroCreationForm(forms.ModelForm):

    categoria = forms.ChoiceField(choices=CATEGORIA_CHOICES, label='Categoria')
    ano = forms.DateField(widget=DateInput, label='Ano')
    descricao = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Livro
        fields = ('nome', 'preco', 'estoque', 'edicao', 'num_paginas', 'autor', 'editora')


class EditoraCreateForm(forms.ModelForm):
    rua = forms.CharField(max_length=100,label='Rua')
    bairro = forms.CharField(max_length=100,label='Bairro')
    numero = forms.IntegerField(initial = 0,label='Número')
    cidade = forms.CharField(max_length=100,label='Cidade')
    estado = forms.CharField(max_length=100,label='Estado')

    class Meta:
        model = Editora
        fields = ('nome',)


class AutorCreationForm(forms.ModelForm):
    data_nascimento = forms.DateField(widget=DateInput, label='Data de nascimento')

    class Meta:
        model = Autor
        fields = ('nome',)





'''

class CheckboxInput(forms.CheckboxInput):
    input_type = 'checkbox'

class LivroForm(forms.ModelForm):
    ano = forms.DateField(widget=DateInput)

    list_editoras = Editora.objects.all().values()

    editora = forms.ChoiceField(choices=[('0','Selecione')]+ [(editora.id, editora.nome) for editora in  Editora.objects.all()])
    descricao = forms.CharField(widget=forms.Textarea())
    categorias = forms.ChoiceField(choices=CATEGORIAS_LIVROS)

   # categoria_nao_encontrada = forms.BooleanField(required=False, label='Não encontrei minha categoria')
    class Meta:
        model = Livro
        fields = ('nome', 'preco','estoque', 'edicao','num_paginas')

class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ('nome',)

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ('rua','bairro','cidade','estado','numero')

class AutorForm(forms.Form):
   
    nomeAutor = forms.CharField(max_length=100,label='Nome do autor')
    ano = forms.DateField(widget=DateInput,label='Ano de nascimento do autor')

class EmprestimoForm(forms.Form):
    data_inicial = forms.DateField(label='Data de início',disabled=True,initial=timezone.now)
    data_devolucao = forms.DateField(label='Data de devolução',widget=DateInput)
    quantidade = forms.IntegerField(label='Quantidade a ser emprestada', initial=0)
    preco = forms.DecimalField(label='Preco a pagar pelo emprestimo',decimal_places=2,disabled=True, initial=0)
  
class Livro_Emprestimo_Form(forms.ModelForm):
    nome = forms.CharField(required=True,max_length=100)
    class Meta:
        model = Livro
        fields = ('nome',)

'''
