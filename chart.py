from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin, Rect
from reportlab.lib import colors
from reportlab.lib.colors import PCMYKColor
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import *
from reportlab.rl_config import defaultPageSize

PAGE_HEIGHT=defaultPageSize[1]
styles = getSampleStyleSheet()
Title = Paragraph("COST OF LIVING ", styles["Heading1"])

drawing = Drawing(400, 200)
data = [
 (1300, 5000, 2000, 2200, 3700, 4500, 1900, 4000, 5000, 2000, 4600, 3800,
  2300, 2100, 6000, 1400),(1900, 4000, 5000, 2000, 4600, 3800,
   2300, 2100, 6000, 1400, 1300, 5000, 2000, 2200, 3700, 4500)
]
catNames = 'Jan-2016 Feb-2016 Mar-2016 Apr-2016 May-2016 Jun-2016 Jul-2016 Aug-2016 Sep-2016 Oct-2016 Nov-2016 Dec-2016 Jan-2017 Feb-2017 Mar-2017 Apr-2017'.split(' ')

lc = HorizontalLineChart()
lc.x = 50
lc.y = 50
lc.height = 125
lc.width = 400
lc.data = data
lc.joinedLines = 1
lc.background = Rect(0, 0, 400, 125, strokeWidth=0, fillColor=PCMYKColor(10,0,50,0))
lc.categoryAxis.categoryNames = catNames
lc.categoryAxis.labels.boxAnchor = 'ne'
lc.valueAxis.valueMin = 0
lc.valueAxis.valueMax = 6000
lc.valueAxis.valueStep = 1000
lc.categoryAxis.labels.dx = 8
lc.categoryAxis.labels.dy = -2
lc.categoryAxis.labels.angle = 30
lc.valueAxis.labelTextFormat = '%0.2f'
lc.lines[0].strokeWidth = 0
lc.lines[1].strokeWidth = 0
lc.lines[0].strokeColor = colors.green
lc.lines[1].strokeColor = colors.red
lc._inFill = 1
drawing.add(lc)
Elements = [Title, drawing]

def go():
   doc = SimpleDocTemplate('chart.pdf')
   doc.build(Elements)

go()
