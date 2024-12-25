from django import forms


class Registration(forms.Form):
    FirstName = forms.CharField(max_length=15)
    LastName = forms.CharField(max_length=15)
    Email = forms.EmailField()
    Password = forms.CharField(max_length=15)
    DOB = forms.CharField()


class MyForm(forms.Form):
    name = forms.CharField(max_length=15, min_length=5)
    salary = forms.IntegerField(max_value=6, min_value=3)
    email = forms.EmailField()
    height = forms.DecimalField(max_digits=8, decimal_places=3)
    terms = forms.BooleanField()
    dob = forms.DateField(input_formats={'%d-%m-Y'})
    time = forms.TimeField()
    gender = forms.ChoiceField(choices=[{'M', "male"}, {"F", "Female"}, {"O", "Other"}])
    # hobbies = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=[{"swim", "swim"}, {"Reading", "Reading"}, {"game", "game"}])
    resume = forms.FileField()
    password = forms.CharField(max_length=10, min_length=5, widget=forms.PasswordInput)
