# 安装
## 1. 安装markdown  
terminal输入：
``` 
pip3 install markdown
```
如果pip3不起作用，就用pip。  
这与你的python版本有关，python3用pip3，
<br/><br/>

## 2. 安装pdfkit  
terminal输入：
```
pip3 install pdfkit
```
如果pip3不起作用，就用pip。  
这与你的python版本有关，python3用pip3，
<br/><br/>

## 3. 安装wkhtmltopdf
terminal输入：
```
brew install Caskroom/cask/wkhtmltopdf 
```
注意：wkhtmltopdf不能用pip3安装，会一直不成功。  
官方安装说明：https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf
<br/><br/>

# 使用
terminal输入：
```
python3 run.py
```
如果python3不起作用，就用python。  
这与你的python版本有关.
<br/><br/>

# 说明
输出文件会有out.html和out.pdf两个文件。  
为了保证输出格式，输出中转了html一层。