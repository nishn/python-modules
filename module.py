#!/usr/bin/env python
# coding: UTF-8


# arguments checker
# reference http://tnakamura.hatenablog.com/entry/20110328/python_inspect

def set_type( **kwargs ):                            # <== decolator
    def middle( func ):                              # <== returned once and will be called immediately
        def arg_check( *func_args, **func_kwargs ):  # <== this will be the function itself
            import inspect                           #     and substituted to 'func'

            # get argument list of func
            args     = inspect.getargspec( func ).args
            tmp_args = func_args + inspect.getargspec( func ).defaults

            # create complete dictionary of kwargs
            for i in range( min(len(tmp_args), len(args)) - len(func_kwargs.keys())):
                func_kwargs[args[i]] = tmp_args[i]
            
            # check arguments type
            for name in kwargs.keys():               # <== check list
                if name in func_kwargs.keys() and not isinstance( func_kwargs[name], kwargs[name] ):
                    raise TypeError( '%s ( "%s", %s is given ) should be of %s.' %
                                     ( name, func_kwargs[name], type(func_kwargs[name]), kwargs[name] ) )
                    
            return func( **func_kwargs ) # <== arg_check
        return arg_check                             # <== middle
    return middle                                    # <== set_type


# func = set_type( kw )( func )



# test
if __name__ == "__main__":
    @set_type( **{ 'x' : int, 'y' : int, 'string' : str } )
    def testfunc( x, y = 0, string = "" ):
        print "x = " + str(x) + ", y = " + str(y) + ", string = " + string

    # ok
    testfunc( 3 )
    testfunc( 3, 4, 'b' )
    testfunc( 2, y = 9, string = '2' )
    testfunc( 33, string = 'sldkfjlskdfjlksdjflskdjf' )
    testfunc( 2, 6, string = 'abc' )
    
    # error
#    testfunc( 'a' )
#    testfunc( x = 's', y = 3, string = 3 )
