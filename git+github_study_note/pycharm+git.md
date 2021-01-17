# Git介绍

git 可以做什么？

git 使用需要学到哪些？

git怎么回退？怎么创建分支和切换分支？怎么将本地的分支推送到远程库？怎么fork两个远程库？

权限模式下怎么去提交申请？审批申请？ 最低权限人员，提交一个代码审批流程是那些在哪里可以模拟这个流程？

## 1.git生成多个秘钥

`ssh-keygen -t rsa -C "YOUR_EMAIL@YOUREMAIL.COM" -f ~/.ssh/aysee`

`Host github.com www.github.com IdentityFile ~/.ssh/aysee`

######  插曲windos 查看公钥  “”“Type id_rsa.pub”“”

### 1.2 测试是否连接成功

`ssh -T git@gitcafe.com`

成功连接提示 Hi ***! You've successfully authenticated, but GitHub does not provide shell access.

## 2.git的基本使用

##### 帮助文档

git help reset 

### .or create a new repository on the command line

```
echo "# pDower" >> README.md
git init  [git clone https://github.com/pDower/pDower.git]
git add README.md
git commit -m "first commit"
git branch -M master
git remote add origin https://github.com/pDower/pDower.git
git push -u origin master
```

### …or push an existing repository from the command line

```
git remote add origin https://github.com/pDower/pDower.git
git branch -M master
git push -u origin master
git push --set-upstream origin master
 git config --global user.email "you@example.com"
 git config --global user.name "Your Name"
```


### 3、流程

添加文件git add <文件名>--》 从暂存区删除 git rm --cached <文件名> 

![gitstatus](.\img\gitstatus.jpg)

[本地库    暂存区   工作区]

git status   查看工作区暂存区状态 

git add <file name>  将工作区的文件添加到暂存区

git commit              将暂存区内容添加到本地库 



![關聯](.\img\關聯.jpg)



### 4、查看日志

git log

git log --pretty=online

git log --online

git log reflog  [显示历史版本步数]s

![回退](.\img\回退.jpg)



### 5、回退的3种方式

git reset --hard <回退的字符>

git reset --hard HEAD^^^

git reset --hard HEAD~2

![1610873523139](.\img\3种回退.png)

![1610873135942](.\img\1610873135942.png)

![1610873183855](.\img\回退2.png)



#### 回退reset 参数 hard和 soft的区别

hard 是回退工作区、暂存区、本地库的整体操作

soft 只移动本地库或者缓存区回退



![1610873885451](.\img\reset1.png)

![1610873974228](.\img\reset2.png)

![1610875204051](.\img\找回删除的文件.png)



### 6、git 文本比较

目的是和暂存区或者本地库当前或者历史版本比较，文件有哪些修改个增加，使用+@@ 表示增加 -表示删除

使用diff 命令指定和暂存区（默认）还是本地库比较

git diff 

git diff <文件名>

git diff HEAD^^ <文件名>

![1610875303160](.\img\diff.png)



### 7、分支

先保留原来版本 必要时再合并

![1610876814266](.\img\branch.png)



查看分支  git branch -v  

新建分支  git branch 【分支名字】

切换分支  git chekout 【分支名字】

合并分支 1、先切换到被合并的分支上面；2.执行 git  merge 【要合并有修改的分支名】 

解决冲突：删除特殊符号，修改要保留的代码，add，commit【commit的时候不带具体的文件名】



![1610880465165](.\img\merge.png)

![1610880597788](.\img\merage1.png)





#### 7、git 原理

##### hash 

md5 、sha1（git使用）、sha256

git 基于快照形式保存文件！

git管理分支 和切换使用 指针Head 





# 实验一 创建一个团队模拟操作

岳不群、令狐冲、东方不败

查看远程库有哪些  git remote -v

为远程库设置别名 git remote add origin [仓库名]

推送 到远程库 git push 【远程库别名】 【分支】



为什么我的成员没有权限？怎样开通权限？



![1610882083796](.\img\sy2.png)







![1610882032496](.\img\sy1.png)





克隆的时候有三个关联动作

![1610883756351](.\img\clone.png)





没有权限的团队成员不能push 文件

![1610884748810](.\img\notPush403.png)



![1610884807759](.\img\添加团队成员.png)



pull是fetch+merge 【fetch是将文件拉取到本地，不做任何操作，merge是和新分支合并】

谨慎处理应该是先 git fetch origin master 比较后觉得可以合并在合并git merge origin/master



![1610885556144](.\img\pull1.png)

![1610885139224](.\img\pull.png)



#### 协同操作时 冲突【不是最新版本的不接受push】

不在最新版本时候修改发生冲突时候，只有先pull最新的让后再push

![1610885986130](.\img\协同冲突.png)

![1610886070062](.\img\chongtu2.png)

![1610886174835](.\img\chongtu3.png)





# 实验2 第三方修改 和两个库之间 fork

![1610886235285](.\img\fork.png)



使用fork

![1610889554413](.\img\1610889554413.png) 

![1610886916699](.\img\1fork.png)



![1610889723846](.\img\1610889723846.png)









创建fork ，修改这个fork 请求合并，应该

ssh 账户只能一次使用一个！！

我们的工作里面应该就是new fork的情况！！

![1610889804214](.\img\1610889804214.png)



![1610889924460](.\img\1610889924460.png)





![1610889983714](.\img\1610889983714.png)

![img](file:///C:/Users/LTD/Desktop/note/img/1610889924460.png?lastModify=1610889997)







困扰我的就是你fork 这里的操作





![1610891351510](.\img\branch10.png)







