from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from auths.forms import UserCreationForm
from auths.models import Profile, User
from core.models import Workout, Friend, FriendRequest
from utils.posts import get_posts_with_comments


def register(request, *args, **kwargs):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect('core:fitness-feed')

    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()

        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')

        messages.success(request, f"Account for {username} created successfully.")

        # Authenticate the user and log them in
        user = authenticate(request, email=email, password=password)
        login(request, user)
        messages.success(request, f"Hi {username}, you are now logged in.")

        # Check if a profile already exists for this user
        profile, created = Profile.objects.get_or_create(user=user)
        if created:
            profile.phone = form.cleaned_data.get('phone')
            profile.gender = form.cleaned_data.get('gender')
            profile.save()
        else:
            messages.warning(request, f"A profile already exists for {username}.")

        return redirect('core:fitness-feed')

    context = {
        'form': form
    }
    return render(request, 'auths/register.html', context)


def signin(request, *args, **kwargs):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect('core:fitness-feed')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Hi {user.username}, you are now logged in.")
            return redirect('core:fitness-feed')
        else:
            messages.error(request, "Invalid email or password. Please try again.")

    return render(request, 'auths/register.html')


def signout(request):
    logout(request)
    return redirect("auths:fitness-register")


@login_required
def my_profile(request):
    # Get the IDs of friends for the current user
    user_friends_ids = Friend.objects.filter(user=request.user).values_list('friend_id', flat=True)

    # Get the IDs of users who have the current user as their friend
    user_users_ids = Friend.objects.filter(friend=request.user).values_list('user_id', flat=True)

    # Combine the two lists to get all friends both ways
    friends_ids = set(user_friends_ids) | set(user_users_ids)

    # Now you have the IDs of all friends, you can query the User model or
    # any other related model to get more information about these friends if needed
    friends = User.objects.filter(id__in=friends_ids)

    posts = get_posts_with_comments(request, author=request.user)
    workouts = Workout.objects.filter(author=request.user)

    context = {
        'current_user': request.user,
        'profile': request.user.profile,
        'friends': friends,
        'posts': posts,
        'workouts': workouts
    }
    return render(request, 'auths/my-profile.html', context)


@login_required
def others_profile(request, username):
    other_user = User.objects.get(username=username)
    if request.user == other_user:
        return redirect('auths:fitness-profile')

    # Get the IDs of friends for the current user
    user_friends_ids = Friend.objects.filter(user=request.user, friend=other_user).values_list('friend_id', flat=True)

    # Get the IDs of users who have the current user as their friend
    user_users_ids = Friend.objects.filter(user=other_user, friend=request.user).values_list('user_id', flat=True)

    # Combine the two lists to get all friends both ways
    friends_ids = set(user_friends_ids) | set(user_users_ids)

    # Now you have the IDs of all friends, you can query the User model or
    # any other related model to get more information about these friends if needed
    friends = User.objects.filter(id__in=friends_ids)

    posts = get_posts_with_comments(request, author=other_user)
    workouts = Workout.objects.filter(author=other_user)

    is_friend_request_sent = False

    from_user = request.user
    to_user = other_user

    # Lookup friend request
    try:
        friend_request = FriendRequest.objects.get(
            Q(from_user=from_user, to_user=to_user) | Q(from_user=to_user, to_user=from_user))
        if friend_request.status == 'pending':
            is_friend_request_sent = True

    except FriendRequest.DoesNotExist:
        is_friend_request_sent = False

    # Check for friendship
    is_friend = Friend.objects.filter(Q(user=from_user, friend=to_user) | Q(friend=from_user, user=to_user)).exists()

    context = {
        'current_user': request.user,
        'other_user': other_user,
        'profile': other_user.profile,
        'friends': friends,
        'posts': posts,
        'workouts': workouts,
        'is_friend_request_sent': is_friend_request_sent,
        'is_friend': is_friend
    }
    return render(request, 'auths/user-profile.html', context)
