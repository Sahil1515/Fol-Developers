
from geopy.geocoders import Nominatim

cities = ["Sitamarhi", "Mysuru", "Dewas", "Noida", "Tikamgarh", "Lateri", "Gwalior", "Tinwari", "Delhi", "Jodhpur",
          "Jaipur", "Hyderabad", "Jodhpur", "Tirunelveli", "Kunigal", "Nandyal", "Ajmer", "Delhi", "Donimalia",
          "Township", "Vrindavan", "Chennai", "Hyderabad", "Manipal", "Mangalore", "kolkata", "Delhi", "Kota", "city",
          "Nasik", "Jodhpur", "Jodhpur", "Mandsaur", "Ujjain", "Mysore", "Mumbai", "Hyderabad", "Manipal", "Sri",
          "Ganganagar", "Dholpur,", "Rajasthan", "Silchar", "Hosur", "Indore", "Hyderabad", "Rowta", "Chariali",
          "Hyderabad", "Pune", "Delhi", "Banswara", "Hyderabad", "Manipal", "udupi", "SRIKAKULAM", "Sriganganagar",
          "Jammu", "patna", "Visakhapatnam", "Pavagada", "Ellenabad", "jablapur", "Shivpuri", "Bagaha", "Agra",
          "Indore", "Kanakapura", "Jodhpur", "Dharwad", "Kota", "Manipal", "Jaipur", "Pandaria", "Nellore", "Jaipur",
          "Patna", "Jodhpur", "Delhi", "Delhi", "Jodhpur", "Kota", "Dandeli", "Manipal", "Vizag", "Siddapur", ",",
          "Dist", "Uttara", "Kannada,", "Karnataka", "Manipal", "udupi", "Ahmedabad", "Hyderabad", "Ranchi", "Kota",
          "Hyderabad", "Indore", "Delhi", "Jodhpur", "Jodhpur", "Mhow", "mp", "Kota", "chitradurga", "Shimoga", "Delhi",
          "Jodhpur", "Kota", "sriganganagar", "Kurnool", "Visakhapatnam", "Davangere", "Hyderabad", "Hyderabad",
          "Kommaghatta,", "kengeri", "Hyderabad", "Channapattana", "Hyderabad", "Raichur", "Jaipur", "Jaora", "Jodhpur",
          "Kerala", "Davangere", "Indore", "Narsinghpur", "Rewa", "Kota", "Chikkamgluru", "Berhampur", "Jodhpur",
          "Hyderabad", "Davangere", "Alwar", "Jodhpur", "Motihari", "Patna", "Manipal", "Kolar", "", "gold", "",
          "field", "Jahazpur", "Delhi", "Tumkur", "Jodhpur", "Honnavar", "Jaipur", "Palakkad", "Chitradurga",
          "Karnataka", "Kota", "Jodhpur", "Mysore", "Davangere", "Davangere", "Hyderabad", "Delhi", "Kolkata",
          "Chandigarh", "Telangana", "Bidar", "Mangaluru", "Haridwar", "Jabalpur", "Belagavi", "Udhampur", "Ganjam,",
          "Shrirangpatna", "Bhopal", "Jodhpur", "Delhi", "chhindwara", "hyderabad", "Narnaul", "Hyderabad", "Jodhpur",
          "Rajasthan", "Indore", "Sriganganagar", "Jaipur", "Delhi", "Navi", "Mumbai", "Firozabad", "Indore", "guna",
          "jodhpur", "Sagar", "Kotkapura", "KESRISINGHPUR", "Rattihalli", "Visakhapatnam", "Lucknow", "Coimbatore",
          "Indore", "Jodhpur", "Ramnagar", "Mumbai", "Hyderabad", "Coimbatore", "Trivandrum", "Davangere", "Davangere",
          "Chitradurga", "Jaipur", "Mandya", "Delhi", "Doddaballapura", "Manipal", "Chitradurga", "Jodhpur",
          "Visakhapatnam", "Dharmapuri", "Mumbai", "Ujjain", "Karwar", "Jaipur", "Kota", "Navi", "Mumbai", "Gadag",
          "Mysore", "Mumbai", "Jaipur", "Indore", "peapully", "Medak", "Ramanagara", "jhunjhunu", "Gwalior", "Pandalam",
          "Bhilwara", "Jodhpur", "Kota", "Paonta", "sahib", "Thane", "Vizag", "Indore", "cuttack", "Sitamarhi",
          "Shimoga", "mumbai", "Thrissur", "Hyderabad", "Makarana", "(nagour)", "Kota", "Indore", "Ramanagara",
          "Meghalaya", "Kota", "Kota", "Jharkhand", "Kota", "Bikaner", "Indore", "Jodhpur", "Indore", "Kota", "Erode",
          "Mansarover", "Tumkur", "Vijayawada", "Jodhpur", "Kota", "Mandya", "Jaipur", "Bikaner", "Pune", "Patna",
          "Chitradurga", "Kota", "Bharatpur", "Jodhpur", "Chennai", "Chintamani", "Chikkaballapur", "dist", "Beawar",
          "Malavalli", "Hiriyur,chitradurga", "district", "Kota", "Delhi", "Udhampur,", "jammu", "Indore", "Hassan",
          "Indore", "Varanasi", "Kolar", "kota", "Kumta", "Bhopal", "Bikaner", "Nellore", "Hyderabad", "Hyderabad",
          "Lucknow", "Honnavar", "Ahmednagar", "Udupi", "Salem", "Udaipur", "Rewa", "Etah", "Manipal", "Indore",
          "BEGUSARAI", "Shivmoga", "Manipal", "udupi", "Kalaburgi", "Jaipur", "Indore", "Indore", "Dungarpur", "Rewa",
          "Raiganj", "Shivamogga", "Delhi", "Varanasi", "Jaipur", "jodhpur", "Jaipur", "Delhi", "JODHPUR", "Ulhasnagar",
          "Pune", "Hyderabad", "Banda", "Sikar", "Jaipur", "Odisha", "jaipur", "Udaipur,", "Rajasthan", "Kota", "Ritu",
          "Alipurduar", "NASHIK", "Lucknow", "Hyderabad", "Manipal", "udupi", "Kota", "Alwar", "baran", "Jodhpur",
          "Indore", "Delhi", "Jodhpur", "Dandeli", "Mumbai", "Nalasopara", "Kolkata", "Mysore", "Jodhpur", "Vrindavan",
          "Jaipur", "Delhi", "Jodhpur", "Jaipur", "Hyderabad", "Vijayawada", "Bihar", "Jaipur", "Chirawajhunjhunu",
          "Nagpur", "Jabalpur", "Jodhpur", "Nanded", "Mumbai", "Hyderabad", "Indore", "Meerut", "Pune", "Thrissur",
          "Gwalior", "Delhi", "Neemuch", "Shivamoga", "Meerut", "VELLORE", "Jodhpur", "khandwa", "Bhilwara", "Udaipur",
          "Jhabua", "Kolar", "Hubli", "Jodhpur", "Hyderabad", "Jhunjhunu", "Jodhpur", "Jodhpur", "Hyderabad", "Jodhpur",
          "Betul", "Hyderabad", "Coimbatore", "Hathras", "Jaipur", "Kumta", "North", "canara", "karnataka", "Kolhapur",
          "Jaipur", "Pune", "Hindupur", "Sriganganagar", "Dhanbad", "Chitradurga", "Nandyal", "Tonk", "Rajasthan",
          "Udupi", "Hyderabad", "Davangere", "Nagaur", "Jaipur", "Hyderabad", "Darbhanga", "jodhpur", "Jalandhar",
          "Mulbagal", "hubli", "Agra", "udaipur", "Kommenahalli", "grama", "jodhpur", "Jodhpur", "Kolkata", "Indore",
          "Indore", "Jodhpur", "Chandrapur", "Surat", "Udaipur", "Jodhpur", "Jodhpur", "Delhi", "Vrindavan", "Mumbai",
          "Indore", "Bhopal", "Jodhpur", "Kota", "Ballari", "Jaipur", "Kota", "Hyderabad", "Dharwad", "Krishnagiri",
          "Jodhpur", "Davangere", "Hyderabad", "Hinganghat", "Bilaspur", "Delhi", "Davangere", "Dehli", "Jodhpur",
          "Manipal", "Jaipur", "Jodhpur", "Udaipur", "Hungund", "Hyderabad", "Hyderabad", "Jodhpur", "Jaipur", "Indore",
          "Kolkata", "Jodhpur", "Mysore", "Kurnool", "Dharwad", "Sambalpur", "Kakinada", "Jodhpur", "Bhopal",
          "Hyderabad", "Hyderabad", "Delhi", "Hyderabad", "Alwar", "Meerut,U.p", "Jaipur", "Bhopal", "Kolkata", "Delhi",
          "Hosur", "Delhi", "Sambalpur", "Hyderabad", "Jodhpur", "Shillong", "Jodhpur", "Hyderabad", "Nimbhahera",
          "Hyderabad", "Jodhpur,", "Rajasthan", "Ahmedabad", "Pathalgaon,Chhtattisgarh", "Rewa", "Mysore", "Maysore",
          "city", "udbur", "villege", "Indore", "Lucknow", "jammu", "Sanjaynagar", "Amritsar", "Kota", "Jodhpur",
          "Banavara", "Davangere", "Alwar", "Indore", "Kota", "Jaipur", "Mumbai", "Dehli", "Gorakhpur", "Hosur",
          "Chickballapur", "Manipal", "Mandya", "Katni", "Kolar", "district", "Kota", "Shivamogga", "Ahmedabad",
          "Indore", "Hindaun", "Hyderabad", "Shillong", "Vrindavan", "Kherli", "(Alwar)", "Beawar", "Varanasi",
          "Dharwd", "Kurnool", "Maski", "Kota", "jhansi", "Jodhpur", "hyderabad", "Hyderabad", "Chikmaglore", "Kota",
          "Korba", "jodhpur", "Chitradurga", "Udaipur", "Davangere", "Indore", "Patna", "Jodhpur", "Mainpuri", "(Up)",
          "Hanumangarh", "Kanpur", "Siliguri", "Jhumritelaiya", "Jamshedpur", "Hyderabad", "Kerala", "Hyderabad",
          "Chikkaballapur", "Hubli", "Rajasthan", "Delhi", "Belagam", "Jodhpur", "Bihar", "Jodhpur", "Tumkur",
          "Kudligi", "(T),", "Bellari", "(D)", "Jaipur", "Vizag", "Surat", "Delhi", "Etawah", "Rajahmundry",
          "Hyderabad", "Jodhpur", "Ballari", "PATNA", "Ramnagar", "Kolar", "Jaipur", "Hyderabad", "Manipal", "udupi",
          "Sikar", "Satna", "Jodhpur", "Jodhpur", "ujjain", "Dharwad", "Hyderabad", "Ujjain", "Varanasi", "Delhi",
          "Delhi", "Seoni", "mp", "Dhanbad", "Kodagu", "Kolar", "jodhpur", "Kolkata", "Pali", "Hyderabad", "Jhujhunu",
          "Jaipur", "Indore", "jabalpur", "Pune", "Hyderabad", "Indore", "Vishakapatnam", "Wardha", "Jodhpur",
          "Coimbatore", "Hyderabad", "JODHPUR", "Davangere", "Indore", "Mehidpur", "Road", "Bhopal", "Sirsi",
          "Mangalagiri", "-", "Andhra", "Preadesh", "Jaipur", "Hyderabad", "Abu", "Road", "Delhi", "Jodhpur", "Nagpur",
          "Hyderabad", "Indore", "Vizag", "Raichur", "Jodhpur", "Ranchi", "Chennai", "Sri", "Ganganagar", "Ludhiana",
          "Tanuku", "Jamshedpur", "Kolkata", "Hosur", "Delhi", "Khandwa", "Kota", "Churu", "Agra", "Anantapur",
          "Ramanagara", "Hyderabad", "Gohad", "Udaipur", "Indore", "Hyderabad", "Hyderabad", "Muzaffarpur", "Uttara",
          "Kannada,", "siddapur", "Jhalrapatan", "distt", "jhalawar", "Palwal", "Delhi", "JODHPUR", "Indore", "Udupi",
          "Surat", "Indore", "Indore", "Imphal", "Rohtak", "ranebennur", "Jaipur", "Hyderabad", "Palakkad", "Raichur",
          "JODHPUR", "Hyderabad", "Vrindavan", "Bikaner", "Hosur", "Delhi", "Indore", "Kolkata", "Hyderabad",
          "Ramanagara", "Sri", "ganganagar", "Jaipur", "Wayanad", "Chandrapur", "Sangli", "Sikar", "Ahmedabad", "Sikar",
          "sri", "ganganagar", "Hyderabaf", "Mumbai", "yehalanka", "Davangere", "Raichur", "Indore", "Pune",
          "Bahadurgarh", "Bhilwara", "Mandya", "Mandya", "Patna", "Udaipur", "Degana", "Sikar", "ALWAR", "(", "RAJ)",
          "Jodhpur", "Jaipur", "Hyderabad", "Bhilai", "Jammu", "Karwar", "Jodhpur", "Jodhpur", "Patna", "Hyderabad",
          "Hyderabad", "Manipal", "udupi", "Haveri", "Indore", "Kasaragod", "Betul", "Mysuru", "jodhpur", "Tiptur",
          "Mandya", "Karnataka", "Kolar", "Indore", "jaipur", "Ernakulam", "Noida", "Patna", "Jodhpur", "Channapatana",
          "Chandigarh", "Khatima", "Chennai", "Bilaspur", "Delhi", "Bokaro", "gwalior", "Jaipur", "Yemmiganur",
          "Chennai", "Indore", "Avathi", "Patna", "800020", "Peapully", "Delhi", "Hyderabad", "Jodhpur", "Jaipur",
          "Kota", "Hyderabad", "Sikar", "Mysuru", "Indore", "Mumbai", "Shivamogga", "Kasganj", "HYDERABAD",
          "Pathanamthitta", "Delhi", "Ajmer", "Bhayandar", "East", "Hyderabad", "Jaipur", "Jodhpur", "Calcutta",
          "Hyderabad", "Bhopal", "Alwar", "Jodhpur", "Patna", "Jaipur", "Raipur", "Delhi", "Indore", "Delhi", "Jodhpur",
          "Kolar", "Dholpur", "Kota", "Nagpur", "Visakhapatnam", "Hyderabad", "Mysore", "Jaipur", "Bhopal", "Nagpur",
          "Silchar", "Hyderabad", "Ooty", "Delhi", "visakhapatnam", "Mandya", "Hyderabad", "Bikaner", "Ranebennur",
          "Hyderabad", "Hy6", "Bihar", "Bikaner", "Chennai", "Kota", "Shimoga", "Tinsukia", "Noida", "Delhi",
          "Sriganganagar", "Mangalore", "Ankola", "Dharwad", "Coimbatore", "Salem", "Betul", "BAGALKOT", "Agra",
          "Visakhapatnam", "Patna", "Manipal", "Kota", "(rajasthan)", "Jodhpur", "Delhi", "muzaffarnagar", "Nellore",
          "Alwar", "Bidar", "Srikakulam", "Kakinada", "Kolar", "jaipur", "Alwar", "Jodhpur", "Davangere", "Mainpuri",
          "Bijainagar", "Davangere", "Hubli", "Koppal", "Kota", "Udaipur", "Baraut", "Mudigere", "Kota", "Vellore",
          "Coimbatore", "Chennai", "Mohali,", "punjab", "Sitamarhi", "Mathura", "Jaipur", "Davangere", "Mumbai",
          "Udaipur", "Mysore", "Mandya", "Ujjain", "Kundapur", "Indore", "Mysuru", "Raipur", "Thrissur", "Indore",
          "Sriganganagar", "Vijayawada", "Bikaner", "Jhansi", "Lucknow", "Jodhpur", "Bhopal", "Mumbai", "Mumbai",
          "Chickmagalur", "Indore", "Pratapgarh", "Patna", "Jodhpur", "Nandyal", "Karwar", "Mirzapur", "Dehli",
          "Dehradun", "Pali", "Palsana,", "Sikar", "Vapi", "Hyderabad", "Khurai", "Kota", "Mathura", "Bhilwara",
          "Pandalam", "pilani", "Udaipur", "Jaipur", "Chintamani", "Hyderabad", "Tanakallu", "Kolar", "Pathanamthitta",
          "Others", "Tumkur", "Dhanbad", "Panipat", "Tumakuru", "Jodhpur", "Vidisha", "Pune", "Baran", "Dharwad",
          "Kota", "Kota", "Chickballapur", "Jaipur", "Vadodara", "Kolar", "Shri", "ganganagar", "Pali,", "Rajasthan",
          "Darbhanga", "Delhi", "Wardha", "hinganghat", "Palakol", "Visakhapatnam", "Jamshedpur", "Coonoor", "Jind",
          "Delhi", "Kolkata", "Ujjain", "Chitrdurga", "Kadapa", "Jodhpur", "Jodhpur,", "Rajasthan", "Mysore,",
          "Karnataka", "Ballari", "Jodhpur", "Rajesthan", "", "Bharatpur", "jodhpur", "Jaipur", "Manipal", "Manipal",
          "Khandwa", "Jodhpur", "Wayanad", "Kota", "Gorakhpur", "RAJAHMUNDRY", "Jodhpur", "Hyderabad", "Jaipur",
          "Kolar", "Mumbai", "Jodhpur", "Bhilwara", "Jaipur", "Surat", "Yellapur", "Ghaziabad", "Jodhpur", "Jodhpur",
          "Delhi", "Pali", ",rajasthan", "Hydearabad", "JAIPUR", "Jodhpur", "Manipal", "Hyderabad", "Thrissur",
          "Kerala", "Mumbai", "Hong", "Kong", "Kota", "Jaipur", "Chennai", "Nandyal", "Jaipur", "Mangalore", "Chennai",
          "Indore", "Jodhpur", "Jodhpur", "Delhi", "Siddapur", "Mumbai", "Coimbatore", "Coimbatore", "Kota", "Sagar",
          "Hyderabad", "Secunderabad", "Haveri", "dst,", "Hirekerur", "Kakinada", "Jaipur", "Sri", "Ganganagar",
          "Raipur", "Jodhpur", "Vizag", "Delhi", "Manipal", "Delhi", "Lucknow", "Jodjpur", "Jodhpur", "Tirupathi",
          "Hyderabad", "Tumkur", "Arasikere", "573103", "JODHPUR", "Bundi", "Visakhapatnam", "Sri", "Ganganagar,",
          "Rajasthan", "Ahmedabad", "Sri", "Ganganagar", "Kota", "Varanasi", "Barghat", "Delhi", "Dhar", "Unnao",
          "Delhi", "Hanumangarh", "Indore", "Sri", "Ganganagar", "Allahabad", "Davangere", "Kota", "Alwar",
          "Rewa/indore", "INDORE", "Hyderabad", "Ujjain", "Shivamogga,karnataka", "Dharwad", "Jaipur", "Hyderabad",
          "Mysuru", "Ujjain", "Manipal", "Jodhpur", "Sullia", "Jodhpur", "Tanuku", "Varanasi", "Chitradurga", "Jodhpur",
          "Davangere", "Kota", "Satna", "Jaipur", "Delhi", "Jaipur", "Parbhani", "Manipal", "udupi", "Purulia",
          "Jodhpur", "Bhagalpur", "Jaipur", "Ranchi", "Kerala,", "alappuzha", "Suryapet", "Jaipur", "Kannur,", "kerala",
          "Jaipur", "UJJAIN", "jodhpur", "Sagar", "Gwalior", "Raipur", "Bhopal", "Indore", "Sikar", "Dharwad",
          "Moradabad", "Tumkur", "PALI", "Bilaspur", "Manipal", "udupi", "Manipal", "Indore", "Indore", "Kasaragod",
          "Davangere", "nagpur", "Ananthapur", "Manipal", "Udupi", "Jaipur", "Hyderabad", "Bhubaneswar", "Tiptur",
          "Jodhpur", "Delhi", "Hyderabad", "Jodhpur", "Dabwali", "Kannur", "Mumbai", "Vijayawada", "Hyderabad",
          "HYDERABAD", "Manipal", "udupi", "Vrindavan", "Sidlaghatta", "Jaipur", "Vijayawada", "Hajipur", "Delhi",
          "Jodhpur", "Jamshedpur", "Kota", "Mandya", "Bandikui", "Dausa", "Rajasthan", "Surat", "Dehradun", "Mumbai",
          "Visakhapatnam", "Mandya", "Delhi", "THRISSUR", "Udupi", "Alwar", "Manipal", "Alwar", "Delhi", "Jaipur",
          "Hong", "Kong", "Delhi", "Kota", "Mulbagal", "Kota", "Noida", "Bagalkot", "Chennai", "Suthaliya", "Kanpur",
          "Jaipur", "kadapa", "Chennai", "Hyderabad", "Chickballapura", "Noida", "Delhi", "Delhi", "Udaipur", "Bhopal",
          "Honnavar", "(Uttar", "kannada", "district)", "Jaipur", "Delhi", "Dehli", "Mandya", "Delhi", "Palakollu",
          "Doddaballapur", "Manipal", "Manipal", "Manipal", "Manipal", "Manipal", "Manipal", "Coimbatore", "Sagar",
          "Manipal", "Manipal", "Manipal", "Manipal", "Manipal", "Kapurthala", "Manipal", "Dehli", "Udupi", "Manipal",
          "Dehli", "Udupi", "Kerala", "Manipal", "Mangalore", "Noida", "Manipal", "Dehli", "Manipal", "Manipal",
          "Udupi", "Manipal", "Siruguppa", "Manipal", "Mangalore", "Noida", "Dehli", "Dehli", "Coimbatore", "Udupi"
]
# Remove Duplicates
cities = list(dict.fromkeys(cities))
print(cities)

geolocator = Nominatim(user_agent="geoapiExercises")

def FindState(states):
    for city in cities:
        try:
            loc = geolocator.geocode(city)
            Latitude = (loc.latitude)
            Longitude = (loc.longitude)
            location = geolocator.reverse(str(Latitude) + "," + str(Longitude))
            location = str(location)
            for state in states:
                if (location.find(state) != -1):
                    if (state == "Uttar Pradesh"):
                        UttarPradesh.append(city)
                    elif (state == "Delhi"):
                        Delhi.append(city)
                    elif (state == "Uttrakhand"):
                        Uttrakhand.append(city)
                    elif (state == "Chandighar"):
                        Chandighar.append(city)
                    elif (state == "Rajasthan"):
                        Rajasthan.append(city)
                    elif (state == "Punjab"):
                        Punjab.append(city)
                    elif (state == "Himachal Pradesh"):
                        HimachalPradesh.append(city)
                    elif (state == "Jammu and Kashmir"):
                        JammuAndKashmir.append(city)
                    print(state)
        except:
            pass
JammuAndKashmir=[]
HimachalPradesh=[]
Punjab=[]
Rajasthan=[]
Chandighar=[]
UttarPradesh=[]
Uttrakhand=[]
Delhi=[]

# North Indian States and Cites
NortStates=["Jammu and Kashmir", "Himachal Pradesh", "Punjab","Rajasthan","Chandighar","Uttrakhand","Uttar Pradesh","Delhi"]
FindState(NortStates)
print(JammuAndKashmir,HimachalPradesh,Punjab,Rajasthan,Chandighar,UttarPradesh,Uttrakhand,Delhi)