from django.shortcuts import redirect


def if_logged(func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        
        return func(request, *args, **kwargs)
    
    return wrapper_func

