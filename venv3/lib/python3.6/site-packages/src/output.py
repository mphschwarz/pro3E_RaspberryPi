import matplotlib.pyplot as plt

html_mask = """<!DOCTYPE html>
<html>
<body>
<h1> {} </h1>
<img src={}>
</body>"""


def make_plot(plot_path, data, plot_name=None):
    """generates a .png plot file of data in plot_path
    :returns path to plot file"""
    time_line = [data_point.time_stamp for data_point in data]
    plt.figure()
    f, axarr = plt.subplots(2, sharex=True)

    axarr[0].plot(time_line, [data_point.voltage for data_point in data], color='green')
    axarr[0].set_ylabel('[V]', color='green')
    axarr2 = axarr[0].twinx()
    axarr2.plot(time_line, [data_point.currant for data_point in data],  'r-', color='blue')
    axarr2.set_ylabel('[A]', color='blue')
    axarr[1].plot(time_line, [data_point.real_power for data_point in data])
    axarr[1].plot(time_line, [data_point.imag_power for data_point in data])
    axarr[1].set_ylabel('[W]')
    axarr[1].set_xlabel('[s]')
    if not plot_name:
        plot_name = '{}/data_{}.png'.format(plot_path, data[0].time_stamp)
    else:
        plot_name = '{}/{}.png'.format(plot_path, plot_name)
    plt.savefig(plot_name)
    return plot_name


def make_html(out_path, data, site_name=None, plot_name=None):
    """generates html document showing a plot"""
    """uses a mask to generate a simple html file with title and data plot"""
    data = make_plot(out_path, data, plot_name=plot_name)
    if not site_name:
        site_name = '{}/data_site.html'.format(out_path)
    else:
        site_name = '{}/{}.html'.format(out_path, site_name)
    out_file = open(site_name, 'w')
    out_file.write(html_mask.format('Power Consumption', data, plot_name))
    out_file.close()
    return site_name

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
