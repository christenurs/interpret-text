import argparse
import logging
import subprocess
import sys

from _utils import _LogWrapper

_logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


def build_argument_parser():
    desc = "Build wheels for interpret-text"

    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("--version-filename",
                        help="The file where the version will be stored.",
                        required=True)

    return parser


def main(argv):
    parser = build_argument_parser()
    args = parser.parse_args(argv)

    with _LogWrapper("installation of interpret-text"):
        subprocess.check_call(["pip", "install", "-e", "./python"])

    with _LogWrapper("storing interpret-text version in {}".format(args.version_filename)):
        import interpret_text
        with open(args.version_filename, 'w') as version_file:
            version_file.write(interpret_text.__version__)

    with _LogWrapper("creation of packages"):
        subprocess.check_call(["python", "setup.py", "sdist", "bdist_wheel"])


if __name__ == "__main__":
    main(sys.argv[1:])
