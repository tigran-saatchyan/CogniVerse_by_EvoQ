from rest_framework.pagination import PageNumberPagination


class CoursesPaginator(PageNumberPagination):
    """
    Paginator for the list of courses.

    This paginator is used to paginate the list of courses in the API
    responses.
    It supports page navigation and allows clients to specify the number of
    items per page.

    Attributes:
        page_size (int): The default number of courses to include on each page.
        page_size_query_param (str): The query parameter used to specify the
        number of items per page.
        max_page_size (int): The maximum number of items per page that a
        client can request.

    Note:
        - The 'page_size' attribute determines the default page size for
        pagination.
        - The 'page_size_query_param' attribute allows clients to override
        the default page size in the URL.
        - The 'max_page_size' attribute restricts the maximum page size to
        prevent excessive data retrieval.

    Usage:
        - Use this paginator class in conjunction with list views to
        paginate and control the number of
          course items returned in API responses.
    """

    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10
