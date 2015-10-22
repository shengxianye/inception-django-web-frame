关于inception-django-web-frame
====
使用djangon+metro_dashboard框架开发的一个页面，主要解决inception 没有web前端的问题    
inception地址： https://github.com/mysql-inception/inception    
metro地址： https://github.com/jiji262/Bootstrap_Metro_Dashboard    
安装方法：
-----
pip install Django==1.8.4    
mysql-python 1.2.5      
https://pypi.python.org/pypi/mysql-python/1.2.5#downloads   
修改环境变量~/.bash_profile   
PATH="/usr/local/mysql/bin:${PATH}"   
export PATH   
export DYLD_LIBRARY_PATH=/usr/local/mysql/lib/    
需要lib包   
ln -s /usr/local/mysql/lib/libmysqlclient.18.dylib /usr/lib/libmysqlclient.18.dylib   
ln -s /usr/local/mysql/lib /usr/local/mysql/lib/mysql   
开启进程    
python manage.py runserver 0.0.0.0:8000   
web:http://127.0.0.1:8000/dbaproject/inception.html/        


联系方式
----
635767825@qq.com


