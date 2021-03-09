from django.contrib.auth.models import User

def register_new_user(request):
    username = request.POST['username']
    user_first_name = request.POST['first_name']
    user_last_name = request.POST['last_name']
    user_pass = request.POST['password']
    user_pas_validate = request.POST['pass2']
    User.objects.create_user(
        username=username,
        first_name=user_first_name,
        last_name=user_last_name,
        password=user_pass
    )

