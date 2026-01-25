
from django import forms
from .models import Photo

# было: PhotоForm (с кириллической "о") и с полем author
class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        # author убираем из формы — его подставим из request.user
        fields = ['title', 'description', 'image']  # если в модели поле называется image
        # если поле в модели называется main_image, то:
        # fields = ['title', 'description', 'main_image']

