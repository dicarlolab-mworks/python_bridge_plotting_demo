from matplotlib import pyplot


values = []


def plot_values(conduit, events):
    rc = conduit.reverse_codec

    values.extend([e.value for e in events
                   # The "if" test is unnecesary in this example, which watches
                   # only one variable, but is needed in the general case
                   if e.code == rc['rand_var']])

    print('Drawing histogram (%d values)' % len(values), flush=True)
    pyplot.cla()
    pyplot.hist(values)
    pyplot.title('Distribution of random values')
    pyplot.draw()


if __name__ == '__main__':
    from conduit import Conduit
    Conduit.main(plot_values, ['rand_var'])
