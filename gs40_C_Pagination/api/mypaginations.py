# from rest_framework.pagination import PageNumberPagination
# from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import CursorPagination

class MyCursorPagination(CursorPagination):
    page_size = 3
    ordering = 'name'
    cursor_query_param = 'cur'


# class MyLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 5
#     limit_query_param = 'mylimit'
#     offset_query_param = 'myoffset'
#     max_limit = 6



# class MyPageNumberPagination(PageNumberPagination):
#     page_size = 5
#     page_query_param = 'pg'
#     page_size_query_param = 'records'
#     max_page_size = 7
#     last_page_strings = 'end'