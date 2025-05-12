# -*- encoding: utf-8 -*-

from routes import *


def main():
    print("app run")

    app.run(host="0.0.0.0",port=10007)
    return None


if __name__ == "__main__":
    main()
