from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from blogs.models import Blog


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.filter(publication_sign=True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "content", "image")
    template_name = "blogs/blog_form.html"
    success_url = reverse_lazy('blogs:blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "content", "image")
    template_name = "blogs/blog_form.html"
    success_url = reverse_lazy('blogs:blog_list')

    def get_success_url(self):
        return reverse('blogs:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blogs/blog_confirm_delete.html"
    success_url = reverse_lazy('blogs:blog_list')
