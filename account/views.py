from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationFrom, UserProfileForm, UserInfoForm, UserForm
# 引入登录检测装饰函数
from django.contrib.auth.decorators import login_required
from .models import UserProfile, UserInfo
from django.contrib.auth.models import User


# Create your views here.

# 用户登录函数
def user_login(request):
    # 如果请求是POSTl类型，接收表单，如果是GET，则返回登录页面
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        # 验证输入的合法性
        if login_form.is_valid():
            # 调用Django内置的登录验证
            cd = login_form.cleaned_data
            # 传入用户名和密码，不存在着返回空
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return HttpResponse('欢迎登录！')
            else:
                return HttpResponse('对不起，您的用户名或密码错误！')
        else:
            return HttpResponse('登录无效！')
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'account/login.html', {'form': login_form})

# 用户注册函数
# def register(request):
#     if request.method == 'POST':
#         user_form = RegistrationFrom(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(user_form.cleaned_data['password'])
#             new_user.save()
#             return HttpResponse('注册成功！')
#         else:
#             return HttpResponse('对不起，你不能注册。')
#     else:
#         user_form = RegistrationFrom()
#         return render(request, 'account/register.html', {'form': user_form})


def register(request):
    if request.method == 'POST':
        user_form = RegistrationFrom(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        # print(user_form, ':', userprofile_form)
        # print(user_form.is_valid())
        # print(userprofile_form.is_valid())
        if user_form.is_valid() * userprofile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            UserInfo.objects.create(user=new_user)
            return HttpResponse('注册成功！')
        else:
            return HttpResponse('注册失败！')
    else:
        user_form = RegistrationFrom()
        userprofile_form = UserProfileForm()
        return render(request, 'account/register.html', {'form': user_form, 'profile': userprofile_form})

# 个人信息视图函数
# 执行前要判断该用户是否登录，所以加上login_required装饰函数，将没有登录的用户跳转到登录页面
@login_required(login_url='/account/login')
def myself(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=user)
    userinfo = UserInfo.objects.get(user=user)

    return render(request, 'account/myself.html', {'user': user, 'userinfo':userinfo, 'userprofile':userprofile})

# 编辑个人视图
# 执行前要判断该用户是否登录，所以加上login_required装饰函数，将没有登录的用户跳转到登录页面
@login_required(login_url='/account/login')
def myself_edit(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user)

    if request.method == 'POST':
        user_from = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)
        if user_from.is_valid() * userprofile_form.is_valid() * userinfo_form.is_valid():
            user_cd = user_from.cleaned_data
            userprofile_cd = userprofile_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data
            print(user_cd['email'])
            user.email = user_cd['email']
            userprofile.birth = userprofile_cd['birth']
            userprofile.phone = userprofile_cd['phone']
            userinfo.school = userinfo_cd['school']
            userinfo.company = userinfo_cd['company']
            userinfo.profession = userinfo_cd['procession']
            userinfo.address = userinfo_cd['address']
            userinfo.aboutme = userinfo_cd['aboutme']
            user.save()
            userprofile.save()
            userinfo.save()
        return HttpResponseRedirect('/account/my-information/')
    else:
        user_form = UserForm(instance=request.user)
        userprofile_form = UserProfileForm(initial={'birth': userprofile.birth,
                                                    'phone': userprofile.phone})
        userinfo_form = UserInfoForm(initial={'school': userinfo.school,
                                              'company': userinfo.company,
                                              'profession': userinfo.profession,
                                              'address': userinfo.address,
                                              'aboutme': userinfo.aboutme})
        return render(request, 'account/myself_edit.html',
                      {'user_form': user_form,
                       'userprofile_form': userprofile_form,
                       'userinfo_form': userinfo_form})