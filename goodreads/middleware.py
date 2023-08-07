# class SimpleMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         # One-time configuration and initialization.

#     def __call__(self, request):
#         print("==========================================")
#         print(f"{request.path}")
#         print("==========================================")

#         response = self.get_response(request)
#         print("==========================================")
#         print(f"{request.path}")
#         print("==========================================")

#         # Code to be executed for each request/response after
#         # the view is called.

#         return response