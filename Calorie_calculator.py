import streamlit as st


activity={"Sedentary (little or no exercise)":1.2, "Lightly active (exercise 1–3 days/week)":1.375, "Active (exercise 6–7 days/week)":1.55, "Very active (hard exercise 6–7 days/week)":1.725}
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
    option = st.radio("Select an option", ["Sedentary (little or no exercise)", "Lightly active (exercise 1–3 days/week)","Moderately active (exercise 3–5 days/week)" ,"Active (exercise 6–7 days/week)", "Very active (hard exercise 6–7 days/week)"])
    calculate= st.form_submit_button("Calculate")
if calculate:
    if validate_input(weight,height,age,Sex,option):
        if Sex=="Female":
                BMR = 655.1 + (9.563*int(weight)) + (1.850*int(height)) - (4.676*int(age))
                AMR = BMR*activity[option]
                st.success("On a 3 meal scale, you should take "+str(round((AMR-200)/3))+"per meal")
                st.write("Your Basal Metabolic Rate is",round(BMR))
                st.write("Your Active Metabolic Rate is",round(AMR))
        else:
                BMR = 66.5 + (13.75*int(weight)) + (5.003*int(height)) - (6.75*int(age))
                AMR = BMR*activity[option]
                st.success("On a 3 meal scale, you should take "+str(round((AMR-200)/3))+" cal per meal with 200 calories for throughout the day snacking")
                st.write("Your Basal Metabolic Rate is",round(BMR))
                st.write("Your Active Metabolic Rate is",round(AMR))
    coeff=[  7.40300629,   5.91606591,  14.91743453,  23.44801225,
         5.1473278 ,   2.00398124,  10.70217296, 719.47050621,
         1.08497681,   1.19603515,   1.30695392,   1.51996267]
    coeff2=[  6.875253  ,   5.49432274,  13.85398532,  21.77589707,
          4.78038547,   1.86102009,   9.93930012, 668.19296854,
          1.16826132,   1.28784451,   1.40727724,   1.63663733]




