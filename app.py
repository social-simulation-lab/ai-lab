import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Social Simulation Lab", layout="wide")

st.title("🧪 AI Social Simulation Lab")
st.subheader("Mô phỏng tác động của Thuật toán Cá nhân hóa đến Sự Phân cực Quan điểm")

# Sidebar - Cấu hình tham số
st.sidebar.header("⚙️ Cấu hình Thí nghiệm")
num_agents = st.sidebar.slider("Số lượng Cá thể (Agents)", 10, 500, 100, step=10)
steps = st.sidebar.slider("Số vòng Mô phỏng (Steps)", 10, 200, 50, step=10)
algo_strength = st.sidebar.slider("Cường độ Thuật toán Cá nhân hóa", 0.0, 1.0, 0.5, step=0.1)

st.write(f"*Số lượng cá thể:* {num_agents} | *Số vòng chạy:* {steps} | *Độ mạnh thuật toán:* {algo_strength}")

# Khởi tạo dữ liệu mô phỏng
np.random.seed(42)
opinions = np.random.uniform(-1.0, 1.0, num_agents)

history = [opinions.copy()]

# Vòng lặp mô phỏng
for _ in range(steps):
    new_opinions = opinions.copy()
    for i in range(num_agents):
        # Chọn cá thể tương tác dựa trên thuật toán
        if np.random.rand() < algo_strength:
            # Chọn cá thể có quan điểm tương đồng
            similar_mask = np.abs(opinions - opinions[i]) < 0.5
            candidates = np.where(similar_mask)[0]
            if len(candidates) > 0:
                j = np.random.choice(candidates)
            else:
                j = np.random.choice(num_agents)
        else:
            j = np.random.choice(num_agents)
        
        # Cập nhật quan điểm
        diff = opinions[j] - opinions[i]
        new_opinions[i] += 0.1 * diff
    
    opinions = np.clip(new_opinions, -1.0, 1.0)
    history.append(opinions.copy())

# Hiển thị biểu đồ kết quả
st.write("### 📊 Biểu đồ Biến đổi Quan điểm Theo Thời gian")
fig, ax = plt.subplots(figsize=(10, 5))
history_arr = np.array(history)
for i in range(min(num_agents, 50)):
    ax.plot(history_arr[:, i], alpha=0.5)

ax.set_xlabel("Vòng mô phỏng")
ax.set_ylabel("Mức độ Quan điểm (-1: Cực đoan A, +1: Cực đoan B)")
ax.set_title("Sự hội tụ và Phân cực Quan điểm Xã hội")
st.pyplot(fig)
Đã gửi
Soạn
Viết cho
