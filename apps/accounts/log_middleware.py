from django.utils.deprecation import MiddlewareMixin


class RequestLog(MiddlewareMixin):
    def process_request(self, request):
        import logging
        parameter = ''
        if request.method == 'GET':
            parameter = request.GET
        if request.method == 'POST':
            parameter = request.POST
        logger = logging.getLogger('django')
        message =  '账号: ' + str(request.session.get('user')) + ' 请求路径: ' + str(request.path) + ' 请求方式: ' + str(request.method) + '  请求参数: '+ str(parameter)
        logger.info(message)
