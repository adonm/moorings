
import traceback
import os
import datetime
import base64
import geojson
from six.moves.urllib.parse import urlparse
from wsgiref.util import FileWrapper
from django.db.models import Q, Min
from django.db import transaction
from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError
from django.conf import settings
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from rest_framework import viewsets, serializers, status, generics, views
from rest_framework.decorators import detail_route, list_route, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, BasePermission
from rest_framework.pagination import PageNumberPagination
from datetime import datetime, timedelta
from collections import OrderedDict
from django.core.cache import cache
from ledger.accounts.models import EmailUser, Address 
from ledger.address.models import Country
from datetime import datetime, timedelta, date
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from wildlifecompliance.components.returns.utils import _is_post_data_valid,_get_table_rows_from_post,_create_return_data_from_post_data
from wildlifecompliance.components.returns.models import (
   Return
)
from wildlifecompliance.components.returns.serializers import (
    ReturnSerializer
)


class ReturnViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ReturnSerializer
    queryset = Return.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset() 
        # Filter by org
        org_id = request.GET.get('org_id',None)
        if org_id:
            queryset = queryset.filter(application__applicant_id=org_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @list_route(methods=['GET',])
    def user_list(self, request, *args, **kwargs):
        qs = self.get_queryset().exclude(processing_status='future')
        
        serializer = ReturnSerializer(qs, many=True)
        return Response(serializer.data)

    @detail_route(methods=['POST',])
    @renderer_classes((JSONRenderer,))
    def update_details(self, request, *args, **kwargs):
        try:
            print("print from api")
            print(self.request.data)
            print("==========posting keys=========")
            print(request.POST.keys())
            print("============printing getlist")
            for key in request.POST.keys():
                print(key)
                print(request.POST.getlist(key))
            

            instance = self.get_object()
            returns_tables=self.request.data.get('table_name')
            print("===========Returns table=====")
            # print(type(returns_tables.encode('utf-8')))
            print(returns_tables)
            # list_returns_tables=eval(returns_tables)
            # print(eval(returns_tables))
            # print(returns_tables['name'])
            if _is_post_data_valid(instance, returns_tables.encode('utf-8'), request.POST):
                print('True')
                _create_return_data_from_post_data(instance, returns_tables.encode('utf-8'), request.POST)
            # amend_data=self.request.data
            # reason=amend_data.pop('reason')
            # application =amend_data.pop('application')
            # text=amend_data.pop('text')
            # activity_type_id=amend_data.pop('activity_type_id')
            # print(type(application))
            # print(application)
            # for item in activity_type_id:
            #     data={
            #         'application':application,
            #         'reason': reason,
            #         'text':text,
            #         'licence_activity_type':item
            #     }
            #     serializer = self.get_serializer(data= data)
            #     serializer.is_valid(raise_exception = True)
            #     instance = serializer.save()
            #     instance.generate_amendment(request)
            # serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except serializers.ValidationError:
            print(traceback.print_exc())
            raise
        except ValidationError as e:
            if hasattr(e,'error_dict'):
                raise serializers.ValidationError(repr(e.error_dict))
            else:
                print e
                raise serializers.ValidationError(repr(e[0].encode('utf-8')))
        except Exception as e:
            print(traceback.print_exc())
            raise serializers.ValidationError(str(e))
