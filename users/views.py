from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages


def new(request):
    return render(request, "users/new.html")


@require_POST
def create(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")

    try:
        # 建立新使用者
        User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        # 建立 profile

        # 認證信

        messages.success(request, f"歡迎加入有名小站，{username}！")
        return redirect("sessions:new")  # 導向登入頁面

    except Exception as e:
        messages.error(request, "註冊發生錯誤，請稍候再試")
        return redirect("users:new")
