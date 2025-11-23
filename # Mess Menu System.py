

menus = {

    "Safal": {
        "Monday": {
            "Breakfast": "Poha, Tea, Bread-Butter-Jam",
            "Lunch": "Rice, Roti, Dal Tadka, Aloo Gobi",
            "Dinner": "Rice, Dal Fry, Mixed Veg"
        },
        "Tuesday": {
            "Breakfast": "Upma, Coconut Chutney, Milk",
            "Lunch": "Rice, Kadhi, Jeera Aloo",
            "Dinner": "Roti, Paneer Butter Masala"
        },
        "Wednesday": {
            "Breakfast": "Aloo Paratha, Curd, Tea",
            "Lunch": "Veg Biryani, Raita",
            "Dinner": "Rice, Kadhi, Sabzi"
        },
        "Thursday": {
            "Breakfast": "Idli, Sambar, Chutney",
            "Lunch": "Rice, Rajma, Roti",
            "Dinner": "Chapati, Egg Curry"
        },
        "Friday": {
            "Breakfast": "Vegetable Sandwich, Tea",
            "Lunch": "Fried Rice, Manchurian",
            "Dinner": "Veg Pulao, Raita"
        },
        "Saturday": {
            "Breakfast": "Poori–Bhaji, Milk",
            "Lunch": "Rice, Kofta Curry, Roti",
            "Dinner": "Roti, Matar Paneer"
        },
        "Sunday": {
            "Breakfast": "Egg Omelette, Bread, Tea",
            "Lunch": "Chicken Curry, Rice, Salad",
            "Dinner": "Chicken Biryani"
        }
    },

    
    "AB Dakshin": {
        "Monday": {
            "Breakfast": "Idli, Sambar, Chutney",
            "Lunch": "Rice, Dal, Paneer Bhurji",
            "Dinner": "Rice, Dal Fry, Sabzi"
        },
        "Tuesday": {
            "Breakfast": "Masala Dosa, Coconut Chutney",
            "Lunch": "Rajma Chawal",
            "Dinner": "Chapati, Chicken Curry"
        },
        "Wednesday": {
            "Breakfast": "Upma",
            "Lunch": "Kofta Curry, Rice",
            "Dinner": "Kadhi, Rice"
        },
        "Thursday": {
            "Breakfast": "Pongal, Vada",
            "Lunch": "Lemon Rice, Curd",
            "Dinner": "Paneer Masala, Roti"
        },
        "Friday": {
            "Breakfast": "Uttapam, Chutney",
            "Lunch": "Veg Biryani, Raita",
            "Dinner": "Veg Pulao"
        },
        "Saturday": {
            "Breakfast": "Poori Masala",
            "Lunch": "Rice, Kadhi, Sabzi",
            "Dinner": "Egg Curry, Rice"
        },
        "Sunday": {
            "Breakfast": "Aloo Paratha, Curd",
            "Lunch": "Egg Curry, Rice",
            "Dinner": "Chicken Biryani"
        }
    },

    "Mayuri": {
        "Monday": {"Breakfast": "Poha", "Lunch": "Dal Aloo Matar", "Dinner": "Veg Pulao"},
        "Tuesday": {"Breakfast": "Omelette, Tea", "Lunch": "Rajma Chawal", "Dinner": "Roti Dal"},
        "Wednesday": {"Breakfast": "Poori Bhaji", "Lunch": "Veg Biryani", "Dinner": "Rice Sabzi"},
        "Thursday": {"Breakfast": "Upma", "Lunch": "Kadhi Rice", "Dinner": "Egg Curry"},
        "Friday": {"Breakfast": "Veg Sandwich", "Lunch": "Kofta Curry", "Dinner": "Paneer Curry"},
        "Saturday": {"Breakfast": "Idli Sambar", "Lunch": "Paneer Masala", "Dinner": "Kadhi Rice"},
        "Sunday": {"Breakfast": "Aloo Paratha", "Lunch": "Chicken Curry", "Dinner": "Chicken Biryani"}
    },

    "Underbelly": {
        "Monday": {"Breakfast": "Scrambled Eggs", "Lunch": "Rice Dal", "Dinner": "Paneer Masala"},
        "Tuesday": {"Breakfast": "Pancakes Honey", "Lunch": "Pasta & Garlic Bread", "Dinner": "Kadhi Rice"},
        "Wednesday": {"Breakfast": "Idli Sambar", "Lunch": "Manchurian Rice", "Dinner": "Chapati Dal"},
        "Thursday": {"Breakfast": "Bread Butter Jam", "Lunch": "Rajma Chawal", "Dinner": "Egg Curry"},
        "Friday": {"Breakfast": "French Toast", "Lunch": "Veg Biryani", "Dinner": "Veg Pulao"},
        "Saturday": {"Breakfast": "Upma", "Lunch": "Egg Curry Rice", "Dinner": "Roti Sabzi"},
        "Sunday": {"Breakfast": "Omelette", "Lunch": "Chicken Curry", "Dinner": "Chicken Biryani"}
    },

    "Renaissance": {
        "Monday": {"Breakfast": "Upma", "Lunch": "Rice Dal Sabzi", "Dinner": "Roti Dal"},
        "Tuesday": {"Breakfast": "Aloo Paratha", "Lunch": "Kofta Curry Rice", "Dinner": "Rice Sabzi"},
        "Wednesday": {"Breakfast": "Bread Butter Jam", "Lunch": "Kadhi Rice", "Dinner": "Egg Curry"},
        "Thursday": {"Breakfast": "Idli Sambar", "Lunch": "Rajma Chawal", "Dinner": "Paneer Butter Masala"},
        "Friday": {"Breakfast": "Poori Bhaji", "Lunch": "Biryani", "Dinner": "Rasam Rice"},
        "Saturday": {"Breakfast": "Omelette", "Lunch": "Paneer Curry", "Dinner": "Veg Pulao"},
        "Sunday": {"Breakfast": "Masala Dosa", "Lunch": "Chicken Curry", "Dinner": "Chicken Biryani"}
    }
}




print("----- College Mess Menu Finder -----")
print("Messes: Safal, AB Dakshin, Mayuri, Underbelly, Renaissance\n")

mess = input("Enter Mess Name: ").strip().title()
day = input("Enter Day (Monday–Sunday): ").strip().title()
meal = input("Enter Meal (Breakfast/Lunch/Dinner): ").strip().title()

if mess in menus:
    if day in menus[mess]:
        if meal in menus[mess][day]:
            print(f" {mess} – {day} – {meal}:")
            print(menus[mess][day][meal])
        else:
            print("Invalid meal type.")
    else:
        print("Invalid day.")
else:
    print("Invalid mess name.")
