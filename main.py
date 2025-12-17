from pyscript import display
from js import document

# keep original variable names
subjects = ['Science', 'Math', 'English', 'Filipino', 'ICT', 'PE']
FIELD_IDS = ["science", "math", "english", "filipino", "ict", "pe"]
units_subject = (5, 3, 2, 1)  # original units tuple (first used for Science/Math/English)

def general_weighted_average(evt=None):
    # clear previous outputs (keep original clearing style)
    document.getElementById('student_info').innerHTML = ' '
    document.getElementById('summary').innerHTML = ' '
    document.getElementById('output').innerHTML = ' '

    # read names (keep original variable names)
    first_name = (document.getElementById('first_name').value or "").strip()
    last_name = (document.getElementById('last_name').value or "").strip()

    # gather and validate grades
    grades = []
    errors = []
    for fid in FIELD_IDS:
        el = document.getElementById(fid)
        val = (el.value or "").strip() if el else ""
        if val == "":
            grades.append(None)
            errors.append(f"{fid}: empty")
            continue
        try:
            g = float(val)
        except Exception:
            grades.append(None)
            errors.append(f"{fid}: invalid number")
            continue
        if g < 0 or g > 100:
            grades.append(None)
            errors.append(f"{fid}: out of range (0-100)")
            continue
        grades.append(g)

    # display name using original display()
    display(f'Name: {first_name} {last_name}', target="student_info")

    # if validation issues, show summary and errors (preserve original summary output behavior)
    if any(g is None for g in grades):
        lines = []
        for subj, g in zip(subjects, grades):
            lines.append(f"{subj}: {g if g is not None else '—'}")
        if errors:
            lines.append("")
            lines.append("Errors:")
            lines.extend(errors)
        display("\n".join(lines), target="summary")
        display("Please correct the errors and ensure all grades are numbers between 0 and 100.", target="output")
        return

    # compute weighted sum using original units_subject logic
    weighted_sum = (
        grades[0] * units_subject[0] +  # Science
        grades[1] * units_subject[0] +  # Math
        grades[2] * units_subject[0] +  # English
        grades[3] * units_subject[1] +  # Filipino
        grades[4] * units_subject[2] +  # ICT
        grades[5] * units_subject[3]    # PE
    )
    total_units = units_subject[0] * 3 + units_subject[1] + units_subject[2] + units_subject[3]
    gwa = weighted_sum / total_units

    # build summary similar to original formatting
    summary = (
        f"{subjects[0]}: {grades[0]:.0f}\n"
        f"{subjects[1]}: {grades[1]:.0f}\n"
        f"{subjects[2]}: {grades[2]:.0f}\n"
        f"{subjects[3]}: {grades[3]:.0f}\n"
        f"{subjects[4]}: {grades[4]:.0f}\n"
        f"{subjects[5]}: {grades[5]:.0f}\n"
    )
    display(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output')