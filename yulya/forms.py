from django import forms
from ckeditor.widgets import CKEditorWidget


class CommentForm(forms.Form):
	author = forms.CharField(max_length=100)
	comment = forms.CharField(widget=CKEditorWidget(config_name = 'mine'))