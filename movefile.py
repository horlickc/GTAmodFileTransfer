import os



def move(a, b):
	return os.rename(a, b)

def swap(a, b):
	return os.rename(b, a)

try:
	mods = "C:/Program Files (x86)/Steam/steamapps/common/Grand Theft Auto V/mods"
	nmods = "C:/Users/horlickc_/Documents/gtamodbackup/mods"
	move(mods, nmods)
except:
	swap(mods, nmods)

try:
	scripts = "C:/Program Files (x86)/Steam/steamapps/common/Grand Theft Auto V/scripts"
	nscripts = "C:/Users/horlickc_/Documents/gtamodbackup/scripts"
	move(scripts, nscripts)
except:
	swap(scripts, nscripts)
	
try:
	dinput8 = "C:/Program Files (x86)/Steam/steamapps/common/Grand Theft Auto V/dinput8.dll"
	ndinput8 = "C:/Users/horlickc_/Documents/gtamodbackup/dinput8.dll"
	move(dinput8, ndinput8)
except:
	swap(dinput8, ndinput8)
	
try:
	opencamerav = "C:/Program Files (x86)/Steam/steamapps/common/Grand Theft Auto V/openCameraV.asi"
	nopencamerav = "C:/Users/horlickc_/Documents/gtamodbackup/openCameraV.asi"
	move(opencamerav, nopencamerav)
except:
	swap(opencamerav, nopencamerav)

try:
	tnopencamerav = "C:/Program Files (x86)/Steam/steamapps/common/Grand Theft Auto V/openCameraV.log"
	ntnopencamerav = "C:/Users/horlickc_/Documents/gtamodbackup/openCameraV.log"
	move(tnopencamerav, ntnopencamerav)
except:
	swap(tnopencamerav, ntnopencamerav)
	
try:
	openiv = "C:/Program Files (x86)/Steam/steamapps/common/Grand Theft Auto V/OpenIV.asi"
	nopeniv = "C:/Users/horlickc_/Documents/gtamodbackup/OpenIV.asi"
	move(openiv, nopeniv)
except:
	swap(openiv, nopeniv)
	
try:
	topeniv = "C:/Program Files (x86)/Steam/steamapps/common/Grand Theft Auto V/OpenIV.log"
	ntopeniv = "C:/Users/horlickc_/Documents/gtamodbackup/OpenIV.log"
	move(topeniv, ntopeniv)
except:
	swap(topeniv, ntopeniv)
	
try:
	shv = "C:/Program Files (x86)/Steam/steamapps/common/Grand Theft Auto V/ScriptHookV.dll"
	nshv = "C:/Users/horlickc_/Documents/gtamodbackup/ScriptHookV.dll"
	move(shv, nshv)
except:
	swap(shv, nshv)
	
try:
	tshv = "C:/Program Files (x86)/Steam/steamapps/common/Grand Theft Auto V/ScriptHookV.log"
	ntshv = "C:/Users/horlickc_/Documents/gtamodbackup/ScriptHookV.log"
	move(tshv, ntshv)
except:
	swap(tshv, ntshv)
	
try:
	shvdn = "C:/Program Files (x86)/Steam/steamapps/common/Grand Theft Auto V/ScriptHookVDotNet.asi"
	nshvdn = "C:/Users/horlickc_/Documents/gtamodbackup/ScriptHookVDotNet.asi"
	move(shvdn, nshvdn)
except:
	swap(shvdn, nshvdn)
	
try:
	dshvdn = "C:/Program Files (x86)/Steam/steamapps/common/Grand Theft Auto V/ScriptHookVDotNet2.dll"
	ndshvdn = "C:/Users/horlickc_/Documents/gtamodbackup/ScriptHookVDotNet2.dll"
	move(dshvdn, ndshvdn)
except:
	swap(dshvdn, ndshvdn)

try:
	tshvdn = "C:/Program Files (x86)/Steam/steamapps/common/Grand Theft Auto V/ScriptHookVDotNet2.log"
	ntshvdn = "C:/Users/horlickc_/Documents/gtamodbackup/ScriptHookVDotNet2.log"
	move(tshvdn, ntshvdn)
except:
	swap(tshvdn, ntshvdn)
	
try:
	ent = "C:/Program Files (x86)/Steam/steamapps/common/Grand Theft Auto V/EnhancedNativeTrainer.asi"
	nent = "C:/Users/horlickc_/Documents/gtamodbackup/EnhancedNativeTrainer.asi"
	move(ent, nent)
except:
	swap(ent, nent)
	
print("All items have been moved!!")

