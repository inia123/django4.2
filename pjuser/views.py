from django.http import JsonResponse
from django.views import View
from .models import PjUser
from django.contrib.auth import authenticate, login
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            confirm_password = data.get('confirm_password')
            email = data.get('email')
            qq = data.get('qq')
            wechat = data.get('wechat')
            mobile = data.get('mobile')

            if not username or not password or not confirm_password or not email:
                return JsonResponse({'error': '用户名、密码和邮箱不能为空！'}, status=400)

            if password != confirm_password:
                return JsonResponse({'error': '两次密码不一致！'}, status=400)

            if PjUser.objects.filter(username=username).exists():
                return JsonResponse({'error': '用户名已经存在！'}, status=400)

            if PjUser.objects.filter(email=email).exists():
                return JsonResponse({'error': '邮箱已经存在！'}, status=400)

            user = PjUser(username=username, email=email, qq=qq, wechat=wechat, mobile=mobile)
            user.set_password(password)
            user.save()

            response = JsonResponse({'message': '注册成功！'})
            response["Access-Control-Allow-Origin"] = "*"
            return response

        except json.JSONDecodeError:
            return JsonResponse({'error': '请求体不是有效的JSON！'}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = JsonResponse({'message': '登录成功！'}, status=200)
            response["Access-Control-Allow-Origin"] = "*"
            return response
        else:
            return JsonResponse({'error': '用户名或密码错误！'}, status=400)

