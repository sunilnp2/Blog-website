from post.models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    name = forms.CharField(label='Enter Name', widget=(forms.TextInput(attrs={'class':'form-control'})), 
    error_messages={'required':"name is required"})
    email = forms.EmailField(label='Enter Email', widget=(forms.EmailInput(attrs={'class':'form-control'})), 
    error_messages={'required':"email is required"})
    website = forms.CharField(label='Enter Website', widget=(forms.TextInput(attrs={'class':'form-control'})), 
    error_messages={'required':"website is required"})
    message = forms.CharField(label='Enter Message', widget=(forms.Textarea(attrs={'class':'form-control'})), 
    error_messages={'required':"message is required"})
    class Meta:
        model = Comment
        fields = ('name', 'email', 'website', 'message')


