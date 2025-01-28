"""
URL configuration for chatbotanalisisaceite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appuno import views
from appuno.views import chatbot


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.chatbot_view),
    path('resumen/', views.resumen),
    path("api/chatbot/", chatbot, name="chatbot_api"),
    path('descargar_resumen/', views.generar_resumen, name='descargar_resumen'),  # URL para generar el resumen
    path('reiniciar_chatbot/', views.reiniciar_chatbot, name='reiniciar_chatbot'),



]
