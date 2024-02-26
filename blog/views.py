from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.all().order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pinned_posts = Post.objects.filter(pinned=True).order_by('-date_posted')
        context['pinned_posts'] = pinned_posts

        return context


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('date_posted')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pinned_posts = Post.objects.filter(pinned=True).order_by('-date_posted')
        context['pinned_posts'] = pinned_posts

        return context

class PostDetailView(DetailView):
    model = Post

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.toggle_pin()
        return redirect(self.request.path)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]

        form = CommentForm()
        post = get_object_or_404(Post, pk=pk)
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        context['posts'] = Post.objects.all()
        pinned_posts = Post.objects.filter(pinned=True).order_by('-date_posted')
        context['pinned_posts'] = pinned_posts
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pinned_posts = Post.objects.filter(pinned=True).order_by('-date_posted')
        context['pinned_posts'] = pinned_posts
        return context


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("post-detail", kwargs={"pk": pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pinned_posts = Post.objects.filter(pinned=True).order_by('-date_posted')
        context['pinned_posts'] = pinned_posts
        return context


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pinned_posts = Post.objects.filter(pinned=True).order_by('-date_posted')
        context['pinned_posts'] = pinned_posts
        return context


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pinned_posts = Post.objects.filter(pinned=True).order_by('-date_posted')
        context['pinned_posts'] = pinned_posts
        return context


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pinned_posts = Post.objects.filter(pinned=True).order_by('-date_posted')
        context['pinned_posts'] = pinned_posts
        return context


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = '/'

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pinned_posts = Post.objects.filter(pinned=True).order_by('-date_posted')
        context['pinned_posts'] = pinned_posts
        return context
