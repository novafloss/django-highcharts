# -*- coding: utf-8 -*-

from django.views.generic import View

from highcharts.views.common import HighChartsBasicView


class HighChartsPieView(HighChartsBasicView, View):
    chart_type = 'pie'

    def get_data(self):
        return super(HighChartsPieView, self).get_data()

    @property
    def series(self):
        return []
