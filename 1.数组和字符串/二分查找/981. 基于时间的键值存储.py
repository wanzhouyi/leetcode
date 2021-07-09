"""
创建一个基于时间的键值存储类TimeMap，它支持下面两个操作：

1. set(string key, string value, int timestamp)

存储键key、值value，以及给定的时间戳timestamp。
2. get(string key, int timestamp)

返回先前调用set(key, value, timestamp_prev)所存储的值，其中timestamp_prev <= timestamp。
如果有多个这样的值，则返回对应最大的timestamp_prev的那个值。
如果没有值，则返回空字符串（""）。


示例 1：

输入：inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
输出：[null,null,"bar","bar",null,"bar2","bar2"]
解释：
TimeMap kv; 
kv.set("foo", "bar", 1); // 存储键 "foo" 和值 "bar" 以及时间戳 timestamp = 1 
kv.get("foo", 1);  // 输出 "bar" 
kv.get("foo", 3); // 输出 "bar" 因为在时间戳 3 和时间戳 2 处没有对应 "foo" 的值，所以唯一的值位于时间戳 1 处（即 "bar"） 
kv.set("foo", "bar2", 4); 
kv.get("foo", 4); // 输出 "bar2" 
kv.get("foo", 5); // 输出 "bar2" 

示例 2：

输入：inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
输出：[null,null,null,"","high","high","low","low"]


提示：

所有的键/值字符串都是小写的。
所有的键/值字符串长度都在[1, 100]范围内。
所有TimeMap.set操作中的时间戳timestamps 都是严格递增的。
1 <= timestamp <= 10^7
TimeMap.set 和TimeMap.get函数在每个测试用例中将（组合）调用总计120000 次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/time-based-key-value-store
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import bisect


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic_val = dict()
        self.dic_timestamp = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.dic_val.get(key):
            self.dic_val[key] = [value]
            self.dic_timestamp[key] = [timestamp]
        else:
            idx = bisect.bisect_left(self.dic_timestamp[key], timestamp)
            self.dic_timestamp[key].insert(idx, timestamp)
            self.dic_val[key].insert(idx, value)
        print(self.dic_val)
        print(self.dic_timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if not self.dic_timestamp.get(key):
            return ''
        if not self.dic_timestamp[key]:
            return ''
        if timestamp < self.dic_timestamp[key][0]:
            return ''
        index = bisect.bisect_left(self.dic_timestamp[key], timestamp)
        if index > len(self.dic_timestamp[key]) - 1:
            return self.dic_val[key][-1]
        elif timestamp == self.dic_timestamp[key][index]:
            return self.dic_val[key][index]
        elif timestamp < self.dic_timestamp[key][index]:
            return self.dic_val[key][index - 1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
if __name__ == '__main__':
    kv = TimeMap()
    kv.set("foo", "bar", 1)
    print(kv.get("foo", 1))
    print(kv.get("foo", 3))
    kv.set("foo", "bar2", 4)
    print(kv.get("foo", 4))
    print(kv.get("foo", 5))

    kv.set('love', 'high', 10)
    # kv.set('love','low',20)
    print(kv.get('love', 5))
    print(kv.get('love', 10))
    print(kv.get('love', 15))
    print(kv.get('love', 20))
    print(kv.get('love', 25))
