import math

fireCode = 50
gapBetweenPanels = 10 / 2
gapFromRoofEdges = 15
roofWidth = 1000
roofLength = 2000
panelLength = 165 + gapBetweenPanels
panelWidth = 99 + gapBetweenPanels

def test_howManyFits():
    
    amountOfSolarPanels = 106
    plotOfSolarPanels = (panelLength * panelWidth) * amountOfSolarPanels
    plotOfTheRoof = (roofWidth - 2 * gapFromRoofEdges) * (roofLength - fireCode - gapFromRoofEdges)
    assert (plotOfTheRoof >= plotOfSolarPanels)

def test_vertical():

    amountOfSolarPanels = 90
    numberOfRows = math.floor((roofWidth - 2 * gapFromRoofEdges) / panelLength)
    realRoofLength = roofLength - fireCode - gapFromRoofEdges
    amountOfSolarPanelsInARow = math.floor(realRoofLength / panelWidth)
    assert (amountOfSolarPanelsInARow * numberOfRows >= amountOfSolarPanels)

def test_horizontal():

    amountOfSolarPanels = 99
    numberOfRows = math.floor((roofWidth - 2 * gapFromRoofEdges) / panelWidth)
    realRoofLength = roofLength - fireCode - gapFromRoofEdges
    amountOfSolarPanelsInARow = math.floor(realRoofLength / panelLength)
    assert (amountOfSolarPanelsInARow * numberOfRows >= amountOfSolarPanels)
