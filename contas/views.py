from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def cadastro_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST) #Carrega os dados do Usuario
        if user_form.is_valid(): #Valido se ta tudo certo
            user_form.save() #Salva
            return redirect('login') #Vai para a tela de Login
    else:
        user_form = UserCreationForm() #se não, tudo em branco.
    return render(request, 
                  'cadastro.html', 
                  {'user_form': user_form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        #Authenticate é um método que verifica se o user existe e a senha ta certa.
        if user is not None: #Se esta válido.
            login(request, user)            #C hamo o Login na sessão do usuario.
            return redirect('lista_carros') # Então o usuario pode ver a lista de carros.
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})

def logout_view(request):
    logout(request)
    return redirect('login')
