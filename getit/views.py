from utils import load_template


def index(data):
    note_template = load_template("components/note.html")
    notes_li = [
        note_template.format(
            title=note["Title"], details=note["Description"], id=note["Id"]
        )
        for note in data
    ]
    notes = "\n".join(notes_li)

    return load_template("index.html").format(notes=notes)


def edit_template(note):
    return load_template("edit_note.html").format(
        id=note["Id"],
        title=note["Title"],
        details=note["Description"],
    )
