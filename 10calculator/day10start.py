#Functions with outputs

def format_name(fName,lName):
    #print ((fName.lower()).title() + " " + (lName.lower()).title())
    fNameFormatted = (fName.lower()).title()
    lNameFormatted = (lName.lower()).title()
    return (f"{fNameFormatted} {lNameFormatted}")

print(format_name("joe", "test"))