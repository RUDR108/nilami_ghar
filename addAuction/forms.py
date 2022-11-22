from django import forms
from store.models import Product

class AuctionForm(forms.ModelForm):

    # product_name = forms.CharField(max_length=200)
    # # slug =forms.SlugField(max_length=200)
    # description=forms.CharField(max_length=200)
    # price = forms.IntegerField()
    # images = forms.ImageField()
    # stock=forms.IntegerField()
    # is_available = forms.BooleanField()
    # category=models.ForeignKey()
    # created_date=forms.DateTimeField()
    # modified_date=forms.DateTimeField()# created_date=forms.DateTimeField()
    # modified_date=forms.DateTimeField()
    # password=forms.CharField(widget=forms.PasswordInput(attrs={
    #     'placeholder':"Enter Password"
    # }))
    # confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={
    #     'placeholder':"confirm Password"
    # }))
    class Meta:
        model =Product
        fields=['product_name',"description","images","price","Bid_owner"]

    def __init__(self,*args,**kwargs):  #overwritting class Meta
        super(AuctionForm,self).__init__(*args,**kwargs)
        self.fields['product_name'].widget.attrs['placeholder']="Enter product name"
        self.fields['description'].widget.attrs['placeholder']="Enter  description"
        self.fields['images'].widget.attrs['placeholder']="Enter image"
        self.fields['price'].widget.attrs['placeholder']="Enter price"
        self.fields['Bid_owner'].widget.attrs['placeholder']="Enter your name"
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'


    # def clean(self):
    #     cleaned_data = super(RegistrationForm,self).clean()
    #     password=cleaned_data.get('password')
    #     confirm_password=cleaned_data.get('confirm_password')

    #     if password!=confirm_password:
    #         raise forms.ValidationError(
    #             "Password Does not match!!"
    #         )