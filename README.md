### 暴力破解zip
因为是单线程，所以肯能会很慢
只用一个密码本存时，强制关闭程序，有可能会在刚刚清空文件还没有写入的时候，会丢失进度，所以用两个，保证任何时候都有一个是有内容的
##### 另外
单线程确实有点慢了，看什么时候搞个多线程吧

23.10.22 重装系统了，用这个来测试git

23.10.30 想到一个优化，不需要每一个生成一个密码就存入密码本，这样读写太频繁了，可以定时保存，每个几分钟存一次（算了，不想改了，就这样吧，以后看看要不要改）