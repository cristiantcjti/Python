from django.shortcuts import render
from django.db.utils import IntegrityError
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse 
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Patient
import json
import logging

# Create your views here.

@csrf_exempt
@require_http_methods(["GET"]) 
def id_handbook(request, id_handbook):
    try:
        patient_data = Patient.objects.filter(id_handbook=id_handbook).values()
    except Patient.DoesNotExist():
        return JsonResponse({'message': ' Patient handbook not found.'}, status=404) 
    return JsonResponse(list(patient_data), safe=False)


@csrf_exempt
@require_http_methods(["POST"]) 
def register(request, rg, cpf):
        
        data = json.loads(request.body)

        handbook_cpf = Patient.objects.filter(cpf=cpf).values()
        if handbook_cpf:
            return JsonResponse({"message": 'CPF is already registered'}, status=200)

        handbook_rg = Patient.objects.filter(rg=rg).values()
        if handbook_rg:
            return JsonResponse({"message": 'RG is already registered'}, status=200)

        handbook = Patient(name=data['name'], surname=data['surname'] , birthday=data['birthday'], gender=data['gender'], 
        cpf=cpf, rg=rg, ufrg=data['ufrg'], email=data['email'], cellphone=data['cellphone'], 
        telephone=data['telephone'], medical_insurance=data['medical_insurance'], card_number=data['card_number'], card_validity=data['card_validity'])

        try: 
            handbook.save()  
        except Exception as error:
            logging.error(error)
            return JsonResponse({'message': 'Error when saving'}, status=500) 
        
        return JsonResponse({"message": 'Register created'}, status=201)
