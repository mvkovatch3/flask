from bokeh.models import TableColumn


def build_columns(fields, titles, widths):
    """Build columns for a bokeh DataTable.
    Fields and titles must be of length N.
    Widths must be of length N or 1.
    """
    # TODO: build in ability to do formatters?
    columns = []
    for (f, t, w) in zip(fields, titles, widths):
        columns.append(TableColumn(field=f, title=t, width=w))
    return columns
