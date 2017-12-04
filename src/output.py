import os
import re
import matplotlib.pyplot as plt

import src.archive

html_mask = """<!DOCTYPE html>
<html>
<body>
<h1> {} </h1>
<img src={}>
<img src={}>
{}
</body>"""


# def make_plot(plot_path, data, plot_name=None):
#     """generates a .png plot file of data in plot_path
#     :returns path to plot file"""
#     if not plot_name:
#         plot_name = '{}/data_{}.png'.format(plot_path, data[0].time_stamp)
#     else:
#         plot_name = '{}/{}.png'.format(plot_path, plot_name)
#     if os.path.isfile(plot_name):
#         os.remove(plot_name)
#     time_line = [data_point.time_stamp for data_point in data]
#     plt.clf()
#     plt.figure()
#     f, axarr = plt.subplots(2)
#
#     axarr[0].plot(time_line, [data_point.voltage for data_point in data], color='green')
#     axarr[0].set_ylabel('Voltage RMS [V]', color='green')
#     axarr2 = axarr[0].twinx()
#     axarr2.plot(time_line, [data_point.current for data_point in data],  'r-', color='blue')
#     axarr2.set_ylabel('Currant RMS [A]', color='blue')
#     axarr[1].plot(time_line, [data_point.total_power for data_point in data])
#     axarr[1].plot(time_line, [data_point.real_power for data_point in data])
#     axarr[1].plot(time_line, [data_point.imag_power for data_point in data])
#     axarr[1].set_ylabel('Power [W]')
#     axarr[1].set_xlabel('Time [s]')
#     if os.path.isfile(plot_name):
#         os.remove(plot_name)
#     plt.savefig(plot_name, format='png')
#     plt.close('all')
#     return plot_name

def make_plot(data, plot_path, plot_name):
    """writes plot to file
    :param data: namedTuple containing data
    :param plot_path: directory containing previous plot
    :param plot_name: plot name"""
    plot_file = '{}/{}.png'.format(plot_path, plot_name)
    if os.path.isfile(plot_file):   # removes old plot
        os.remove(plot_file)
    plt.clf()
    plt.figure()
    f, axarr = plt.subplots(2)
    axarr[0].plot(data.time_stamp, data.voltage, color='green')
    axarr[0].set_ylabel('Voltage RMS [V]', color='green')
    axarr2 = axarr[0].twinx()
    axarr2.plot(data.time_stamp, data.current,  'r-', color='blue')
    axarr2.set_ylabel('Current RMS [A]', color='blue')
    axarr[1].plot(data.time_stamp, data.total_power)
    axarr[1].plot(data.time_stamp, data.real_power)
    axarr[1].plot(data.time_stamp, data.imag_power)
    axarr[1].set_ylabel('Power [W]')
    axarr[1].set_xlabel('Time [s]')
    # if os.path.isfile(plot_name):
    #     os.remove(plot_name)
    plt.savefig(plot_file, format='png')
    plt.close('all')
    return plot_file


# def make_full_plot(data_path, plot_name, plot_path):
#     """plots contents of text database"""
#     if not plot_name:
#         plot_name = '{}/data_{}.png'.format(plot_path, 'temp')
#     else:
#         plot_name = '{}/{}.png'.format(plot_path, plot_name)
#     if os.path.isfile(plot_name):
#         os.remove(plot_name)
#     if os.path.isfile(plot_name):
#         lines = open(plot_name, 'r').readlines()
#     else:
#         return plot_name
#     time_stamp = []
#     voltage = []
#     current = []
#     total_power = []
#     real_power = []
#     imag_power = []
#     for line in lines:
#         t, v, i, s, p, q = re.findall(src.archive.read_reg, line)[0]
#         time_stamp.append(t)
#         voltage.append(v)
#         current.append(i)
#         total_power.append(s)
#         real_power.append(p)
#         imag_power.append(q)
#     plt.clf()
#     plt.figure()
#     f, axarr = plt.subplots(2)
#     axarr[0].plot(time_stamp, voltage, color='green')
#     axarr[0].set_ylabel('Voltage RMS [V]', color='green')
#     axarr2 = axarr[0].twinx()
#     axarr2.plot(time_stamp, current,  'r-', color='blue')
#     axarr2.set_ylabel('Current RMS [A]', color='blue')
#     axarr[1].plot(time_stamp, total_power)
#     axarr[1].plot(time_stamp, real_power)
#     axarr[1].plot(time_stamp, imag_power)
#     axarr[1].set_ylabel('Power [W]')
#     axarr[1].set_xlabel('Time [s]')
#     if os.path.isfile(plot_name):
#         os.remove(plot_name)
#     plt.savefig(plot_name, format='png')
#     plt.close('all')
#     return plot_name
#
#
def make_html(out_path, latest_plot, total_plot, site_name=None):
    """generates html document showing a plot"""
    """uses a mask to generate a simple html file with title and data plot"""
    # data = make_plot(out_path, data, plot_name=plot_name)
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
    for file in all_files:
        if 'db' in file:
            db_files.append(file)
    table_string = '<br /> <table style=\"width:25%\">\n <tr> <th> previous data bases </th> </tr> \n'
    for file in db_files:
        table_string += '<tr> <th> <a href=\"{}/{}\"> {} </a> </th> </tr> \n'.format(path, file, file)
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
