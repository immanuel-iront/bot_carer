import time
import random


def exampels_for_carear_roads():
    first_names=[
                "James", "Olivia", "Liam", "Emma",
                "Noah", "Ava", "William", "Sophia",
                "Benjamin", "Isabella", "Lucas", "Mia", 
                "Henry", "Charlotte", "Alexander", "Amelia",
                "Michael", "Harper", "Ethan", "Evelyn",
                "Daniel", "Abigail", "Matthew",
                "Ella", "Joseph", "Grace",
                "Samuel", "Lily", "David", 
                "Aria", "Jack", "Scarlett", "Aiden",
                "Chloe", "John", "Nora", "Leo", "Zoey", "Caleb", "Hazel"
]    
    last_name=[
                "Smith", "Johnson", "Williams", "Brown", "Jones",
                "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
                "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", 
                "Thomas", "Taylor", "Moore", "Jackson", "Martin",
                "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez",
                "Clark", "Ramirez", "Lewis", "Robinson",
                "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", 
                "Nguyen", "Hill", "Flores","Green", "Adams",
                "Nelson", "Baker", "Hall", "Rivera", "Campbell", 
                "Mitchell", "Carter", "Roberts",
                "Gomez", "Phillips", "Evans", "Turner", 
                "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes",
                "Stewart", "Morris", "Morales", "Murphy",
                "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper",
                "Peterson", "Bailey", "Reed", "Kelly", 
                "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson",
]

    f_name=random.choice(first_names)
    l_name=random.choice(last_name)
    age=random.randint(18,34)
    person="when "+f_name+" "+l_name+f" was {age} years old he"  
    first_step=["started a new business","began studying", "moved to live in another country,","launched a new venture"]
    first_step_choice=random.choice(first_step)
    



    if first_step_choice=="started a new business":
        str_new_bs=[
"importing and exporting electronics",
"digital marketing and social media management",
"organic farming and sustainable agriculture",
"software development and mobile apps",
"real estate investments",
"interior design and home décor",
"online education platforms",
"fitness training and personal coaching",
"eco-friendly product manufacturing",
"event planning and coordination",
"food delivery services",
"handmade crafts and gifts",
"tourism and travel services",
"financial consulting and budgeting",
"pet grooming and care",
"photography and video production",
"automobile repair and detailing",
"web design and graphic services",
"language translation and interpretation",
"coffee roasting and café management",
] 
        str_new_bs_choice=random.choice(str_new_bs)


        str_new_bs_second=[
"Thanks to the business, he became a millionaire",
"He decided to leave the business because it was unprofitable",
"A big company bought his business and he received a lot of money",
"His business became a giant company",
"He decided to leave the business and focus on family and experiences",
"His business didn’t succeed, but he didn’t give up and started a new business"
]
        str_new_bs_second_choice=random.choice(str_new_bs_second)
        carer_road=first_step_choice+" "+str_new_bs_choice + " "+ str_new_bs_second_choice
        carer_road_final=person+" "+ carer_road
        print(carer_road_final)
        return carer_road_final

    elif first_step_choice=="began studying":
        began_studying_second=["programming and got a good job","how to start a business and succeeded in life","a university degree, and new career opportunities opened up for him"]
        began_studying_second_choice=random.choice(began_studying_second)
        carer_road=" "+ first_step_choice+" "+ began_studying_second_choice
        carer_road_final=person+carer_road
        print(carer_road_final)
        return carer_road_final
        


    elif first_step_choice=="moved to live in another country,":
        moved_country=["then he started a business there","then he began learning about the country and the opportunities it offers."]
        moved_country_choice=random.choice(moved_country)
        carer_road=" "+ first_step_choice+" "+ moved_country_choice
        carer_road_final=person+carer_road
        print(carer_road_final)
        return carer_road_final
    


    elif first_step_choice=="launched a new venture":
        launched_veture=["an initiative working for the benefit of underprivileged communities.","an initiative working for environmental protection"]
        launched_veture_choice=random.choice(launched_veture)
        carer_road=" "+ first_step_choice+" "+ launched_veture_choice
        carer_road_final=person+carer_road
        print(carer_road_final)
        return carer_road_final


    else:
        print("error") 
        pass


    print(person+first_step_choice)



questions={
    "whats of this things is the most important for you":["1-work","2-improve yourself","3-enjoy","4-family"],
    "what of this activity your favotite":["1-coding","2-read a books","3-learn new things","4-creating new things"],

}

def carear_questions():
    questions_send=questions.keys()
    return questions_send

