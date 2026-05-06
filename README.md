 Git 实践过程记录

 一、学习资料来源
- [Git 官方文档](https://git-scm.com/doc)
- [Pro Git 中文版](https://git-scm.com/book/zh/v2)

 二、实践流程
1. 安装 Git，配置 user.name / user.email。
2. 创建本地仓库 `git-practice`。
3. 编写 `hello.py`，完成 3 次提交（基础功能→用户输入→异常处理）。
4. 在 GitHub 创建公开仓库 `git-practice-demo`。
5. 关联并推送本地提交到远程。

 三、每次提交说明
| 提交 | 说明 |
|------|------|
| 第1次 | 添加 hello.py，打印 "Hello, Git!" |
| 第2次 | 增加 input，支持自定义名字 |
| 第3次 | 添加 try-except 和注释 |

四、遇到的问题及解决方法
 问题1：git push 失败，提示远程有我没有的文件
解决：先 `git pull --rebase origin main`，再重新 `git push`。

问题2：推送代码一直不显示
解决：根据AI指导一步步排查完成。

五、学习心得
通过本次实践，我掌握了 Git 的基本工作流：工作区 → 暂存区 → 本地仓库 → 远程仓库。理解了 add、commit、push 各自的作用，也学会了如何处理常见的冲突和错误。Git 不仅适合个人代码版本管理，更是团队协作的基石 —— 分支管理、合并请求、代码回滚等特性让我体会到它的强大。后续我还会继续学习分支操作（branch、merge）、远程协作（fetch、pull）以及 rebase 的高级用法。

 仓库地址
https://github.com/你的用户名/git-practice-demo
