import pandas as pd
import os

# 确保这里的路径是正确的，并且文件存在
file_path = r'E:\Neiman Marcus 数据库\NeimanMarcus\data\name_2.csv'

# 检查文件是否存在
if not os.path.exists(file_path):
    print(f"文件未找到: {file_path}")
else:
    # 读取整个 CSV 文件
    data = pd.read_csv(file_path)

    # 指定需要的列，若列不存在则填充为 NaN
    columns_to_extract = [
        'MTF_CUST_NAME', 'EMAIL_ADDRESS', 'MTF_PHONE',
        'MTF_ADDR1', 'MTF_ADDR2', 'MTF_CITY',
        'MTF_STATE', 'MTF_ZIP', 'MTF_COUNTRY_CD',
        'MTF_DOB', 'MTF_TF_ACCT', 'MTF_CARD_TYPE'
    ]

    # 创建一个新的 DataFrame，只包含指定的列，缺失的列将填充 NaN
    extracted_data = data.reindex(columns=columns_to_extract)

    # 转换出生日期格式
    if 'MTF_DOB' in extracted_data.columns:
        extracted_data['MTF_DOB'] = pd.to_datetime(extracted_data['MTF_DOB'], errors='coerce').dt.strftime('%Y-%m-%d')

    # 去重，保留第一次出现的记录
    extracted_data = extracted_data.drop_duplicates()

    # 重命名字段
    extracted_data.rename(columns={
        'MTF_CUST_NAME': '客户姓名',
        'MTF_PHONE': '主要电话号码',
        'MTF_ADDR1': '地址行1',
        'MTF_ADDR2': '地址行2',
        'MTF_CITY': '城市',
        'MTF_STATE': '州',
        'MTF_ZIP': '邮政编码',
        'MTF_DOB': '出生日期',
        'EMAIL_ADDRESS': '电子邮件地址',
        'MTF_TF_ACCT': '信用卡相关账户信息',
        'MTF_CARD_TYPE': '信用卡类型'
    }, inplace=True)

    # 输出提取的数据
    print(extracted_data)

    # 保存到指定路径，使用 tab 作为分隔符
    output_path = r'E:\Neiman Marcus 数据库\NeimanMarcus\data\name_split_4\name_1_split_5.tsv'
    extracted_data.to_csv(output_path, sep='\t', index=False, header=True)

    print(f"数据已成功保存到: {output_path}")
