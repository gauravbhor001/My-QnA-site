from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from .forms import QuestionForm ,AnswerForm
from django.contrib.auth import login
from .forms import UserRegistrationForm


def home_redirect_view(request):
    # Redirects to the "All Questions" page
    return redirect('question_list')  # Redirect to the question list
def register(request):
    if request.user.is_authenticated:  # If the user is already logged in
        return redirect('question_list')  # Redirect them to another page

    if request.method == 'POST':  # If the request is a POST request
        form = UserRegistrationForm(request.POST)
        if form.is_valid():  # If the form is valid
            user = form.save()  # Create a new user
            login(request, user)  # Log in the new user
            return redirect('question_list')  # Redirect after successful registration
    else:
        form = UserRegistrationForm()  # Render an empty form

    return render(request, 'registration/register.html', {'form': form})  # Render the registration page
@login_required
def profile(request):
    user = request.user
    return render(request, 'accounts/profile.html', {'user': user})

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'qa/question_list.html', {'questions': questions})

def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect('question_detail', question_id=question.id)
    else:
        form = AnswerForm()
    return render(request, 'qa/question_detail.html', {'question': question, 'form': form})

def question_create(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You must be logged in to ask a question.")

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('question_list')
    else:
        form = QuestionForm()
    return render(request, 'qa/question_create.html', {'form': form})

def user_question_list(request, user_id):
    user = get_object_or_404(User, id=user_id)
    questions = Question.objects.filter(author=user)
    return render(request, 'accounts/profile.html', {'user': user, 'questions': questions})


@login_required  # Ensure only logged-in users can access this view
def delete_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)  # Find the question

    if question.author != request.user:  # Ensure the user is the question's author
        return HttpResponseForbidden("You are not allowed to delete this question.")  # Forbid access

    question.delete()  # Delete the question
    return redirect('user_question_list', user_id=request.user.id)  # Redirect to the user's questions list