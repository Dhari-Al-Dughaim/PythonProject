import streamlit as st

st.title("🧑‍💻 الدرس 1: الطباعة في بايثون - print()")

st.markdown("""
في هذا الدرس، سنتعلم كيف نطبع نصوص أو أرقام باستخدام الدالة `print()`.

الدالة `print()` هي من أهم الدوال في بايثون، وتُستخدم لعرض البيانات على الشاشة.

### 🧪 مثال:
```python
print("مرحباً بك في عالم بايثون!")
```
""")

st.code('print("مرحباً بك في عالم بايثون!")', language='python')

st.markdown("### ✍️ جربها بنفسك!")

user_code = st.text_area("اكتب كود الطباعة الخاص بك هنا 👇", height=150)

if st.button("تشغيل الكود"):
    try:
        with st.redirect_stdout(st.stdout):
            exec(user_code)
    except Exception as e:
        st.error(f"❌ خطأ في الكود: {e}")