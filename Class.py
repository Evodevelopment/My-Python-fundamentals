class
define objects
finish your old exercise

Do new one on Udemy

define class (__init__)
  character
  atribute
  different atribute

#Example:
#Lets say my class has many methods, and I want to apply my decorator on each one of them, later when I add new methods, 
#I want the same decorator to be applied, but I dont want to write @mydecorator above the method declaration all the time?

#If I look into __call__ is that the right way to go?

#IMPORTANT: the example below appears to be solving a different problem than the original question asked about.

#EDIT: Id like to show this way, which is a similar solution to my problem for anyobody finding this question later, using a mixin as 
#mentioned in the comments.

class WrapinMixin(object):
    def __call__(self, hey, you, *args):
        print 'entering', hey, you, repr(args)
        try:
            ret = getattr(self, hey)(you, *args)
            return ret
        except:
            ret = str(e)
            raise
        finally:
            print 'leaving', hey, repr(ret)
          
#Then you can in another

class Wrapmymethodsaround(WrapinMixin): 
    def __call__:
         return super(Wrapmymethodsaround, self).__call__(hey, you, *args)

#source URL: https://stackoverflow.com/questions/6307761/how-to-decorate-all-functions-of-a-class-without-typing-it-over-and-over-for-eac

