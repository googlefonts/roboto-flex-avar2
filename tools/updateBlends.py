import ufoProcessor
import json

myPath = "../source/Parametric-avar2/Roboto-Delta.designspace"

doc = ufoProcessor.DesignSpaceProcessor()

doc.read(myPath)

blends = {}

for instance in doc.instances:
    
    print( '\t\t"' + instance.styleName + '": {')
    
    blend ={}
     
    for location in instance.designLocation:
        
        if location == "Optical size" or location == "Slant" or location == "Weight" or location == "Width":
            pass
        else:
            print ('\t\t\t"' + location + '"' + ": " + str(instance.designLocation[location]) + ",")
    
    print("\t\t},")
    
#print ( blends )
    
#print(json.dumps(blends, indent = 4))