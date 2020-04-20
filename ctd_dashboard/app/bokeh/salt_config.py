flag_options = [
    ("1", "1 [Uncalibrated]"),
    ("2", "2 [Acceptable]"),
    ("3", "3 [Questionable]"),
    ("4", "4 [Bad]"),
]

cast_columns = dict(
    fields=[
        "SSSCC",
        "SAMPNO",
        "CTDPRS",
        "CTDSAL",
        "SALNTY",
        "diff",
        "flag",
        "Comments",
    ],
    titles=[
        "SSSCC",
        "Bottle",
        "CTDPRS",
        "CTDSAL",
        "SALNTY",
        "Residual",
        "Flag",
        "Comments",
    ],
    widths=[40, 20, 75, 65, 65, 65, 15, 135],
)

changes_columns = dict(
    fields=["SSSCC", "SAMPNO", "diff", "flag_old", "flag_new", "Comments"],
    titles=["SSSCC", "Bottle", "Residual", "Old", "New", "Comments"],
    widths=[40, 20, 40, 20, 20, 200],
)
