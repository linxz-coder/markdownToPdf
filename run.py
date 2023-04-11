import os
import markdown
import pdfkit

# 文件夹路径
folder_path = "/Users/lxz/Downloads/md_to_pdf/"

# 获取文件夹内的所有文件列表
files = os.listdir(folder_path)

# 找到第一个以".md"结尾的文件
md_file = None
for file in files:
    if file.endswith(".md"):
        md_file = file
        break

# 如果找到了md文件
if md_file:
    md_file_path = os.path.join(folder_path, md_file)
    str = "<meta charset='utf-8'>" #这一步是为了解决中文乱码问题

    with open(md_file_path, "r", encoding="utf-8") as f:
        text = f.read()
    html = markdown.markdown(text)
    with open(os.path.join(folder_path, "out.html"), "w", encoding="utf-8") as f:
        f.write(str) #这一步是为了解决中文乱码问题
        f.write(html)

    pdfkit.from_file(os.path.join(folder_path, "out.html"), os.path.join(folder_path, "out.pdf"))
else:
    print("没有找到md文件。")
