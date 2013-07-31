import os
import ctypes
from pyobjus import autoclass, dereference, load_usr_lib

load_usr_lib('usrlib.dylib', usr_path=False)
Car = autoclass('Car')
car = Car.alloc().init()

# In pyobjus you can use properties in the same way as in native objective c
# So if we have property defined on this way:
# @property (assign) int propInt;
# .
# .
# .
# @synthesize propInt;

# You can assign some value to property on this way
car.propInt = 12345

# So, after assigning you can see actual value of property:
print car.propInt

# If you have property which is pointer to some type, pyobjus also can deal with those properties
# @property (assign) double *propDoublePtr;
# .
# .
# .
# @synthesize propDoublePtr;
car.propDoublePtr = 345.543

# As you can see, you don't need to worry about dereferencing pointer when you asigning value, 
# pyobjus will do it for you :)
# After this you can get actual value on which pointer points
print dereference(car.propDoublePtr)

# But can pyobjus deal with @dynamic properties? Yes, it can
# @property (assign) NSString *propNsstringDyn;
# .
# .
# .
# @dynamic propNsstringDyn;
car.propNsstringDyn = autoclass('NSString').stringWithUTF8String_('test from python')

# And now, let we get value:
print car.propNsstringDyn.UTF8String()

# And what if I don't have default getter/setters for some property?
# Pyobjus also can deal with that
# @property (nonatomic, assign, getter = getPropIntGtr, setter = customSetPropInt:) int propIntCst;
# .
# .
# .
# @synthesize propIntCst = _prop_int_cst;
#
# - (int) getPropIntGtr {
#       return _prop_int_cst;
# }

# - (void) customSetPropInt:(int)prop_int_cst {
#       _prop_int_cst = prop_int_cst;
# }

# You set value on the same way as the previous ones:
car.propIntCst = 7654

# And get it also on the same way:
print car.propIntCst
