### views和forms

视图函数中，渲染模板的字段，从实例化的modelform中取

### forms和model

model中的字段，一般会通过

```python
from web import models

class Meta:
    model = models.UserInfo
    
```

来传递给forms