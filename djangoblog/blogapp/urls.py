from django.urls import path
from . import views

app_name = "blogapp"

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('author/<name>', views.GetAuthor.as_view(), name="author"),
    path('article/<int:id>', views.GetSingle.as_view(), name="single_post"),
    path('topic/<name>', views.getTopic, name="topic"),
    path('login/', views.GetLogin.as_view(), name="login"),
    path('logout/', views.getLogout, name="logout"),
    path('create/', views.getCreate, name="create"),
    path('profile/', views.getProfile, name="profile"),
    path('update/<int:pid>', views.getUpdate, name="update"),
    path('delete/<int:pid>', views.getDelete, name="delete"),

    path('register/', views.getRegister, name="register"),
    path('activate/<uid>/<token>', views.activate, name="activate"),

    path('topics', views.getCategory, name="category"),
    path('topics/create', views.createTopic, name="createTopic")
]
