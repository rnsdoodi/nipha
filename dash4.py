import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="BioPerfectus | Nipah Update 2026", layout="wide")

# القسم الأول: التعريف بالشركة (About Us)
# استخدام أعمدة لوضع الشعار بجانب النص التعريفي
col_logo, col_about = st.columns([1, 4])
with col_logo:
    # يمكنك وضع رابط شعار الشركة هنا
    st.image("5.png", width=100)

with col_about:
    st.title("BioPerfectus: Leading Molecular Diagnostics")
    st.caption("SSE: 688399 | Specializing in Infectious Disease & Women's Health")

with st.expander(" Learn more about BioPerfectus", expanded=False):
    st.write("""
    Founded in 2010, **BioPerfectus** is a leading molecular diagnostics company committed to the R&D, manufacturing, and distribution of in vitro diagnostic reagents and devices. 
    With a portfolio of over **700 products**, we serve medical institutions and CDCs in more than **100 countries**. 
    Our mission is to contribute to a healthier future through accurate, efficient, and streamlined diagnostic technologies.
    """)

st.divider()

# القسم الثاني: تحديث تفشي الفيروس (Current Outbreak Alert 2026)
st.header(" Urgent Health Alert: West Bengal Outbreak")
st.error("""
**Current Situation (January 2026):**
Health authorities in **West Bengal, India**, are responding to a confirmed Nipah virus (NiV) outbreak, with **five cases reported** as of late January 2026. 
Rapid response measures, including quarantine and contact tracing, are currently underway.
""")

# القسم الثالث: حقائق منظمة الصحة العالمية (Key Facts from WHO)
st.header(" Key Facts & Pathogen Profile")
st.info("""
The **World Health Organization (WHO)** classifies Nipah virus as a high-risk pathogen with a fatality rate ranging from **40% to 75%**. 
Currently, there are no licensed vaccines or specific antiviral treatments available.
""")

# عرض الحقائق بنظام القائمة المنظمة
st.markdown("""
* **Severe Illness:** Symptoms range from fever and respiratory issues to fatal encephalitis.
* **Transmission:** Spread via infected animals (fruit bats), contaminated food, and direct human-to-human contact.
* **Critical Need:** Early detection is the only way to control outbreaks and support public health efforts.
""")

st.divider()

# القسم الرابع: الحلول التشخيصية (Diagnostic Solutions)
st.header(" Diagnostic Solutions")
st.write("To support global health response, BioPerfectus provides advanced tools for early detection:")

# إنشاء بطاقة لمنتج الـ PCR
st.success("""
**BioPerfectus Real-Time PCR Solution for Nipah Virus**
* **Rapid Detection:** Reliable results to aid in outbreak response.
* **Reliability:** High accuracy for patient management and clinical laboratories.
""")

# إضافة رابط خارجي (CTA)
st.markdown("🔗 **Explore the full diagnostic solution here:** [BioPerfectus NiV PCR Kit](https://www.linkedin.com/company/bioperfectus/posts/?feedView=all)")

st.divider()

# ملحوظة ندرة البيانات (المطلوبة سابقاً)
st.warning(" **Data Scarcity Warning:** Statistical analysis for early-stage outbreaks (like the current 5 cases in West Bengal) is highly sensitive due to the small sample size. Interpret early data with caution.")

# تذييل الصفحة
st.caption("© 2026 BioPerfectus. Supporting Global Health through Molecular Innovation.")

