from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView  # новое изменение
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NotesForm
from .models import Notes


class BlogListView(LoginRequiredMixin, ListView):
    paginate_by = 5
    model = Notes
    template_name = 'notes_page/home.html'


class BlogDetailView(LoginRequiredMixin, UpdateView):
    model = Notes
    fields = ['task_complete']
    template_name = 'notes_page/post_detail.html'
    success_url = reverse_lazy('home')


class BlogCreateView(LoginRequiredMixin, CreateView):  # новое изменение
    form_class = NotesForm
    template_name = 'notes_page/new_post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView): # Новый класс
    form_class = NotesForm
    model = Notes
    template_name = 'notes_page/post_edit.html'
    success_url = reverse_lazy('home')


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    template_name = 'notes_page/post_delete.html'
    success_url = reverse_lazy('home')


class CompleteView(LoginRequiredMixin, DetailView):
    model = Notes
    template_name = 'notes_page/post_complete.html'

class ListCompleteView(LoginRequiredMixin, ListView):
    model = Notes
    template_name = 'notes_page/home_complete.html'



