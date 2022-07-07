from django.shortcuts import render
from core.models import Products


def product_list(request):
    product = Products.objects.all()
    return render(
        request,
        'main.html',
        {
            'products': product
        }
    )
from django.shortcuts import render
from django.http import JsonResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, parsers

from core.models import Products, EmpLoyee, Category
from core.serializers import ProductSerializer
from core.forms import CategoryForms,  EmployeeForms



def product_list(request):
#request принимает запрос
# render  перевод с русского языка. Оказывать
    items = Products.objects.all()
    return render(
        request,
        'main.html',
        {
            'products': items
        }
    )


def employee_list(request):
    employee = EmpLoyee.objects.all()
    return render(
        request,
        'employee.html',
        {
            'employee': employee
        }
    )
@csrf_exempt
def product_list_api(request):
    """
        List all courses or create a new course
    """
    if request.method == 'GET':
        product = Products.objects.all()
        serializer = ProductSerializer(instance=product, many=True)
        return JsonResponse(data=serializer.data, safe=False, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = parsers.JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryCreateView(generic.CreateView):
    model = Category
    form_class = CategoryForms
    template_name ='category.html'
    success_url = '/category/create/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        context['category'] = category
        return context

