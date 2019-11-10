from django.urls import path, include

from minhaapp import views

urlpatterns = [
    path('', views.index),
    path('new', views.CriaPresencaView.as_view(), name='presenca_new'),
    path('view/<int:pk>', views.DetailPresencaView.as_view(), name='presenca_view'),
    path('edit/<int:pk>', views.EditPresencaView.as_view(), name='presenca_edit'),
    path('delete/<int:pk>', views.DeletePresencaView.as_view(), name='presenca_delete'),
    path('list', views.ListaPresencaView.as_view(), name='presenca_list'),
]