from django import forms

class CommentForm(forms.Form):
    title = forms.CharField(label='search', 
                            widget=forms.TextInput(attrs={'placeholder': 'Title', 'class':'span4', 'size':"16"}), 
                            max_length = 40)
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'span6', 'id':'comment_text'}))