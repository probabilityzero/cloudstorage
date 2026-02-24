#python 3.7.1
import os

# Expanded Dictionary of domains and professions
domains = {
    "Health and Medicine": [
        "Doctor", "Nurse", "Dentist", "Pharmacist", "Surgeon", "Paramedic", "Radiologist", 
        "Physiotherapist", "Optometrist", "Veterinarian", "Chiropractor", "Anesthesiologist", 
        "Psychiatrist", "Medical Lab Technician", "Occupational Therapist", "Speech Therapist"
    ],
    "Engineering and Technology": [
        "Civil Engineer", "Mechanical Engineer", "Software Engineer", "Electrical Engineer", 
        "Biomedical Engineer", "Chemical Engineer", "Aerospace Engineer", "Industrial Engineer", 
        "Environmental Engineer", "Robotics Engineer", "Computer Hardware Engineer", "Systems Engineer"
    ],
    "Business, Finance, and Economics": [
        "Accountant", "Financial Analyst", "Economist", "Investment Banker", "Marketing Manager", 
        "Human Resources Manager", "Business Analyst", "Tax Consultant", "Auditor", "Real Estate Agent", 
        "Entrepreneur", "Supply Chain Manager", "Operations Manager", "Product Manager"
    ],
    "Law and Governance": [
        "Lawyer", "Judge", "Paralegal", "Public Policy Expert", "Legal Consultant", "Corporate Lawyer", 
        "Criminal Defense Lawyer", "Mediator", "Diplomat", "Government Administrator", "Compliance Officer"
    ],
    "Creative and Media Arts": [
        "Artist", "Writer", "Journalist", "Graphic Designer", "Filmmaker", "Animator", "Photographer", 
        "Editor", "Musician", "Fashion Designer", "Interior Designer", "Actor", "Screenwriter", 
        "Sound Engineer", "Art Director", "Video Game Designer"
    ],
    "Education and Research": [
        "Teacher", "Professor", "Researcher", "Curriculum Designer", "Educational Consultant", 
        "Librarian", "Instructional Designer", "Academic Counselor", "School Principal", 
        "Teaching Assistant", "Special Education Teacher", "Lab Technician"
    ],
    "Public Service and Nonprofit": [
        "Social Worker", "Community Organizer", "Charity Worker", "Policy Advisor", "Nonprofit Manager", 
        "Volunteer Coordinator", "Environmental Activist", "Public Health Administrator", "Youth Worker", 
        "Disaster Relief Coordinator", "Fundraising Specialist", "Crisis Counselor"
    ],
    "Trades and Craftsmanship": [
        "Carpenter", "Electrician", "Plumber", "Mechanic", "Welder", "HVAC Technician", 
        "Construction Worker", "Blacksmith", "Painter", "Machinist", "Boat Builder", 
        "Textile Worker", "Roofer", "Bricklayer", "Glazier", "Furniture Maker"
    ],
    "Agriculture and Environmental Sciences": [
        "Farmer", "Agricultural Engineer", "Environmental Scientist", "Conservationist", "Forester", 
        "Horticulturist", "Soil Scientist", "Marine Biologist", "Ecologist", "Wildlife Manager", 
        "Aquaculture Specialist", "Hydrologist", "Park Ranger", "Agronomist"
    ],
    "Information Technology and Data Science": [
        "Data Scientist", "Software Developer", "Cybersecurity Expert", "Network Administrator", 
        "Web Developer", "Database Administrator", "DevOps Engineer", "IT Support Specialist", 
        "AI Researcher", "Machine Learning Engineer", "Cloud Solutions Architect", "Blockchain Developer", 
        "Mobile App Developer", "Systems Administrator", "UXUI Designer"
    ],
    "Construction and Infrastructure Development": [
        "Construction Manager", "Surveyor", "Urban Planner", "Structural Engineer", "Site Supervisor", 
        "Landscape Architect", "Architect", "Quantity Surveyor", "Civil Drafter", "Building Inspector", 
        "Real Estate Developer", "Mason", "Geotechnical Engineer"
    ],
    "Hospitality and Tourism": [
        "Hotel Manager", "Chef", "Tour Guide", "Event Planner", "Travel Agent", "Concierge", 
        "Flight Attendant", "Bartender", "Housekeeper", "Sommelier", "Restaurant Manager", 
        "Resort Manager", "Cruise Director", "Food and Beverage Manager"
    ],
    "Retail and Wholesale": [
        "Retail Manager", "Sales Associate", "Customer Service Representative", "Merchandiser", 
        "Buyer", "Store Manager", "Visual Merchandiser", "Inventory Manager", "E-commerce Manager", 
        "Warehouse Supervisor", "Logistics Coordinator", "Cashier", "Store Planner"
    ],
    "Media and Communications": [
        "Public Relations Specialist", "Communications Manager", "Media Planner", "Content Writer", 
        "Social Media Manager", "Broadcast Journalist", "Radio Host", "Advertising Executive", 
        "Brand Strategist", "Copywriter", "Film Editor", "SEO Specialist", "Podcast Producer"
    ],
    "Sports and Recreation": [
        "Professional Athlete", "Sports Coach", "Personal Trainer", "Physical Education Teacher", 
        "Sports Manager", "Athletic Trainer", "Recreation Coordinator", "Sports Commentator", 
        "Sports Photographer", "Umpire or Referee", "Fitness Instructor", "Gym Manager", 
        "Lifeguard", "Sports Scout"
    ],
    "Transport and Logistics": [
        "Truck Driver", "Airline Pilot", "Logistics Manager", "Supply Chain Coordinator", 
        "Warehouse Manager", "Customs Broker", "Freight Forwarder", "Ship Captain", 
        "Train Conductor", "Fleet Manager", "Delivery Driver", "Transport Planner", "Dock Worker"
    ],
    "Energy and Utilities": [
        "Electrical Engineer", "Power Plant Operator", "Wind Turbine Technician", "Solar Panel Installer", 
        "Energy Consultant", "Nuclear Engineer", "Petroleum Engineer", "Hydrologist", 
        "Water Treatment Specialist", "Environmental Engineer", "Renewable Energy Specialist", 
        "Geologist", "Drilling Engineer", "Pipeline Operator"
    ],
    "Military and Defense": [
        "Soldier", "Navy Officer", "Air Force Pilot", "Military Engineer", "Defense Analyst", 
        "Intelligence Officer", "Combat Medic", "Logistics Officer", "Drone Operator", "Weapon Specialist", 
        "Cyber Warfare Specialist", "Cryptographer", "Explosives Specialist"
    ]
}

# Function to create folder structure with professions inside domain folders
def create_folders_and_files(base_directory="Professions"):
    if not os.path.exists(base_directory):
        os.makedirs(base_directory)
    
    for domain, professions in domains.items():
        # Create domain folder
        domain_folder = os.path.join(base_directory, domain)
        os.makedirs(domain_folder, exist_ok=True)
        
        # Create profession files inside the domain folder
        for profession in professions:
            profession_file = os.path.join(domain_folder, f"{profession}.md")
            with open(profession_file, 'w') as file:
                file.write(f"This is the {profession} profession inside the {domain} domain.\n")
    
    print(f"Folder structure created under '{base_directory}'.")

# Run the function
create_folders_and_files()