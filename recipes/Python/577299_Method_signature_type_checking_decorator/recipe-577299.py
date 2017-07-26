def typecheck(func):

   if not hasattr(func,'__annotations__'): return method

   import inspect
   argspec = inspect.getfullargspec(func)

   def check( t, T ):
      if type(T) == type: return isinstance(t,T)   #types
      else: return T(t)                            #predicates   

   def wrapper(*args):

      if len(argspec.args) != len(args):
         raise TypeError( "%s() takes exactly %s positional argument (%s given)"
                           %(func.__name__,len(argspec.args),len(args)) )

      for argname,t in zip(argspec.args, args):
         if argname in func.__annotations__:
            T = func.__annotations__[argname]
            if not check( t, T  ):
               raise TypeError(  "%s( %s:%s ) but received %s=%s"
                                 % (func.__name__, argname,T, argname,repr(t)) )

      r = func(*args)

      if 'return' in func.__annotations__:
         T = func.__annotations__['return']
         if not check( r, T ):
            raise TypeError( "%s() -> %s but returned %s"%(func.__name__,T,repr(r)) )
      
      return r

   return wrapper
