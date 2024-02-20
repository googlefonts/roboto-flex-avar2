from fontTools.designspaceLib import DesignSpaceDocument, AxisDescriptor, SourceDescriptor, InstanceDescriptor, AxisMappingDescriptor
import ufoProcessor
from lxml import etree

myPath = "source/Parametric-avar2/RobotoAvar2-avar1.designspace"

doc = ufoProcessor.DesignSpaceProcessor()

doc.read(myPath)

tag_fence = "XOPQ"

tag_opsz = "Optical size"
tag_width = "Width"
tag_weight = "Weight"

fences_designspace = "tools/fenceLocation.designspace"

for instance in doc.instances:
    
    if instance.designLocation[tag_opsz] == 144.0  and instance.designLocation[tag_width] == 100 and instance.designLocation[tag_weight] == 100:
        
        #print ( instance )
        
        m1 = AxisMappingDescriptor()
        
        m1.inputLocation = { tag_opsz : instance.designLocation[tag_opsz],
        				     tag_width : instance.designLocation[tag_width],
        				     tag_weight : instance.designLocation[tag_weight],
        				     tag_fence : instance.designLocation[tag_fence],
         }
        
        for location in instance.designLocation:
            
            #print ('\t\t\t"' + location + '"' + ": " + str(instance.designLocation[location]) + ",")
            #m1.inputLocation = {k: v for k, v in instance.designLocation.items()}
            m1.outputLocation = {k: v for k, v in instance.designLocation.items()}
        
        #print ( m1 )
        
        designspace = DesignSpaceDocument()
        
        designspace.addAxisMapping(m1)
        
        designspace.write(fences_designspace)