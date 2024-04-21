from error_proxy import error_proxy


class argument_exception:
    __inner_error:error_proxy=error_proxy()

    def __init__ (Self,*args:object):
        super().__init__(*args)
        Self.__inner_error.create_error(Self)
    
    @property
    def error(self):
        return self.__inner_error
    

class operation_exception(argument_exception):
    pass