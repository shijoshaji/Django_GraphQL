# NOTE: descibes our data models
import graphene
from django.db.models import fields
from graphene_django import DjangoObjectType

from .models import Books


class BooksType(DjangoObjectType):
    class Meta:
        model = Books
        fields=('title','id','body')
        
class Query(graphene.ObjectType):
    all_books = graphene.List(BooksType)
    selected_books = graphene.List(BooksType, title = graphene.String(required=True))
   
    def resolve_all_books(root,info):
        return Books.objects.all()
    
    def resolve_selected_books(root,info,title):
        return Books.objects.filter(title=title)
    
schema = graphene.Schema(query=Query) 
