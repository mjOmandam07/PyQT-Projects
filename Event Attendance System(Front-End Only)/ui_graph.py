from main import *


import sys, random
from PyQt5.QtChart import QChart, QChartView, QValueAxis, QBarCategoryAxis, QBarSet, QBarSeries
from PyQt5.Qt import Qt


class UIGraph(MainWindow):
    def statBar(self):
        set0 = QBarSet('X0')

        set0.append([random.randint(0, 10) for i in range(6)])
       
        series = QBarSeries()
        series.append(set0)
        

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle('Bar Chart Kunuhay')
        chart.setAnimationOptions(QChart.SeriesAnimations)

        months = ('Q', 'W', 'E', 'R', 'T', 'Y')

        axisX = QBarCategoryAxis()
        axisX.append(months)

        axisY = QValueAxis()
        axisY.setRange(0, 15)

        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartView = QChartView(chart)

    

        self.ui.stat_graph_verticalLayout.addWidget(chartView)


    def conCheckBar(self):
        set0 = QBarSet('X0')

        set0.append([random.randint(0, 10) for i in range(6)])
       
        series = QBarSeries()
        series.append(set0)
        

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle('Bar Chart Kunuhay')
        chart.setAnimationOptions(QChart.SeriesAnimations)

        months = ('Q', 'W', 'E', 'R', 'T', 'Y')

        axisX = QBarCategoryAxis()
        axisX.append(months)

        axisY = QValueAxis()
        axisY.setRange(0, 15)

        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartView = QChartView(chart)

    
        self.ui.conCheck_graph_verticalLayout.addWidget(chartView)
