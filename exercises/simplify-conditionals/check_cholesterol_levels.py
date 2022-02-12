# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

# Blood test analysis program
total_cholostrol = 230
ldl = 150
triglyceride = 170

def high_cholesterol_alert():
    print('*** High cholestrol level ***')
    print('start taking pills such as statins')
    print('start TLC diet')
def tlc_diet_alert():
    print('*** Borderline to moderately elevated ***')
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')

if total_cholostrol < 200 and ldl < 100 and triglyceride < 150:
    # good level
    print('*** Good level of cholestrol ***')
elif 200 < total_cholostrol > 240 or ldl > 160 or triglyceride >= 200:
    # High cholestrol level
    high_cholesterol_alert()
elif 200 <total_cholostrol < 240 or 130 < ldl < 160 or 150 <= triglyceride < 200:
    #TLC_diet
    tlc_diet_alert()
else:
    print('Error: unhandled case.')
