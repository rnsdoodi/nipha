import streamlit as st



pages = {
    "Overview": [
        st.Page("dash1.py", title="Nipah Virus NiV - WHO"),
        st.Page("dash2.py", title="Nipah Virus NiV - PRD Kerala"),
        st.Page("dash4.py", title="Nipah Virus NiV - BioPerfectus"),
    ],
    "Diagnosis Statistics": [
        st.Page("app.py", title=" Kerala Communicable Diseases Analysis"),
    #     st.Page("dash2.py", title=" Gender Diagnosis Statistics "),
    #     st.Page("dash3.py", title="Lipid profile in SCH group"),
    #     st.Page("dash4.py", title=" Lipid Profile: Overt Hypothyroidism vs. Euthyroid "),
    #     st.Page("dash5.py", title=" Correlation Matrix: TSH vs. Lipid Parameters "),
    #     st.Page("dash6.py", title=" SBP, DBP with euthyroid group (p.value) "),
    #     st.Page("dash7.py", title=" BMI and euthyroid group (p.value)  "),
    ],
    
    "Final Recommendations": [
        st.Page("dash3.py", title="Recommendations"),

    ],
      
}


with st.sidebar:
    st.image("4.JPG", use_container_width=True)
    # st.markdown("### Clinical Analysis Lab")
    st.divider()



pg = st.navigation(pages)
pg.run()



