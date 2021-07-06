"""
字典wordList 中从单词 beginWord和 endWord 的 转换序列 是一个按下述规格形成的序列：

序列中第一个单词是 beginWord 。
序列中最后一个单词是 endWord 。
每次转换只能改变一个字母。
转换过程中的中间单词必须是字典wordList 中的单词。
给你两个单词 beginWord和 endWord 和一个字典 wordList ，找到从beginWord 到endWord 的最短转换序列中的单词数目。
如果不存在这样的转换序列，返回 0。

示例 1：

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：5
解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
示例 2：

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：0
解释：endWord "cog" 不在字典中，所以无法进行转换。


提示：

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord、endWord 和 wordList[i] 由小写英文字母组成
beginWord != endWord
wordList 中的所有字符串 互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-ladder
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList_new = [beginWord] + wordList
        n = len(beginWord)
        m = len(wordList_new)
        dic = collections.defaultdict(set)
        for i in range(n):
            wordList_new_rep = list(
                map(lambda x: '{}{}{}'.format(x[:i], '*', x[i + 1:]), wordList_new))
            # print(wordList_new_rep)
            for j in range(m):
                for k in range(j + 1, m):
                    if wordList_new_rep[j] == wordList_new_rep[k]:
                        dic[wordList_new[j]].add(wordList_new[k])
                        dic[wordList_new[k]].add(wordList_new[j])

        # print(dic)
        stack = {beginWord}
        visited = set()
        cnt = 0
        while stack:
            cnt += 1
            shadow_stack = stack.copy()
            stack.clear()
            for word in shadow_stack:
                if word == endWord:
                    return cnt
                visited.add(word)
                stack.update(dic[word] - visited)
        return 0

class Solution:
    # 官解方法一：广度优先搜索 + 优化建图
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        本题要求的是最短转换序列的长度，看到最短首先想到的就是广度优先搜索。
        想到广度优先搜索自然而然的就能想到图，但是本题并没有直截了当的给出图的模型，因此我们需要把它抽象成图的模型。

        我们可以把每个单词都抽象为一个点，如果两个单词可以只改变一个字母进行转换，那么说明他们之间有一条双向边。
        因此我们只需要把满足转换条件的点相连，就形成了一张图。

        基于该图，我们以 beginWord 为图的起点，以 endWord 为终点进行广度优先搜索，
        寻找 beginWord 到 endWord 的最短路径。

        算法

        基于上面的思路我们考虑如何编程实现。
        首先为了方便表示，我们先给每一个单词标号，即给每个单词分配一个 id。
        创建一个由单词 word 到 id 对应的映射 wordId，并将 beginWord 与 wordList 中所有的单词都加入这个映射中。
        之后我们检查 endWord 是否在该映射内，若不存在，则输入无解。我们可以使用哈希表实现上面的映射关系。

        然后我们需要建图，依据朴素的思路，我们可以枚举每一对单词的组合，判断它们是否恰好相差一个字符，
        以判断这两个单词对应的节点是否能够相连。但是这样效率太低，我们可以优化建图。

        具体地，我们可以创建虚拟节点。对于单词 hit，我们创建三个虚拟节点 *it、h*t、hi*，
        并让 hit 向这三个虚拟节点分别连一条边即可。如果一个单词能够转化为 hit，
        那么该单词必然会连接到这三个虚拟节点之一。对于每一个单词，我们枚举它连接到的虚拟节点，把该单词对应的 id 与这些虚拟节点对应的 id 相连即可。

        最后我们将起点加入队列开始广度优先搜索，当搜索到终点时，我们就找到了最短路径的长度。
        注意因为添加了虚拟节点，所以我们得到的距离为实际最短路径长度的两倍。同时我们并未计算起点对答案的贡献，所以我们应当返回距离的一半再加一的结果。

        作者：LeetCode-Solution
        链接：https://leetcode-cn.com/problems/word-ladder/solution/dan-ci-jie-long-by-leetcode-solution/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """

        def addWord(word: str):
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum
                nodeNum += 1

        def addEdge(word: str):
            addWord(word)
            id1 = wordId[word]
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                newWord = "".join(chars)
                addWord(newWord)
                id2 = wordId[newWord]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp

        wordId = dict()
        edge = collections.defaultdict(list)
        nodeNum = 0

        for word in wordList:
            addEdge(word)

        addEdge(beginWord)
        if endWord not in wordId:
            return 0

        dis = [float("inf")] * nodeNum
        beginId, endId = wordId[beginWord], wordId[endWord]
        dis[beginId] = 0

        que = collections.deque([beginId])
        while que:
            x = que.popleft()
            if x == endId:
                return dis[endId] // 2 + 1
            for it in edge[x]:
                if dis[it] == float("inf"):
                    dis[it] = dis[x] + 1
                    que.append(it)

        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.ladderLength(beginWord="hit", endWord="cog",
                         wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
