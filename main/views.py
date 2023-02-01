from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserProfileForm, CommentForm, PostForm
from .models import UserProfile, Post, Comment


@login_required
def home(request):
    posts = Post.objects.all().order_by('-date')
    comment_form = CommentForm()
    comments_ids = Comment.objects.filter(user=request.user).values_list('id', flat=True)
    
    return render(request, 'home.html', {'posts': posts, 'comment_form': comment_form, 'users_comments': comments_ids})


def sign_up(request):
    if request.method == 'POST':
        user_registration_form = UserRegistrationForm(request.POST or None)
        user_profile_form = UserProfileForm()
        
        if user_registration_form.is_valid():
            user_profile = user_profile_form.save(commit=False)
            user = user_registration_form.save()
            user_profile.user = user
            user_profile.save()

            login(request, user)
            return redirect('home')

    user_registration_form = UserRegistrationForm()
    return render(request, 'registration/sign_up.html', {'form': user_registration_form})


@login_required
def edit_account(request, id):
    profile = UserProfile.objects.get(id=id)
    user = profile.user
    
    user_form = UserRegistrationForm(instance=user)
    
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        return redirect(home)

    return render(request, 'settings/edit_account.html', {'user_form': user_form})

@login_required
def edit_profile(request, id):
    profile = get_object_or_404(UserProfile, pk=id)
    profile_form = UserProfileForm(request.POST or None, request.FILES or None, instance=profile)
    if profile_form.is_valid():
        profile = profile_form.save(commit=False)
        profile.user = request.user
        profile.save()
        
        return redirect(user_profile, id)

    return render(request, 'settings/edit_profile.html', {'profile': profile_form})


@login_required
def user_profile(request, id):
    profile = UserProfile.objects.get(id=id)
    gender = profile.GENDER[profile.gender][1]
    posts = profile.user.posts.all().order_by('-date')
    comment_form = CommentForm()
    comments_ids = Comment.objects.filter(user=request.user).values_list('id', flat=True)
      
    return render(request, 'user_profile.html', {'profile': profile, 'gender': gender, 'posts': posts, 'comment_form': comment_form, 'users_comments': comments_ids})


@login_required
def add_post(request):
    post_form = PostForm(request.POST or None, request.FILES or None)
    user = UserProfile.objects.get(user=request.user)

    if post_form.is_valid():   
        post = post_form.save(commit=False)
        post.user = request.user        
        user.posts_amount += 1
        
        user.save()
        post.save()

        return redirect('home')

    return render(request, 'add_post.html',  {'post_form': post_form})

@login_required
def edit_post(request, id):
    user = request.user
    get_post = get_object_or_404(Post, pk=id)
    post_form = PostForm(request.POST or None, request.FILES or None, instance=get_post)

    if get_post.user != user:
        return redirect('home')

    if request.method == 'POST':
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = user
            post.save()

        return redirect('home')

    return render(request, 'edit_post.html', {'post_form': post_form})

@login_required
def delete_post(request, id):
    user = request.user
    post = Post.objects.get(id=id)

    if post.user != user:
        return redirect('home')
    user.userprofile.posts_amount -= 1
    user.userprofile.save()
    post.delete()
    return redirect('home')

@login_required
def add_comment(request, post_id):
    user_profile = UserProfile.objects.get(user=request.user)
    posts = Post.objects.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            print(post_id)
            comment.post = posts.get(id=post_id)
            comment.user = user_profile.user
            comment.save()
            
    return redirect('home')

    
@login_required
def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect('home')
    
    