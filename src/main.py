import os
import click

import src.input
import src.output


@click.command()
@click.option('--plot_path', type=click.Path(exists=True), help='directory for plots')
@click.option('--out_path', type=click.Path(exists=True), help='directory for html files')
@click.option('--plot_interval', type=int, default=100, help='sample intervall with which a plot is made')
@click.option('--buffer_size', type=int, default=1000, help='number of samples in buffer')
def main(plot_interval, buffer_size, plot_path='.', out_path='.'):
    last_db_index = 0
    for file in os.listdir(out_path):
        if 'db' in file and 'plot' not in file and int(file.split('db')[1]) > last_db_index:
            last_db_index = int(file.split('db')[1])
    last_db_index += 1

    data_base_name = '{}/db{}'.format(str(out_path), last_db_index)

    total_db_plot = open('{}/db{}plot.png'.format(str(out_path), last_db_index), 'w')
    total_db_plot.close()

    cache = []
    device = src.input.init_devs()
    count = 0
    previous_index = 0
    total_plot = '{}/latest.png'.format(plot_path)
    latest_plot = '{}/total.png'.format(plot_path)
    data_base = open(data_base_name, 'a')
    data_base.write(' ')
    # data_base.write('{}; {}, {}; {}, {}, {}\n'.format(time.time(), '0.00', '0.00', '0.00', '0.00', '0.00', '0.00'))

    while True:
        data_point, previous_index = src.input.request_data(device, previous_index, debug=True)
        cache.append(data_point)
        if len(cache) > buffer_size:
            data_base = open(data_base_name, 'a')
            data_base.write(str(cache.pop(0)))
            data_base.write('\n')
            data_base.close()
        if count % plot_interval == 0:  # plots recent data
            latest_plot = src.output.make_plot(
                    src.DataSet([float(data_point.time_stamp) for data_point in cache],
                                [float(data_point.voltage) for data_point in cache],
                                [float(data_point.current) for data_point in cache],
                                [float(data_point.total_power) for data_point in cache],
                                [float(data_point.real_power) for data_point in cache],
                                [float(data_point.imag_power) for data_point in cache]),
                    plot_path,
                    plot_name='latest')
            src.output.make_html(out_path, latest_plot, total_plot)
        if count % plot_interval == 0:  # plots all data
            total_plot = src.output.make_plot(src.read_data_set(data_base_name),
                                              plot_path,
                                              plot_name='total')
            total_db_plot = src.output.make_plot(src.read_data_set(data_base_name),
                                                 plot_path,
                                                 plot_name='db{}plot'.format(last_db_index))

        count += 1


if __name__ == '__main__':
    main()
