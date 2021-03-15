
def user_status(request):
    user = request.user
    if user.is_authenticated:
        status = 'авторизованн'
    else:
        status = 'не авторизованн'
    return {'status': status}