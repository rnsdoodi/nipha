import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Nipah Virus Analysis 2025", layout="wide")

# العنوان الرئيسي مع أيقونة منظمة الصحة العالمية
col_logo, col_text = st.columns([1, 5])
with col_logo:
    st.image("https://img.icons8.com/color/96/world-health-organization.png", width=80)

with col_text:
    st.header("Nipah Virus (NiV): Kerala Outbreak Overview (2025 -2026)")

st.divider()

# قسم الملخص العام (Situation at a Glance)
st.header("Situation Overview")
st.info("""
Between **May 17 and July 12, 2025**, the Government of Kerala reported **four confirmed cases** of Nipah virus (NiV), including **two deaths**, across the districts of **Malappuram** and **Palakkad**. 
This marks the first-ever recorded outbreak in Palakkad District. 
Currently, the risk of international spread is considered **low**, with no evidence of human-to-human transmission internationally.
""")

# قسم تفاصيل الحالات (Case Description)
st.header(" 2025 Case Summary")
st.write("- **Total Cases:** 4 confirmed cases (Adults).")
st.write("- **Geographic Distribution:** 2 cases in Malappuram, 2 cases in Palakkad.")
st.write("- **Outcome:** 2 patients survived (in critical care), and 2 patients passed away.")
st.write("- **Investigation:** Cases appear to be independent spillover events from fruit bats; no direct links were found between the patients.")

st.divider()

# قسم علم الأوبئة (Epidemiology)
st.header(" Epidemiology & Symptoms")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Transmission")
    st.write("- **Source:** Zoonotic disease from fruit bats (*Pteropus* species).")
    st.write("- **Methods:** Contact with infected animals (bats/pigs), contaminated food (saliva/urine), or close human contact.")
    st.write("- **Incubation:** Typically 4 to 14 days (up to 45 days reported).")

with col2:
    st.subheader("Clinical Impact")
    st.write("- **Symptoms:** Ranges from acute respiratory infection to fatal encephalitis (brain inflammation).")
    st.write("- **Fatality Rate:** Typically ranges from **40% to 100%** in regional outbreaks.")
    st.warning("Currently, there are no licensed vaccines or therapeutics available for NiV.")

st.divider()

# قسم الاستجابة الصحية (Public Health Response)
st.header(" Response Measures")
st.write("Local authorities have implemented rigorous protocols to contain the virus:")
st.success("""
1. **Contact Tracing:** Over **723 contacts** identified and monitored across multiple districts.
2. **Special Teams:** 26 teams deployed for symptom monitoring and community mapping.
3. **Route Mapping:** Public release of movement maps for infected cases to identify potential exposure.
4. **Hospital Vigilance:** Special alerts issued to hospitals in 6 districts to report any suspected cases immediately.
""")

# قسم نصائح منظمة الصحة العالمية (WHO Advice)
st.header(" Prevention Strategies")
with st.expander("How to reduce infection risk"):
    st.markdown("### 🦇 Bat-to-Human")
    st.write("- Avoid areas where bats are known to roost.")
    st.write("- Fruits showing signs of bat bites should be discarded.")
    st.write("- Boil freshly collected date palm juice before consumption.")
    
    st.markdown("###  Human-to-Human")
    st.write("- Avoid unprotected physical contact with infected individuals.")
    st.write("- Regular hand washing after caring for or visiting sick people.")
    
    st.markdown("###  Health Care Settings")
    st.write("- Implement standard infection control and droplet precautions at all times.")

# تذييل الصفحة
st.divider()
st.caption("Information synthesized from official WHO and Government of Kerala reports (July 2025).")
