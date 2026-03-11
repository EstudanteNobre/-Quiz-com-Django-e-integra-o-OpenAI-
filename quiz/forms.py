from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import PerfilUsuario, Tema, Dificuldade


class CadastroForm(forms.ModelForm):
    """Formulário de cadastro de usuário"""
    username = forms.CharField(
        label='Usuário',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Digite seu nome de usuário',
            'autocomplete': 'username'
        })
    )
    
    password = forms.CharField(
        label='Senha',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Digite sua senha',
            'autocomplete': 'new-password'
        }),
        min_length=8,
        help_text='A senha deve ter pelo menos 8 caracteres.'
    )
    
    password_confirm = forms.CharField(
        label='Confirmar Senha',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Confirme sua senha',
            'autocomplete': 'new-password'
        })
    )
    
    tipo_usuario = forms.ChoiceField(
        label='Tipo de Usuário',
        choices=PerfilUsuario.TIPO_USUARIO_CHOICES,
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-input',
        }),
        initial='aluno'
    )
    
    class Meta:
        model = User
        fields = ['username']
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Este nome de usuário já está em uso.')
        return username
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        tipo_usuario = cleaned_data.get('tipo_usuario')
        
        if password and password_confirm:
            if password != password_confirm:
                raise ValidationError({
                    'password_confirm': 'As senhas não coincidem.'
                })
        
        # Garantir que tipo_usuario seja sempre válido (padrão: aluno)
        if not tipo_usuario or tipo_usuario not in ['aluno', 'professor']:
            cleaned_data['tipo_usuario'] = 'aluno'
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class ImportarPerguntasForm(forms.Form):
    """Formulário para importar perguntas a partir de texto"""
    tema_personalizado = forms.CharField(
        label='Tema',
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Digite o tema personalizado para este quiz'
        }),
        help_text='Digite o nome do tema personalizado para este quiz'
    )
    
    texto_perguntas = forms.CharField(
        label='Texto com Perguntas e Respostas',
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-input',
            'rows': 20,
            'placeholder': 'Cole aqui o texto completo com perguntas e respostas.\n\nFormato esperado:\n1. Pergunta aqui?\na) Alternativa A\nb) Alternativa B\nc) Alternativa C\nd) Alternativa D\nResposta: A\n\n2. Outra pergunta?\na) ...\nb) ...\nc) ...\nd) ...\nResposta: B'
        }),
        help_text='Cole o texto completo. O sistema tentará identificar automaticamente as perguntas e alternativas.'
    )

