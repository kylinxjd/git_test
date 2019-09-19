命令行创建仓库


### create a new repository on the command line
echo "# dddd" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/kylinxjd/dddd.git
git push -u origin master



### push an existing repository from the command line

git remote add origin https://github.com/kylinxjd/dddd.git
git push -u origin master


