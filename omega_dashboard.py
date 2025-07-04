
import streamlit as st
import pandas as pd

# Sample data
orders = pd.DataFrame({
    'Order ID': ['001', '002', '003'],
    'Customer': ['John Doe', 'Alice Smith', 'Mike Lee'],
    'Item': ['iPhone 16', 'Galaxy S22', 'MacBook Air'],
    'Status': ['Delivered', 'In Transit', 'Refunded'],
    'Refund Requested': ['Yes', 'No', 'Yes']
})

st.set_page_config(page_title="Omega Refund Dashboard", layout="wide")
st.title("📦 Omega Refund Dashboard")
st.markdown("Simplified demo of your Omega-powered return & refund system.")

# Orders Table
st.subheader("📋 Orders Overview")
st.dataframe(orders)

# Manual Refund Section
st.subheader("🔧 Manual Refund Control")
selected_order = st.selectbox("Select Order ID", orders['Order ID'])
if st.button("Mark as Refunded"):
    st.success(f"Order {selected_order} has been marked as refunded.")

# Upload proof
st.subheader("🧾 Upload Proof / Receipt")
uploaded_file = st.file_uploader("Upload a file for this order:", type=['png', 'jpg', 'jpeg', 'pdf'])
if uploaded_file:
    st.success("File uploaded successfully!")

# Tracking input
st.subheader("🚚 Courier Tracker")
tracking = st.text_input("Enter Tracking Number")
if tracking:
    st.info(f"Tracking {tracking}... Status: In Transit")

# Lost in tracking
if st.button("⚠️ Mark as Lost in Tracking"):
    st.warning(f"Order {selected_order} has been flagged as LOST IN TRACKING.")

# Analytics
st.subheader("📊 Refund Stats Summary")
refund_count = (orders['Refund Requested'] == 'Yes').sum()
st.metric(label="Total Refund Requests", value=refund_count)
