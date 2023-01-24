from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from Api.sterilizers import ProductSerializers,ProductModelserial,Userserilizer,CartSerilizer,ReviewSerilizer
from Api.models import Product,Carts,Review
from rest_framework import viewsets
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework import authentication,permissions


from rest_framework import generics
class Productview(APIView):
    def get(self,request,*args,**kwargs):
        print("hello world")
        qs=Product.objects.all()
        # print(qs)
        serializer=ProductModelserial(qs,many=True)
        # print(serializer.data)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serilaizer=ProductSerializers(data=request.data)
        if serilaizer.is_valid():
            # serilaizer.save()
            Product.objects.create(**serilaizer.validated_data)
            return Response(data=serilaizer.data)
        else:
            return Response(data=serilaizer.errors)

class ProductDetails(APIView):
    def get(self, request, *args, **kwargs):
        id=kwargs.get("id")
        qs=Product.objects.get(id=id)
        sterializer=ProductSerializers(qs,many=False)
        return Response(data=sterializer.data)

    def put(self, request, *args, **kwargs):
        id=kwargs.get("id")
        Product.objects.filter(id=id).update(**request.data)
        qs=Product.objects.get(id=id)
        serializer=ProductSerializers(qs,many=False)
        return Response(data=serializer.data)

    def delete(self, request, *args, **kwargs):
        id=kwargs.get("id")
        qs=Product.objects.filter(id=id).delete()
        return Response(data="delete product")
class Productdetailsview(viewsets.ModelViewSet):
    serializer_class = ProductModelserial
    queryset = Product.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # def list(self,request,*args,**kwargs):
    #     qs=Product.objects.all()
    #     serializer=ProductModelserial(qs,many=True)
    #     return Response(data=serializer.data)
    # def create(self,request,*args,**kwargs):
    #     serializer=ProductModelserial(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data)
    #     else:
    #         return Response(data=serializer.errors)
    # def retrieve(self,request,*args,**kwargs):
    #     id=kwargs.get('pk')
    #     qs=Product.objects.get(id=id)
    #     serializer=ProductModelserial(qs,many=False)
    #     return Response(data=serializer.data)
    # def destroy(self,request,*args,**kwargs):
    #     id=kwargs.get('pk')
    #     Product.objects.filter(id=id).delete()
    #     return Response('deleted')
    # def update(self,request,*args,**kwargs):
    #     id=kwargs.get('pk')
    #     obj=Product.objects.get(id=id)
    #     serializer=ProductModelserial(data=request.data,instance=obj)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return  Response(data=serializer.data)
    #     else:
    #         return Response(data=serializer.errors)
    @action(methods=["GET"],detail=False)
    def catagory(self,request,*args,**kwargs):
        ras=Product.objects.values_list("catagory",flat=True).distinct()
        return Response(data=ras)
    @action(methods=["POST"],detail=True)
    def addto_cart(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        item=Product.objects.get(id=id)
        user=request.user
        user.carts_set.create(product=item)
        return Response(data="item add to cart")

    @action(methods=["POST"], detail=True)
    def addto_review(self, request, *args, **kwargs):
        user=request.user
        id = kwargs.get("pk")
        item = Product.objects.get(id=id)
        serilizer=ReviewSerilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save(product=item,user=user)
            return Response(data=serilizer.data)
        else:
            return Response(data=serilizer.errors)

    @action(methods=["GET"], detail=True)
    def review(self,request,*args,**kwargs):
        product=self.get_object()
        qs=product.review_set.all()
        serilizer=ReviewSerilizer(qs,many=True)
        return Response(data=serilizer.data)



class UserView(viewsets.ModelViewSet):
    serializer_class = Userserilizer
    queryset = User.objects.all()
class CartView(viewsets.ModelViewSet):
    serializer_class = CartSerilizer
    queryset = Carts.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Carts.objects.filter(user=self.request.user)
    #
    # def list(self, request, *args, **kwargs):
    #     qs=request.user.carts_set.all()
    #     serilizer=CartSerilizer(qs,many=True)
    #     return Response(data=serilizer.data)


    #def create(self,request,*args,**kwargs):
        # serilizer=Userserilizer(data=request.data)
        # if serilizer.is_valid():
        #     serilizer.save()
        #     return Response(data=serilizer.data)
        # else:
        #     return Response(data=serilizer.errors)

class ReviewDeleteView(APIView):
    def delete(self,request,*args,**kwargs):
         id=kwargs.get("pk")
         Review.objects.filter(id=id).delete()
         return Response(data="deletereview")

