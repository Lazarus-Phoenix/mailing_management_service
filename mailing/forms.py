from django import forms
from .models import Client, Message, Mailing


class ClientForm(forms.ModelForm):
    """
    Форма для создания и редактирования клиентов.
    """

    class Meta:
        model = Client
        fields = ["email", "full_name", "comment"]
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }


class MessageForm(forms.ModelForm):
    """
    Форма для создания и редактирования сообщений.
    """

    class Meta:
        model = Message
        fields = ["subject", "body"]
        widgets = {
            "Тема": forms.TextInput(attrs={"class": "form-control"}),
            "Сообщение": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }


class MailingForm(forms.ModelForm):
    """
    Форма для создания и редактирования рассылок.
    """

    class Meta:
        model = Mailing
        fields = ["start_time", "end_time", "status", "message", "clients"]

        widgets = {
            "start_time": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "end_time": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "status": forms.Select(attrs={"class": "form-control"}),
            "message": forms.Select(attrs={"class": "form-control"}),
            "clients": forms.SelectMultiple(attrs={"class": "form-control"}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Ограничиваем выбор сообщений и клиентов только для текущего пользователя
            if self.instance.owner:
                self.fields["message"].queryset = Message.objects.filter(
                    owner=self.instance.owner
                )
                self.fields["clients"].queryset = Client.objects.filter(
                    owner=self.instance.owner
                )
