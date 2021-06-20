"""
一个王国里住着国王、他的孩子们、他的孙子们等等。每一个时间点，这个家庭里有人出生也有人死亡。

这个王国有一个明确规定的皇位继承顺序，第一继承人总是国王自己。我们定义递归函数Successor(x, curOrder)，给定一个人x和当前的继承顺序，该函数返回 x的下一继承人。

Successor(x, curOrder):
    如果 x 没有孩子或者所有 x 的孩子都在 curOrder 中：
        如果 x 是国王，那么返回 null
        否则，返回 Successor(x 的父亲, curOrder)
    否则，返回 x 不在 curOrder 中最年长的孩子
比方说，假设王国由国王，他的孩子Alice 和 Bob （Alice 比 Bob年长）和 Alice 的孩子Jack 组成。

一开始，curOrder为["king"].
调用Successor(king, curOrder)，返回 Alice ，所以我们将 Alice 放入 curOrder中，得到["king", "Alice"]。
调用Successor(Alice, curOrder)，返回 Jack ，所以我们将 Jack 放入curOrder中，得到["king", "Alice", "Jack"]。
调用Successor(Jack, curOrder)，返回 Bob ，所以我们将 Bob 放入curOrder中，得到["king", "Alice", "Jack", "Bob"]。
调用Successor(Bob, curOrder)，返回null。最终得到继承顺序为["king", "Alice", "Jack", "Bob"]。
通过以上的函数，我们总是能得到一个唯一的继承顺序。

请你实现ThroneInheritance类：

ThroneInheritance(string kingName) 初始化一个ThroneInheritance类的对象。国王的名字作为构造函数的参数传入。
void birth(string parentName, string childName)表示parentName新拥有了一个名为childName的孩子。
void death(string name)表示名为name的人死亡。一个人的死亡不会影响Successor函数，也不会影响当前的继承顺序。你可以只将这个人标记为死亡状态。
string[] getInheritanceOrder()返回 除去死亡人员的当前继承顺序列表。


示例：

输入：
["ThroneInheritance", "birth", "birth", "birth", "birth", "birth", "birth", "getInheritanceOrder", "death", "getInheritanceOrder"]
[["king"], ["king", "andy"], ["king", "bob"], ["king", "catherine"], ["andy", "matthew"], ["bob", "alex"], ["bob", "asha"], [null], ["bob"], [null]]
输出：
[null, null, null, null, null, null, null, ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"], null, ["king", "andy", "matthew", "alex", "asha", "catherine"]]

解释：
ThroneInheritance t= new ThroneInheritance("king"); // 继承顺序：king
t.birth("king", "andy"); // 继承顺序：king > andy
t.birth("king", "bob"); // 继承顺序：king > andy > bob
t.birth("king", "catherine"); // 继承顺序：king > andy > bob > catherine
t.birth("andy", "matthew"); // 继承顺序：king > andy > matthew > bob > catherine
t.birth("bob", "alex"); // 继承顺序：king > andy > matthew > bob > alex > catherine
t.birth("bob", "asha"); // 继承顺序：king > andy > matthew > bob > alex > asha > catherine
t.getInheritanceOrder(); // 返回 ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]
t.death("bob"); // 继承顺序：king > andy > matthew > bob（已经去世）> alex > asha > catherine
t.getInheritanceOrder(); // 返回 ["king", "andy", "matthew", "alex", "asha", "catherine"]


提示：

1 <= kingName.length, parentName.length, childName.length, name.length <= 15
kingName，parentName，childName和name仅包含小写英文字母。
所有的参数childName 和kingName互不相同。
所有death函数中的死亡名字 name要么是国王，要么是已经出生了的人员名字。
每次调用 birth(parentName, childName) 时，测试用例都保证 parentName 对应的人员是活着的。
最多调用105次birth 和death。
最多调用10次getInheritanceOrder。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/throne-inheritance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import defaultdict
from typing import List


class who:
    def __init__(self, parent_name, current_name):
        self.parent = parent_name
        self.name = current_name
        self.children = []
        self.is_alive = True


class ThroneInheritance:
    def __init__(self, kingName: str):
        self.dic = dict()
        self.king = kingName
        node = who('root', kingName)
        self.dic[kingName] = node

    def birth(self, parentName: str, childName: str) -> None:
        node = who(parentName, childName)
        self.dic[childName] = node
        self.dic[parentName].children.append(childName)

    def death(self, name: str) -> None:
        self.dic[name].is_alive = False

    def getInheritanceOrder(self) -> List[str]:
        def dfs(name):
            res = [name] if self.dic[name].is_alive else []
            if self.dic[name].children:
                for minzhi in self.dic[name].children:
                    res.extend(dfs(minzhi))
            return res

        return dfs(self.king)


# --------------以下是官解
class ThroneInheritance:
    """
    方法一：多叉树的前序遍历
    思路与算法
    
    我们可以发现，题目中定义的 Successor(x,curOrder) 函数，与多叉树的前序遍历过程是一致的：
    
    「返回 x 不在 curOrder 中最年长的孩子」对应着选择 x 在树中的一个子节点，递归地进行遍历操作；
    
    「返回 Successor(x的父亲,curOrder)」对应着当我们将以 x 为根的子树遍历完成后，回溯到 x 的父节点继续进行遍历；
    
    「返回 null」对应着我们将整棵树遍历完成。
    
    因此，对于题目中需要实现的每一个函数，我们可以分别设计出如下的算法：
    
    ThroneInheritance(kingName)：我们将 kingName 作为树的根节点；
    
    birth(parentName,childName)：我们在树中添加一条从 parentName 到childName 的边，将childName 作为 parentName 的子节点；
    
    death(name)：我们使用一个哈希集合记录所有的死亡人员，将 name 加入该哈希集合中；
    
    getInheritanceOrder()：我们从根节点开始对整棵树进行前序遍历。需要注意的是，如果遍历到死亡人员，那么不能将其加入继承顺序列表中。
    
    细节
    
    那么我们如何存储这棵树呢？
    
    一种可行的方法是使用哈希映射。记哈希映射为edges，那么对于 edges 中的每一个键值对 (k,v)，键 k 表示一个人，值 v 以列表的形式存放了这个人所有的孩子，列表可以为空。
    
    这样一来，对于birth(parentName,childName) 操作，我们只需要将childName 加入parentName 在哈希映射中的列表末尾即可。
    
    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/throne-inheritance/solution/huang-wei-ji-cheng-shun-xu-by-leetcode-s-p6lk/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def __init__(self, kingName: str):
        self.edges = defaultdict(list)
        self.dead = set()
        self.king = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.edges[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = list()

        def preorder(name: str) -> None:
            if name not in self.dead:
                ans.append(name)
            if name in self.edges:
                for childName in self.edges[name]:
                    preorder(childName)

        preorder(self.king)
        return ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

if __name__ == '__main__':
    t = ThroneInheritance('king')
    t.birth("king", "andy")
    print(t.getInheritanceOrder())
    t.birth("king", "bob")
    print(t.getInheritanceOrder())
    t.birth("king", "catherine")
    print(t.getInheritanceOrder())
    t.birth("andy", "matthew")
    print(t.getInheritanceOrder())
    t.birth("bob", "alex")
    print(t.getInheritanceOrder())
    t.birth("bob", "asha")
    print(t.getInheritanceOrder())
    t.death("bob")
    print(t.getInheritanceOrder())
