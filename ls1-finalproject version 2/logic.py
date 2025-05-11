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





questions={
    "What makes you happiest?": ["1 - Being outside, in nature or on trips",
        "2 - Creating – drawing, writing, or building",
        "3 - Playing or hanging out with friends",
        "4 - Sitting quietly with a book or music"
    ],
    "What do you feel is missing most in your life right now?": [
        "1 - A sense of purpose and meaning",
        "2 - Quality time alone",
        "3 - Deep and meaningful friendships",
        "4 - A new challenge or adventure"
    ],
    "If you had no limitations, what would you do?": [
        "1 - Start your own business",
        "2 - Travel the world",
        "3 - Perform in front of a huge audience",
        "4 - Study something big and complex"
    ],
    "What type of people inspire you the most?": [
        "1 - Those who live simply and close to nature",
        "2 - Inventors and innovators",
        "3 - People with lots of friends and social circles",
        "4 - Teachers or researchers who dive deep into subjects"
    ],
    "What did you love doing most as a child?": [
        "1 - Running and climbing outdoors",
        "2 - Drawing or making up stories",
        "3 - Organizing games with friends",
        "4 - Reading books and discovering new things"
    ],
    "When have you felt most proud of yourself?": [
        "1 - Overcoming a physical obstacle or outdoor challenge",
        "2 - Completing a creative project",
        "3 - Helping a friend or family member",
        "4 - Getting a high grade or recognition for learning"
    ],
    "What lifestyle attracts you the most?": [
        "1 - A quiet, nature-centered life",
        "2 - A creative and innovative life",
        "3 - A life full of people and shared experiences",
        "4 - A peaceful life with lots of learning and knowledge"
    ],
    "What would you most like to change about yourself?": [
        "1 - Be more active and take initiative",
        "2 - Develop more creativity",
        "3 - Get stronger socially and build new connections",
        "4 - Improve focus and persistence"
    ],
    "What field always draws your attention?": [
        "1 - Nature and animals",
        "2 - Art, design, or writing",
        "3 - Social activities and events",
        "4 - Science, technology, or history"
    ],
    "What’s your wildest dream?": [
        "1 - Climb a high mountain in the world",
        "2 - Open a large studio or gallery",
        "3 - Perform on TV or in a big show",
        "4 - Make an important scientific discovery"
    ]
}



def carear_questions():
    
    questions_send=questions.keys()
    return questions_send



def Recommendations_for_improving_productivity():
    productivity_tips = [
        "Set clear goals — know exactly what you want to achieve daily, weekly, and monthly.",
        "Break tasks into smaller steps — small tasks feel less overwhelming and are easier to start.",
        "Use a to-do list — write down your tasks so you can see them and track progress.",
        "Work by priority — start with what’s most important or urgent, not necessarily what’s easiest.",
        "Set time limits for tasks — decide in advance how much time you’ll spend on each task.",
        "Avoid multitasking — focus on one thing at a time for better quality and faster results.",
        "Take short breaks — 5–10 minute breaks help you reset and maintain focus over long periods.",
        "Organize your workspace — a clean space helps you stay focused and reduces distractions.",
        "Reduce distractions — put your phone on silent or out of sight while you work.",
        "Use the Pomodoro technique — work 25 minutes, then take a 5-minute break, and repeat.",
        "Start early — mornings are often quieter and you have more mental energy.",
        "Set screen time boundaries — avoid social media or games during productive hours.",
        "Prepare everything in advance — get materials or tools ready the night before.",
        "Get good sleep — 7–8 hours of quality sleep improves focus and mental sharpness.",
        "Do physical activity — even short walks or stretches boost energy and concentration.",
        "Practice meditation or deep breathing — helps reduce stress and regain focus.",
        "Reward yourself — after completing hard tasks, give yourself a small treat or break.",
        "Use digital tools — apps like Todoist, Trello, Notion, or Google Calendar help organize tasks.",
        "Learn to say no — avoid overloading yourself with too many commitments.",
        "Reflect on your day — take 5 minutes at night to review what went well and what to improve."
        "Plan your day the night before — outline your top tasks so you wake up with a clear plan.",
        "Batch similar tasks together — handle emails, calls, or errands in one block of time.",
        "Limit decision-making — reduce small daily choices (like what to wear) to save mental energy.",
        "Use time blocks — dedicate specific time slots for focused work, meetings, or creative tasks.",
        "Keep a distraction list — when random thoughts pop up, write them down and return later.",
        "Declutter digital spaces — organize your computer files and clean your inbox regularly.",
        "Set clear boundaries with others — let people know when you need uninterrupted focus time.",
        "Use positive self-talk — encourage yourself instead of criticizing when things get tough.",
        "Apply the 80/20 rule — focus on the 20% ,of tasks that bring 80%, of the results.",
        "Work standing up or change positions — small physical changes can refresh your focus.",
        "Visualize success — imagine completing tasks to build motivation and clarity.",
        "Avoid perfectionism — aim for progress, not flawless results.",
        "Use accountability — tell someone your goals so you’re more likely to follow through.",
        "Review your goals weekly — adjust plans based on what’s working and what’s not.",
        "Use background music or white noise — for some people, it boosts focus.",
        "Limit meetings — only schedule necessary ones with clear agendas.",
        "Automate routine tasks — use tools or shortcuts to save time on repetitive work.",
        "Start with a quick win — completing an easy task early can build momentum for the day.",
        "Keep water and snacks nearby — staying hydrated and fed helps maintain energy.",
        "Learn keyboard shortcuts — they can save significant time on your computer work."
        "Set a clear intention before each work session — know what you want to achieve.",
        "Use visual timers — seeing time pass can motivate you to stay on track.",
        "Practice saying 'done is better than perfect' — avoid wasting time polishing endlessly.",
        "Schedule difficult tasks for your peak energy times — when you’re most alert.",
        "Prepare a 'not-to-do' list — identify habits or tasks that waste your time.",
        "Keep a journal — reflecting on your progress helps clarify what’s effective.",
        "Minimize context switching — avoid jumping between unrelated tasks.",
        "Invest in good tools — high-quality equipment can make your work smoother and faster.",
        "Practice mindfulness — stay fully present with the task at hand.",
        "Create a consistent daily routine — routines reduce decision fatigue.",
        "Identify your productivity triggers — find what conditions make you work best.",
        "Declutter your mental space — write down worries or unrelated thoughts before starting work.",
        "Celebrate milestones — mark progress when you hit big or small goals.",
        "Practice gratitude — recognizing what’s going well boosts motivation.",
        "Designate a 'shutdown' ritual — signal the end of your workday to separate work and rest.",
        "Learn to delegate — give tasks to others when possible to free up your time.",
        "Reduce open tabs or apps — limit what’s on your screen to what’s needed.",
        "Adjust your environment — lighting, temperature, and noise can affect focus.",
        "Keep learning — read or listen to tips from productivity experts regularly.",
        "Be kind to yourself — accept that some days won’t be perfect and keep moving forward."
        "Start each day by reviewing your long-term goals — remind yourself why you’re doing the work.",
        "Use affirmations — positive statements can boost confidence and motivation.",
        "Avoid overcommitting — know your limits and protect your time.",
        "Plan buffer time between tasks — give yourself space to transition smoothly.",
        "Organize your notes — keep your ideas, reminders, and plans in one tidy system.",
        "Use checklists for repetitive tasks — ensure consistency and save mental effort.",
        "Prioritize learning — regularly upgrade your skills to work more effectively.",
        "Limit news and media consumption — avoid wasting time on excessive updates.",
        "Experiment with different work locations — a change of scene can refresh your mind.",
        "Use color coding — visually organize tasks or calendar events for clarity.",
        "Apply the two-minute rule — if a task takes less than two minutes, do it immediately.",
        "Practice deep work — set aside blocks of time for fully focused, high-value tasks.",
        "Reflect on past successes — remind yourself of wins to stay motivated.",
        "Build habits gradually — introduce one new productive habit at a time.",
        "Stay curious — ask questions and look for better ways to work.",
        "Keep a clean digital desktop — avoid clutter that can distract you.",
        "Prepare backup plans — know what you’ll do if things don’t go as expected.",
        "Protect your peak hours — guard your most productive time from interruptions.",
        "Be flexible — adjust plans when necessary instead of rigidly sticking to them.",
        "End each week with a review — celebrate progress and set intentions for the next week."
    ]


    productivity_tip=random.choice(productivity_tips)
    return productivity_tip


def motivations_images():
    #IMAGES URLS : 

    urls=["https://t4.ftcdn.net/jpg/00/85/73/13/360_F_85731355_OnRtt6VxWHeEKsEs9I2CqTIoe3qNMkPa.jpg",
      "https://instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-15/495937824_17881462887293737_7519973693748749968_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkZFRUQuaW1hZ2VfdXJsZ2VuLjEzNTB4MTY4Ny5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=101&_nc_oc=Q6cZ2QEso2l4ZWKn3MQljJO7FMFLKUUArVXdGHOLsmugaajhZQlMCPEhKBNXqL2s23EqaSMkEJBsSqS6JwU0b8NNqHwc&_nc_ohc=Kp46zZC_BnQQ7kNvwGxJ3rA&_nc_gid=CEz4WKmFJCZqz7BJ4xLEcg&edm=APNOSGoBAAAA&ccb=7-5&ig_cache_key=MzYyODA0NzcyNDQxOTY4Njk1Mw%3D%3D.3-ccb7-5&oh=00_AfL6lQQY-oZcZTfDfJ5LldikTyQVc05mstebyv9uBUU34A&oe=6824018B&_nc_sid=ca40e6",
      "https://instagram.ftlv1-1.fna.fbcdn.net/v/t51.29350-15/495659904_1136934581450367_5732019075112518607_n.heic?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkZFRUQuaW1hZ2VfdXJsZ2VuLjE0NDB4MTgwMC5zZHIuZjI5MzUwLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=103&_nc_oc=Q6cZ2QGBZxAEP60uskDG2v3QMCsp-p7V0EnHPEcO2YquElOEddR18XZIqVJAEcGKCx3fxTcKQxjTUFQiV-rjB8xRSa7d&_nc_ohc=3Ih1GQDCoKsQ7kNvwHN91f-&_nc_gid=ismkZMqSlI7qm43eUqCD2Q&edm=AOmX9WgBAAAA&ccb=7-5&ig_cache_key=MzYyNjI1ODg3MzYwNDYwNzMyOQ%3D%3D.3-ccb7-5&oh=00_AfIscb7904XzP28QhQ-v580Sj36_kzYcWEb8NvoiNoAiVg&oe=68240169&_nc_sid=bfaa47",
      "https://instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-15/491415750_17876403429318344_3115223497971121149_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkZFRUQuaW1hZ2VfdXJsZ2VuLjEzNTB4MTY4Ny5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=108&_nc_oc=Q6cZ2QFELdwhJE3Jt9rBc07jAV-U9zVPVPtFP9e0KATeIwlNRpCwv9hnbZMjIbvqhnH5gWFlwKMf89ojxKHJUtiNoYWn&_nc_ohc=i7Pk5fIH1NcQ7kNvwFjjuU-&_nc_gid=sJOsIJqOQp8bMOpnDiTlPQ&edm=APNOSGoBAAAA&ccb=7-5&ig_cache_key=MzYyMDI5MTkyODI4NDk3ODczOQ%3D%3D.3-ccb7-5&oh=00_AfLo4A48AvyCIWqNLnf-ZfP60Sas0wYm5mxvmk7dqhcvKg&oe=68241D03&_nc_sid=ca40e6",
      "https://instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-15/495474887_17949593357977220_2378791307723318193_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkZFRUQuaW1hZ2VfdXJsZ2VuLjEyNzd4MTU5Mi5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=108&_nc_oc=Q6cZ2QFELdwhJE3Jt9rBc07jAV-U9zVPVPtFP9e0KATeIwlNRpCwv9hnbZMjIbvqhnH5gWFlwKMf89ojxKHJUtiNoYWn&_nc_ohc=gMou1ZCzNzQQ7kNvwGMRYES&_nc_gid=sJOsIJqOQp8bMOpnDiTlPQ&edm=APNOSGoBAAAA&ccb=7-5&ig_cache_key=MzYyNjM0NzAwMzY5NDk1ODU4Mw%3D%3D.3-ccb7-5&oh=00_AfIpWdWkuleVy-1SuwokCZV4uNullz-MSXx4T8DsTZ6ARQ&oe=68242979&_nc_sid=ca40e6",
      "https://instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-15/494775668_17876707614318344_88805588377684724_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkZFRUQuaW1hZ2VfdXJsZ2VuLjEzNTB4MTY4Ny5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=108&_nc_oc=Q6cZ2QFhSTud8icNs-7FnTw1_wW7WLreNKMLy2sAobUpKIMjjnrS2uF5JIQyQMsSXOmckwJfBI0nDjXFBKmkCIzFTq6p&_nc_ohc=_ntcvKdD3mgQ7kNvwG79X3u&_nc_gid=To0CzMMUAIXPx8ktvgfc1w&edm=APNOSGoBAAAA&ccb=7-5&ig_cache_key=MzYyMjI0MTY5MDU4MDA3OTIxMQ%3D%3D.3-ccb7-5&oh=00_AfJtlW1S5UQenj1yXAzaxKryNN9HV7lJHPdDbCA-OGWwIA&oe=6823FEDE&_nc_sid=ca40e6",
      "https://instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-15/496175937_17949958217977220_8546627188381448707_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkZFRUQuaW1hZ2VfdXJsZ2VuLjEyNzd4MTU5Mi5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=108&_nc_oc=Q6cZ2QHuSh1hFVwma3K14aFNJf-BRjVfvscNHXQUYspwkv1mF7h0msUkJZ_Ycf2u-vZmFe_bMzljYNh92sDnM-5Xt6hq&_nc_ohc=vF7Oyb2UbrkQ7kNvwFBBUTL&_nc_gid=YgYGV7sEFnV7kjaJfYyc4g&edm=APNOSGoBAAAA&ccb=7-5&ig_cache_key=MzYyODY5MTAxODg5NzQ5MDAyOQ%3D%3D.3-ccb7-5&oh=00_AfILE6I07mKup3XvAFIspIlV9hT3FqEO3k15fbVlh1sN9A&oe=6824B4AA&_nc_sid=ca40e6",
      "https://instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-15/495921246_17881221588293737_5960753598892202045_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkZFRUQuaW1hZ2VfdXJsZ2VuLjEzNTB4MTY4Ny5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=101&_nc_oc=Q6cZ2QHuSh1hFVwma3K14aFNJf-BRjVfvscNHXQUYspwkv1mF7h0msUkJZ_Ycf2u-vZmFe_bMzljYNh92sDnM-5Xt6hq&_nc_ohc=DaJEa5KMdJkQ7kNvwESlZsq&_nc_gid=YgYGV7sEFnV7kjaJfYyc4g&edm=APNOSGoBAAAA&ccb=7-5&ig_cache_key=MzYyNjU5NDMxMDE5NjE4MTE3NQ%3D%3D.3-ccb7-5&oh=00_AfJzy3ETxzws9gUo4oFGWAvxtYavbsIT5FpuF5nfkx1VNQ&oe=6824CEF2&_nc_sid=ca40e6",
      "https://instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-15/495447715_18498414199045818_1198478249995516817_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkNBUk9VU0VMX0lURU0uaW1hZ2VfdXJsZ2VuLjEyOTB4MTQ5MC5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=106&_nc_oc=Q6cZ2QHuSh1hFVwma3K14aFNJf-BRjVfvscNHXQUYspwkv1mF7h0msUkJZ_Ycf2u-vZmFe_bMzljYNh92sDnM-5Xt6hq&_nc_ohc=cjwpWc2VZXcQ7kNvwGVtnxK&_nc_gid=YgYGV7sEFnV7kjaJfYyc4g&edm=APNOSGoBAAAA&ccb=7-5&ig_cache_key=MzYyNTE3NTAxMzkzNTk0MDU2NA%3D%3D.3-ccb7-5&oh=00_AfJzaGqPs1w8nO18oc7Lt9yuND7OTnx6D03SqWwCo6RL1A&oe=6824B622&_nc_sid=ca40e6",
      "https://instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-15/495968813_17949626732977220_4522990131809923581_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkZFRUQuaW1hZ2VfdXJsZ2VuLjEyNzd4MTU5Mi5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=108&_nc_oc=Q6cZ2QHuSh1hFVwma3K14aFNJf-BRjVfvscNHXQUYspwkv1mF7h0msUkJZ_Ycf2u-vZmFe_bMzljYNh92sDnM-5Xt6hq&_nc_ohc=XMbEDEWecuQQ7kNvwGLEuB_&_nc_gid=YgYGV7sEFnV7kjaJfYyc4g&edm=APNOSGoBAAAA&ccb=7-5&ig_cache_key=MzYyNjU2Nzk1NTkxMzQzMDIwMQ%3D%3D.3-ccb7-5&oh=00_AfKJp_0PmJSLm_bQhyYRl9to3uHGJLNuijXLXnLDDuSPZQ&oe=6824B46B&_nc_sid=ca40e6",
      "https://instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-15/491426762_18494173336060214_8707298483715842627_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkNBUk9VU0VMX0lURU0uaW1hZ2VfdXJsZ2VuLjE0NDB4MTgwMC5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=102&_nc_oc=Q6cZ2QE3f_xeRnxKiWAPyjHFNokf1ZU2MdMnh154Ll-5FVRp6mJttLQq3f20zKQxsetNX5l8hWQkQTAZEA9o3vSci_PQ&_nc_ohc=4hxTXSPsIHsQ7kNvwHiB0p7&_nc_gid=6i1aWYutpKbIfBj5Q3MyCw&edm=APNOSGoBAAAA&ccb=7-5&ig_cache_key=MzYxNDM1OTMzODk5MjE1ODk0MA%3D%3D.3-ccb7-5&oh=00_AfIsqEYQyYXwgTvu2cNWnOyB7j6MKcwkrAaWrpxfFh3t9A&oe=6824C82F&_nc_sid=ca40e6",
      "https://instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-15/496029452_17981546159823048_5766772126119513279_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkZFRUQuaW1hZ2VfdXJsZ2VuLjE0NDB4MTgwMC5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=100&_nc_oc=Q6cZ2QE3f_xeRnxKiWAPyjHFNokf1ZU2MdMnh154Ll-5FVRp6mJttLQq3f20zKQxsetNX5l8hWQkQTAZEA9o3vSci_PQ&_nc_ohc=rMDNWBl-YRYQ7kNvwEvuvOU&_nc_gid=6i1aWYutpKbIfBj5Q3MyCw&edm=APNOSGoBAAAA&ccb=7-5&ig_cache_key=MzYyNzI1Nzc4MzU0MDgzNjE1MQ%3D%3D.3-ccb7-5&oh=00_AfIru3K7I6ajNzQA4YZw6QTNcCJBIokQ1fOz_5V7K0hKmA&oe=6824BD42&_nc_sid=ca40e6",
      "https://instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-15/491437330_17981600117822497_2974311525208482645_n.webp?efg=eyJ2ZW5jb2RlX3RhZyI6IkNBUk9VU0VMX0lURU0uaW1hZ2VfdXJsZ2VuLjE0NDB4MTgwMC5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=101&_nc_oc=Q6cZ2QFCANw1IeRMl_X3uHqNJMJynnToeM0LWg-t4ZtLsPEq_kXZqrSEy_HVBV61thwMxMIBpHNWwqtXySM_oHB4BiBc&_nc_ohc=ky4oBsGIGTUQ7kNvwFwcx39&_nc_gid=BykiPlqtrzyS5tB6KJHOLA&edm=APNOSGoBAAAA&ccb=7-5&ig_cache_key=MzYxNzY2MzE3ODI5MjQ1MTczNQ%3D%3D.3-ccb7-5&oh=00_AfJVFP9neaHykUGwweZnrFjxs4yd40PZaAklaasduOjOLA&oe=6824B724&_nc_sid=ca40e6",
      "https://instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-15/491452964_17981600135822497_4625781637989307451_n.webp?efg=eyJ2ZW5jb2RlX3RhZyI6IkNBUk9VU0VMX0lURU0uaW1hZ2VfdXJsZ2VuLjE0NDB4MTgwMC5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=101&_nc_oc=Q6cZ2QFCANw1IeRMl_X3uHqNJMJynnToeM0LWg-t4ZtLsPEq_kXZqrSEy_HVBV61thwMxMIBpHNWwqtXySM_oHB4BiBc&_nc_ohc=4yHN9oNlNXQQ7kNvwE3d1SJ&_nc_gid=BykiPlqtrzyS5tB6KJHOLA&edm=APNOSGoBAAAA&ccb=7-5&ig_cache_key=MzYxNzY2MzE3ODMwMDgxNTgxMg%3D%3D.3-ccb7-5&oh=00_AfLljIs8ATSbfV5W4QWZlHo-RkHpy7HK7-qqW3hW_Zgm4A&oe=6824CE8C&_nc_sid=ca40e6",
      "https://instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-15/491419154_18194109985308017_5085291960856909877_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkNBUk9VU0VMX0lURU0uaW1hZ2VfdXJsZ2VuLjEyMDB4MTUwMC5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=105&_nc_oc=Q6cZ2QFCANw1IeRMl_X3uHqNJMJynnToeM0LWg-t4ZtLsPEq_kXZqrSEy_HVBV61thwMxMIBpHNWwqtXySM_oHB4BiBc&_nc_ohc=rWmH5ceP3Y0Q7kNvwFvbZLW&_nc_gid=BykiPlqtrzyS5tB6KJHOLA&edm=APNOSGoBAAAA&ccb=7-5&ig_cache_key=MzYyMzA2NDEzNjE5NzkwMjI1MQ%3D%3D.3-ccb7-5&oh=00_AfJXdC2VOe0UuKY89xAZ0ZqxVk05iCsTN_p7r24aeGH0Jg&oe=6824E08F&_nc_sid=ca40e6",
      "https://instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-15/491440183_18083261794632252_2670130139529443307_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkNBUk9VU0VMX0lURU0uaW1hZ2VfdXJsZ2VuLjEwODB4MTM0Ni5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=100&_nc_oc=Q6cZ2QFCANw1IeRMl_X3uHqNJMJynnToeM0LWg-t4ZtLsPEq_kXZqrSEy_HVBV61thwMxMIBpHNWwqtXySM_oHB4BiBc&_nc_ohc=ki3PhrXuL9QQ7kNvwFDgToh&_nc_gid=BykiPlqtrzyS5tB6KJHOLA&edm=APNOSGoBAAAA&ccb=7-5&ig_cache_key=MzYxNDg5MTQ2NTQ5NzA2MjkyMg%3D%3D.3-ccb7-5&oh=00_AfIQTVbg6KDyAqNaKomv5xPta1qO0LV5MoOEXUKluJsTvQ&oe=6824DA67&_nc_sid=ca40e6",
      "https://instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-15/491443607_18083261782632252_1005489084413421076_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkNBUk9VU0VMX0lURU0uaW1hZ2VfdXJsZ2VuLjEwODB4MTM0Ni5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=100&_nc_oc=Q6cZ2QFCANw1IeRMl_X3uHqNJMJynnToeM0LWg-t4ZtLsPEq_kXZqrSEy_HVBV61thwMxMIBpHNWwqtXySM_oHB4BiBc&_nc_ohc=RMQExZ2UkHwQ7kNvwHhqmK5&_nc_gid=BykiPlqtrzyS5tB6KJHOLA&edm=APNOSGoBAAAA&ccb=7-5&ig_cache_key=MzYxNDg5MTQ2NTUxMzcwMDU0MA%3D%3D.3-ccb7-5&oh=00_AfL3ZRvRgKIXFZ8rQ002mQCPQMd0Vg-9Ok7bevwb4lv_4w&oe=6824D582&_nc_sid=ca40e6",
      "https://instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-15/490633653_18083261815632252_6395893617428998058_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkNBUk9VU0VMX0lURU0uaW1hZ2VfdXJsZ2VuLjEwODB4MTM0Ni5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=100&_nc_oc=Q6cZ2QFCANw1IeRMl_X3uHqNJMJynnToeM0LWg-t4ZtLsPEq_kXZqrSEy_HVBV61thwMxMIBpHNWwqtXySM_oHB4BiBc&_nc_ohc=Jn4VlyupGiAQ7kNvwEQuGS4&_nc_gid=BykiPlqtrzyS5tB6KJHOLA&edm=APNOSGoBAAAA&ccb=7-5&ig_cache_key=MzYxNDg5MTQ2NTUxMzc3OTcwNQ%3D%3D.3-ccb7-5&oh=00_AfLEI-0A27tGD6zPtZL4-CZXbDPDD2UdxZ2cBDeqNCXNlg&oe=6824DE19&_nc_sid=ca40e6",
      "https://instagram.ftlv1-1.fna.fbcdn.net/v/t51.29350-15/495663022_1327932058305027_6548912634181520806_n.heic?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkNBUk9VU0VMX0lURU0uaW1hZ2VfdXJsZ2VuLjE0NDB4MTc5OS5zZHIuZjI5MzUwLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=103&_nc_oc=Q6cZ2QGVwaSUJw9j2GYgf3mo8oAojqfQXbueD8ubIAM1p11C23ghiu0BUYaEbV8UU3l8mO3XHSRjMVKu4wr9Fsl6zV0c&_nc_ohc=VQtEx8FPNVoQ7kNvwGtNqHo&_nc_gid=UrCpRBf46MqJQ10X3Rdc-g&edm=APNOSGoBAAAA&ccb=7-5&ig_cache_key=MzYyNTc5ODk0MjI3MzQxMjk5Mg%3D%3D.3-ccb7-5&oh=00_AfIP4yacT-5-jLRhtaTjTlPr_v2vWj8FtkWQ1qEH09iWBA&oe=6824D98E&_nc_sid=ca40e6",
      "https://instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-15/491431411_18059975669514294_2041059314918292359_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkZFRUQuaW1hZ2VfdXJsZ2VuLjEzNDl4MTY4NS5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=106&_nc_oc=Q6cZ2QGVwaSUJw9j2GYgf3mo8oAojqfQXbueD8ubIAM1p11C23ghiu0BUYaEbV8UU3l8mO3XHSRjMVKu4wr9Fsl6zV0c&_nc_ohc=s3nBxlkc4lMQ7kNvwHRDI-Q&_nc_gid=UrCpRBf46MqJQ10X3Rdc-g&edm=APNOSGoBAAAA&ccb=7-5&ig_cache_key=MzYyMTkxOTY5MjgyMzQ5MzMyNg%3D%3D.3-ccb7-5&oh=00_AfIrlACNN6fRm0jsOaGCCtfvQm4KBqJleKRRlCHz6PJMRA&oe=6824C372&_nc_sid=ca40e6",
      "https://instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-15/496899189_18357230647196249_7183019462663609402_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkZFRUQuaW1hZ2VfdXJsZ2VuLjE0NDB4MTgwMC5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=105&_nc_oc=Q6cZ2QHjwJEQF3HIXo4BGi_YKCzwA3Zz7EfBFsRQiB_TFsJuP44KPwMnwLXaDLbS-UG9wbXyWZNAvmxdPibeL4JpedqK&_nc_ohc=rUOL6X3hg2MQ7kNvwFnQjEt&_nc_gid=nFtdplmxbiq32Z35JGkY4g&edm=APNOSGoBAAAA&ccb=7-5&ig_cache_key=MzYyODgzNjQxMzU3MzI1NzM3Mg%3D%3D.3-ccb7-5&oh=00_AfJ_zwH5MX4LZZaEne_fmecmRYctPcfx1vD3iDt9OV3RWQ&oe=6824E226&_nc_sid=ca40e6",
      "https://instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-15/491438431_17954754974950401_1917073856136919966_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkNBUk9VU0VMX0lURU0uaW1hZ2VfdXJsZ2VuLjEwODB4MTM0Ni5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=109&_nc_oc=Q6cZ2QHjwJEQF3HIXo4BGi_YKCzwA3Zz7EfBFsRQiB_TFsJuP44KPwMnwLXaDLbS-UG9wbXyWZNAvmxdPibeL4JpedqK&_nc_ohc=sTUA38zt5MQQ7kNvwE9uJBz&_nc_gid=nFtdplmxbiq32Z35JGkY4g&edm=APNOSGoBAAAA&ccb=7-5&ig_cache_key=MzYyMzAyMjAxNDk4NDAwNzQ5MA%3D%3D.3-ccb7-5&oh=00_AfJH5wLdY9P7M29eLqMKLWqV7zEHXYULo_RHthJB0qhoYg&oe=6824E195&_nc_sid=ca40e6",
      "https://instagram.ftlv1-1.fna.fbcdn.net/v/t51.2885-15/491436603_17954754983950401_5351611709238678116_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkNBUk9VU0VMX0lURU0uaW1hZ2VfdXJsZ2VuLjEwNzR4MTMzOS5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=109&_nc_oc=Q6cZ2QHjwJEQF3HIXo4BGi_YKCzwA3Zz7EfBFsRQiB_TFsJuP44KPwMnwLXaDLbS-UG9wbXyWZNAvmxdPibeL4JpedqK&_nc_ohc=ZRa8A_HCzeUQ7kNvwEs4bfz&_nc_gid=nFtdplmxbiq32Z35JGkY4g&edm=APNOSGoBAAAA&ccb=7-5&ig_cache_key=MzYyMzAyMjAxNTI1MjMzNzQwOA%3D%3D.3-ccb7-5&oh=00_AfLFA7znwoRsVx5-cPNvTelRfK7rmYuMOyZPwNS_4_jajA&oe=6824E811&_nc_sid=ca40e6",
      ]


 
    img_random=random.choice(urls)
    return img_random


 
