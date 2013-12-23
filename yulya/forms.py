from django import forms
from ckeditor.widgets import CKEditorWidget


class CommentForm(forms.Form):

    comment = forms.CharField(widget=CKEditorWidget(config_name = 'mine'))