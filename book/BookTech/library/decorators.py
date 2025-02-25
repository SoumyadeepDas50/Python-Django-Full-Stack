import time 
from functools import wraps
from django.http import HttpResponse

def log_execution_time(view_func):
    @wraps(view_func)
    def _wrapped_view(request,*args,**kwargs):
        start_time=time.time()
        response=view_func(request,*args,**kwargs)
        end_time=time.time()
        execution_time=end_time-start_time
        print(f"Execution time for {view_func.__name__}:{execution_time}seconds")
        return response
    return _wrapped_view