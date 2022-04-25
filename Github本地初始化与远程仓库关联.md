# Github本地初始化与远程仓库关联

---

-- Github 本地初始化与远程仓库关联也可参见 https://blog.csdn.net/qq_39530821/article/details/118072372 。

---



1、远程仓库的创建的本地仓库的初始化可以分开进行，先进行哪一个都可以。

2、我先初始化本地仓库，使用命令如下：

```shell
git init
```

初始化完成之后，在本地文件夹中出现一个名为 .git 的隐藏文件夹。

3、在本地仓库中编写代码，并提交到本地仓库。

```shell
git add . 
git commit -m "注释..."
git status
got log --graph # 查看刚才的提交信息
```

4、在 Github 中设置ssh keys。

​      4.1 查看在用户目录下是否有.ssh目录，如果有，再进入查看是否有id_rsa和id_rsa.pub两个文件。如果没有，在GitBash/shell中执行：ssh-keygen -t rsa -C “helloworld@qq.com”。其中id_rsa是私钥，不可告诉别人，id_rsa.pub是公钥，可以告诉别人。命令运行成功后，可在.ssh文件夹中发现id_rsa和id_rsa.pub两个文件。

​       4.2 在Github网页中，找到右上角个人头像，并点击下方的Setting按钮，进入个人设置中心。在左侧菜单中找到 “SSH and GPG keys”栏，点积“New SSH keys”的绿色按钮创建一个ssh。将id_rsa.pub中的内容全部复制到“Key”框中，Title框则随意取一个名字。完成后点击下方的 “Add SSH key”的绿色按钮完成创建。如此操作之后，本地进行push时不再需要输入用户名等信息。

5、在Github中创建干净的远程仓库。

6、将远程仓库与本地仓库相关联。首先，进入到本地仓库中，使用GitBash指定本地仓库的主分支。命令如下。需要先查看远程仓库中的主分支是否为main（可能是master）。

```shell
 git branch -M main
```

第二步，关联本地仓库和远程仓库。命令如下。git@github.com:xxx.git来自刚才创建的远程仓库中的SSH。

```shell
git remote add origin git@github.com:xxx.git
```

第三步，将本地仓库中的内容提交到远程

```shell
git push -u origin main
```





