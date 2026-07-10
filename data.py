from datetime import datetime, timedelta

# ===================================================
# The following is the list of Library Branches
# ===================================================

branches = {
    "DBN001": {
        "name": "Durban Central Library",
        "address": "45 Anton Lembede St, Durban CBD",
        "librarian": "Mrs Marias",
        "catalogue_size": 12000,
        "max_daily_loans": 75,
        "active_loans": 0
    },

    "PIN002": {
        "name": "Pinetown Public Library",
        "address": "41 Kings Road, Pinetown",
        "librarian": "Mrs Singh",
        "catalogue_size": 7500,
        "max_daily_loans": 75,
        "active_loans": 0
    },

    "UML003": {
        "name": "Umlazi Community Library",
        "address": "Section V, Umlazi Township",
        "librarian": "Mr Khumalo",
        "catalogue_size": 5800,
        "max_daily_loans": 75,
        "active_loans": 0
    }
}

# ===================================================
# Thesse are the Membership Rules
# ===================================================

MEMBERSHIP_RULES = {
    "Junior": {"limit": 3, "period": 14},
    "Standard": {"limit": 5, "period": 21},
    "Senior": {"limit": 8, "period": 30},
    "Student": {"limit": 10, "period": 21}
}

# ===================================================
# The folllowing is the List of Members:
# ===================================================

members = {
    "EML01": {
        "name": "Akayliah Perumal",
        "sa_id": "0803077645321",
        "contact": "0615423784",
        "email": "akayliah06@gmail.com",
        "branch": "PIN002",
        "membership_type": "Student",
        "status": "Active",
        "active_loans": [],
        "outstanding_fines": 0
    },

    "EML02": {
        "name": "Rayleen Govender",
        "sa_id": "9810203289731",
        "contact": "0746789874",
        "email": "RayleenGov@gmail.com",
        "branch": "DBN001",
        "membership_type": "Standard",
        "status": "Active",
        "active_loans": [],
        "outstanding_fines": 0
    },

    "EML03": {
        "name": "Nadine Jasmin Singh",
        "sa_id": "0801023486215",
        "contact": "0823658765",
        "email": "nadinejs@gmail.com",
        "branch": "UML003",
        "membership_type": "Student",
        "status": "Active",
        "active_loans": [],
        "outstanding_fines": 0
    },

    "EML04": {
        "name": "Deevashnee Naidoo",
        "sa_id": "6012297864523",
        "contact": "0832537865",
        "email": "DeevashneeN@gmail.com",
        "branch": "DBN001",
        "membership_type": "Senior",
        "status": "Active",
        "active_loans": [],
        "outstanding_fines": 0
    },

    "EML05": {
        "name": "Jade Dhorai",
        "sa_id": "1512178320987",
        "contact": "0625674356",
        "email": "Dhoraijade@gmail.com",
        "branch": "UML003",
        "membership_type": "Junior",
        "status": "Active",
        "active_loans": [],
        "outstanding_fines": 0
    },

    "EML06": {
        "name": "Vaneshree Govender",
        "sa_id": "8708212649327",
        "contact": "0795953969",
        "email": "gvaneshree@gmail.com",
        "branch": "PIN002",
        "membership_type": "Standard",
        "status": "Active",
        "active_loans": [],
        "outstanding_fines": 0
    },

    "EML07": {
        "name": "Bryson Rampersad",
        "sa_id": "1811128109364",
        "contact": "0613815141",
        "email": "brysonR@gmail.com",
        "branch": "UML003",
        "membership_type": "Junior",
        "status": "Active",
        "active_loans": [],
        "outstanding_fines": 0
    },

    "EML08": {
        "name": "Nicolette Naidoo",
        "sa_id": "9510013894267",
        "contact": "0837919026",
        "email": "nicolette05@gmail.com",
        "branch": "DBN001",
        "membership_type": "Standard",
        "status": "Active",
        "active_loans": [],
        "outstanding_fines": 0
    },

   "EML09": {
        "name": "Tashmika Rampersad",
        "sa_id": "6702208490245",
        "contact": "0626578904",
        "email": "tash04@gmail.com",
        "branch": "PIN002",
        "membership_type": "Senior",
        "status": "Active",
        "active_loans": [],
        "outstanding_fines": 0
    },

    "EML10": {
        "name": "Shivani Govender",
        "sa_id": "9711059486214",
        "contact": "0785239857",
        "email": "shiavnig02@gmail.com",
        "branch": "DBN001",
        "membership_type": "Standard",
        "status": "Active",
        "active_loans": [],
        "outstanding_fines": 0
    } 
}

# ===================================================
# The following is the List of Books:
# ===================================================

books = [
    {
        "isbn": "9780131103628",
        "title": "Intro to Computers",
        "author": "N. Singh",
        "copies": 10,
        "branch": "DBN001"
    },

    {
        "isbn": "9780316769488",
        "title": "Everything You Need To Know About AWS",
        "author": "L. Rampersad",
        "copies": 8,
        "branch": "PIN002"
    },

    {
        "isbn": "9781491957660",
        "title": "Making Python Simpler",
        "author": "A. Muchumayiri",
        "copies": 6,
        "branch": "UML003"
    },

    {
        "isbn": "9780596007973",
        "title": "The Basics of HTML",
        "author": "T. Aphane",
        "copies": 4,
        "branch": "DBN001"
    },


    {
        "isbn": "9780131103627",
        "title": "Proggramming Made Easier",
        "author": "B. Rampersad",
        "copies": 5,
        "branch": "PIN002"
    },

    {
        "isbn": "9780201616224",
        "title": "Intro to E-Commerce",
        "author": "A. Rampursad",
        "copies": 7,
        "branch": "PIN002"
    },

    {
        "isbn": "9780262033848",
        "title": "Networking Basics",
        "author": "S. Singh",
        "copies": 4,
        "branch": "UML003"
    },

    {
        "isbn": "9780132350884",
        "title": "Learning Java",
        "author": "N. Naidoo",
        "copies": 6,
        "branch": "DBN001"
    },

    {
        "isbn": "9781492051367",
        "title": "Cloud Computing Basics",
        "author": "S. Reddy",
        "copies": 5,
        "branch": "PIN002"
    },

    {
        "isbn": "9781449355739",
        "title": "Web Development Essentials",
        "author": "T. Pillay",
        "copies": 3,
        "branch": "UML003"
    },

    {
        "isbn": "9780596009205",
        "title": "HTML and CSS Guide",
        "author": "R. Pillay",
        "copies": 6,
        "branch": "DBN001"
    },

    {
        "isbn": "9781787125933",
        "title": "Cyber Security Fundamentals",
        "author": "K. Naicker",
        "copies": 5,
        "branch": "PIN002"
    },

    {
        "isbn": "9781119457894",
        "title": "Computer Networks",
        "author": "W.Mthombeni",
        "copies": 8,
        "branch": "UML003"
    },

    {
        "isbn": "9781801070799",
        "title": "Software Engineering Concepts",
        "author": "D. Ramsunder",
        "copies": 4,
        "branch": "DBN001"
    },

    {
        "isbn": "9781839214111",
        "title": "Artificial Intelligence Basics",
        "author": "P. Khumalo",
        "copies": 6,
        "branch": "PIN002"
    },

    {
        "isbn": "9781484283566",
        "title": "Machine Learning for Beginners",
        "author": "Y. Naicker",
        "copies": 5,
        "branch": "UML003"
    },

    {
        "isbn": "9781098104030",
        "title": "Programming Logic",
        "author": "L. Reddy",
        "copies": 7,
        "branch": "DBN001"
    },

    {
        "isbn": "9781803234014",
        "title": "Introduction to Algorithms",
        "author": "B. Nair",
        "copies": 4,
        "branch": "PIN002"
    },

    {
        "isbn": "9781789957648",
        "title": "Computer Architecture",
        "author": "N. Chetty",
        "copies": 5,
        "branch": "UML003"
    },

    {
        "isbn": "9781800568105",
        "title": "Digital Literacy Skills",
        "author": "G. Naicker",
        "copies": 6,
        "branch": "DBN001"
    },

    {
        "isbn": "9781801812443",
        "title": "Database Management Systems",
        "author": "N. Daniels",
        "copies": 3,
        "branch": "PIN002"
    },

]

# ===================================================
# Different Staff Accounts
# ===================================================

staff_accounts = {
    "librarian": {
        "password": "confidential@12",
        "role": "Librarian",
        "full_name": "Mary-Anne",
        "branch_code": "DBN001"
    },

    "senior": {
        "password": "Moorton123",
        "role": "Senior Librarian",
        "full_name": "Ariana Moodley",
        "branch_code": "PIN002"
    },

    "admin": {
        "password": "admin@12",
        "role": "System Administrator",
        "full_name": "System Admin",
        "branch_code": "DBN001"
    }
}

# ===================================================
# Loans and Payments
# ===================================================

loan_records = [

    {
        "loan_id": 1,
        "member_id": "EML01",
        "isbn": "9780131103627",
        "branch_code": "PIN002",
        "issue_date": datetime.now() - timedelta(days=10),
        "due_date": datetime.now() + timedelta(days=11),
        "return_date": None,
        "days_overdue": 0,
        "fine_amount": 0,
        "fine_paid": False
    },

    {
        "loan_id": 2,
        "member_id": "EML02",
        "isbn": "9780201616224",
        "branch_code": "DBN001",
        "issue_date": datetime.now() - timedelta(days=30),
        "due_date": datetime.now() - timedelta(days=9),
        "return_date": None,
        "days_overdue": 9,
        "fine_amount": 22.50,
        "fine_paid": False
    },

    {
        "loan_id": 3,
        "member_id": "EML03",
        "isbn": "9780262033848",
        "branch_code": "UML003",
        "issue_date": datetime.now() - timedelta(days=15),
        "due_date": datetime.now() + timedelta(days=6),
        "return_date": None,
        "days_overdue": 0,
        "fine_amount": 0,
        "fine_paid": False
    },

    {
        "loan_id": 4,
        "member_id": "EML04",
        "isbn": "9780132350884",
        "branch_code": "DBN001",
        "issue_date": datetime.now() - timedelta(days=40),
        "due_date": datetime.now() - timedelta(days=10),
        "return_date": None,
        "days_overdue": 10,
        "fine_amount": 10.00,
        "fine_paid": False
    },

    {
        "loan_id": 5,
        "member_id": "EML05",
        "isbn": "9781492051367",
        "branch_code": "UML003",
        "issue_date": datetime.now() - timedelta(days=8),
        "due_date": datetime.now() + timedelta(days=13),
        "return_date": None,
        "days_overdue": 0,
        "fine_amount": 0,
        "fine_paid": False
    },

    {
        "loan_id": 6,
        "member_id": "EML06",
        "isbn": "9781449355739",
        "branch_code": "PIN002",
        "issue_date": datetime.now() - timedelta(days=50),
        "due_date": datetime.now() - timedelta(days=20),
        "return_date": None,
        "days_overdue": 20,
        "fine_amount": 50.00,
        "fine_paid": False
    },

    {
        "loan_id": 7,
        "member_id": "EML07",
        "isbn": "9780596009205",
        "branch_code": "UML003",
        "issue_date": datetime.now() - timedelta(days=5),
        "due_date": datetime.now() + timedelta(days=16),
        "return_date": None,
        "days_overdue": 0,
        "fine_amount": 0,
        "fine_paid": False
    },

    {
        "loan_id": 8,
        "member_id": "EML08",
        "isbn": "9781787125933",
        "branch_code": "DBN001",
        "issue_date": datetime.now() - timedelta(days=25),
        "due_date": datetime.now() - timedelta(days=4),
        "return_date": None,
        "days_overdue": 4,
        "fine_amount": 10.00,
        "fine_paid": False
    },

    {
        "loan_id": 9,
        "member_id": "EML09",
        "isbn": "9781119457894",
        "branch_code": "PIN002",
        "issue_date": datetime.now() - timedelta(days=12),
        "due_date": datetime.now() + timedelta(days=9),
        "return_date": None,
        "days_overdue": 0,
        "fine_amount": 0,
        "fine_paid": False
    },

    {
        "loan_id": 10,
        "member_id": "EML10",
        "isbn": "9781801070799",
        "branch_code": "DBN001",
        "issue_date": datetime.now() - timedelta(days=35),
        "due_date": datetime.now() - timedelta(days=5),
        "return_date": None,
        "days_overdue": 5,
        "fine_amount": 12.50,
        "fine_paid": False
    },

    {
        "loan_id": 11,
        "member_id": "EML01",
        "isbn": "9781839214111",
        "branch_code": "PIN002",
        "issue_date": datetime.now() - timedelta(days=7),
        "due_date": datetime.now() + timedelta(days=14),
        "return_date": None,
        "days_overdue": 0,
        "fine_amount": 0,
        "fine_paid": False
    },

    {
        "loan_id": 12,
        "member_id": "EML03",
        "isbn": "9781484283566",
        "branch_code": "UML003",
        "issue_date": datetime.now() - timedelta(days=18),
        "due_date": datetime.now() - timedelta(days=1),
        "return_date": None,
        "days_overdue": 1,
        "fine_amount": 1.50,
        "fine_paid": False
    },

    {
        "loan_id": 13,
        "member_id": "EML05",
        "isbn": "9781098104030",
        "branch_code": "UML003",
        "issue_date": datetime.now() - timedelta(days=9),
        "due_date": datetime.now() + timedelta(days=12),
        "return_date": None,
        "days_overdue": 0,
        "fine_amount": 0,
        "fine_paid": False
    },

    {
        "loan_id": 14,
        "member_id": "EML07",
        "isbn": "9781803234014",
        "branch_code": "UML003",
        "issue_date": datetime.now() - timedelta(days=28),
        "due_date": datetime.now() - timedelta(days=7),
        "return_date": None,
        "days_overdue": 7,
        "fine_amount": 6.00,
        "fine_paid": False
    },

    {
        "loan_id": 15,
        "member_id": "EML10",
        "isbn": "9781789957648",
        "branch_code": "DBN001",
        "issue_date": datetime.now() - timedelta(days=14),
        "due_date": datetime.now() + timedelta(days=7),
        "return_date": None,
        "days_overdue": 0,
        "fine_amount": 0,
        "fine_paid": False
    }

]

payments = []

reservations = []

def initialise_data():
    return (
        branches,
        members,
        books,
        staff_accounts,
        loan_records,
        payments,
        reservations
    )