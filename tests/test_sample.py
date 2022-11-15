gapBetweenPanel = 5
panelIlgis = 165 + gapBetweenPanel
panelPlotis = 99 + gapBetweenPanel
norimasPlotas = panelIlgis * panelPlotis
def panelPlot():

  plotOfPanel = panelIlgis * panelPlotis
  return plotOfPanel

def test_answer():
    gautasPlotas = panelPlot()
    assert gautasPlotas == norimasPlotas