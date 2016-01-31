from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Expense,
    )

class ExpenseViews(object):
    def __init__(self, request):

        self.request = request
        #send_mail(request)


    @view_config(route_name='view_expense', renderer="templates/site_view.pt")
    def view_expense(self):

        return {'project':'pybudget'}

    @view_config(route_name='edit_expense', renderer="templates/site_view.pt")
    def edit_expense(self):
        return {'one':'one'}

    @view_config(route_name='add_expense', renderer="templates/site_view.pt")
    def add_expense(self):
        return {'one':'one'}


@view_config(route_name='view_budget', renderer='templates/mytemplate.pt')
def my_view(request):
    try:
        one = DBSession.query(Expense).filter(Expense.expense_date == '2016-01-31').all()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'one': one, 'project': 'pybudget'}


conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_pybudget_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

