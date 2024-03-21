import streamlit as st


activity={"Sedentary (little or no exercise)":1.16826132, "Lightly active (exercise 1–3 days/week)":1.28784451, "Active (exercise 6–7 days/week)":1.40727724,"Very active (hard exercise 6–7 days/week)":1.63663733}
st.title('Calorie Calculator')
def validate_input(weight,height,age,sex,activity):
    if not height:
        st.warning("Please enter your height.")
        return False
    if not weight:
        st.warning("Please enter your weight.")
        return False
    if not age:
        st.warning("Please enter your age.")
        return False
    if not sex:
        st.warning("Please select your sex.")
        return False
    if not activity:
        st.warning("Please select your activity level.")
        return False
    if age < 0 or age > 150:
        st.warning("Please enter a valid age between 0 and 150.")
        return False
    return True


with st.form(key='form1',clear_on_submit=True):
    st.subheader("About you")
    Sex= st.radio("Select an option",["Male","Female"], horizontal=True, label_visibility="hidden")
    height = st.number_input("Height", placeholder="in cm",value=None)
    weight = st.number_input("Weight", placeholder="in kg",value=None)
    age = st.number_input("Age", placeholder="in years",value=None)
    st.subheader("How active are you?")
    option = st.radio("Select an option", ["Sedentary (little or no exercise)", "Lightly active (exercise 1–3 days/week)","Active (exercise 6–7 days/week)", "Very active (hard exercise 6–7 days/week)"])
    calculate= st.form_submit_button("Calculate")
if calculate:
    if validate_input(weight,height,age,Sex,option):
        if Sex=="Female":
                BMR = 668.19296854+ (9.93930012*int(weight)) + (1.86102009*int(height)) - (4.78038547*int(age)) 
                AMR = BMR*activity2[option]
                st.success("On a 3 meal scale, you should take "+str(round((BMR-200)/3))+"per meal")
                st.write("Your Basal Metabolic Rate is",round(BMR))
                st.write("Your Active Metabolic Rate is",round(AMR))
        else:
                BMR = 21.77589707 + (13.85398532*int(weight)) + (5.49432274*int(height)) - (6.875253*int(age))
                AMR = BMR*activity2[option]
                st.success("On a 3 meal scale, you should take "+str(round((BMR-200)/3))+" cal per meal with 200 calories for throughout the day snacking")
                st.write("Your Basal Metabolic Rate is",round(BMR))
                st.write("Your Active Metabolic Rate is",round(AMR))




