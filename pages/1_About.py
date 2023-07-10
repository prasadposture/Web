import streamlit as st
st.set_page_config(page_title='Prasad Posture',layout='wide',page_icon='logo.ico')
markdown='''
<style>
[data-testid="stAppViewContainer"]{
background-color:#000000;
color:#ffffff;
}
[data-testid="stHeader"]{
opacity:0.0;
}
[data-testid="stSidebar"]{
background-color:#171717
}
[class="css-pkbazv e1fqkh3o5"]{
color:#ffffff
}
[class="css-17lntkn e1fqkh3o5"]{
color:#ffffff
}
[data-testid="collapsedControl"]{
color:#ffffff;
}
[class="css-1nm2qww e1fqkh3o2"]{
color:#ffffff;
}
</style>

'''

st.markdown(markdown,unsafe_allow_html=True)

st.markdown("""
<h1 style='color:#ffffff; font-family:Times New Roman ;'>About Me </h1>
<p style='font-family:sheriff; font-size:110%;'>I graduated in the field of mathematics with data analytics. 
I have particular interest in astronomy, and aiming to be in 
the field of data driven astronomy, where I can use my knowledge of physics, 
mathematics and data science for space exploration and reveal the secret of cosmos.
Being from mathematics background,
I naturally posses great problem solving abilities
with a unique algorithmic approach that particularly focuses on breaking down the problem
into simpler forms and tackling each part of it.
</p>
<hr style="border-color:#ffffff;">
""", unsafe_allow_html=True)
st.markdown("""
<h3 style='color:#ffffff;'>Education</h3>
""", unsafe_allow_html=True)

a,b,c = st.columns(3)
with a:
    st.markdown("""
<p style='font-family:sheriff; font-size:110%; border:1px solid gray; border-radius:10px; background-color:#171717;'>
<b>&nbsp B.Sc. Mathematics</b><br>
&nbsp Jai Hind College, Mumbai<br>
&nbsp CGPA : 9.75<br>
</p>""", unsafe_allow_html=True)

with b:
    st.markdown("""
<p style='font-family:sheriff; font-size:110%; border:1px solid gray; border-radius:10px; background-color:#171717;'>
<b>&nbsp HSC (PCMB)</b><br>
&nbsp Jai Hind College, Mumbai<br>
&nbsp Percentage : 75.34%<br>
</p>""", unsafe_allow_html=True)

with c:
    st.markdown("""
<p style='font-family:sheriff; font-size:110%; border:1px solid gray; border-radius:10px; background-color:#171717;'>
<b>&nbsp SSC</b><br>
&nbsp Panderi-Peve Highschool<br>
&nbsp Percentage : 93.40%<br>
</p>""", unsafe_allow_html=True)

st.markdown("""
<h3 style='color:#ffffff;'>Skills</h3>
""", unsafe_allow_html=True)
a,b = st.columns([1,4])
with a:
    st.markdown("""
<p style='font-family:sheriff; font-size:110%;'>
<b>Tech Skills:</b>
</p>
""", unsafe_allow_html=True)
    
with b:
    st.markdown("""
<p style='font-family:sheriff; font-size:110%;'>Python, &nbsp R, &nbsp SQL</p>
""", unsafe_allow_html=True)

a,b = st.columns([1,4])
with a:
    st.markdown("""
<p style='font-family:sheriff; font-size:110%;'>
<b>Python Libraries:</b>
</p>
""", unsafe_allow_html=True)
    
with b:
    st.markdown("""
<p style='font-family:sheriff; font-size:110%;'>Pandas, &nbsp NumPy, &nbsp Matplotlib, &nbsp Seaborn, &nbsp Streamlit,
&nbsp Plotly, &nbsp Scikit-Learn</p>
""", unsafe_allow_html=True)

a,b = st.columns([1,4])
with a:
    st.markdown("""
<p style='font-family:sheriff; font-size:110%;'>
<b>Data Skills:</b>
</p>
""", unsafe_allow_html=True)
    
with b:
    st.markdown("""
<p style='font-family:sheriff; font-size:110%;'>Data Cleaning, &nbsp Data Manipulation, &nbsp Data Visualization, &nbsp Question Based Analysis, &nbsp Exploratory Data Analysis,
&nbsp Predictive Analysis, &nbsp Web Scraping</p>
""", unsafe_allow_html=True)

a,b = st.columns([1,4])
with a:
    st.markdown("""
<p style='font-family:sheriff; font-size:110%;'>
<b>Microsoft Tools:</b>
</p>
""", unsafe_allow_html=True)
    
with b:
    st.markdown("""
<p style='font-family:sheriff; font-size:110%;'>Word, &nbsp Excel, &nbsp PowerPoint, &nbsp PowerBI</p>
""", unsafe_allow_html=True)
    
a,b = st.columns([1,4])
with a:
    st.markdown("""
<p style='font-family:sheriff; font-size:110%;'>
<b>Maths Skills:</b>
</p>
""", unsafe_allow_html=True)
    
with b:
    st.markdown("""
<p style='font-family:sheriff; font-size:110%;'>Probability, &nbsp Statistics, &nbsp Calculus, &nbsp Algebra, 
&nbsp Real and Complex Analysis, &nbsp Mathematical Methods</p>
""", unsafe_allow_html=True)

a,b = st.columns([1,4])
with a:
    st.markdown("""
<p style='font-family:sheriff; font-size:110%;'>
<b>Soft Skills:</b>
</p>
""", unsafe_allow_html=True)
    
with b:
    st.markdown("""
<p style='font-family:sheriff; font-size:110%;'>Effective Communication, &nbsp Time Management, &nbsp Problem Solving,
&nbsp Critical Thinking, &nbsp Creative Writing</p>
""", unsafe_allow_html=True)
    


st.markdown("""
<h3 style='color:#ffffff;'>Courses</h3>
<a href="https://jovian.com/certificate/MFQTQMJYGI">Machine Learning with Python: from Zero to GBM </a><br>
<a href="https://jovian.com/certificate/MFQTOOJVGI">Data Analysis with Python: from Zero to Pandas </a><br>
<a href="https://drive.google.com/file/d/1oe2VOHz4Jp9FrKoiiKCtJPQqB9U8uOWm/view">Aritifical Intelligence </a><br>
<a href="https://drive.google.com/file/d/1l6aKdzuxLXTd1IvpoQirhfJGbWHhMh4Y/view">Data Analytics with Python </a><br>
<a href="https://www.kaggle.com/learn/certification/prasadposture121/intro-to-sql">Introduction to SQL </a><br>
<a href="https://drive.google.com/file/d/1W5hc0f0CWodbbIwdvwBfiBR3Cwu__-QY/view">Data Analysis using Excel </a><br>
<a href="https://drive.google.com/file/d/1OeJaKndjOAfAvBMx4nM_MGYrwjb9yTKq/view">PowerBI for Beginners </a>

""", unsafe_allow_html=True)

st.markdown("""
<h3 style='color:#ffffff;'>Achievements</h3>
<p style='font-family:sheriff; font-size:110%;'>
1. Been on the achievers list of Jai Hind College, Mumbai<br>
2. Achieved highest rank 708 among 270k+ notebook experts on kaggle<br>
3. AIR 216 in IIT JAM Physics
</p>
""", unsafe_allow_html=True)
