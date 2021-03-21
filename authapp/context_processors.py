
def user_status(request):
    user = request.user
    if user.is_authenticated:
        status = 'Пользователь авторизованн'
    else:
        status = 'Пользователь не авторизованн'
    return {'status': status}






