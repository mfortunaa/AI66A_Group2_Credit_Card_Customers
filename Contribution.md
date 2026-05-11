## 👥 Team Contribution

**1. Mai Tuấn Mạnh (11247318)**
* **Data Preprocessing Pipeline:** Phụ trách xử lý dữ liệu thô, mã hóa biến phân loại (Label/One-Hot Encoding) và chuẩn hóa dữ liệu (Scaling).
* **Imbalanced Class Handling:** Áp dụng thuật toán SMOTE kết hợp với Stratified K-Fold CV để đảm bảo mô hình không bị rò rỉ dữ liệu (data leakage).
* **Baseline Modeling:** Khởi tạo và đánh giá hiệu năng ban đầu của các mô hình Gradient Boosting (LightGBM, XGBoost, CatBoost).

**2. Nguyễn Khôi Nguyên (11247331)**
* **Advanced Tuning:** Thiết lập không gian tìm kiếm (search space) và chạy thuật toán tối ưu hóa Bayesian sử dụng framework Optuna để tối đa hóa F1-Score.
* **Stacking Ensemble:** Thiết kế kiến trúc meta-model với Level-0 là các mô hình Boosting và Level-1 là Logistic Regression.
* **Threshold Optimization:** Phân tích đường cong Precision-Recall để chọn ra ngưỡng ra quyết định tối ưu (0.5629) nhằm cân bằng chi phí kinh doanh.

**3. Nguyễn Bảo Tài (11247348)**
* **Exploratory Data Analysis (EDA):** Phân tích và trực quan hóa phân phối dữ liệu, vẽ ma trận tương quan để tìm ra các biến phân biệt nhóm khách hàng Churn.
* **Model Interpretability:** Triển khai thư viện SHAP để giải thích lý do rời bỏ của khách hàng ở cả góc độ toàn cục (Global) và cá nhân (Local).
* **Documentation:** Tổng hợp toàn bộ kết quả, đưa ra Strategic Action Plan cho bộ phận CRM và biên soạn báo cáo LaTeX chuẩn học thuật.