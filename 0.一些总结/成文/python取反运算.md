```python
>>> ~3
-4
>>> ~-4
3
>>> 
```

取反运算符的原理：

1.对3取反：（取4位二进制）  
①化为二进制：  
3→0011  
②对二进制结果取反：  
0011→1100  
③对结果先取反再加1：  
1100→（~1100+1）→0011+1→0100  
④对符号取反并化为十进制：  
-0100→-4

2.对-4取反：  
①化为二进制：  
4→0100  
②对二进制结果取反：  
0100→1011  
③对结果先加1再取反：  
1011→~（1011+1）→ ~1100→0011  
④对符号取反并化为十进制：  
+0011→3

3.从结果来说：  
取反结果为：原数+1再变相反数。