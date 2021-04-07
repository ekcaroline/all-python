def avg(*args):
    if len(args) >= 1:
        average = sum(args) / len(args)
        return "# {}".format(average)
    else:
        return "# {}".format(None)
