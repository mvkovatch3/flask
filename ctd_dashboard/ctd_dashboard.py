import sys
from app import app


if __name__ == "__main__":
    print("Opening CTD Dashboard with embedded Bokeh app on http://0.0.0.0:8000/")
    # ctDash?

    if "--show" in sys.argv[1:]:  # open browser
        import webbrowser
        from threading import Timer

        def open_browser():
            webbrowser.open_new("http://0.0.0.0:8000/")

        Timer(1, open_browser).start()

    debug = False
    if "--debug" in sys.argv[1:]:  # launch with debug mode
        debug = True

    app.run(host="0.0.0.0", port=8000, debug=debug)
    # (debug = True) is what gives "OSError: [Errno 48] Address already in use"
