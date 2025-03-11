# 🏫 Tuwaiq Academy  
## 📊 Data Science and Machine Learning Bootcamp  
### 💄 Use Case 8 - Project 5: Niceone Makeup  

---

## 📌 Introduction  
This dataset was collected from the **Nice One** website on **March 7, 2025**.  
Nice One is a leading Saudi **e-commerce platform** specializing in **beauty, care, and perfume** products.

---

## ❓ Problem Statement  
Customers often struggle to find makeup products that fit their **budget** and **preferences**.  
This project aims to **apply K-means clustering** to group makeup products based on key features such as:  

- **Price** (Original & Discounted)  
- **Makeup Type**  
- **Brand Name**  
- **Review Count**  

This approach helps users effortlessly discover **low-cost, affordable, and luxury** options.

---

## 📂 Dataset  
The dataset was **scraped on March 7, 2025**, from the **Niceone** official website.  
It consists of **9 key features**:

| Feature          | Description |
|-----------------|-------------|
| **Original Price** | The product's price before any discount |
| **Discount Price** | The price after the discount (if `0`, no discount was applied) |
| **Name** | The name of the product or tool |
| **Brand Name** | The brand of the product |
| **Rating Number** | The product's rating (out of 5) |
| **Reviews Number** | The number of customer reviews |
| **Skin Type** | The skin type suitable for the product |
| **Makeup Type** | The category of makeup (e.g., foundation, lipstick). `"Not Available"` means no specified type |
| **Texture** | The product’s texture (e.g., liquid, powder). `"Not Available"` means no specified texture |

---

## ⚙️ Model Used: **K-Means Clustering**  
### 🎯 **Purpose**  
To categorize makeup products into distinct clusters based on key features, making it easier for users to find suitable products.  

### 🏷️ **Product Categories Identified**  
1. **💰 Affordable Essentials** - Budget-friendly options for daily use.  
2. **🔬 High-Quality Tools** - Premium products known for performance and durability.  
3. **👑 Luxury Essentials** - High-end, exclusive makeup items for a luxurious experience.  
4. **🎯 Budget-Friendly Options** - Products that balance quality and affordability.  

---
## 🚀 Model Deployment  

We deployed the model using **FastAPI**, starting with **library installation** and **API development**.  
After **local testing via Swagger UI**, we uploaded the project to **GitHub** and deployed it on **Render** by configuring a **Web Service**.  
Finally, we integrated the API with **Streamlit**, creating an **interactive UI** for users to send data and view predictions.  

🔗 **Live Demo:** [Streamlit App](https://app-app-idrjhys4fh8ndhuqznrprq.streamlit.app) 🚀

---

## 👥 Team Members  
- **Munirah Alzuman**  
- **Raghad Alharbi**  
- **Yaqeen Alhalal**  
- **Tahani Alotaibi**  

---

📌 *This project is part of the Tuwaiq Academy Data Science and Machine Learning Bootcamp.*  
🚀 *Happy Clustering!*
