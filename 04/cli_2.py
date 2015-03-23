import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="get the given name, optionally also the surname")
    parser.add_argument("given_name", help="given name of the person")
    parser.add_argument(
        "-s", "--surname", help="the surname of the person")
    args = parser.parse_args()
    print(args.given_name)
    if args.surname:
        print(args.surname)
