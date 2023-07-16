from django.shortcuts import render
from django.views.generic import TemplateView
from rest_condition import Or
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from blog.models import Post, Comment
from blog.permissions import PostUpdatePermissions
from blog.serializers import PostSerializer, CommentSerializer, UserPostSerializer


class HomePageView(TemplateView):
    template_name = 'blog/index.html'

    def index(request):
        return render(request, 'blog/index.html')


class AboutView(TemplateView):
    template_name = 'blog/about.html'

    def index(request):
        return render(request, 'blog/about.html')


class ContactView(TemplateView):
    template_name = 'blog/contact.html'

    def index(request):
        return render(request, 'blog/contact.html')


class ServicesView(TemplateView):
    template_name = 'blog/services.html'

    def index(request):
        return render(request, 'blog/services.html')


class SubscribeView(TemplateView):
    template_name = 'subscribe/subscription.html'

    def index(request):
        return render(request, 'subscribe/subscription.html')


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [AllowAny]
    template_name = 'blog/blog.html'

    def index(request):
        return render(request, 'blog/blog.html')


class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = UserPostSerializer
    queryset = Post.objects.all()
    permission_classes = [Or(IsAuthenticated, AllowAny)]
    template_name = 'blog/add-post.html'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [AllowAny]


class PostUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserPostSerializer
    queryset = Post.objects.all()
    permission_classes = [Or(IsAdminUser, PostUpdatePermissions)]


class PostDestroyAPIView(generics.DestroyAPIView):
    serializer_class = UserPostSerializer
    queryset = Post.objects.all()
    permission_classes = [Or(IsAdminUser, PostUpdatePermissions)]


class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        print(request)
        return super().list(request, *args, **kwargs)


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [Or(IsAdminUser, PostUpdatePermissions)]


class CommentDestroyAPIView(generics.DestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [Or(IsAdminUser, PostUpdatePermissions)]
