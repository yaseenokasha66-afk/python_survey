import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

file_name = "answers.csv"

# الأسئلة الستة
questions = {
    "أين أفضل وضع اللوغو؟": ["وسط الإعلان", "أعلى يمين", "أعلى يسار", "أسفل الإعلان"],
    "هل تفضل الألوان فاتحة أم داكنة؟": ["فاتحة", "داكنة", "محايد"],
    "هل النص الكبير أفضل أم الصغير؟": ["كبير", "صغير", "محايد"],
    "هل تفضل الصور في الإعلان؟": ["نعم", "لا", "محايد"],
    "هل الإعلان القصير أفضل أم الطويل؟": ["قصير", "طويل", "محايد"],
    "هل تفضل العروض والخصومات في الإعلان؟": ["نعم", "لا", "محايد"]
}

# تحميل البيانات إذا موجودة، أو إنشاء جديد
if os.path.exists(file_name):
    df = pd.read_csv(file_name)
else:
    df = pd.DataFrame(columns=questions.keys())

st.title("استبيان الإعلان التفاعلي")

# جمع إجابات المستخدم
user_answers = {}
for q, options in questions.items():
    user_answers[q] = st.radio(q, options)

# زر إرسال الإجابات
if st.button("إرسال الإجابات"):
    df = df.append(user_answers, ignore_index=True)
    df.to_csv(file_name, index=False)
    st.success("تم تسجيل إجاباتك!")

# عرض المخططات البيانية لكل سؤال
st.subheader("نتائج الاستبيان حتى الآن")
for q in questions.keys():
    counts = df[q].value_counts()
    plt.figure(figsize=(6,4))
    counts.plot(kind='bar', color='skyblue')
    plt.title(q)
    plt.xlabel("الاختيارات")
    plt.ylabel("عدد الأصوات")
    st.pyplot(plt)