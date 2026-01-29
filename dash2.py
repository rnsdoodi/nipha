import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Nipah Update - Palakkad", layout="wide")

# العنوان الرئيسي مع صورة الشعار
col_logo, col_text = st.columns([1, 5])
with col_logo:
    # يمكنك استبدال الرابط بأي صورة شعار محلية أو رابط مباشر
    st.image("3.jpg", width=150)

with col_text:
    st.title("Nipah Virus Update: Palakkad Case & Response")

st.divider()

st.subheader("📥 Download Resources")

with open("IDSP-Daily-Report.pdf", "rb") as file:
    st.download_button(
        label="Download Official Situation Report (PDF)",
        data=file,
        file_name="Kerala_Nipah_Report_2025.pdf",
        mime="application/pdf"
    )

# قسم تفاصيل الحالة الجديدة (New Case Details)
st.header(" Latest Case Announcement")
st.info("""
**Health Minister Veena George** announced the death of a **57-year-old man from Palakkad** who tested positive for Nipah virus. 
The infection was initially confirmed at Manjiri Medical College, with further confirmation pending from the **Pune Institute of Virology**.
""")

# قسم تتبع المخالطين (Contact Tracing)
st.header(" Contact Tracing & Surveillance")
st.write("Immediate measures have been taken to contain any potential spread:")
st.write("- **Immediate Identification:** 46 individuals have been identified as contacts of the new case.")
st.write("- **Advanced Tracking:** Authorities are using CCTV footage and monitoring cell tower locations for surveillance.")
st.write("- **Mapping:** A detailed contact tracing map and a family tree have been created.")
st.write("- **Field Efforts:** Fever monitoring and field activities in the affected area have been intensified.")

st.divider()

# قسم الإحصائيات الحالية (Current Statistics)
st.header(" State-wide Statistics")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Contact Registry")
    st.write("- **Total Registered Contacts:** 543 individuals.")
    st.write("- **Palakkad District:** 219 contacts.")
    st.write("- **Malappuram District:** 208 contacts.")
    st.write("- **Kozhikode District:** 114 contacts.")
    st.write("- **Ernakulam District:** 2 contacts.")

with col2:
    st.subheader("Clinical Status")
    st.write("- **High-Risk Category:** 36 people considered high-risk, with 128 under observation.")
    st.write("- **Treatment:** 10 people in Malappuram (2 in ICU) and 1 in isolation in Palakkad.")
    st.write("- **Testing:** 62 samples in Malappuram have tested negative to date.")

st.divider()

# قسم التوجيهات العامة (Public Health Advisories)
st.header(" Public Safety Guidelines")
st.warning("The Ministry of Health advises strict adherence to the following measures, especially in Palakkad and Malappuram districts:")
st.success("""
1. **Minimize Hospital Visits:** Avoid unnecessary visits to hospitals unless essential.
2. **Limit Visitors:** Avoid visiting relatives or friends receiving treatment.
3. **Escort Policy:** Only one person is permitted to accompany a patient.
4. **Protective Gear:** Healthcare workers, patients, and companions **must wear masks** at all times in hospitals.
""")

# قسم الاستجابة الإدارية (Administrative Response)
with st.expander(" High-Level Coordination"):
    st.write("A high-level meeting chaired by Minister Veena George was held with key health officials to reinforce the response teams.")
    st.write("Attendees included the First Additional Secretary, Directors of Health and Medical Education, and National Health Programme missions.")

# تذييل الصفحة
st.caption("Information based on the official statement from the Information & Public Relations Department - Government of Kerala.")



