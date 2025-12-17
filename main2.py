from pyscript import display, document


# Define club information using dictionaries
club_info = {
            "chess": {
                "name": "Chess Club",
                "description": "A club for chess enthusiasts of all skill levels.",
                "meeting_time": "Every Wednesday 3:30-5:00 PM",
                "location": "Room 405",
                "advisor": "Mr. Santos",
                "members": 20,
                "category": "Special"
            },
            "math": {
                "name": "Math Club",
                "description": "For students interested in mathematics, and geometry.",
                "meeting_time": "Every Monday and Thursday 3:00-5:00 PM",
                "location": "Room 221",
                "advisor": "Mr. Norris",
                "members": 19,
                "category": "Academic"
            },
            "robotics": {
                "name": "Robotics Club",
                "description": "Design, build, and program robots for competitions.",
                "meeting_time": "Every Tuesday 3:30-5:30 PM",
                "location": "Computer Lab",
                "advisor": "Ms. Onofre",
                "members": 18,
                "category": "Special"
            },
            "debate": {
                "name": "Debate Club",
                "description": "Develop public speaking and argumentation skills.",
                "meeting_time": "Every Friday 3:30-5:00 PM",
                "location": "Room 507",
                "advisor": "Ms. Carabot",
                "members": 12,
                "category": "Academic"
            },
            "art": {
                "name": "Art Club",
                "description": "Explore various art mediums and techniques.",
                "meeting_time": "Every Wednesday 3:45-5:15 PM",
                "location": "Art Room",
                "advisor": "Mr. Ross",
                "members": 20,
                "category": "Special"
            }
        }
        
def show_club_info(e):
    output_div = document.getElementById("club-info")
    selected_club = document.getElementById("club-select").value

    output_div.innerHTML = ""

    if not selected_club:
        display("Please select a club first.", target="club-info")
        return

    info = club_info[selected_club]

    output = f"""
    <h3>{info['name']}</h3>
    <p><b>Description:</b> {info['description']}</p>
    <p><b>Meeting Time:</b> {info['meeting_time']}</p>
    <p><b>Location:</b> {info['location']}</p>
    <p><b>Advisor:</b> {info['advisor']}</p>
    <p><b>Members:</b> {info['members']}</p>
    <p><b>Category:</b> {info['category']}</p>
    """

    display(output, target="club-info")
    document.getElementById("club-info").innerHTML = output