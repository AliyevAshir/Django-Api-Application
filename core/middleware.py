from django.http import JsonResponse

class BlockIPMiddleware:
    BLOCKED_IPS = ['192.168.137.143']  # Example blocked IPs

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.META['REMOTE_ADDR'] in self.BLOCKED_IPS:
            return JsonResponse({'error': 'Access denied.'}, status=403)
        return self.get_response(request)
from django.utils.deprecation import MiddlewareMixin

class LogIPMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        print(f"IP Address: {ip}")  # Konsola yazdırma
        # Burada IP'yi bir veritabanına kaydedebilirsiniz