from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CalculationSerializer
from .services import CalculatorService

class CalculateView(APIView):
    def post(self, request):
        serializer = CalculationSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            operation = data['operation']
            a = data['a']
            b = data.get('b')

            try:
                if operation == 'add':
                    result = CalculatorService.add(a, b)
                elif operation == 'subtract':
                    result = CalculatorService.subtract(a, b)
                elif operation == 'multiply':
                    result = CalculatorService.multiply(a, b)
                elif operation == 'divide':
                    result = CalculatorService.divide(a, b)
                elif operation == 'power':
                    result = CalculatorService.power(a, b)
                elif operation == 'sqrt':
                    result = CalculatorService.sqrt(a)
                else:
                    return Response({"error": "Invalid operation"}, status=status.HTTP_400_BAD_REQUEST)

                return Response({"result": result}, status=status.HTTP_200_OK)

            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"error": "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HomeView(APIView):
    def get(self, request):
        return Response({
            "message": "Welcome to the Calculator API",
            "endpoints": {
                "calculate": "/api/calculate/"
            },
            "supported_operations": ["add", "subtract", "multiply", "divide", "power", "sqrt"],
            "example_payload": {
                "operation": "add",
                "a": 10,
                "b": 5
            }
        })

class CalculatorGUIView(APIView):
    def get(self, request):
        return render(request, 'calculator/index.html')
