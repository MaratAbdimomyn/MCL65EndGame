from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.contrib.auth import authenticate, login
from .models import *
from .forms import *

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class Login(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('tracks_list')

class Logout(LogoutView):
    template_name = 'logout.html'
    next_page = reverse_lazy('tracks_list')
    http_method_names = ['post']

class TracksListView(ListView):
    model = Track
    template_name = 'tracks_list.html'
    context_object_name = 'tracks'
    paginate_by = 5

    def get_queryset(self):
        return Track.objects.order_by('song')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            for track in context['tracks']:
                track.has_like = user.like_set.filter(track=track).exists()
        else:
            for track in context['tracks']:
                track.has_like = False
        all_performers = Track.objects.values_list('performer', flat=True).distinct()
        context['all_performers'] = all_performers.order_by('performer')
        return context

class OnlyTracksListView(ListView):
    model = Track
    template_name = 'tracks_only_list.html'
    context_object_name = 'tracks'

    def get_queryset(self):
        if self.request.GET.get("performer"):
            performer_name = self.request.GET['performer']
            return Track.objects.filter(performer__icontains=performer_name)
        else:
            return Track.objects.order_by('song')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            for track in context['tracks']:
                track.has_like = user.like_set.filter(track=track).exists()
        else:
            for track in context['tracks']:
                track.has_like = False
        all_performers = Track.objects.values_list('performer', flat=True).distinct()
        context['all_performers'] = all_performers
        return context

class CreateLikeView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def post(self, request, track_id):
        if request.user.is_authenticated:
            track = Track.objects.get(pk=track_id)
            Like.objects.create(user=request.user, track=track)
        return redirect(request.META.get('HTTP_REFERER', 'tracks_list'))

class DeleteLikeView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def post(self, request, track_id):
        if request.user.is_authenticated:
            try:
                like = Like.objects.get(user=request.user, track_id=track_id)
                like.delete()
            except Like.DoesNotExist:
                pass
        return redirect(request.META.get('HTTP_REFERER', 'tracks_list'))

class FavoriteTracksListView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        if request.user.is_authenticated:
            favorite_tracks = Like.objects.filter(user=request.user)
            return render(request, 'tracks_list_favorite.html', {'favorite_tracks': favorite_tracks})
        else:
            return render(request, 'tracks_list_favorite.html', {'favorite_tracks': None})

class TopLikedTracksListView(ListView):
    model = Track
    template_name = 'tracks_top.html'
    context_object_name = 'tracks_top'

    def get_queryset(self):
        return Track.objects.annotate(num_likes=Count('like')).order_by('-num_likes')

class TrackCreateView(LoginRequiredMixin, CreateView):
    model = Track
    form_class = TrackCreateForm
    template_name = 'track_create.html'
    success_url = reverse_lazy('tracks_list')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)
    
class TrackUpdateView(LoginRequiredMixin, UpdateView):
    model = Track
    form_class = TrackCreateForm
    template_name = 'track_update.html'
    success_url = reverse_lazy('tracks_list')
    login_url = reverse_lazy('login')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs
    
class TrackDetailView(DetailView):
    model = Track
    template_name = 'track_about.html'
    context_object_name = 'track'

class TrackDeleteView(DeleteView):
    model = Track
    template_name = 'track_delete.html'
    success_url = reverse_lazy('tracks_list')
    context_object_name = 'track_delete_confirm'

