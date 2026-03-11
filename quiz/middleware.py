"""
Middleware personalizado para controle de sessão.
"""
from django.contrib.auth import logout


class SessionControlMiddleware:
    """
    Middleware que verifica se a sessão do navegador é válida.
    Força logout quando o navegador é reaberto após fechar.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Pular verificação para páginas de login/logout/cadastro/home
        path = request.path
        skip_paths = ['/login/', '/logout/', '/cadastro/', '/admin/', '/home/', '/']
        should_skip = any(path.startswith(p) or path == p for p in skip_paths)
        
        response = self.get_response(request)
        
        # Se o usuário está logado, garantir que o cookie existe
        if request.user.is_authenticated:
            # Verificar se existe o cookie de sessão do navegador
            browser_session = request.COOKIES.get('browser_session_active')
            
            # Se não há cookie E não estamos em uma página de skip, fazer logout
            if not browser_session and not should_skip:
                logout(request)
                from django.shortcuts import redirect
                return redirect('quiz:login')
            
            # Definir cookie de sessão do navegador (expira ao fechar)
            # max_age=None significa que expira ao fechar o navegador
            response.set_cookie(
                'browser_session_active',
                'true',
                max_age=None,  # Expira ao fechar o navegador
                httponly=False,  # Precisamos acessar via JavaScript
                samesite='Lax'
            )
        
        return response

