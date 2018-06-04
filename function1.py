glovar=0
def set_globvar_to_one():
	global glovar
	glovar=1
def print_globvar():
	print(glovar)

set_globvar_to_one()
print(glovar)
print_globvar()