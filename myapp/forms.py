from django import forms

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super().__init__(*args, **kwargs)
        for index, question in enumerate(questions):
            self.fields[f'question_{index}'] = forms.ChoiceField(
                label=question.text,
                choices=[
                    ('A', question.option_a),
                    ('B', question.option_b),
                    ('C', question.option_c),
                    ('D', question.option_d),
                ],
                widget=forms.RadioSelect,
            )
