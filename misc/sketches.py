
# show available memory
import gc
gc.collect()
gc.mem_free()

# show available storage
def df():
  import os
  s = os.statvfs('//')
  return ('{0} MB'.format((s[0]*s[3])/1048576))