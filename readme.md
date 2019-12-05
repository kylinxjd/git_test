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

我们希望把如下分支B、C、D三个提交记录合并为一个完整的提交，然后再push到公共仓库。

![Alt](https://upload-images.jianshu.io/upload_images/2147642-42195cacced56729.png)

现在我们在测试分支上添加了四次提交，我们的目标是把最后三个提交合并为一个提交：
![alt](https://upload-images.jianshu.io/upload_images/2147642-ce849c4eab3d803b.png)



使用命令`git rebase -i  [startpoint]  [endpoint]`



其中-i的意思是--interactive，即弹出交互式的界面让用户编辑完成合并操作，[startpoint] [endpoint]则指定了一个编辑区间，如果不指定[endpoint]，则该区间的终点默认是当前分支HEAD所指向的commit(注：该区间指定的是一个前开后闭的区间)。
在查看到了log日志后，我们运行以下命令：


`git rebase -i 36224db`


会看到如下界面

![alt](https://upload-images.jianshu.io/upload_images/2147642-03d48aa767efb307.png)


1.  pick：保留该commit（缩写:p）
2. reword：保留该commit，但我需要修改该commit的注释（缩写:r）
3. edit：保留该commit, 但我要停下来修改该提交(不仅仅修改注释)（缩写:e）
4. squash：将该commit和前一个commit合并（缩写:s）
5. fixup：将该commit和前一个commit合并，但我不要保留该提交的注释信息（缩写:f）
6. exec：执行shell命令（缩写:x）
7. drop：我要丢弃该commit（缩写:d）


我们编辑内容如下：


![alt](https://upload-images.jianshu.io/upload_images/2147642-a651234e62ed20a5.png)


然后修改注释





![alt](https://upload-images.jianshu.io/upload_images/2147642-44bbd784dcadfb31.png)



编辑完保存就可以合并了：



![alt](https://upload-images.jianshu.io/upload_images/2147642-334e0a5c47a24f87.png)








git pull ceshi

