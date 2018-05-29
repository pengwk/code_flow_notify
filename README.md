# code_flow_notify
提交代码前提醒自己做代码风格检查和运行测试

## 如何使用？

在`.hgrc`里增加 `pre-commit hook`：

```
[hooks]
pre-commit=python:/path/to/pre_commit.py:code_flow_check
```

