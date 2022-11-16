
from graphics import *
import math
# TODO: make the dimensions of the roof bigger
# TODO: equally make the fircode and other restraints bigger

# Roof face points need to be written clock-wise, meaning [0,0] is the bottom-left corner, [0,300] is the top-left corner, etc.
roofPoint = [
  [0, 0],
  [0, 300],
  [300, 300],
  [300, 0],
]

changedRoofPoint = []
changedRoofPoint.extend(roofPoint)

chimneys = []
skylights =[]
fireCode = 20
gapBetweenPanel = 5
gapFromRoofEdges = 15

solarPanelLength = 165
solarPanelWidth = 99

def panelArea():
  panelL = solarPanelLength + gapBetweenPanel
  panelW = solarPanelWidth + gapBetweenPanel

  areaOfPanel = panelL * panelW
  return areaOfPanel

def addFireProtocol(originalRoof):
  originalRoof[1][1] = originalRoof[1][1] - fireCode
  originalRoof[2][1] = originalRoof[2][1] - fireCode 
  return originalRoof


def calculateRoofWithGapsFromEdge(originalRoof):
  for j in range(0, 2):
    for i in range(0,4):
      if(j == 0 ):
        if(i < 2):
          originalRoof[i][j] = originalRoof[i][j] + gapFromRoofEdges
        else: originalRoof[i][j] = originalRoof[i][j] - gapFromRoofEdges
      else:
        if(i % 3 == 0):
          originalRoof[i][j] = originalRoof[i][j] + gapFromRoofEdges
        else:
          originalRoof[i][j] = originalRoof[i][j] - gapFromRoofEdges
  
  return originalRoof

def amountOfPanelsOnTheRoof():
  if(fireCode > 0):
    fireCodeRoof = addFireProtocol(roofPoint)
    changedRoofPoint = calculateRoofWithGapsFromEdge(fireCodeRoof)
  else: changedRoofPoint = calculateRoofWithGapsFromEdge(roofPoint)
  print(changedRoofPoint)

  roofWidth = math.sqrt(math.pow((changedRoofPoint[1][0] - changedRoofPoint[0][0]) + (changedRoofPoint[1][1] - changedRoofPoint[0][1]),2))
  roofLength = math.sqrt(math.pow((changedRoofPoint[3][0] - changedRoofPoint[0][0]) + (changedRoofPoint[3][1] - changedRoofPoint[0][1]),2))
  
  amountOfLines = math.floor(roofWidth / (solarPanelWidth + gapBetweenPanel))
  amountofPanelsInOneLine = math.floor(roofLength / (solarPanelLength + gapBetweenPanel))

  amountofPanels = amountOfLines * amountofPanelsInOneLine
  return amountofPanels



# TODO: check why the original array for roofPoint is being changed inside the function - it shouldn't
print("ROOFBEFORE: ", roofPoint)
print("ROOFAFTER: ", roofPoint)
amountOfPanelsOnTheRoof()



# TODO: fix this function too

def main():
  win = GraphWin("Solar Panel Placement Tool - Area3", 700, 800)
  roof = Rectangle(Point(0,0), Point(300,300))
  roof1 = Rectangle(Point(changedRoofPoint[0][0], changedRoofPoint[0][1]), Point(changedRoofPoint[2][0], changedRoofPoint[2][1]))
  solarPanel = Rectangle(Point(changedRoofPoint[0][0], changedRoofPoint[0][1]), Point(99, 165))
  solarPanel1 = Rectangle(Point(changedRoofPoint[0][0] + (99 + gapBetweenPanel), changedRoofPoint[0][1]), Point(99 + (99 + gapBetweenPanel), 165))
  # rec2.setFill('red')
  roof1.setFill('green')
  roof.draw(win)
  roof1.draw(win)
  solarPanel.draw(win)
  solarPanel1.draw(win)
  # rec2.draw(win)
  win.getMouse()
  win.close()

main()