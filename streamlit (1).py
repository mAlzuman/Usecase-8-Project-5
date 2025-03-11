import streamlit as st
import pandas as pd
import requests  # مكتبة لإرسال البيانات إلى FastAPI

# إعداد الصفحة
st.set_page_config(
    page_title="تحليل فئات منتجات المكياج في نايس ون",
    page_icon="💄",
    layout="wide"
)

# إضافة صورة في الهيدر
image_url = "https://i.postimg.cc/zBTBbn7f/Innisfree-2020-Jeju-Color-Picker-Cherry-Blossom-Edition.jpg"
st.image(image_url, use_container_width=True)

# العنوان الرئيسي
st.markdown("<h1 style='text-align: center; color: #E91E63;'>!تحليل فئات منتجات المكياج في نايس ون🌸🛍️</h1>", unsafe_allow_html=True)

st.markdown("---")

# تحميل البيانات
file_path = "products_data.csv"

try:
    # قراءة الملف
    df = pd.read_csv(file_path)

    # استخراج قائمة البراندات الفريدة
    if "brand_name" in df.columns:
        brand_list = df["brand_name"].dropna().unique().tolist()
        brand_list.sort()
    else:
        brand_list = ["لا توجد بيانات متاحة"]

    # اختيار البراند
    st.markdown("<div style='text-align: center; font-size: 18px; font-weight: bold;'> :اختر نوع البراند🏷️</div>", unsafe_allow_html=True)
    selected_brand = st.selectbox("", brand_list)

    # استخراج قائمة أنواع المكياج الفريدة
    if "makeup_type" in df.columns:
        makeup_type_list = df["makeup_type"].dropna().unique().tolist()
        makeup_type_list.sort()
    else:
        makeup_type_list = ["لا توجد بيانات متاحة"]

    # اختيار نوع المكياج
    st.markdown("<div style='text-align: center; font-size: 18px; font-weight: bold;'> :اختر نوع المكياج💄</div>", unsafe_allow_html=True)
    selected_makeup_type = st.selectbox("", makeup_type_list)

    # إدخال عدد المراجعات
    st.markdown("<div style='text-align: center; font-size: 18px; font-weight: bold;'> :أدخل عدد المراجعات⭐</div>", unsafe_allow_html=True)
    reviews_number = st.number_input("", min_value=0, step=1, value=10)

    # إدخال السعر الأصلي
    st.markdown("<div style='text-align: center; font-size: 18px; font-weight: bold;'> :أدخل السعر الأصلي💰</div>", unsafe_allow_html=True)
    original_price = st.number_input("", min_value=0.0, step=1.0, value=100.0, format="%.2f")

    # اختيار نسبة الخصم
    st.markdown("<div style='text-align: center; font-size: 18px; font-weight: bold;'> :اختر نسبة الخصم📉</div>", unsafe_allow_html=True)
    discount_options = list(range(0, 101, 5))  # نسب الخصم من 0% إلى 100% بزيادة 5%
    selected_discount_percentage = st.selectbox("", discount_options)

    # حساب السعر بعد الخصم
    discounted_price = original_price * (1 - selected_discount_percentage / 100)

    st.markdown(f"""
        <div style="text-align: center; font-size: 18px; font-weight: bold;">
             :نسبة الخصم المختارة
            <div style="margin-top: 5px; color:#E91E63; font-weight: bold; font-size: 20px;">
                {selected_discount_percentage}%
            </div>
            <br>
             :السعر بعد الخصم
            <div style="margin-top: 5px; color:#4CAF50; font-weight: bold; font-size: 20px;">
                {discounted_price:.2f} ريال
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # زر لإرسال البيانات إلى FastAPI
    if st.button("تنبأ 🔮 "):
        try:
            # بيانات الإدخال التي سيتم إرسالها إلى API
            input_data = {
                "brand_name": selected_brand,
                "makeup_type": selected_makeup_type,
                "original_price": original_price,
                "discounted_price": discounted_price,
                "reviews_number": reviews_number
            }

            # إرسال البيانات إلى FastAPI
            api_url = "https://fastapi-app-8.onrender.com/predict"  
            response = requests.post(api_url, json=input_data)

            # عرض النتيجة
            if response.status_code == 200:
                prediction_result = response.json()
                predicted_category = prediction_result["predicted_category"]

                st.markdown(f"""
                    <div style="text-align: center; font-size: 20px; font-weight: bold; color:#E91E63;">
                        : التصنيف المتوقع لهذا المنتج🎯
                        <br>
                        <span style="font-size: 24px; color:#4CAF50;">{predicted_category}</span>
                    </div>
                """, unsafe_allow_html=True)

            else:
                st.error(f"⚠️ خطأ في الاتصال بـ API: {response.status_code}")

        except Exception as e:
            st.error(f"❌ حدث خطأ أثناء الاتصال بـ API: {str(e)}")

except Exception as e:
    st.error(f"⚠️ حدث خطأ أثناء تحميل الملف: {e}")
