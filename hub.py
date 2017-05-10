import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fileName')
    parser.add_argument('-tt', '--textTiling', action='store_const', const=True, default=False)
    parser.add_argument('-lsatt', '--LSA_TT', action='store_const', const=True, default=False)

    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()

    # print (namespace)

    print(namespace.fileName)
    print(namespace.textTiling)
    print(namespace.LSA_TT)

