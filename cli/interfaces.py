from base.interfaces import InterfacesBase
from typing import Callable

class InterfacesCLI(InterfacesBase):
    def __init__( self, name ):
        self.set_name(name)
        self._value = {}
        self._result = {}
        self._list_get_value = {}
    
    def set_name( self, name ):
        self._name = name

    def get_name( self ):
        return self._name

    def _get_value( self, name, **kwargs  ):
        if "kwargs" in kwargs:
            kwargs = kwargs["kwargs"]

        func = lambda text : text 
        if "func" in kwargs:
            func = kwargs["func"]
        
        input_warning = f"masukkan nilai {name}: "
        if "inpur_warning" in kwargs:
            input_warning = kwargs["input_warning"]
        
        error_warning = ""
        if "error_warning" in kwargs:
            error_warning = kwargs["error_warning"]
        
        try:
            self._value[name] = func( input(input_warning).strip() )
        except ValueError:
            print(error_warning)
            return self._get_value( name, kwargs=kwargs )
        
    def _add_getter( self, name, options : dict ):
        if not "func" in options:
            options["func"] = lambda text : text

        if not "input_warning" in options:
            options["input_warning"] = f"masukkan nilai {name}:"
        
        if not "error_warning" in options:
            options["error_warning"] = "tidak bisa menkonversi input yang dilakukan"

        self._list_get_value[name] = {
            "func" : options["func"],
            "input_warning" : options["input_warning"],
            "error_warning" : options["error_warning"]
        }

    def add_func( self, name, func : Callable[ [ dict ], None ] ):
        if not name in self._result:
            self._result[name] = []

        self._result[name].append( func )

    def show_result( self ):
        for name, val in self._list_get_value.items():
            self._get_value( name, kwargs=val )
        for name, val in self._result.items():
            self._value["_name"] = name
            for func in val:
                print(f"{name} = { func(self._value) }")
