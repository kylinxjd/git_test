命令行创建仓库


### create a new repository on the command line
```
echo "# dddd" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/kylinxjd/dddd.git
git push -u origin master
```


### push an existing repository from the command line
```
git remote add origin https://github.com/kylinxjd/dddd.git
git push -u origin master
```

### SSH设置

#### 生成公钥和私钥
一、打开git bash。

二、执行命令ssh-keygen -t rsa -C "邮箱"。

三、按三次回车后完成收工，如图2。

四、按提示的目录找到对应的两个文件，分别为私钥和公钥，如图1。

![Alt](https://img-blog.csdnimg.cn/20190706223006129.png)

图1 


#### 使用公钥和私钥
一、登录GitHub账号并打开settings，如图3。

二、打开“SSH and GPG keys”页签，然后点击“new key”，如图4。

三、随便输入一个Title名字，然后打开id_rsa.pub文件，把文件内容复制到key的输入框中，保存，如图5。至此公钥设置完成。

四、打开git bash窗口，执行命令“ssh -T git@github.com”，然后输入yes。如图6。至此本地私钥设置完成。



### 分支
1、查看分支
`git branch` 

2、创建分支
`git checkout -b branchname`  

3、切换分支
`git checkout branchname`    

4、将远程master代码下载到本地
`git pull`

5、将其他分支合并到master

`git merge newbranch`


`git merge newbranch --squash`  

--squash合并的时候不会将newbranch的commit记录带到当前分支，所以当前分支需要总结再commit一次。



### 合并多个已提交的commit为一个commit


链接：https://www.jianshu.com/p/4a8f4af4e803









git pull ceshi

