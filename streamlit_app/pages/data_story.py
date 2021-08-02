import streamlit as st
import streamlit.components.v1 as components
import datetime
import pandas as pd
import numpy as np

def app():

    st.title("The State of Food Security in California")

    groceries_img = "https://lh3.googleusercontent.com/pw/AM-JKLVfk_Uyx4sjyEKchX_hggQqT_mzDX-eo_Eoc4H7hcEfnn10CQlANoJ7XLXp-pwmps52icT7vV5G1VuglFzNRHIUHhDa7-Izyn1q7giBQ7sh3CbOHrfBt4wXub88qjzOzCWD50hTpMw9geqtaygg9S8=w960-h640-no"
    st.image(groceries_img)

    st.write("As of 2020, about 10-20% of Californians are food insecure? But what does that mean? Is 10% a number we should be happy with? What causes food insecurity in the first place?")

    st.write("We the Secure the Bag team have also been thinking about these same questions time and time again. To get a better understanding, we delved into the data. While the USDA Economic Research Service provides great research for the national level, we wanted to take a closer look at the situation in California, a state containing a wealth of racial/ethnic and socioeconomic diversity as well as a large immigrant population. And so, we turned to various data sources to get more definitive answers.")

    st.success('_“Food insecurity and hunger are problems of access.” – Anonymous interviewee_')

    st.write("Let’s start with a definition of food security. Imagine never having to worry about the price of groceries. Every day, you’d never have to worry about running out of food because of money, always having the means and access to eat something when you’re hungry. Take that all away, and you have **food insecurity**.")

    st.header("What Do the Numbers Say?") # Header

    st.write("Now let’s take a look at some statistics related to food insecurity. (insert chart belows)")

    st.write("At first glance, these numbers look good, but when we zoom into vulnerable populations, we see that the picture begins to look different.")

    CA_counties = """<div class='tableauPlaceholder' id='viz1626125213787' style='position: relative'><noscript><a href='#'><img alt='CA Food Insecurity Rates Apr2020-Oct2020  ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;se&#47;secure_the_bag&#47;2020CArates&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='secure_the_bag&#47;2020CArates' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;se&#47;secure_the_bag&#47;2020CArates&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1626125213787');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(CA_counties, height = 410)

    with st.beta_expander("Explore the map of CA counties above"):
        st.markdown('<font color="green">Press the top two buttons on the top left to zoom in and out. Press the arrow on the left side to toggle between the different mouse over options. Press the right arrow above “Show history” to begin the animation.</font>', unsafe_allow_html=True)

    st.write("Looking at the rates of food insecurity across the state counties shows a similar trend. From April to October 2020, the California Association of Food Banks found widely varying rates of food security across California as seen in the chart above/below. Why and how is this happening?")

    st.write("One reason is the distribution of wealth. In 2019, California reported a median household income of $75,235, which sounds great, but not every county enjoys that amount of wealth, as shown in the wide range of food insecurity rates across the state. Take Imperial County for instance. It has a median income of $47,622, and so, it has a higher rate of food insecurity (median household income data from 2019 was used due to the lack of estimates for 2020 at this time).")

    st.header("What Are Some Indicators of Food Insecurity?")

    st.write("Okay, we now have a clearer picture that even with a 10% rate of food insecurity for the entire state, there is still a lot of inequality that exists within the state. So what are some signs of food insecurity?")

    shap_feature_impact = "https://lh3.googleusercontent.com/pw/AM-JKLUihieYlHfUa6dWxGbNderDZPz57THTRSJofJGSZBiJukFwZKQsGdM3rvmgM3FzIpd45ELbNlUHwl5_eHcejNJ6VfsDzgE7x1aMTn__bZIhp1BmMVhdI75ZFwZvTCxWynT26ZaWBL8JsvXv8rgjM9w=w911-h393-no"
    st.image(shap_feature_impact, caption = "Feature Importance Graph")

    st.write("In our work, we looked at several variables measured in the California Health Interview Survey (CHIS), compiled by UCLA researchers, when running machine learning models to observe what characteristics are associated with food security. The chart above shows which variables help most strongly predict food insecurity. We can see that the strongest indicators are Medi-Cal coverage, educational attainment, and psychological health.")

    medical_insecurity = """<div class='tableauPlaceholder' id='viz1627931278206' style='position: relative'><noscript><a href='#'><img alt='Covered by Medi-Cal &amp; Food Insecurity&#47;Security Relationship ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ca&#47;capstone_medi-cal_eda&#47;Sheet1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='capstone_medi-cal_eda&#47;Sheet1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ca&#47;capstone_medi-cal_eda&#47;Sheet1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1627931278206');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(medical_insecurity, height = 230)

    with st.beta_expander("What do Inapplicable, Food Secure, and Food Insecure mean?"):
        st.write("Here, “inapplicable” is defined as individuals who are well above 200% of the poverty line and have sufficient resources to be classified as food secure throughout the year. “Food secure” individuals are those at or below the poverty line but have sufficient access to nutritious food throughout the year. In contrast, “food insecure” individuals have limited access to nutritious food and may experience episodes of hunger due to a lack of food.")

    st.write("First, a larger proportion of individuals who are food insecure are also on Medi-Cal, while only a small proportion of inapplicable individuals receive Medi-Cal benefits. We believe that this is because those in need of Medi-Cal benefits are along the poverty threshold and likely need food aid and benefits as well.")

    education_insecurity = """<div class='tableauPlaceholder' id='viz1627931014801' style='position: relative'><noscript><a href='#'><img alt='Educational Attainment &amp; Food Insecurity&#47;Security Relationship ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ed&#47;EducationalAttainmentFoodInsecuritySecurityRelationship&#47;Sheet1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='EducationalAttainmentFoodInsecuritySecurityRelationship&#47;Sheet1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ed&#47;EducationalAttainmentFoodInsecuritySecurityRelationship&#47;Sheet1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1627931014801');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(education_insecurity, height = 350)

    st.write("For education, we can see that the proportion of **food insecure** individuals are larger for the categories with lower educational attainment. In contrast, the proportions of **inapplicable** and **food secure** individuals increase as educational attainment rises. (Note: the numbers in the chart come from survey data and do not reflect actual population numbers)")

    psych_insecurity = """<div class='tableauPlaceholder' id='viz1627931057203' style='position: relative'><noscript><a href='#'><img alt='Serious Psychological Distress Level &amp; Food Insecurity ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Se&#47;SeriousPsychologicalDistressLevelFoodInsecurity&#47;Sheet2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='SeriousPsychologicalDistressLevelFoodInsecurity&#47;Sheet2' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Se&#47;SeriousPsychologicalDistressLevelFoodInsecurity&#47;Sheet2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1627931057203');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(psych_insecurity, height = 410)

    st.write("Our data also shows that mental health plays a large role in determining one’s food security status. In the above chart, while the proportion of individuals experiencing mental distress are similar across the three food security categories, there are several more food insecure individuals expressing a high rating for serious psychological distress compared to the other categories.")

    st.header("What Could Happen If...?") # Header

    st.write("Imagine a world in which no one experienced mental distress, or one in which everyone got a college degree. We were curious to see how these food security numbers might change if we adjusted the variables from above, and so, we went back to our data to create some forecasting models.")

    st.write("For our visualizations below, we have used an upsampled dataset. The original CHIS data is imbalanced, with a disproportionate representation of all levels of food insecurity. Therefore, we upsampled the data to give equal weight to our target variables.")

    predicted_pop = """<div class='tableauPlaceholder' id='viz1627847688279' style='position: relative'><noscript><a href='#'><img alt='Dashboard 3 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ca&#47;capstone_forecasting_dashboard&#47;Dashboard3&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='capstone_forecasting_dashboard&#47;Dashboard3' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ca&#47;capstone_forecasting_dashboard&#47;Dashboard3&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1627847688279');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='777px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(predicted_pop, height = 900, scrolling = True)

    st.header("Piecing it All Together")

    st.write("First, take a deep breath. We’ve just gone through a lot of information, and it can certainly be overwhelming. While California has achieved a food insecurity rate of 10%, we have a long way to go still. There are thousands of households in the state with limited access to fresh produce and nutritious foodstuffs. We saw that wealth isn’t distributed evenly across the state. We saw other factors that play a role in food security from education levels to one’s own mental health. To ensure we reach each of these food insecure individuals, we collectively have a lot of work left to do: as researchers, policymakers, and fellow neighbors.")
