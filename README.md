# BLOOD-APP

<h1>Blood Donor Management System</h1>

## <h3>Project Overview</h3>
This project implements a Blood Donor Management System using Python and MySQL, designed to facilitate the registration and retrieval of blood donor information across various cities. It allows users to register their details, search for donors by blood group and city, and manage emergency blood requests efficiently.

## <h3>Tools and Technologies Used</h3>
- **Python**: Used for the core logic and interaction with users through the command-line interface.
- **MySQL**: Database management system used to store donor and emergency contact information.
- **Colorama**: Python library for colored terminal text output, enhancing user experience.
- **JSON**: Initially considered for data storage before migrating to MySQL, can be extended for future requirements.
- **Git and GitHub**: Version control and repository hosting platform for collaboration and code management.

## <h3>Methods Implemented</h3>

1. **Registration of Donor Information**:
   - Allows users to input their name, city, mobile number, and blood group which is stored in a MySQL database.

2. **Search Donors by City and Blood Group**:
   - Retrieves a list of donors matching a specified city and blood group from the MySQL database.

3. **List of Donors for a Specific Blood Group Across Cities**:
   - Displays donors available for a specified blood group across all registered cities.

4. **Blood Matching Algorithm**:
   - Provides compatibility information for blood donation and reception based on blood group types.

5. **Display All Donors in a City**:
   - Lists all donors registered in a particular city across all blood groups.

6. **Emergency Contact Details**:
   - Manages emergency patient details including their name, blood group, hospital name, and contact number stored in MySQL.

7. **Update and Delete Emergency Details**:
   - Allows updating and deletion of emergency contact details based on patient name or contact number.

## <h3>Getting Started</h3>
To run this project locally:
1. Clone this repository.
2. Ensure Python 3.x and MySQL are installed on your system.
3. Install the necessary Python dependencies using `pip install -r requirements.txt`.
4. Set up your MySQL database using the provided schema (`BloodDonors.sql`).
5. Update MySQL connection details in the Python code (`Main.py`) as per your configuration.
6. Run `Main.py` to start the Blood Donor Management System.

## <h3>Future Improvements</h3>
- Enhance user interface with a graphical user interface (GUI) for better usability.
- Implement user authentication and access control for more secure data management.
- Expand functionalities to include more complex queries and statistical reporting.

Feel free to contribute by forking and submitting pull requests!

---
