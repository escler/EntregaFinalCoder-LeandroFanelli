from django.urls import path

from AppCoder.views import  Curso_CreateView, Curso_DeleteView, Curso_DetailView, Curso_ListView, Curso_UpdateView, Estudiante_CreateView, Estudiante_DeleteView, Estudiante_DetailView, Estudiante_ListView, Estudiante_UpdateView, Profesor_CreateView, Profesor_DeleteView, Profesor_DetailView, Profesor_ListView, Profesor_UpdateView, buscarCurso, resultadoBuscarCurso, Page_DeleteView, Page_CreateView, Page_DetailView, Page_ListView, Page_UpdateView

urlpatterns = [
    path('cursos/', Curso_ListView.as_view(), name='cursos'),
    path('cursos/add/', Curso_CreateView.as_view(), name='curso_add'),
    path('curso/update/<pk>', Curso_UpdateView.as_view(), name='curso_update'),
    path('curso/delete/<pk>', Curso_DeleteView.as_view(), name='curso_delete'),
    path('curso/view/<pk>', Curso_DetailView.as_view(), name='curso_view'),
    path('cursos/buscarCurso/', buscarCurso, name='BuscarCurso'),
    path('cursos/resultadoBuscarCurso/', resultadoBuscarCurso, name='ResultadoBuscarCurso'),
    path('estudiantes/', Estudiante_ListView.as_view(), name='estudiantes'),
    path('estudiantes/add/', Estudiante_CreateView.as_view(), name='estudiante_add'),
    path('estudiantes/update/<pk>', Estudiante_UpdateView.as_view(), name='estudiante_update'),
    path('estudiantes/delete/<pk>', Estudiante_DeleteView.as_view(), name='estudiante_delete'),
    path('estudiantes/view/<pk>', Estudiante_DetailView.as_view(), name='estudiante_view'),
    path('profesores/', Profesor_ListView.as_view(), name='profesores'),
    path('profesores/add/', Profesor_CreateView.as_view(), name='profesor_add'),
    path('profesores/update/<pk>', Profesor_UpdateView.as_view(), name='profesor_update'),
    path('profesores/delete/<pk>', Profesor_DeleteView.as_view(), name='profesor_delete'),
    path('profesores/view/<pk>', Profesor_DetailView.as_view(), name='profesor_view'),
    path('pages/', Page_ListView.as_view(), name='pages'),
    path('pages/add/', Page_CreateView.as_view(), name='page_add'),
    path('pages/update/<pk>', Page_UpdateView.as_view(), name='page_update'),
    path('pages/delete/<pk>', Page_DeleteView.as_view(), name='page_delete'),
    path('pages/view/<pk>', Page_DetailView.as_view(), name='page_view'),
]