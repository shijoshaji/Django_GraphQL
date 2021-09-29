
from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from books.schema import schema
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # NOTE: Only a single URL to access GraphQL
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))), # NOTE: Change graphiql=True to graphiql=False if you do not want to use the GraphiQL API browser.

]




    