from flask import Flask, render_template, request, jsonify
import os
import Snapshot_cal_branch as psse_logic

app = Flask(__name__)

# CẤU HÌNH ĐƯỜNG DẪN
DATA_ROOT_FOLDER = r'D:\OneDrive - NSMO\Du lieu\1. Phuong thuc van hanh\03. PTVH Tuan\Snapshot' 
UPLOAD_FOLDER = 'uploads'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_folders')
def get_folders():
    folders = []
    try:
        if os.path.exists(DATA_ROOT_FOLDER):
            items = os.listdir(DATA_ROOT_FOLDER)
            for item in items:
                full_path = os.path.join(DATA_ROOT_FOLDER, item)
                if os.path.isdir(full_path) and item.startswith('2025_'):
                    folders.append(item)
            folders.sort(reverse=True)
    except Exception as e:
        return jsonify({'error': str(e)})
    return jsonify(folders)

@app.route('/run_simulation_compare', methods=['POST'])
def run_simulation_compare():
    try:
        # 1. Nhận dữ liệu
        selected_date = request.form.get('date')
        uploaded_file = request.files.get('script_file')
        
        target_folder = os.path.join(DATA_ROOT_FOLDER, selected_date)
        
        script_path = ""
        if uploaded_file:
            script_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(script_path)
            
        print(f"--- Bắt đầu phân tích ngày: {selected_date} ---")

        # 2. CHẠY LẦN 1: Dữ liệu GỐC (Base Case) - Không có script phụ
        # Lưu ý: file_py_path truyền vào là chuỗi rỗng hoặc None
        print("1. Đang chạy dữ liệu Gốc (Không Script)...")
        data_base = psse_logic.data_file_multicore(target_folder, file_py_path="")

        # 3. CHẠY LẦN 2: Dữ liệu MỚI (Modified Case) - Có script phụ
        print(f"2. Đang chạy dữ liệu có Script tác động ({script_path})...")
        if script_path:
            data_modified = psse_logic.data_file_multicore(target_folder, file_py_path=script_path)
            msg = f"Đã so sánh dữ liệu Gốc vs Dữ liệu chạy Script {uploaded_file.filename}"
        else:
            # Nếu không upload script thì 2 file giống nhau
            data_modified = data_base
            msg = "Không có script phụ. Dữ liệu trước và sau giống nhau."

        # 4. Tính toán Delta (Mới - Gốc)
        # data_modified là File 1, data_base là File 2
        data_delta = psse_logic.compare_data_in_memory(data_base, data_modified)

        return jsonify({
            'status': 'success',
            'message': msg,
            'payload': {
                'file1': data_modified, # Dữ liệu có Script (Mới)
                'file2': data_base,     # Dữ liệu Gốc (Cũ)
                'delta': data_delta,
                'info': {'date': selected_date, 'script': uploaded_file.filename if uploaded_file else 'None'}
            }
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    print("Server đang chạy tại http://127.0.0.1:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)

