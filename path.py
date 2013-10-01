from mysys import *

root=shell("pwd")[0]
user=shell("locate -b User | grep "+root)[0]
