import os
import re
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

html_mask = """<!DOCTYPE html>
<html>
<body>

<h1> {} </h1>

<table class="image">
<tr><td><img src={}></td> <td><img src={}></td></tr>
<tr><td class="caption">latest data</td> <td class="caption">total data</td></tr>
<tr><td> black: total power </td><td> black: total power </td></tr>
<tr><td> blue: real power </td><td> blue: real power </td></tr>
<tr><td> red: imaginary power </td><td> red: imaginary power </td></tr>
</table>

{} <!-- This is where the table of data goes -->
</body>"""

delete_button = """<?php
delete({})
?>
<a href="?run=true">delete</a>"""


def make_plot(data, plot_path, plot_name, title=None):
    """writes plot to file
    :param data: namedTuple containing data
    :param plot_path: directory containing previous plot
    :param plot_name: plot name
    :param title: title above plots"""
    plot_file = '{}/{}.png'.format(plot_path, plot_name)
    plt.clf()
    plt.figure()

    f, axarr = plt.subplots(2)
    axarr[0].plot(data.time_stamp, data.voltage, color='green')
    axarr[0].set_ylabel('Voltage RMS [V]', color='green')
    axarr2 = axarr[0].twinx()
    axarr2.plot(data.time_stamp, data.current,  'r-', color='blue')
    axarr2.set_ylabel('Current RMS [A]', color='blue')
    if title:
        plt.suptitle(title)
    axarr[1].plot(data.time_stamp, data.total_power, color='black')
    axarr[1].plot(data.time_stamp, data.real_power, color='blue')
    axarr[1].plot(data.time_stamp, data.imag_power, color='red')
    axarr[1].set_ylabel('Power [W]')
    axarr[1].set_xlabel('Time [s]')
    f.tight_layout()
    plt.locator_params(axis='x', nbins=10)
    plt.locator_params(axis='y', nbins=10)
    plt.savefig(plot_file, format='png')
    plt.close('all')
    return plot_file


def make_html(out_path, latest_plot='/latest.png', total_plot='/total.png', site_name=None):
    """uses a mask to generate a simple html file with title and data plot"""
    if not site_name:
        site_name = '{}/data_site.html'.format(out_path)
    else:
        site_name = '{}/{}.html'.format(out_path, site_name)
    out_file = open(site_name, 'w')
    out_file.write(html_mask.format('Power Consumption', latest_plot, total_plot, make_table(out_path)))
    out_file.close()
    return site_name

def make_table(path):
    all_files = os.listdir(path)
    db_files = []
    plot_files = []
    for file in all_files:
        if 'db' in file and 'plot' not in file:
            db_files.append(file)
        if 'db' in file and 'plot' in file:
            plot_files.append(file)
    db_files.sort()
    plot_files.sort()

    table_string = '<br /> <table style=\"width:25%\">\n <tr> <th> previous data bases </th> </tr> \n'
    for filenumber, file in enumerate(db_files):
        full_db_path = '{}/{}'.format(path, db_files[filenumber])
        full_plot_path = '{}/{}'.format(path, plot_files[filenumber])
        table_string += '<tr> <th> <a href={}> {} </a> </th> <th> <a href={}> {} </a> </th> </tr> \n'\
            .format(full_db_path, db_files[filenumber], full_plot_path, plot_files[filenumber])
    table_string += '</table>'
    return table_string

def make_text(out_path, data, out_name=None):
    """makes text file containing voltage, currant, imag_power and real_power"""
    if not out_name:
        out_name = '{}/data_{}_{}.txt'.format(out_path, data[0].time_stamp, data[-1].time_stamp)
    else:
        out_name = '{}/{}.txt'.format(out_path, out_name)
    out_file = open(out_name, 'w')
    out_file.close()
    out_file = open(out_name, 'a')
    for data_point in data:
        out_file.write(data_point)
    out_file.close()
