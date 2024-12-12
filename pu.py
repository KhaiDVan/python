import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL của trang fbref chứa dữ liệu cầu thủ
url = 'https://fbref.com/en/comps/9/stats/Premier-League-Stats'

# Gửi yêu cầu HTTP để lấy nội dung trang
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Tìm bảng chứa dữ liệu cầu thủ
table = soup.find('table', {'id': 'stats_standard'})

# Lấy tiêu đề các cột
headers = [th.text for th in table.find('thead').find_all('th')]

# Lấy dữ liệu các cầu thủ
rows = table.find('tbody').find_all('tr')

# Tạo danh sách để lưu dữ liệu
data = []

for row in rows:
    player_data = [td.text for td in row.find_all('td')]
    if player_data:
        data.append(player_data)

# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data, columns=headers)

# Chuyển đổi cột 'Min' sang kiểu số nguyên để lọc
df['Min'] = pd.to_numeric(df['Min'], errors='coerce')

# Lọc các cầu thủ có số phút thi đấu nhiều hơn 90 phút
df = df[df['Min'] > 90]

# Sắp xếp theo tên và tuổi
df = df.sort_values(by=['Player', 'Age'], ascending=[True, False])

# Lưu kết quả vào file CSV
df.to_csv('results.csv', index=False)

print("Dữ liệu đã được thu thập và lưu vào file 'results.csv'.")
