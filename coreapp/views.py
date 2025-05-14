from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from coreapp.forms import *
from coreapp.models import *

# Create your views here.
def home_view(request):
    return render(request,'home.html')
def signup_view(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request,user)
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
def loginview(request):
    if request.method=='POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
@login_required
def dashboard(request):
    submit=QuestionAnswer.objects.filter(user=request.user).order_by('-submittedat')
    return render(request, 'dashboard.html', {'submit': submit})

@login_required
def question_view(request):
    if request.method == 'POST':
        nums = [
            int(request.POST.get('number1')),
            int(request.POST.get('number2')),
            int(request.POST.get('number3')),
            int(request.POST.get('number4')),
            int(request.POST.get('number5')),
        ]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        second_highest = nums[-2]
        QuestionAnswer.objects.create(
            user=request.user,
            numbers=nums,
            answer=second_highest,
        )
        return redirect('dashboard')

    return render(request, 'question.html')

from django.http import HttpResponse
from openpyxl import Workbook
from .models import QuestionAnswer

def export_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Submissions"
    ws.append(['Username', 'Numbers Entered', 'Second Highest'])

    submissions = QuestionAnswer.objects.all()

    for submission in submissions:
        username = submission.user.username
        numbers = submission.numbers

        try:
            nums = list(map(int, numbers))
            nums = sorted(set(nums), reverse=True)
            second_highest = nums[1] if len(nums) > 1 else 'N/A'
        except:
            second_highest = 'Invalid'

        ws.append([username, ','.join(map(str, numbers)), second_highest])

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="submissions.xlsx"'
    wb.save(response)
    return response
def logout_view(request):
    logout(request)
    return redirect('home')


