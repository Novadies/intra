from django.contrib.flatpages.models import FlatPage
from django.core.cache import cache
from django.http import JsonResponse
from django.contrib.flatpages.middleware import FlatpageFallbackMiddleware
from django.conf import settings

from logs.logger import logger


class YourMiddlewareClass:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.debug(f'Вызвано {request}')
        response = self.get_response(request)
        return response

    @staticmethod
    def process_view(request, view_func, view_args, view_kwargs):
        """ Вызывается непосредственно перед тем, как Django вызывает представление """
        if hasattr(request, 'user') and request.user.is_authenticated:
            backend_name = request.session.get('_auth_user_backend')
            if backend_name:
                logger.debug(f'Использован бэкенд аутентификации: {backend_name}')

    def process_exception(self, request, exception)-> JsonResponse:
        """ Стандартная функция обработки исключений в случае Json ответов"""
        if not settings.DEBUG:
            response_data = {'success': False, 'errorMessage': str(exception)}
            status = 400
            logger.warning(f'Исключение обрабатываемое в Мидлвеар, {response_data["errorMessage"]}')
            return self._response(response_data, status=status)

    @staticmethod
    def _response(data:str, *, status:int) -> JsonResponse:
        """ Формирование Json ответа """
        return JsonResponse(
            data,
            status=status,
            safe=not isinstance(data, list),
            json_dumps_params={'ensure_ascii': False, 'indent': 2},)

