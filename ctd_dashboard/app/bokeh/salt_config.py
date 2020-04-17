from bokeh.models import TableColumn, StringFormatter

# https://docs.bokeh.org/en/latest/_modules/bokeh/models/widgets/tables.html#DataTable

flag_options = [
    ("1", "1 [Uncalibrated]"),
    ("2", "2 [Acceptable]"),
    ("3", "3 [Questionable]"),
    ("4", "4 [Bad]"),
]

columns = [
    TableColumn(
        field="SSSCC",
        title="SSSCC",
        width=40,
        formatter=StringFormatter(text_align="right"),
    ),
    TableColumn(
        field="SAMPNO",
        title="Bottle",
        width=20,
        formatter=StringFormatter(text_align="right"),
    ),
    TableColumn(
        field="CTDPRS",
        title="CTDPRS",
        width=75,
        formatter=StringFormatter(text_align="right"),
    ),
    TableColumn(
        field="CTDSAL",
        title="CTDSAL",
        width=65,
        formatter=StringFormatter(text_align="right"),
    ),
    TableColumn(
        field="SALNTY",
        title="SALNTY",
        width=65,
        formatter=StringFormatter(text_align="right"),
    ),
    TableColumn(
        field="diff",
        title="Residual",
        width=65,
        formatter=StringFormatter(text_align="right"),
    ),
    TableColumn(
        field="flag",
        title="Flag",
        width=15,
        formatter=StringFormatter(text_align="center", font_style="bold"),
    ),
    TableColumn(
        field="Comments",
        title="Comments",
        width=135,
        formatter=StringFormatter(text_align="left"),
    ),
]

columns_changed = [
    TableColumn(
        field="SSSCC",
        title="SSSCC",
        width=40,
        formatter=StringFormatter(text_align="right"),
    ),
    TableColumn(
        field="SAMPNO",
        title="Bottle",
        width=20,
        formatter=StringFormatter(text_align="right"),
    ),
    TableColumn(
        field="diff",
        title="Residual",
        width=40,
        formatter=StringFormatter(text_align="right"),
    ),
    TableColumn(
        field="flag_old",
        title="Old",
        width=20,
        formatter=StringFormatter(text_align="center", font_style="bold"),
    ),
    TableColumn(
        field="flag_new",
        title="New",
        width=20,
        formatter=StringFormatter(
            text_align="center", font_style="bold", text_color="red"
        ),
    ),
    TableColumn(
        field="Comments",
        title="Comments",
        width=200,
        formatter=StringFormatter(text_align="left"),
    ),
]
