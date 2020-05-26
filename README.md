
Django CMS Chart <- InfluxDB
================

A plugin for DjangoCMS that creates easy to use and fully customisable ChartJs (ver 1.0.2) charts - with a table and csv upload interface.
You also have the possibility of live updating the charts from an InfluxDB stack.

Quick start
===========
1. Add 'djangocms_influx_charts' to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'djangocms_influx_charts',
    ]

2. Run `python manage.py migrate` to create the djangocms_influx_charts models.

3. Ensure you have your own version of jQuery added to block 'js'. See here: https://django-sekizai.readthedocs.io/en/latest/#example

4. Add a DjangoCMS Chart object to your web page!

ChartJs
=======
`ChartJs <http://www.chartjs.org/>`_ is a dynamic charting application giving users an interactive and visually appealing chart in an html 5 canvas. Each type of chart is available:
- Line
- Bar
- Radar
- Polar
- Pie
- Doughnut

ChartJs-Sass
============
To format the charts we recommend using `ChartJs-Sass <https://github.com/mcldev/ChartJS-Sass>`_   which creates an easy to use SASS template system so that charts and colours are kept out of the HTML and JS code.

Inputs
======
Use the normal inputs to select the data for the chart, the header rows and the orientation of the data i.e. in rows/columns.
 The full set of customisation inputs are available in the 'Advanced Settings' for each chart or in the main Administration settings for all charts.

Future Development
==================
Future development will include updating ChartJs versions and adding Highcharts as another Chart type.
