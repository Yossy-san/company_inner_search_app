import chardet

input_path = 'data/社員について/社員名簿.csv'
output_path = 'data/社員について/社員名簿_utf8.csv'

# 1. まずバイナリで読み込んでエンコーディング判定
with open(input_path, 'rb') as f:
    raw = f.read()
    result = chardet.detect(raw)
    encoding = result['encoding']
    print(f"推定エンコーディング: {encoding}")

# 2. 推定エンコーディングで読み込み、utf-8で保存
with open(input_path, 'r', encoding=encoding) as f_in:
    content = f_in.read()

with open(output_path, 'w', encoding='utf-8') as f_out:
    f_out.write(content)

print("変換完了")