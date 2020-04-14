def run(a=1, b="two"):
    print(a, b)


if __name__ == '__main__':
    import argparse
    print(f"experiment.py :: running as a script\n{__file__}")

    parser = argparse.ArgumentParser()
    parser.add_argument('a', type=int)
    parser.add_argument('b', type=str)

    run(**vars(parser.parse_args()))
