from flask import Flask, render_template

app = Flask(__name__)

# ── DATA ─────────────────────────────────────────────────────────────────────

projects = [
    {
       "name": "Contribo",
       "description": "A cross-platform project management and contribution tracking system that helps teams coordinate projects through task assignment, proof-based completion, contribution scoring, and automated progress tracking across Discord and Telegram.",
       "tech": ["Python", "Discord API", "Telegram API", "SQLite"],
       "repo": "https://github.com/firah08/skillshiftclub",
    },
    {
        "name": "CoLab Management Platform",
        "description": "A social web platform that connects youth and elderly users through community events, user suggested activities, and admin led approval workflows.",
        "tech": ["Python", "Flask", "Jinja2", "JavaScript"],
        "repo": "https://github.com/firah08/skillshiftclub",
    },
    {
        "name": "SkillShift Club",
        "description": "A simple website for a mock polytechnic CCA featuring Wushu, Netball, Dragon Boat, an events calendar, a click to reveal FAQ, and a friendly 404 error page.",
        "tech": ["HTML", "JavaScript", "CSS"],
        "repo": "https://github.com/firah08/skillshiftclub",
    },
    {
        "name": "Personal Portfolio Website",
        "description": "A personal portfolio website showcasing my projects, skills, and experiences.",
        "tech": ["HTML", "JavaScript", "CSS"],
        "repo": "https://github.com/firah08/mushfira_portfolio",
    },
]

events = [
    {
       "name": "Sengkang Community Night 2026",
       "host": "Sengkang Community Club",
       "date": "July 2026",
       "takeaway": "Developed confidence in public speaking and event hosting by co-emceeing a large-scale community event, managing programme flow, and engaging residents throughout the evening.",
    },
    {
       "name": "National Family Festival 2026",
       "host": "Families for Life",
       "date": "June 2026",
       "takeaway": "Developed stronger public engagement and teamwork skills by interacting with families, and supporting an interactive booth activity for parents and children.",
    },
    {
        "name": "Parents' Day Event",
        "host": "Sengkang Community Club",
        "date": "June 2026",
        "takeaway": "Strengthened my communication and interpersonal skills by engaging with residents of different age groups, facilitating board games, and creating a welcoming environment that encouraged community interaction.",
    },
    {
        "name": "Claude Code Workshop",
        "host": "SYAI × YouthTech SG",
        "date": "May 2026",
        "takeaway": "Gained hands on experience prompting Claude directly in my own terminal to automate coding tasks and improve workflow efficiency.",
    },
    {
        "name": "Sengkang North Edusave Awards Presentation",
        "host": "Sengkang North Youth Network",
        "date": "May 2026",
        "takeaway": "Hosted the Edusave award ceremony at Sengkang North while guiding the programme flow.",
    },
    {
        "name": "EcoFest 2026",
        "host": "Sengkang North Youth Network",
        "date": "Apr 2026",
        "takeaway": "Planned a stage game and hosted the stage game segment at EcoFest focused on sustainability and environmental awareness.",
    },
    {
        "name": "Halloween 2025 ",
        "host": "Sengkang North Youth Network",
        "date": "Oct 2025",
        "takeaway": "Managed the redemption booth and handled redemption cards for game booths at the community Halloween event.",
    },
    
]

work = [
    {
        "role": "Community Management Intern",
        "org": "Ethrealm",
        "period": "2026 — Present",
        "current": True,
        "bullets": [
            "Manage community engagement across Discord, Telegram, and social media platforms",
            "Coordinate online events, AMAs, and community-driven campaigns",
            "Monitor community sentiment and escalate feedback to the core team",
        ],
    },
]

volunteer = [
    {
        "role": "Youth Volunteer",
        "org": "Sengkang North Youth Network",
        "period": "2025 — Present",
        "current": True,
        "bullets": [
            "Support planning and execution of community initiatives and outreach events",
            "Collaborate in team-based environments to serve the local youth community",
            "Build leadership, communication, and event management skills hands-on",
        ],
    },
]

contact = {
    "email": "firah2026@gmail.com",       
    "github": "https://github.com/firah08",  
    "linkedin": "https://linkedin.com/in/mushfira08",  
}


# ── ROUTES ───────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template(
        "index.html",
        projects=projects,
        events=events,
        work=work,
        volunteer=volunteer,
        contact=contact,
    )


if __name__ == "__main__":
    app.run(debug=True)
