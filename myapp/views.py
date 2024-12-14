from django.shortcuts import render
from .models import Question
from .forms import QuizForm

def home(request):
    return render(request, 'home.html')

def quiz(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            score = 0
            for index, question in enumerate(questions):
                user_answer = form.cleaned_data.get(f'question_{index}')
                if user_answer == question.correct_option:
                    score += 1
            return render(request, 'result.html', {'score': score, 'total': len(questions)})
    else:
        form = QuizForm(questions=questions)
    return render(request, 'quiz.html', {'form': form})
