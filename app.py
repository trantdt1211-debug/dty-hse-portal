import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="DTY HSE & ISO Portal", page_icon="🛡️", layout="wide")

st.title("🛡️ HỆ THỐNG QUẢN LÝ ATSKNN & ISO - XƯỞNG DTY")
st.markdown("---")

# Sidebar
st.sidebar.markdown("### 👤 Người quản lý")
st.sidebar.text("Phạm Nguyễn Tố Trân\nBộ phận DTY - PolytEx")
st.sidebar.markdown("---")

menu = st.sidebar.selectbox("Chọn Phân hệ quản lý:", [
    "1. Nhân sự & Chứng chỉ An toàn",
    "2. ISO & Lịch Truyền thông Hàng tháng",
    "3. Checklist Tự Đánh Giá ISO 45001",
    "4. Quản lý Tem & Tài sản",
    "5. Quản lý Tủ Y Tế (Form 5VEXXHR221)"
])

if "1." in menu:
    st.header("👥 Quản lý Biến động Nhân sự & Chứng chỉ An toàn")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Tổng Nhân Sự DTY", "262 người", "+3 mới")
    col2.metric("Nhóm 4 Tự Động", "100%", "Hạn: Vào làm + 1 năm")
    col3.metric("Chứng Chỉ Sắp Hết Hạn", "18", "Cần tái huấn luyện")
    col4.metric("Nhân Sự Đã Nghỉ Việc", "1 người", "Đàm Trung Kiên (008969)")

    st.warning("⚠️ **Cảnh báo Biến động:** Phát hiện nhân viên **Đàm Trung Kiên (008969)** đã nghỉ việc nhưng còn trong danh sách PCCC & Xe nâng.")
    if st.button("Tự động xóa khỏi danh sách chứng chỉ"):
        st.success("Đã cập nhật hệ thống và loại bỏ nhân sự nghỉ việc thành công!")

    st.subheader("📥 Smart Import (Kéo & Thả file HR / Excel)")
    uploaded_file = st.file_uploader("Tải lên file Excel danh sách nhân sự HR hoặc Kiểm kê:", type=["xlsx", "xls", "csv"])
    if uploaded_file is not None:
        st.success("Đã trích xuất file thành công! Hệ thống tự động gán Nhóm 4 cho nhân viên mới và lọc người nghỉ.")

    st.subheader("📊 Báo cáo Tổng hợp Chứng chỉ (Form Summary)")
    data_summary = {
        "Tên Lớp Học / Chứng chỉ": ["N1 - ATVSLĐ Nhóm 1", "N2 - ATVSLĐ Nhóm 2", "N3 - Xe Nâng Hàng (堆高機)", "N3 - Xe Nâng Người", "N3 - Bình Chịu Áp Lực", "SCC - Sơ Cấp Cứu"],
        "Nhu cầu (A)": [4, 2, 22, 9, 6, 12],
        "Có Chứng Chỉ (C)": [4, 5, 30, 14, 8, 12],
        "Hết Hạn (E)": [1, 1, 5, 7, 3, 0],
        "Chờ Đào Tạo (B)": [0, 0, 0, 0, 0, 0]
    }
    st.dataframe(pd.DataFrame(data_summary), use_container_width=True)
    if st.button("📥 Xuất File Báo cáo Excel Summary"):
        st.success("Đã xuất file báo cáo Summary(1) chuẩn thành công!")

elif "2." in menu:
    st.header("📅 Quản lý Lịch Truyền thông SOP & ISO Hàng tháng")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### 📢 Nội dung truyền thông Tháng 10/2026")
        st.info("1. Tuyên truyền An toàn đầu ca & Hỏi thăm sức khỏe (Đã thực hiện)")
        st.info("2. Tuyên truyền danh mục công việc ảnh hưởng sức khỏe sinh sản (Đã thực hiện)")
        st.warning("3. Khảo sát ý kiến NLĐ về mức độ phù hợp PPE (Chuẩn bị làm - Tháng 12)")
    with col2:
        st.markdown("### ✉️ Mail Hỏi Thăm Sự Cố")
        st.write("Ngày gửi tự động: 25 hàng tháng")
        if st.button("✅ Xác nhận: KHÔNG CÓ SỰ CỐ"):
            st.success("Đã ghi nhận báo cáo ISO tháng không có TNLĐ!")
        if st.button("⚠️ Báo cáo Có Sự Cố (Mẫu 5VEXXHR382)"):
            st.error("Mở form ghi nhận sự cố suýt xảy ra (near-miss).")

elif "3." in menu:
    st.header("📋 ISO 45001 Audit Readiness (Sẵn sàng Đánh giá)")
    st.error("🚨 BÁO ĐỎ: 02 mục cần bổ sung trước kỳ đánh giá ISO tháng 11/2026:\n- Thiếu Biên bản tham vấn NLĐ 5VEXXHR102-02\n- 3 nhân sự vận hành Bình áp lực chưa tái huấn luyện.")
    
    audit_data = {
        "Điều khoản": ["4.1 & 4.2", "5.3", "5.4", "8.1"],
        "Hạng mục": ["Bối cảnh tổ chức", "Vai trò & Trách nhiệm", "Tham gia tham vấn", "Kiểm tra tự động"],
        "Trạng thái": ["Đạt", "Đạt", "Thiếu (Không đạt)", "Đạt"],
        "Minh chứng": ["5VEXXHR411.pdf", "QĐ_PCCC.pdf", "Chưa có", "5VEXXHR401.pdf"]
    }
    st.dataframe(pd.DataFrame(audit_data), use_container_width=True)
    if st.button("🖨️ In Biên Bản Tự Đánh Giá ISO"):
        st.success("Đã tạo biên bản tự đánh giá sẵn sàng in!")

elif "4." in menu:
    st.header("🏷️ Quản lý Tem & Tài sản")
    search_code = st.text_input("🔍 Tra cứu nhanh theo Mã tài sản hoặc Tên thiết bị:", placeholder="Nhập 14004161-0...")
    
    asset_data = {
        "Mã Tài Sản": ["14004161-0", "70000146-0", "30000366-0"],
        "Tên Thiết Bị": ["Máy khoan điện KSD-340", "Xe HONDA LEAD 125CC", "Máy sấy khí hấp thụ"],
        "Bộ Phận": ["513301100 (100ha)", "513301000 (HR)", "513301000 (Công dụng)"],
        "Trạng thái Tem": ["Xin không dán tem", "Chưa dán - HR chuyển", "Đã dán tem"]
    }
    st.dataframe(pd.DataFrame(asset_data), use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📄 Tạo Đơn Xin Không Dán Tem (Form II)"):
            st.success("Đã tự động điền dữ liệu vào form 【0-H-003-P-FA001-附件二】 sẵn sàng in!")
    with col2:
        if st.button("📄 Tạo Đơn Điều Động Tài Sản (Form III)"):
            st.success("Đã tự động điền dữ liệu vào form 【0-H-003-P-FA001-附件三】 sẵn sàng in!")

elif "5." in menu:
    st.header("💊 Quản lý Tủ Y Tế & Vật Tư (Form 5VEXXHR221)")
    col1, col2, col3 = st.columns(3)
    col1.metric("Vật Tư Sắp Hết Hạn", "2 mục", "Povidine & Gạc vô trùng")
    col2.metric("Cảnh Báo Hao Hụt", "1 mục", "Băng cá nhân (Còn 5/20)")
    col3.metric("Trạng Thái Tủ", "Đạt chuẩn", "Kiểm tra 01/10/2026")

    med_data = {
        "Tên Thuốc / Vật Tư": ["Povidine 10%", "Băng keo cá nhân (Urgo)", "Gạc y tế tiệt trùng"],
        "Tồn Thực Tế": ["2 chai", "5 cuộn (Dưới tối thiểu)", "12 gói"],
        "Hạn Sử Dụng": ["05/11/2026 (Sắp hết)", "12/2027", "08/2028"],
        "Hành Động": ["Đề xuất bù kho", "Đề xuất cấp thêm", "Bình thường"]
    }
    st.dataframe(pd.DataFrame(med_data), use_container_width=True)
    if st.button("🖨️ In Biểu Kiểm Tra Định Kỳ 5VEXXHR221"):
        st.success("Đã xuất biểu mẫu kiểm tra tủ y tế định kỳ hàng tháng!")
