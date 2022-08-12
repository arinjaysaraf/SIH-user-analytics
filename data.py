import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

states = [ "Andhra Pradesh", "Arunachal Pradesh", "Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttarakhand", "Uttar Pradesh", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Delhi", "Lakshadweep", "Puducherry"]

fNames = ["Saanvi", "Anya", "Aadhya", "Aaradhya", "Ananya", "Pari", "Anika", "Navya", "Angel", "Diya", "Myra", "Sara", "Iraa", "Ahana", "Anvi", "Prisha", "Riya", "Aarohi", "Anaya", "Akshara", "Eva", "Shanaya", "Kyra", "Siya","Aarav", "Vihaan", "Vivaan", "Ananya", "Diya", "Advik", "Kabir", "Anaya", "Aarav", "Vivaan", "Aditya", "Vivaan", "Vihaan", "Arjun", "Vivaan", "Reyansh", "Mohammed", "Sai", "Arnav", "Aayan", "Krishna", "Ishaan", "Shaurya", "Atharva", "Advik", "Pranav", "Advaith", "Aaryan", "Dhruv", "Kabir", "Ritvik", "Aarush", "Kian", "Darsh", "Veer"]

sNames = ["Bedi", "Gandhi", "Parekh", "Kohli", "Ahluwalia", "Chandra", "Jha", "Khanna", "Bajwa", "Chawla", "Lal", "Anand", "Gill", "Chakrabarti", "Dubey", "Kapoor", "Khurana", "Modi", "Kulkarni", "Khatri", "Kaur", "Saraf", "Kumar", "Gupta", "Naidu", "Das", "Jain", "Chowdhury", "Dalal", "Thakur", "Gokhale", "Apte", "Sachdev", "Mehta", "Ganguly", "Bhasin", "Mannan", "Ahuja", "Singh", "Bakshi", "Basu", "Ray", "Mani", "Datta", "Balakrishna", "Biswas", "Laghari", "Malhotra", "Dewan", "Purohit", "Pal"]

gender = ["Male", "Female", "Others"]

categories = ["AYUSH", "Prime Minister's Office","Department of Atomic Energies", "Ministry of Agriculture and Farmers Welfare","Ministry of Civil Aviation", "Ministry of Culture","Ministry of Defence", "Ministry of Communications", "Ministry of Commerce and Industry", "Ministry of Coal","Ministry of Company Affairs", "Ministry of Electronics and IT","Ministry of External Affairs", "Ministry of Information and Broadcasting", "Ministry of Power", "Ministry of Petroleum and Natural Gases", "Ministry of Steel", "Ministry of Tourism", "Ministry of Science and Technology", "Ministry of Youth Affairs and Sports", "Ministry of Tribal Affairs", "PM Speech", "UPSC", "Ministry of Housing and Urban Affairs", "Ministry of Law and Justice"]

userData = pd.DataFrame()

for i in range(0,5000):
    ctSize = int(np.random.randint(1, 5, size=1)[0])
    # print(ctSize)
    userCategories = random.sample(categories, ctSize)
    # print(userCategories)

    userGender = random.choices(gender,weights=[55,50,1],k=1)[0]
    # print(userGender)
    userFirstName = random.sample(fNames,1)[0]
    # print(userFirstName)
    userLastName = random.sample(sNames,1)[0]
    # print(userLastName)

    userState = random.sample(states,1)[0]
    # print(userState)
    userHitCount = int(np.random.randint(1, 100, size=1)[0])
    userViewsCount = int(np.random.randint(1, 98, size=1)[0])
    userDict = {
        'id': i+1,
        'F Name': [userFirstName],
        'L Name': [userLastName],
        'Gender': [userGender],
        'Location': [userState],
        'Categories': [userCategories],
        'Hit count': [userHitCount],
        'Total Views': [userViewsCount]
    }
    user = pd.DataFrame(userDict)
    userData = pd.concat([userData, user])
# export to csv
# userData.to_csv('userData.csv', index=False)


userData['Location'].value_counts().plot(kind='line', figsize=(5, 5))

# plot = userData.plot.pie(y='Location', figsize=(10,10))