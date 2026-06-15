import logging
from django.http import HttpRequest, HttpResponse

logger = logging.getLogger("metrics")


class CustomHeaderMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        """The box of responses is updated with new values."""
        response = self.get_response(request)
        response["X-Project-Developer"] = "Zack"
        response["X-Learning-Source"] = "Hillel-Course-Practice"
        response["X-Custom-Security-Policy"] = "Active"
        return response


class RequestMetricsMiddleware:
    total_requests = 0

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        """Looking for updates to get into the logger file."""
        RequestMetricsMiddleware.total_requests += 1
        logger.info(
            f"Path: {request.path} | "
            f"Total requests since start: {RequestMetricsMiddleware.total_requests}"
        )
        response = self.get_response(request)
        return response