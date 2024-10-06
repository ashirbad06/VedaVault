from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Home route for testing
def home(request):
    return HttpResponse("Welcome to VedaVault!")

# Endpoint to return services (can be mocked or fetched from Flask microservice)
def services(request):
    # Option to fetch data from Flask microservice via HTTP
    # Or mock the service data as below
    services_list = [
        {'plan': 'Basic', 'description': 'Includes fundamental strategies and access to resources.', 'price': 10},
        {'plan': 'Standard', 'description': 'Includes advanced strategies and personalized services.', 'price': 20},
        {'plan': 'Premium', 'description': 'Complete access to all services with 24/7 support.', 'price': 50}
    ]
    return JsonResponse(services_list, safe=False)

# Endpoint to process contact form data
def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Process the contact form data
        response_message = f"Thank you, {name}! We will get back to you soon."
        return JsonResponse({'message': response_message})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
