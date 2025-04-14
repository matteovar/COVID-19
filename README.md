# 🏦 Market Sales Dashboard

An interactive dashboard built with Python, Pandas, and Streamlit for analyzing retail sales data. The project provides insights into product performance, customer behavior, sales channels, discount strategies, and returns.

## 📊 Features

- Time-series analysis of sales trends
- KPIs: Total Revenue, Average Ticket, Top-Selling Products
- Discount vs. Sales Quantity relationship
- Customer behavior by age, gender, and loyalty status
- Multi-page navigation via Streamlit

## 🚀 Getting Started

1. [Streamlit link](https://market-sales.streamlit.app)

## 📂 Expected Data Format

The CSV file should contain the following columns:

TransactionID, ProductID, ProductName, ProductCategory, SalesQuantity, SalesPrice, DiscountAmount, FinalSalePrice, TransactionDate, TimeOfDay, SalesChannel, PaymentMethod, PaymentStatus, TransactionStatus, CustomerID, CustomerAge, CustomerGender, CustomerLocation, LoyaltyProgramMember, CustomerFeedbackRating, ReturnFlag, ReturnReason, StoreLocation, Region, PromoCodeUsed, DiscountPercentage, ShippingMethod, ShippingFee, ShippingStatus, SalesTax, CrossSellProducts, UpsellProducts

[Access to Dataset](https://www.kaggle.com/datasets/harinkl/sales-data)

## 📈 Sample Visualizations

- Scatter plot: Discount % vs Final Sale Price (with quantity size)
- Bar chart: Top 10 selling products
- Line chart: Sales trend over time
- KPIs: Total revenue, ticket size, return rate

## ⚖️ Technologies Used

- Python 3.10+
- pandas
- streamlit
- plotly
