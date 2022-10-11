from rest_framework.pagination import PageNumberPagination


class MyDisptachListPagination(PageNumberPagination):
    page_size = 10