from . import views

app_name = 'basic_app'


urlpatterns=[
path('/register',views.register, name='register')
]
