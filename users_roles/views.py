from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile, Groups
from .forms import UserForm, GroupForm, LogInForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.method == 'GET':
        return render(request, 'users_roles/login_user.html', {'form': LogInForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'users_roles/login_user.html', {'form': LogInForm(), 'error': 'Wrong password'})
        else:
            login(request, user)
            return redirect('all_users')


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('all_users')


def all_users(request):
    users = Profile.objects.all()
    return render(request, 'users_roles/all_users.html', {'users': users})


def create_user(request):
    if request.method == 'GET':
        select_groups = Groups.objects.all()
        return render(request, 'users_roles/create_user.html', {'form': UserForm(), 'select_groups': select_groups})
    else:
        try:
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(all_users)
            else:
                return render(request, 'users_roles/create_user.html', {'form': UserForm(), 'error': form.errors})
        except ValueError:
            return render(request, 'users_roles/create_user.html', {'form': UserForm(), 'error': 'Bad data'})


@login_required
def edit_user(request, user_pk):
    user = get_object_or_404(Profile, pk=user_pk)
    if request.method == 'GET':
        form = UserForm(instance=user)
        return render(request, 'users_roles/edit_user.html', {'user': user, 'form': form})
    else:
        try:
            form = UserForm(request.POST, instance=user)
            form.save()
            return redirect(all_users)
        except ValueError:
            return render(request, 'users_roles/edit_user.html', {'error': 'Bad data'})


@login_required
def delete_user(request, user_pk):
    user = get_object_or_404(Profile, pk=user_pk)
    if request.method == 'POST':
        try:
            user.delete()
        finally:
            return redirect('all_users')


def all_groups(request):
    user = request.user
    groups = Groups.objects.all()
    error = request.session.get('error', None)
    if error:
        del request.session['error']
    if error is not None:
        return render(request, 'users_roles/all_groups.html', {'groups': groups, 'user': user, 'error': error})
    else:
        return render(request, 'users_roles/all_groups.html', {'groups': groups, 'user': user, })


def create_group(request):
    if request.method == 'GET':
        return render(request, 'users_roles/create_group.html', {'form': GroupForm()})
    else:
        try:
            form = GroupForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(all_groups)
            else:
                return render(request, 'users_roles/create_group.html', {'form': GroupForm(), 'error': form.errors})
        except ValueError:
            return render(request, 'users_roles/create_group.html', {'form': GroupForm(), 'error': 'Bad data'})


def edit_group(request, group_pk):
    group = get_object_or_404(Groups, pk=group_pk)
    if request.method == 'GET':
        form = GroupForm(instance=group)
        return render(request, 'users_roles/edit_group.html', {'group': group, 'form': form})
    else:
        try:
            form = GroupForm(request.POST, instance=group)
            form.save()
            return redirect(all_groups)
        except ValueError:
            return render(request, 'users_roles/edit_group.html', {'error': 'Bad data'})


@login_required
def delete_group(request, group_pk):
    current_user = request.user
    group = get_object_or_404(Groups, pk=group_pk)
    if request.method == 'POST':
        if current_user.group_id != group.id:
            try:
                group.delete()
            except ValueError:
                return render(request, 'users_roles/all_groups.html',
                              {'error': 'Something went wrong!'})
            except IntegrityError:
                return render(request, 'users_roles/all_groups.html',
                              {'error': 'Something went wrong!'})
            except TypeError:
                return render(request, 'users_roles/all_groups.html',
                              {'error': 'Something went wrong!'})
        else:
            request.session['error'] = 'You cant delete your own group!'
            return redirect(all_groups)
    return redirect(all_groups)
