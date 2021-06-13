def configure():
    from rich import pretty, print
    from rich.progress import track
    from icecream import install, ic
    import datetime

    pretty.install()  # rich
    install()  # ic

    def time_str():
        t = datetime.datetime.now().time()
        return f"{t.hour}:{t.minute}:{t.second}|"

    ic.configureOutput(prefix=time_str, includeContext=True)

    print("Done importing settings and modules")
