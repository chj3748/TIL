# collection_Deque

```python
import collections
d = collections.deque([10, 20, 30, 40, 50])
print('Deque: ', d)
# 'Deque: ', deque([10, 20, 30, 40, 50])
# 오른쪽에 추가
d.append(60)
print('Deque: ', d)
# 'Deque: ', deque([10, 20, 30, 40, 50, 60])
# 왼쪽에 추가
d.appendleft(0)
print('Deque: ', d)
# 'Deque: ', deque([0, 10, 20, 30, 40, 50, 60])
# 입력값을 순환하면서 오른쪽에 추가(append)
d.extend([70, 80])
print('Deque: ', d)
# 'Deque: ', deque([0, 10, 20, 30, 40, 50, 60, 70, 80])
# 입력값을 순환하면서 왼쪽에 추가(appendleft)
d.extendleft([-10, -20, -30])
print('Deque: ', d)
# 'Deque: ', deque([-30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80])
# 값 삭제
d.remove(0)
print('Deque: ', d)
# 'Deque: ', deque([-30, -20, -10, 10, 20, 30, 40, 50, 60, 70, 80])
# 오른쪽의 끝값 가져오면서 deque에서 제거
maxValue = d.pop()
print('maxValue:', maxValue)
# maxValue: 80
print('Deque: ', d)
# Deque:  deque([-30, -20, -10, 10, 20, 30, 40, 50, 60, 70])
# 왼쪽의 끝값 가져오면서 deque에서 제거
minValue = d.popleft()
print('minValue:', minValue)
# minValue: -30
print('Deque: ', d)
# Deque:  deque([-20, -10, 10, 20, 30, 40, 50, 60, 70])
# 값 회전(rotating)
d = collections.deque(range(5))
print('Deque: ', d)
# Deque:  deque([0, 1, 2, 3, 4])
d.rotate(1)
print('Deque.rotate(1): ', d)
# Deque.rotate(1):  deque([4, 0, 1, 2, 3])
d.rotate(1)
print('Deque.rotate(1): ', d)
# Deque.rotate(1):  deque([3, 4, 0, 1, 2])
d.rotate(-1)
print('Deque.rotate(-1): ', d)
# Deque.rotate(-1):  deque([4, 0, 1, 2, 3])
d.rotate(-1)
print('Deque.rotate(-1): ', d)
# Deque.rotate(-1):  deque([0, 1, 2, 3, 4])
```

