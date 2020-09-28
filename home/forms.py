from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            "class": "form-control", 'placeholder': 'Enter your name', 'name': 'name', 'id': 'name',
            'onfocus': "this.placeholder = ''", "onblur": "this.placeholder = 'Enter your name'"
        }
        self.fields['email'].widget.attrs = {
            "class": "form-control", 'placeholder': 'Enter email address', 'name': 'email', 'id': 'email',
            'onfocus': "this.placeholder = ''",
            "onblur": "this.placeholder = 'Enter email address'"
        }
        self.fields['subject'].widget.attrs = {
            'placeholder': 'Enter Subject', "name": "subject", "id": "subject", "class": "form-control",
            'onfocus': "this.placeholder = ''", "onblur": "this.placeholder = 'Enter Subject'"
        }
        self.fields['message'].widget.attrs = {
            "class": "form-control w-100", "name": "message", 'placeholder': 'Enter Message', 'cols': '30',
            'rows': '10',
            "id": "message", 'onfocus': "this.placeholder = ''", "onblur": "this.placeholder = 'Enter Message'",
        }

    class Meta:
        fields = ('name', 'email', 'subject', 'message')
