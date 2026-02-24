import os

# List of top 50 universities and their famous programs
universities_with_programs = {
    # North America
    "University of Toronto": ["Medicine", "Engineering", "Business"],
    "University of Michigan": ["Engineering", "Business", "Law"],
    "Harvard University": ["Law", "Business", "Medicine"],
    "Massachusetts Institute of Technology (MIT)": ["Engineering", "Computer Science", "Physics"],
    
    # Europe
    "University of Amsterdam": ["Social Sciences", "Economics", "Law"],
    "University of Edinburgh": ["Medicine", "Engineering", "Humanities"],
    "ETH Zurich": ["Engineering", "Natural Sciences", "Architecture"],
    "University of Copenhagen": ["Biology", "Medicine", "Law"],
    
    # Asia
    "National University of Singapore (NUS)": ["Engineering", "Computer Science", "Business"],
    "Tsinghua University": ["Engineering", "Computer Science", "Business"],
    "University of Tokyo": ["Engineering", "Law", "Humanities"],
    "Peking University": ["Economics", "Political Science", "Law"],
    
    # Australia
    "University of Melbourne": ["Medicine", "Arts", "Business"],
    "Australian National University (ANU)": ["Political Science", "Economics", "Law"],
    "University of Sydney": ["Business", "Engineering", "Medicine"],
    
    # Africa
    "University of Cape Town": ["Commerce", "Health Sciences", "Engineering"],
    "University of the Witwatersrand": ["Engineering", "Business", "Law"],
    "University of Nairobi": ["Social Sciences", "Agriculture", "Engineering"],
    
    # South America
    "University of São Paulo (USP)": ["Engineering", "Social Sciences", "Biology"],
    "Universidad Nacional Autónoma de México (UNAM)": ["Arts", "Social Sciences", "Medicine"],
    "Pontifical Catholic University of Chile": ["Engineering", "Social Sciences", "Business"],
    
    # Middle East
    "American University of Beirut": ["Business", "Engineering", "Arts"],
    "United Arab Emirates University": ["Engineering", "Business", "Health Sciences"],
    "King Saud University": ["Engineering", "Health Sciences", "Business"],
    
    # Additional Global
    "University of Tokyo": ["Engineering", "Humanities", "Natural Sciences"],
    "Seoul National University": ["Engineering", "Business", "Social Sciences"],
    "Universität Mannheim": ["Business", "Economics", "Social Sciences"],
    "University of Helsinki": ["Social Sciences", "Natural Sciences", "Health Sciences"],
    "University of Queensland": ["Biology", "Engineering", "Business"],
    "University of Alberta": ["Engineering", "Business", "Health Sciences"],
    "University of Kentucky": ["Agriculture", "Engineering", "Business"],
    "University of Iowa": ["Public Health", "Business", "Education"],
    "University of Minnesota": ["Engineering", "Social Sciences", "Medicine"],
    "University of Tennessee": ["Agriculture", "Business", "Health Sciences"],
    "University of South Florida": ["Engineering", "Business", "Public Health"],
    "Ohio State University": ["Engineering", "Business", "Health Sciences"],
    "University of Colorado Denver": ["Business", "Health Sciences", "Public Affairs"],
    "Virginia Commonwealth University": ["Art", "Health Sciences", "Business"],
    "Michigan State University": ["Agriculture", "Business", "Education"],
    "University of Notre Dame": ["Business", "Engineering", "Law"],
    "University of Richmond": ["Business", "Law", "International Relations"],
    "University of Massachusetts Lowell": ["Engineering", "Business", "Health Sciences"],
    "University of Illinois at Chicago": ["Health Sciences", "Business", "Education"],
    "University of Cape Town": ["Commerce", "Health Sciences", "Engineering"],
    "University of Toronto Scarborough": ["Business", "Social Sciences", "Environmental Science"],
    "York University": ["Business", "Law", "Environmental Studies"],
    "Simon Fraser University": ["Business", "Engineering", "Social Sciences"],
    "University of Calgary": ["Engineering", "Business", "Medicine"],
    "McMaster University": ["Health Sciences", "Engineering", "Business"],
    "University of Victoria": ["Social Sciences", "Business", "Engineering"],
    "University of Otago": ["Health Sciences", "Arts", "Business"],
    "University of Canterbury": ["Engineering", "Arts", "Science"],
    "Victoria University of Wellington": ["Arts", "Business", "Science"],
    "University of Waikato": ["Management", "Education", "Social Sciences"],
    "Massachusetts Institute of Technology (MIT)": ["Engineering", "Computer Science", "Physics", "Economics"],
    "Stanford University": ["Business", "Engineering", "Law", "Computer Science"],
    "Harvard University": ["Law", "Business", "Economics"],
    "California Institute of Technology (Caltech)": ["Physics", "Engineering", "Chemistry"],
    "University of Oxford": ["Philosophy", "Economics", "Law", "Medicine"],
    "University of Cambridge": ["Mathematics", "Engineering", "Law"],
    "Imperial College London": ["Engineering", "Medicine", "Life Sciences"],
    "ETH Zurich": ["Engineering", "Computer Science", "Natural Sciences"],
    "University of Chicago": ["Economics", "Law", "Sociology"],
    "University College London (UCL)": ["Architecture", "Medicine", "Psychology"],
    "National University of Singapore (NUS)": ["Engineering", "Computer Science", "Life Sciences"],
    "Peking University": ["Law", "Economics", "Philosophy"],
    "Tsinghua University": ["Engineering", "Computer Science"],
    "University of Pennsylvania": ["Business", "Law", "Economics"],
    "Yale University": ["Law", "Political Science", "History"],
    "Columbia University": ["Journalism", "International Relations", "Engineering"],
    "Princeton University": ["Mathematics", "Economics", "Philosophy"],
    "University of Tokyo": ["Engineering", "Business", "Life Sciences"],
    "Johns Hopkins University": ["Medicine", "Public Health", "International Relations"],
    "University of California, Berkeley": ["Engineering", "Law", "Economics"],
    "University of Edinburgh": ["Law", "Literature", "Philosophy"],
    "Cornell University": ["Agriculture", "Engineering", "Business"],
    "University of Michigan": ["Engineering", "Law", "Business"],
    "Northwestern University": ["Business", "Journalism", "Law"],
    "University of Toronto": ["Medicine", "Law", "Computer Science"],
    "London School of Economics and Political Science (LSE)": ["Economics", "Political Science"],
    "Duke University": ["Medicine", "Law", "Public Policy"],
    "University of Hong Kong (HKU)": ["Law", "Business", "Architecture"],
    "University of Melbourne": ["Law", "Engineering", "Business"],
    "University of California, Los Angeles (UCLA)": ["Film", "Medicine", "Business"],
    "University of Sydney": ["Medicine", "Law", "Business"],
    "New York University (NYU)": ["Law", "Business", "Performing Arts"],
    "Carnegie Mellon University": ["Computer Science", "Engineering", "Robotics"],
    "University of British Columbia": ["Forestry", "Engineering", "Economics"],
    "King's College London": ["Law", "Medicine", "International Relations"],
    "University of Manchester": ["Engineering", "Business", "Computer Science"],
    "University of California, San Diego (UCSD)": ["Oceanography", "Medicine", "Biology"],
    "University of New South Wales (UNSW Sydney)": ["Engineering", "Law", "Business"],
    "McGill University": ["Medicine", "Law", "Engineering"],
    "Australian National University (ANU)": ["Political Science", "Economics", "Philosophy"],
    "University of Warwick": ["Economics", "Business", "Law"],
    "University of Queensland": ["Biology", "Engineering", "Business"],
    "University of Amsterdam": ["Social Sciences", "Economics", "Medicine"],
    "Brown University": ["Economics", "Public Policy", "Philosophy"],
    "University of Copenhagen": ["Biology", "Medicine", "Economics"],
    "University of Illinois at Urbana-Champaign": ["Engineering", "Computer Science", "Business"],
    "KU Leuven": ["Engineering", "Law", "Medicine"],
    "Sorbonne University": ["Humanities", "Law", "Philosophy"],
    "Seoul National University (SNU)": ["Law", "Engineering", "Business"],
    "University of Alberta": ["Engineering", "Medicine", "Business"],
    "University of Wisconsin-Madison": ["Engineering", "Business", "Law"],
    "University of California, Irvine (UCI)": ["Biological Sciences", "Engineering", "Law"],
    "University of Edinburgh": ["Business", "Medicine", "Engineering"],
    "National Taiwan University (NTU)": ["Engineering", "Business", "Social Sciences"],
    "University of Cape Town (UCT)": ["Commerce", "Engineering", "Humanities"],
    "University of Lagos": ["Engineering", "Social Sciences", "Business"],
    "University of Buenos Aires": ["Social Sciences", "Humanities", "Law"],
    "Universidad Nacional Autónoma de México (UNAM)": ["Humanities", "Engineering", "Social Sciences"],
    "University of São Paulo (USP)": ["Engineering", "Biological Sciences", "Humanities"],
    "Tsinghua University": ["Engineering", "Computer Science", "Management"],
    "Universidad de Chile": ["Social Sciences", "Law", "Engineering"],
    "University of Sydney": ["Medicine", "Engineering", "Arts"],
    "Cairo University": ["Engineering", "Medicine", "Law"],
    "University of Nairobi": ["Engineering", "Social Sciences", "Business"],
    "University of the Witwatersrand": ["Commerce", "Engineering", "Humanities"],
    "University of Queensland": ["Philosophy", "Biology", "Education"],
    "University of Alberta": ["Agriculture", "Engineering", "Health Sciences"],
    "University of Warwick": ["Mathematics", "Economics", "Business"],
    "University of Hong Kong": ["Engineering", "Architecture", "Medicine"],
    "University of the Pacific": ["Business", "Education", "Music"],
    "University of South Africa (UNISA)": ["Arts", "Business", "Education"],
    "Dartmouth College": ["Business", "Government", "Health Sciences"],
    "University of Pittsburgh": ["Medicine", "Engineering", "Social Work"],
    "Vanderbilt University": ["Education", "Law", "Medicine"],
    "Universidad de los Andes (Chile)": ["Business", "Engineering", "Social Sciences"],
    "Universidad de Santiago de Chile": ["Engineering", "Humanities", "Social Sciences"],
    "Universidad de Antioquia": ["Medicine", "Engineering", "Social Sciences"],
    "University of Tokyo": ["Engineering", "Economics", "Natural Sciences"],
    "University of Chile": ["Medicine", "Arts", "Social Sciences"],
    "University of Edinburgh": ["Business", "Medicine", "Engineering"],
    "University of California, Santa Barbara (UCSB)": ["Environmental Studies", "Physics", "Psychology"],
    "University of Glasgow": ["Medicine", "Engineering", "Arts"],
    "University of Southern California (USC)": ["Film", "Business", "Engineering"],
    "University of Queensland": ["Biology", "Education", "Engineering"],
    "National University of Ireland, Galway": ["Arts", "Science", "Engineering"],
    "University of St Andrews": ["Philosophy", "International Relations", "Economics"],
    "Lund University": ["Engineering", "Social Sciences", "Medicine"],
    "University of Helsinki": ["Social Sciences", "Biology", "Law"],
    "University of Copenhagen": ["Business", "Social Sciences", "Health Sciences"],
    "University of Mannheim": ["Business", "Economics", "Social Sciences"],
    "Aalto University": ["Engineering", "Business", "Art and Design"],
    "University of Zurich": ["Economics", "Law", "Natural Sciences"],
    "Universidad Complutense de Madrid": ["Social Sciences", "Law", "Humanities"],
    "University of Amsterdam": ["Social Sciences", "Economics", "Law"],
    "University of Porto": ["Engineering", "Business", "Health Sciences"],
    "University of Vienna": ["Humanities", "Social Sciences", "Law"],
    "Stockholm University": ["Environmental Science", "Social Sciences", "Humanities"],
    "University of Bergen": ["Marine Research", "Health Sciences", "Social Sciences"],
    "University of Cape Town": ["Commerce", "Health Sciences", "Engineering"],
    "Universidad de la Habana": ["Social Sciences", "Engineering", "Humanities"],
    "University of Nairobi": ["Social Sciences", "Agriculture", "Engineering"],
    "University of the Andes": ["Business", "Engineering", "Health Sciences"],
    "University of Helsinki": ["Engineering", "Architecture", "Art"],
    "University of Exeter": ["Business", "Politics", "Environmental Science"],
    "University of Exeter": ["Engineering", "Medicine", "Business"],
    "University of Otago": ["Health Sciences", "Business", "Humanities"],
    "University of Queensland": ["Biology", "Social Sciences", "Business"],
    "University of Sussex": ["Social Sciences", "Engineering", "Business"],
    "Monash University": ["Medicine", "Business", "Engineering"],
    "University of Nottingham": ["Business", "Social Sciences", "Engineering"],
    "University of Glasgow": ["Engineering", "Humanities", "Social Sciences"],
    "University of Toronto Mississauga": ["Arts", "Social Sciences", "Business"],
    "University of Illinois at Chicago": ["Medicine", "Public Health", "Business"],
    "University of Kansas": ["Engineering", "Education", "Business"],
    "Purdue University": ["Engineering", "Agriculture", "Business"],
    "Florida State University": ["Business", "Education", "Social Sciences"],
    "University of North Carolina at Chapel Hill": ["Public Health", "Business", "Journalism"],
    "University of Missouri": ["Journalism", "Business", "Education"],
    "University of Massachusetts Amherst": ["Business", "Education", "Natural Sciences"],
    "Virginia Tech": ["Engineering", "Architecture", "Business"],
    "University of Arkansas": ["Agriculture", "Engineering", "Education"],
    "San Diego State University": ["Business", "Public Health", "Engineering"],
    "University of Oklahoma": ["Engineering", "Business", "Education"],
    "Oregon State University": ["Marine Sciences", "Engineering", "Agriculture"],
    "University of Kentucky": ["Agriculture", "Business", "Education"],
    "University of Idaho": ["Agriculture", "Natural Resources", "Engineering"],
    "Louisiana State University": ["Engineering", "Business", "Environmental Science"],
    "University of South Carolina": ["Business", "Engineering", "Health Sciences"],
    "Texas A&M University": ["Engineering", "Business", "Veterinary Medicine"],
    "University of Nevada, Reno": ["Agriculture", "Environmental Science", "Business"],
    "University of Hawaii at Manoa": ["Tropical Agriculture", "Oceanography", "Business"],
    "University of Colorado Boulder": ["Engineering", "Environmental Sciences", "Business"],
    "University of Illinois at Springfield": ["Public Affairs", "Health Sciences", "Business"],
    "Western Michigan University": ["Business", "Education", "Engineering"],
    "University of New Mexico": ["Native American Studies", "Business", "Engineering"],
    "University of Wyoming": ["Energy Resources", "Agriculture", "Engineering"],
    "Montana State University": ["Engineering", "Biological Sciences", "Business"],
    "Wayne State University": ["Law", "Business", "Engineering"],
    "North Dakota State University": ["Agriculture", "Engineering", "Business"],
    "University of Maine": ["Marine Sciences", "Business", "Education"],
    "Appalachian State University": ["Sustainable Development", "Business", "Education"],
    "Ball State University": ["Education", "Architecture", "Business"],
    "Binghamton University": ["Business", "Psychology", "Engineering"],
    "University of Southern Indiana": ["Business", "Health Sciences", "Education"],
    "California State University, Long Beach": ["Business", "Engineering", "Health Sciences"],
    "George Mason University": ["Public Policy", "Business", "Health Sciences"],
    "Cleveland State University": ["Business", "Law", "Engineering"],
    "Eastern Michigan University": ["Business", "Education", "Social Sciences"],
    "California State University, Sacramento": ["Business", "Public Policy", "Health Sciences"],

    # India
    "Indian Institute of Technology Bombay (IIT Bombay)": ["Engineering", "Computer Science", "Design"],
    "Indian Institute of Science (IISc)": ["Engineering", "Natural Sciences", "Management"],
    "University of Delhi": ["Arts", "Science", "Commerce"],
    "Jawaharlal Nehru University (JNU)": ["Social Sciences", "International Relations", "Language Studies"],
    "Indian Institute of Management Ahmedabad (IIMA)": ["Business", "Management", "Finance"],
    "National Institute of Fashion Technology (NIFT)": ["Fashion Design", "Textiles", "Management"],
    "Banaras Hindu University (BHU)": ["Arts", "Science", "Social Sciences"],
    
    # Moldova
    "Moldova State University": ["Law", "Economics", "History"],
    "Technical University of Moldova": ["Engineering", "Information Technology", "Architecture"],
    "Alecu Russo Balti State University": ["Education", "Social Sciences", "Arts"],
    "University of European Studies of Moldova": ["Political Science", "International Relations", "Law"],
    
    # UAE
    "United Arab Emirates University": ["Engineering", "Business", "Health Sciences"],
    "American University of Sharjah": ["Business", "Engineering", "Architecture"],
    "University of Sharjah": ["Health Sciences", "Engineering", "Arts"],
    "Abu Dhabi University": ["Business", "Engineering", "Health Sciences"],
    
    # China
    "Fudan University": ["Business", "Law", "International Relations"],
    "Shanghai Jiao Tong University": ["Engineering", "Management", "Computer Science"],
    "Zhejiang University": ["Engineering", "Natural Sciences", "Medicine"],
    "Renmin University of China": ["Social Sciences", "Law", "Economics"],
    "Sun Yat-sen University": ["Medicine", "Business", "Humanities"],
    "Nankai University": ["Economics", "Mathematics", "Chemistry"],
    "Tianjin University": ["Engineering", "Architecture", "Computer Science"],
}

# Base directory for creating university folders
base_dir = "Universities Info"
os.makedirs(base_dir, exist_ok=True)


# Create folders for each university
for university, programs in universities_with_programs.items():
    # Use the original university name for the folder name
    folder_name = university
    
    # Create a folder for each university inside the base directory
    university_dir = os.path.join(base_dir, folder_name)
    os.makedirs(university_dir, exist_ok=True)
    
    # Create a placeholder for general university information, naming it with the university name
    about_file_name = f"{university}.md"
    about_file_path = os.path.join(university_dir, about_file_name)
    with open(about_file_path, "w") as f:
        f.write(f"# About {university}\n")
        f.write("## Location:\n- [Enter location here]\n")
        f.write("## Other Details:\n- [Enter additional information here]\n")
    
    # Create a separate file for the list of programs
    programs_file_name = f"All available programmes at {university}.md"  # Corrected line
    programs_file_path = os.path.join(university_dir, programs_file_name)
    with open(programs_file_path, "w") as f:
        f.write(f"# Programs Offered at {university}\n\n")
        for program in programs:
            f.write(f"## {program}\n")
            f.write("- [Enter program details here]\n\n")
            f.write("---\n")  # Horizontal line between programs
    
    # Create folders for famous programs within each university
    for program in programs:
        program_dir = os.path.join(university_dir, program)
        os.makedirs(program_dir, exist_ok=True)
        
        # Create a placeholder file for program-specific notes
        with open(os.path.join(program_dir, "Notes.md"), "w") as f:
            f.write(f"# Notes for {program} at {university}\n")
            f.write("- [Add course notes here]\n")

print("Folders and files created successfully!")