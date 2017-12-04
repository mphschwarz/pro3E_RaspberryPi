import time
import os
import click

import src.archive
import src.input
import src.output

cache_length = 10


@click.command()
@click.option('--data_base', type=str, default=None, help='database to be extended')
@click.option('--plot_path', type=click.Path(exists=True), help='directory for plots')
@click.option('--out_path', type=click.Path(exists=True), help='directory for html files')
def main(data_base, plot_path='.', out_path='.'):
    if not data_base:
        data_base_name = \
            '{}/db{}'.format(str(out_path), sum(['db' in list_item for list_item in os.listdir(str(out_path))]))
    else:
        data_base_name = data_base
    cache = []
    device = src.input.init_devs()
    # data_base = open(str(data_base), 'a')
    count = 0
    previous_index = 0
    total_plot = '{}/latest.png'.format(plot_path)
    latest_plot = '{}/total.png'.format(plot_path)
    data_base = open(data_base_name, 'a')
    data_base.write('{}; {}, {}; {}, {}, {}\n'.format(time.time(), '0.00', '0.00', '0.00', '0.00', '0.00', '0.00'))
    while True:
        t_start = time.time()
        data_point, previous_index = src.input.request_data(device, previous_index + 1, debug=True)
        cache.append(data_point)
        if len(cache) > cache_length:
            data_base = open(data_base_name, 'a')
            data_base.write(str(cache.pop(0)))
            data_base.write('\n')
            data_base.close()
        if count % 10 == 0:  # plots recent data
            latest_plot = src.output.make_plot(
                    src.archive.DataSet([float(data_point.time_stamp) for data_point in cache],
                                        [float(data_point.voltage) for data_point in cache],
                                        [float(data_point.current) for data_point in cache],
                                        [float(data_point.total_power) for data_point in cache],
                                        [float(data_point.real_power) for data_point in cache],
                                        [float(data_point.imag_power) for data_point in cache]),
                    plot_path,
                    plot_name='latest')
            src.output.make_html(out_path, latest_plot, total_plot)
        if count % 10 == 0:  # plots all data
            total_plot = src.output.make_plot(
                    src.archive.read_data_set(data_base_name),
                    # src.archive.DataSet([data_point.time_stamp for data_point in cache],
                    #                     [data_point.voltage for data_point in cache],
                    #                     [data_point.current for data_point in cache],
                    #                     [data_point.total_power for data_point in cache],
                    #                     [data_point.real_power for data_point in cache],
                    #                     [data_point.imag_power for data_point in cache]),
                    plot_path,
                    plot_name='total')
            # src.output.make_full_plot(data_base, plot_name='total', plot_path=plot_path)

        # time.sleep(time.time() - t_start)
        count += 1


if __name__ == '__main__':
    main()
