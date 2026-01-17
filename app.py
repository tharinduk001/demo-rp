import streamlit as st
import ipaddress

# Page Configuration
st.set_page_config(page_title="Tharinduk001 - Subnet Calculator Version 1", page_icon="🌐", layout="centered")

# Custom Styling
st.markdown("""
    <style>
    /* 1. Remove Streamlit Branding/Header */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}

    /* 2. Main background */
    .main {
        background-color: #f5f7f9;
    }

    /* 3. Force Black Font in Metric Boxes */
    [data-testid="stMetricValue"] {
        color: black !important;
        font-weight: 700;
    }
    [data-testid="stMetricLabel"] {
        color: black !important;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border: 1px solid #e1e4e8;
    }
    
    /* Brand Styling for the Sidebar - YELLOW UPDATE */
    .brand-text {
        font-size: 26px;
        font-weight: bold;
        color: #FFD700; /* Gold/Yellow */
        text-shadow: 1px 1px 2px #000000; /* Dark shadow for readability */
        margin-bottom: -10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (Branding & Inputs) ---
with st.sidebar:
    # Your Brand Title in Yellow
    st.markdown('<p class="brand-text"> Tharinduk001🔥</p>', unsafe_allow_html=True)
    st.caption("Network Solutions v1.0")
    st.divider()
    
    st.header("Input Parameters")
    ip_input = st.text_input("IP Address", value="192.168.1.0")
    cidr_input = st.slider("CIDR Prefix (0-32)", min_value=0, max_value=32, value=24)
    
    st.sidebar.markdown("---")
    st.sidebar.info("Developed by Tharinduk001")

# --- MAIN CONTENT ---
st.title("🌐 Network Subnet Calculator")
st.title("✨HELLO WORLD✨")
st.write("Professional utility for fast network address calculation.")

# Logic Section
try:
    network_str = f"{ip_input}/{cidr_input}"
    net = ipaddress.ip_network(network_str, strict=False)
    
    # The 4 Metric Boxes
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Network Address", str(net.network_address))
        st.metric("Broadcast Address", str(net.broadcast_address))
    with col2:
        st.metric("Subnet Mask", str(net.netmask))
        st.metric("Total Hosts", f"{net.num_addresses:,}")

    st.divider()

    # Detailed Table
    st.subheader("📋 Detailed Information")
    
    if net.num_addresses > 2:
        first_host = net.network_address + 1
        last_host = net.broadcast_address - 1
        usable_hosts = net.num_addresses - 2
    elif net.num_addresses == 2:
        first_host, last_host, usable_hosts = net.network_address, net.broadcast_address, 2
    else:
        first_host, last_host, usable_hosts = net.network_address, "N/A", 1

    details = {
        "Property": ["Brand Owner", "CIDR Notation", "Wildcard Mask", "First Usable Host", "Last Usable Host", "Usable Hosts"],
        "Value": [
            "Tharinduk001",
            f"/{cidr_input}",
            str(net.hostmask),
            str(first_host),
            str(last_host),
            str(usable_hosts)
        ]
    }
    st.table(details)

except ValueError:
    st.error("Invalid IP Address or CIDR. Please check your input.")