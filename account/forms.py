from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, UserInfo

# 用户登录表单类
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# 用户注册表单类
class RegistrationFrom(forms.ModelForm):
    # 在顶部引入了User类，因此不需要再建立user模型
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    # 这是一个内部类，声明本表单类所应用的数据模型，即表单要写入哪个数据库表里
    class Meta:
        model = User
        # 说明选用了哪些字段
        fields = ('username', 'email')

    # 检验两次密码是否一致
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('两次密码不一致。')
        return cd['password2']

# 用户注册表单补充
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'birth')


# 用户信息表单
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('school', 'company', 'profession', 'address', 'aboutme', 'photo')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)