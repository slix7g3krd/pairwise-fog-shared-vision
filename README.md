# pairwise-fog-shared-vision

## 领域

游戏、图形与多媒体

## 主题

战争迷雾与队伍共享视野

## 说明

跨帧脏格清除、队伍视野引用回收、分块版本校验。

初始状态下 `game/fog_vision.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
