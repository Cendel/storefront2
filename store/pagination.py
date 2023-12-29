from rest_framework.pagination import PageNumberPagination

# we create a custom pagination class:


class DefaultPagination(PageNumberPagination):
    page_size = 10
